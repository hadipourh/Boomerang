# Author: Hosein Hadipour
# Created on Feb 28, 2020
# 9 Esfand 1398 (When the Coronavirus was being spread over the world)

from skinny128 import Skinny128
from argparse import ArgumentParser, RawTextHelpFormatter
import yaml

def loadparameters(args):
    """
    Get parameters from the argument list and inputfile.
    """
    # Load default values
    params = {"rounds" : 5,
              "blocksize": 128,
              "mode" : 0,
              "sweight" : 0,
              "endweight" : 128,              
              "timelimit" : -1,
              "fixedVariables" : {}}

    # Check if there is an input file specified
    if args.inputfile:
        with open(args.inputfile[0], 'r') as input_file:
            doc = yaml.load(input_file, Loader=yaml.FullLoader)            
            params.update(doc)
            if "fixedVariables" in doc:
                fixed_vars = {}
                for variable in doc["fixedVariables"]:
                    fixed_vars = dict(list(fixed_vars.items()) +
                                      list(variable.items()))
                params["fixedVariables"] = fixed_vars

    # Override parameters if they are set on commandline    
    if args.rounds:
        params["rounds"] = args.rounds[0]    

    if args.sweight:
        params["sweight"] = args.sweight[0]

    if args.endweight:
        params["endweight"] = args.endweight[0]

    if args.mode:
        params["mode"] = args.mode[0]

    if args.timelimit:
        params["timelimit"] = args.timelimit[0]

    return params

def main():
    '''
    Parse the arguments and start the request functionality with the provided
    parameters.
    '''
    parser = ArgumentParser(description="This tool finds the best differential"
                                        "trail in a cryptographic primitive"
                                        "using Gurobi",
                            formatter_class=RawTextHelpFormatter)
    
    parser.add_argument('--sweight', nargs=1, type=int,
                        help="Starting weight for the trail search.")
    parser.add_argument('--endweight', nargs=1, type=int,
                        help="Stop search after reaching endweight.")    
    parser.add_argument('--rounds', nargs=1, type=int,
                        help="The number of rounds for the cipher")
    parser.add_argument('--mode', nargs=1, type=int, 
                        choices=[0, 1], help=
                        "0 = search characteristic for fixed round\n"                        
                        "1 = determine the probability of the differential\n")
    parser.add_argument('--timelimit', nargs=1, type=int,
                        help="Set a timelimit for the search in seconds.")    
    parser.add_argument('--inputfile', nargs=1, help="Use an yaml input file to"
                                                     "read the parameters.")    

    # Parse command line arguments and construct parameter list.
    args = parser.parse_args()
    params = loadparameters(args)
    skinny = Skinny128(params, True)
    skinny.make_model()
    skinny.solve()

if __name__ == "__main__":
    main()
