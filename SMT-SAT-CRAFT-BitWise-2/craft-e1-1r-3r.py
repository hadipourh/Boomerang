'''
Applying the SAT-SMT-based method to find differential distinguishers of CRAFT
Copyright (C) December 8, 2019  Hosein Hadipour

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from cryptanalysis import search1
from ciphers import (craft, craftrtk, craftrtk1, craftrtk2, craftrtk3)
from config import PATH_STP, PATH_CRYPTOMINISAT, PATH_BOOLECTOR

from argparse import ArgumentParser, RawTextHelpFormatter

import yaml
import os
import math
import json


def startsearch(tool_parameters):
    """
    Starts the search tool for the given parameters
    """

    cipher_suite = {"craft" : craft.CraftCipher(),
                    "craftrtk" : craftrtk.CraftCipherRTK(),
                    "craftrtk1" : craftrtk1.CraftCipherRTK1(),
                    "craftrtk2" : craftrtk2.CraftCipherRTK2(),
                    "craftrtk3" : craftrtk3.CraftCipherRTK3()}

    cipher = None

    if tool_parameters["cipher"] in cipher_suite:
        cipher = cipher_suite[tool_parameters["cipher"]]
    else:
        print("Cipher not supported!")
        return

    # Handle program flow
    if tool_parameters["mode"] == 0:
        search1.findMinWeightCharacteristic(cipher, tool_parameters)
    elif tool_parameters["mode"] == 1:
        search1.searchCharacteristics(cipher, tool_parameters)
    elif tool_parameters["mode"] == 2:
        search1.findAllCharacteristics(cipher, tool_parameters)
    elif tool_parameters["mode"] == 3:
        search1.findBestConstants(cipher, tool_parameters)
    elif tool_parameters["mode"] == 4:
        fileobj = open("possible_outputs.txt", 'r')
        possible_inputs = fileobj.readlines()
        fileobj.close()
        fileobj = open("result_boomerang.txt", "w")
        distribution = [0]*len(possible_inputs)
        tool_parameters_backup = tool_parameters.copy()
        number_of_possible_trails = 0

        stweight = int(tool_parameters["sweight"])
        endweight = int(tool_parameters["endweight"])
        ntrails = [[0] for i in range(len(possible_inputs))]

        for i in range(len(possible_inputs)):
            tool_parameters = tool_parameters_backup.copy()
            tool_parameters["fixedVariables"]["x0"] = possible_inputs[i][0:-1]
            print("output[%d]: %s" % (i, possible_inputs[i][0:-1]))
            fileobj.write("output[%d]: %s\n" % (i, possible_inputs[i][0:-1]))
            pr, ntrails[i] = search1.computeProbabilityOfDifferentials(cipher, tool_parameters)
            distribution[i] = pr
            if pr > 0.0:
                prob_disp = "Probability: 2^(" + str(math.log(pr, 2)) + ")"
                print(prob_disp)
                fileobj.write(prob_disp)
                fileobj.write("\n")
                number_of_possible_trails += 1
            else:
                print("Probability: 0")
                fileobj.write("Probability: 0\n")
            trails = "#Trails: %s" % ntrails[i]
            print(trails)
            fileobj.write(trails)
            fileobj.write("\n\n")
    fileobj.write("Distribution : %s\n" % distribution)
    for w in range(stweight, endweight):
        fileobj.write("#Trails of weigth %d: [" % w)
        temp = [0]*(len(possible_inputs))
        for t in range(len(possible_inputs)):
            temp[t] = str(ntrails[t][w])
        fileobj.write(", ".join(temp))
        fileobj.write("]\n")    
    fileobj.write("\nNumber of possible trails : %d out of %d" % (number_of_possible_trails, 15))    
    fileobj.close()
    return

def checkenviroment():
    """
    Basic checks if the enviroment is set up correctly
    """

    if not os.path.exists("./tmp/"):
        os.makedirs("./tmp/")

    if not os.path.exists(PATH_STP):
        print("ERROR: Could not find STP binary, please check config.py")
        exit()

    if not os.path.exists(PATH_CRYPTOMINISAT):
        print("WARNING: Could not find CRYPTOMINISAT binary, please check "
              "config.py.")

    if not os.path.exists(PATH_BOOLECTOR):
        print("WARNING: Could not find BOOLECTOR binary, \"--boolector\" "
              "option not available.")

    return


def loadparameters(args):
    """
    Get parameters from the argument list and inputfile.
    """
    # Load default values
    params = {"cipher" : "craft",
              "rounds" : 5,
              "mode" : 0,
              "wordsize" : 64,
              "blocksize" : 64,
              "sweight" : 0,
              "endweight" : 1000,
              "iterative" : False,
              "boolector" : False,
              "dot" : None,
              "latex" : None,
              "nummessages" : 1,
              "timelimit" : -1,
              "fixedVariables" : {},
              "blockedCharacteristics" : []}

    # Check if there is an input file specified
    if args.inputfile:
        with open(args.inputfile[0], 'r') as input_file:
            doc = yaml.load(input_file)
            params.update(doc)
            if "fixedVariables" in doc:
                fixed_vars = {}
                for variable in doc["fixedVariables"]:
                    fixed_vars = dict(list(fixed_vars.items()) +
                                      list(variable.items()))
                params["fixedVariables"] = fixed_vars

    # Override parameters if they are set on commandline
    if args.cipher:
        params["cipher"] = args.cipher[0]

    if args.rounds:
        params["rounds"] = args.rounds[0]

    if args.wordsize:
        params["wordsize"] = args.wordsize[0]

    if args.blocksize:
        params["blocksize"] = args.blocksize[0]        

    if args.sweight:
        params["sweight"] = args.sweight[0]

    if args.endweight:
        params["endweight"] = args.endweight[0]

    if args.mode:
        params["mode"] = args.mode[0]

    if args.timelimit:
        params["timelimit"] = args.timelimit[0]

    if args.iterative:
        params["iterative"] = args.iterative

    if args.boolector:
        params["boolector"] = args.boolector

    if args.nummessages:
        params["nummessages"] = args.nummessages[0]

    if args.dot:
        params["dot"] = args.dot[0]

    if args.latex:
        params["latex"] = args.latex[0]

    return params


def main():
    """
    Parse the arguments and start the request functionality with the provided
    parameters.
    """
    parser = ArgumentParser(description="This tool finds the best differential"
                                        "trail in a cryptopgrahic primitive"
                                        "using STP and CryptoMiniSat.",
                            formatter_class=RawTextHelpFormatter)

    parser.add_argument('--cipher', nargs=1, help="Options: simon, speck, ...")
    parser.add_argument('--sweight', nargs=1, type=int,
                        help="Starting weight for the trail search.")
    parser.add_argument('--endweight', nargs=1, type=int,
                        help="Stop search after reaching endweight.")    
    parser.add_argument('--rounds', nargs=1, type=int,
                        help="The number of rounds for the cipher")
    parser.add_argument('--wordsize', nargs=1, type=int,
                        help="Wordsize used for the cipher.")
    parser.add_argument('--blocksize', nargs=1, type=int,
                        help="Blocksize used for the cipher.")    
    parser.add_argument('--nummessages', nargs=1, type=int,
                        help="Number of message blocks.")
    parser.add_argument('--mode', nargs=1, type=int, 
                        choices=[0, 1, 2, 3, 4], help=
                        "0 = search characteristic for fixed round\n"
                        "1 = search characteristic for all rounds starting at"
                        "the round specified\n"
                        "2 = search all characteristic for a specific weight\n"
                        "3 = used for key recovery\n"
                        "4 = determine the probability of the differential\n")
    parser.add_argument('--timelimit', nargs=1, type=int,
                        help="Set a timelimit for the search in seconds.")
    parser.add_argument('--iterative', action="store_true",
                        help="Only search for iterative characteristics")
    parser.add_argument('--boolector', action="store_true",
                        help="Use boolector to find solutions")
    parser.add_argument('--inputfile', nargs=1, help="Use an yaml input file to"
                                                     "read the parameters.")
    parser.add_argument('--dot', nargs=1, help="Print the trail in .dot format.")
    parser.add_argument('--latex', nargs=1, help="Print the trail in .tex format.")

    # Parse command line arguments and construct parameter list.
    args = parser.parse_args()
    params = loadparameters(args)

    # Check if enviroment is setup correctly.
    checkenviroment()

    # Start the solver
    startsearch(params)


if __name__ == '__main__':      
    main()
