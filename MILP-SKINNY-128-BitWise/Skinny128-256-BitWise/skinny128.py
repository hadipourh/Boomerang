# Author: Hosein Hadipour
# Created on Feb 28, 2020
# 9 Esfand 1398 (When the Coronavirus was being spread over the world)

import time
from gurobipy import read
from gurobipy import GRB
import itertools
import math

"""
Modeling the differential analysis of Skinny-128-256 by an MILP problem,
in order to find the best differential trail, and compute the differential
effect considering the clustering effect

x_roundNumber_byteNumber_bitNumber
x_roundNumber_byteNumber_0: msb
x_roundNumber_byteNumber_7: lsb

State at the input of (i + 1)-th round or before the Subcell:
x_i_0	x_i_1	x_i_2	x_i_3
x_i_4	x_i_5	x_i_6	x_i_7
x_i_8	x_i_9	x_i_10	x_i_11
x_i_12	x_i_13	x_i_14	x_i_15

State before the AddTweakey or after the SubCell:
y_i_0	y_i_1   y_i_2	y_i_3
y_i_4	y_i_5	y_i_6	y_i_7
y_i_8	y_i_9	y_i_10	y_i_11
y_i_12	y_i_13	y_i_14	y_i_15

State before the ShiftRows or after the AddTweakey:
z_i_0	z_i_1	z_i_2	z_i_3
z_i_4	z_i_5	z_i_6	z_i_7
z_i_8	z_i_9	z_i_10	z_i_11
z_i_12	z_i_13	z_i_14	z_i_15

State before the MixColumns or after the ShiftRows:
pz_i_0	pz_i_1	pz_i_2	pz_i_3
pz_i_4	pz_i_5	pz_i_6	pz_i_7
pz_i_8	pz_i_9	pz_i_10	pz_i_11
pz_i_12	pz_i_13	pz_i_14	pz_i_15
Note that pz is only used in the code not in the MILP model

The TK1 which is used in the (i + 1)'th round:
tk1_i_0	    tk1_i_1	    tk1_i_2	    tk1_i_3
tk1_i_4	    tk1_i_5	    tk1_i_6	    tk1_i_7
tk1_i_8	    tk1_i_9	    tk1_i_10	tk1_i_11
tk1_i_12	tk1_i_13	tk1_i_14	tk1_i_15

The TK2 which is used in the (i + 1)'th round:
tk2_i_0	    tk2_i_1	    tk2_i_2	    tk2_i_3
tk2_i_4	    tk2_i_5	    tk2_i_6	    tk2_i_7
tk2_i_8	    tk2_i_9	    tk2_i_10	tk2_i_11
tk2_i_12	tk2_i_13	tk2_i_14	tk2_i_15

(i + 1)'th round tweakey
tk_i_0	tk_i_1	tk_i_2	tk_i_3
tk_i_4	tk_i_5	tk_i_6	tk_i_7
 
The permuted twakey in the (i + 1)'th round:
ptk1_i_0	    ptk1_i_1	    ptk1_i_2	    ptk1_i_3
ptk1_i_4	    ptk1_i_5	    ptk1_i_6	    ptk1_i_7
ptk1_i_8	    ptk1_i_9	    ptk1_i_10	    ptk1_i_11
ptk1_i_12	    ptk1_i_13	    ptk1_i_14	    ptk1_i_15

ptk2_i_0	    ptk2_i_1	    ptk2_i_2	    ptk2_i_3
ptk2_i_4	    ptk2_i_5	    ptk2_i_6	    ptk2_i_7
ptk2_i_8	    ptk2_i_9	    ptk2_i_10	    ptk2_i_11
ptk2_i_12	    ptk2_i_13	    ptk2_i_14	    ptk2_i_15
ptk1, and ptk2 are only used in the code, not in the MILP model

Sbox indicators variables:
q_roundNumber_byteNumber : shows the activity of an Sbox
q2_roundNumber_byteNumber
q2_4150_roundNumber_byteNumber
q2_6781_roundNumber_byteNumber
q3_roundNumber_byteNumber
q3_1926_roundNumber_byteNumber
q3_4150_roundNumber_byteNumber
q3_6781_roundNumber_byteNumber
q4_roundNumber_byteNumber
q4_4150_roundNumber_byteNumber
q5_roundNumber_byteNumber
q5_4150_roundNumber_byteNumber
q6_roundNumber_byteNumber
q7_roundNumber_byteNumber
q_roundNumber_byteNumber = q2_roundNumber_byteNumber + q2_4150_roundNumber_byteNumber + q2_6781_roundNumber_byteNumber
                         + q3_roundNumber_byteNumber + q3_1926_roundNumber_byteNumber + q3_4150_roundNumber_byteNumber
                         + q3_6781_roundNumber_byteNumber + q4_roundNumber_byteNumber + q4_4150_roundNumber_byteNumber
                         + q5_roundNumber_byteNumber + q5_4150_roundNumber_byteNumber + q6_roundNumber_byteNumber + 
                         + q7_roundNumber_byteNumber

Objective function: Minimize Sum(2*q2_roundNumber_byteNumber + 2.4150*q2_4150_roundNumber_byteNumber + 2.6781*q2_6781_roundNumber_byteNumber
                                + 3*q3_roundNumber_byteNumber + 3.1926*q3_1926_roundNumber_byteNumber + 3.4150*q3_4150_roundNumber_byteNumber
                                + 3.6781*q3_6781_roundNumber_byteNumber + 4*q4_roundNumber_byteNumber + 4.4150*q4_4150_roundNumber_byteNumber
                                + 5*q5_roundNumber_byteNumber + 5.4150*q5_4150_roundNumber_byteNumber + 6*q6_roundNumber_byteNumber + 
                                + 7*q7_roundNumber_byteNumber)
"""


class Skinny128:
    '''
    Convert the differential analysis of Skinny128-256 to a MILP problem, in order to obtain the best differential trail, 
    and compute the differential effect for a given fixed input/output differences
    '''
    count = 0
    def __init__(self, param, exact = None):
        self.blocksize = param['blocksize']
        self.rounds = param['rounds']
        self.start_weight = param['sweight']
        self.end_weight = param['endweight']
        self.time_limit = param['timelimit']
        self.mode = param['mode']
        self.fixed_variables = param['fixedVariables']
        self.exact = exact #exact is a boolean variable indicating whether the model is exact or not. In the non-exact model all DDT entries equal or less than 16 (or 2^-4) are ignored
        self.total_weight = None
        ######################
        ### Instead of Big-M method, it is better to use the indicator constraint "=>" to avoid the numerical issues
        ## if you want to model "if binary x is 0, then a continuous variable y should be 0 as well", 
        ## you can do this using an indicator constraint (available since version 7.0): x = 0 -> y = 0
        self.big_m = 2*8 
        ## According to the page 128 of https://tosc.iacr.org/index.php/ToSC/article/view/805/759, M = 2*n, where n is the size of Sbox, is sufficiently big.
        ## The range of numerical coefficients is one indication of potential numerical issues.
        ## As a very rough guideline, the ratio of the largest to the smallest coefficient should be less than 1e9 (10^9).
        ## Using the indicator constraints causes some problems in computing the clustering effect! (at least when we use Gurobi v8).
        ## Using the indicator constraints causes the performance to be decreased too! (at least when we use Gurobi v8).
        ######################
        self.eps = 1e-3
        self.obj_func = ''
        self.used_variables = [] # All of the variables used in the MILP model are stored in this list
        self.permuteation = [0x0, 0x1, 0x2, 0x3, 0x7, 0x4, 0x5, 0x6, 0xa, 0xb, 0x8, 0x9, 0xd, 0xe, 0xf, 0xc]
        self.tk_permutation = [0x9, 0xf, 0x8, 0xd, 0xa, 0xe, 0xc, 0xb, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7]
        self.model_filename = "skinny128-256_" + str(self.rounds) + "r.lp"
        fileobj = open(self.model_filename, "w")
        fileobj.close()

        # The precomputed constraints for Sbox layer
        # In the following constraints, it is supposed that a0, and b0 are MSBs, and a7, and b7 are LSBs
        self.q2_ineqs = ['- a6 - a7 >= -1', 'a6 - b4 >= 0', 'a7 - b2 >= 0', 'a3 - b1 >= 0', '- a4 + b3 >= 0', '- a5 + b7 >= 0', '- b3 - b7 >= -1', 'a2 - b0 >= 0', 'a0 - b6 >= 0', '- a1 + b5 >= 0', '- a3 - a7 >= -1', '- a3 - a6 >= -1', '- a2 - b7 >= -1', '- a0 - b3 >= -1', 'a4 - a6 + b4 >= 0', 'a4 + a5 - a7 + b2 >= 0', '- b5 - b6 >= -1', '- b3 - b5 >= -1', '- a2 - a4 >= -1', '- a0 - a2 >= -1', '- b0 - b1 >= -1', '- b3 - b4 >= -1', 'a1 + a4 + a5 + b0 + b1 + b2 + b4 + b6 >= 1', '- a3 + b6 - b7 >= -1', '- b2 - b3 >= -1', '- b5 - b7 >= -1', '- a0 - b1 >= -1', '- a2 - b5 >= -1', '- a2 - b4 >= -1', '- b2 - b7 >= -1', '- b0 - b2 >= -1', '- a0 - a5 >= -1', '- a0 - b4 >= -1', 'a0 - a3 + b1 + b5 >= 0', '- a0 - b2 >= -1', '- b1 - b5 >= -1', '- b2 - b5 >= -1', '- b4 - b5 >= -1', '- a5 - b4 >= -1', '- a4 - b1 >= -1']
        self.q2_4150_ineqs = ['a3 - b7 >= 0', '- b6 >= 0', '- b5 >= 0', '- b2 >= 0', '- b1 >= 0', '- a7 >= 0', '- a5 >= 0', '- a4 >= 0', '- b3 - b4 >= -1', '- a0 - a1 >= -1', 'a0 - a2 >= 0', 'a1 - a6 >= 0', 'a2 - b0 >= 0', 'b4 - b7 >= 0', '- a3 + b0 + b7 >= 0', 'a3 + b4 >= 1', 'a6 - b4 >= 0']
        self.q2_6781_ineqs = ['- b5 >= 0', '- b3 >= 0', '- b2 >= 0', '- b1 >= 0', '- b0 >= 0', '- a7 >= 0', '- a5 >= 0', '- a4 >= 0', '- a2 >= 0', 'a0 >= 1', 'a1 >= 1', 'a6 >= 1', 'b4 >= 1', 'b6 >= 1', 'a3 - b7 >= 0', '- a3 + b7 >= 0']
        self.q3_ineqs = ['- b0 - b4 >= -1', '- a1 - b2 >= -1', '- b2 - b5 >= -1', '- a4 - b0 >= -1', '- a6 - b0 >= -1', '- b1 - b6 >= -1', '- a0 + b5 + b6 >= 0', 'a4 + b0 + b1 - b3 >= 0', '- a2 + b0 + b1 + b2 >= 0', '- a4 + b1 + b3 >= 0', 'a5 + b4 + b6 - b7 >= 0', '- a5 + b4 + b6 + b7 >= 0', 'a0 + a1 - a3 + b1 >= 0', '- a7 - b6 >= -1', 'a4 - a6 + b2 + b4 >= 0', '- a0 + a1 - b5 >= -1', 'a3 - a7 - b1 >= -1', '- b1 - b7 >= -1', '- a1 + a5 + a7 + b5 >= 0', '- b1 - b4 >= -1', '- a1 - b3 - b7 >= -2', 'b0 - b3 - b6 >= -1', '- a4 + a7 - b5 >= -1', 'a4 + a6 + a7 - b2 >= 0', '- a5 - b0 >= -1', 'a1 + a5 + a6 - b5 >= 0', 'a5 - a6 - a7 - b4 >= -2', 'a2 + a6 + b1 - b3 - b5 >= -1', '- a1 + a6 - a7 + b7 >= -1', 'a4 + a5 + b0 + b2 + b4 + b5 >= 1', '- a6 + a7 - b2 + b7 >= -1', 'a6 + b2 + b3 - b4 >= 0', '- a5 - a6 - b5 >= -2', 'a1 + a6 + b0 + b1 + b3 + b4 + b5 + b7 >= 1', 'a2 + a6 + b1 + b3 + b4 + b6 + b7 >= 1', 'a1 + a3 + b2 + b4 + b5 + b6 + b7 >= 1', '- a1 - a5 - b5 >= -2', '- a0 - a3 + b6 - b7 >= -2', '- a5 - b3 - b4 >= -2', '- a0 - b1 + b3 >= -1', '- a0 - b0 - b6 >= -2', 'a0 + b0 + b5 - b6 >= 0', 'a0 + a1 + a2 + a4 + b1 + b2 + b4 + b5 >= 1', 'a0 - a3 - a6 + b3 - b5 + b7 >= -2', '- a1 - a7 - b5 >= -2', '- a5 - b4 - b6 >= -2', '- a6 - a7 - b1 + b5 >= -2', '- b2 - b6 >= -1', '- b2 - b3 - b7 >= -2', '- a5 - b2 - b4 >= -2', '- a4 - b1 - b2 >= -2', '- b0 - b5 - b6 >= -2', '- b0 - b1 - b5 >= -2', 'a4 + a5 + a7 - b4 + b5 + b6 >= 0', '- a1 - a6 + b3 + b5 >= -1', '- a1 - b4 - b6 >= -2', 'a2 - a6 - b1 >= -1', 'a0 + a7 - b1 - b3 - b5 >= -2', '- a7 - b0 - b1 >= -2', '- a2 - a4 + a6 + b2 >= -1', '- b2 - b3 - b4 >= -2', '- a6 - a7 - b2 - b7 >= -3', '- a1 + b5 - b6 - b7 >= -2', 'a0 - a1 + a3 - b4 - b7 >= -2', '- a0 + a3 - b4 + b6 + b7 >= -1', '- a5 - b5 - b6 - b7 >= -3', '- a2 - b0 - b2 - b3 >= -3']
        self.q3_1926_ineqs = ['- b7 >= 0', '- b5 >= 0', '- b4 >= 0', '- b2 >= 0', '- b1 >= 0', '- a7 >= 0', '- a6 >= 0', '- a5 >= 0', '- a4 >= 0', '- a3 >= 0', '- a1 >= 0', 'a0 >= 1', 'a2 >= 1', 'b0 >= 1', 'b6 >= 1']
        self.q3_4150_ineqs = ['- b5 >= 0', 'a0 - b6 >= 0', '- b2 - b4 >= -1', 'b4 - b7 >= 0', 'a1 - a6 >= 0', '- a1 - b0 >= -1', '- b1 - b4 >= -1', '- a3 - a4 + b7 >= -1', '- a0 + b0 + b6 >= 0', 'a3 - a5 + b7 >= 0', 'a6 - b4 >= 0', 'a0 + a4 + a5 >= 1', '- a4 + b3 >= 0', 'a3 - a7 + b4 >= 0', 'a7 - b2 >= 0', '- a5 + b4 >= 0', 'a4 - a7 - b6 >= -1', 'a7 - b3 - b6 >= -1', '- a4 + a7 >= 0', 'b1 + b2 + b4 >= 1', '- a3 - b1 >= -1', '- a2 - b4 >= -1', 'a3 + b3 - b6 + b7 >= 0', '- a5 - b3 >= -1', '- a3 + b3 - b7 >= -1', 'a3 - b3 - b7 >= -1', 'a2 + b1 + b3 + b4 >= 1', '- a2 - b2 - b3 >= -2']
        self.q3_6781_ineqs = ['- b5 >= 0', '- b4 >= 0', '- b2 >= 0', '- b1 >= 0', '- a7 >= 0', '- a6 >= 0', '- a5 >= 0', '- a4 >= 0', '- a3 >= 0', '- a1 >= 0', 'a0 >= 1', 'a2 >= 1', 'b0 >= 1', 'b6 >= 1', 'b7 >= 1']
        self.q4_ineqs = ['- a6 - b2 - b6 >= -2', '- a0 + b0 + b5 + b6 >= 0', 'a5 + b4 + b6 - b7 >= 0', '- a5 + b4 + b6 + b7 >= 0', 'a4 - a6 + b2 + b4 >= 0', 'a4 + a5 - a7 + b2 >= 0', 'a4 + a6 + b2 - b4 >= 0', 'a1 + a5 + a6 - b5 >= 0', 'a0 + b0 + b5 - b6 >= 0', 'a4 + b0 + b1 - b3 >= 0', '- a2 + b0 + b1 + b2 >= 0', '- a1 + a5 + a6 + b5 >= 0', '- a5 - b1 - b4 >= -2', '- a4 + b0 + b1 + b3 >= 0', 'a2 - b0 + b1 + b2 >= 0', 'a0 + a1 - a3 + b1 >= 0', '- a0 + a1 - b1 - b4 >= -2', '- b0 - b1 - b4 >= -2', '- a5 - a6 - b0 + b2 >= -2', 'a0 + a1 + a3 - b1 >= 0', '- a1 + a7 - b2 - b5 >= -2', '- b0 - b1 - b5 - b6 >= -3', '- a1 - a7 - b5 - b6 >= -3', '- a1 - b2 - b4 + b5 >= -2', '- a1 - a6 - b0 + b4 >= -2', '- a0 + a1 - b2 - b5 >= -2', '- a0 + a1 - b0 - b5 >= -2', '- a4 - b1 + b4 + b5 - b6 >= -2', 'a4 + a6 + a7 - b2 + b4 >= 0', '- a6 - b2 - b4 - b5 >= -3', '- a0 + a5 - a7 - b4 + b6 >= -2', '- a5 - b3 - b4 - b5 >= -3', '- a4 - b2 - b6 >= -2', '- a4 - b0 - b7 >= -2', '- a1 - a5 + a7 - b4 - b6 >= -3', '- a5 - b3 - b4 - b6 >= -3', '- a3 - b0 + b1 + b5 - b6 >= -2', '- a2 - a4 - a5 + a6 + b2 >= -2', '- a0 + a3 - a4 - b0 + b1 >= -2', 'a2 - a4 + a6 - b1 - b4 >= -2', 'a0 - a3 - a5 - b4 - b7 >= -3', '- a1 - a5 - b1 >= -2', '- a0 - a4 - a5 + b6 >= -2', '- a1 - a4 + a5 + a7 - b6 >= -2', 'a7 - b0 - b2 - b4 >= -2', '- a4 - b1 - b3 - b6 >= -3', 'a0 - a1 + a3 - b0 + b6 - b7 >= -2', 'a0 - a1 + a3 - a5 + b7 >= -1', '- a5 - b0 - b1 >= -2', 'a0 - a1 - a3 - b1 + b6 - b7 >= -3', '- a2 - a4 - a6 + b2 - b4 >= -3', '- b1 - b2 + b5 - b6 >= -2', 'a2 + a4 - b0 + b1 + b3 >= 0', '- a2 + a4 + b1 - b2 - b3 >= -2', '- a5 + a6 - a7 + b3 - b4 >= -2', 'a4 + a5 + a6 + a7 + b0 + b6 >= 1', 'a1 + a4 - b1 - b3 - b5 + b6 >= -2', '- a1 + a5 - a6 - a7 - b5 >= -3', 'a0 - a4 + b0 + b3 - b5 + b6 >= -1', '- a0 + a4 + b0 - b1 + b3 + b6 >= -1', '- a5 - b2 - b3 - b4 >= -3', '- a0 - a7 - b5 - b6 >= -3', 'a1 + a5 - a6 - a7 + b2 + b5 >= -1', 'a2 - a6 + b0 - b1 + b2 + b4 >= -1', 'a1 - a4 + a5 + a7 + b2 - b5 >= -1', 'a0 - a1 - a7 + b0 - b2 - b3 >= -3', '- a1 - a5 - b2 - b3 >= -3', 'a4 + a7 - b2 - b5 + b7 >= -1', 'a3 - b0 + b2 + b4 + b5 - b6 + b7 >= -1', 'a0 + a4 - b1 + b3 - b5 - b6 >= -2', '- a4 - b0 - b4 >= -2', '- a0 + a5 + a6 - b0 + b5 - b7 >= -2', '- a3 + a7 - b0 - b2 + b7 >= -2', 'a0 - a3 + a4 - a6 - b0 + b7 >= -2', 'a1 - a5 + a6 - b3 + b5 - b6 + b7 >= -2', '- a7 - b0 + b2 - b6 >= -2', '- a0 - a5 - b1 >= -2', '- a1 - a4 + a7 - b1 + b5 >= -2', '- a4 - a7 - b2 - b5 >= -3', 'a2 - a4 + a6 - b0 + b2 >= -1', '- a1 + a7 + b0 + b1 + b3 + b4 + b7 >= 0', '- a0 - a1 + a5 + b1 - b4 + b5 >= -2', 'a1 - a6 + a7 - b2 + b5 + b7 >= -1', 'a1 + a7 + b4 - b5 - b6 - b7 >= -2', 'a3 + a4 - b0 - b1 + b5 >= -1', '- a1 + a7 + b4 + b5 - b6 - b7 >= -2', '- a1 - a5 - b0 >= -2', 'a0 + a1 + b0 + b2 + b4 + b6 + b7 >= 1', '- a1 - b1 - b2 + b5 >= -2', '- a4 - b2 - b5 - b7 >= -3', '- a0 - a4 - b1 - b3 - b5 >= -4', '- a6 - b0 - b2 - b4 >= -3', '- a0 + a1 - a5 - b4 - b5 >= -3', '- a1 - a5 - b2 - b5 >= -3', '- a0 + a3 - a6 + b1 + b5 + b6 >= -1', '- a1 + a3 + a5 + b0 - b4 + b5 + b7 >= -1', 'a4 - a6 - a7 + b4 - b7 >= -2', '- a4 - b1 - b2 - b7 >= -3', 'a0 - a1 + a4 - a6 - b1 - b3 >= -3', '- a0 + a3 - b0 + b4 + b6 - b7 >= -2', 'a1 - a5 - b2 + b5 - b6 + b7 >= -2', '- a0 + a1 - a6 - a7 + b4 - b7 >= -3', '- a6 - a7 - b1 + b3 - b4 + b6 >= -3', '- a1 - a2 - b4 - b6 >= -3', 'a2 - a5 - b1 - b6 - b7 >= -3', '- a4 - b0 - b1 - b2 >= -3', '- a5 + b0 + b1 + b2 + b3 + b5 + b6 >= 0', 'a5 + b0 + b1 + b2 - b3 + b5 + b6 >= 0', 'a1 + a4 + a5 + b0 + b1 + b2 + b5 >= 1', 'a0 + a3 - b1 - b4 + b7 >= -1', '- a2 - a4 + a6 + b4 - b5 >= -2', '- a0 - a3 - b1 + b5 + b6 >= -2', '- a1 - a5 - b3 - b5 >= -3', 'a6 + a7 + b0 + b1 + b3 + b5 - b6 >= 0', '- a0 - a1 - a3 + b0 + b3 - b4 + b6 + b7 >= -3', '- a0 - a1 + a3 + b0 + b3 - b4 + b6 - b7 >= -3', '- a1 - a3 + a5 + b0 - b4 + b5 - b7 >= -3', 'a3 + a4 - b1 - b3 + b6 - b7 >= -2', 'a1 + b0 + b1 + b4 + b5 + b6 + b7 >= 1', '- a6 - b1 - b2 - b4 >= -3', '- a2 - a6 - b0 - b1 >= -3', 'a2 - a4 - b0 - b2 - b3 >= -3', '- a0 - a1 + a3 + a5 + b1 - b4 + b6 + b7 >= -2', '- a2 - a4 + b1 - b2 + b3 >= -2', '- a0 - b1 - b3 - b5 - b6 >= -4', '- a0 - a1 - a3 + a5 + b1 + b6 - b7 >= -3', '- b2 - b5 - b6 - b7 >= -3', 'a3 + b1 - b2 - b4 - b5 - b7 >= -3', 'a4 + a6 + b1 - b2 + b4 + b5 + b6 + b7 >= 0', '- a3 + a4 + b2 + b4 + b5 + b6 + b7 >= 0', '- b0 - b1 - b2 - b5 >= -3', '- a5 - a6 - a7 + b4 - b5 + b7 >= -3', '- a6 + a7 - b2 - b4 >= -2', 'a0 - a3 + b1 - b3 - b4 + b7 >= -2', 'a0 - a1 + a3 + b1 - b3 - b4 - b7 >= -3', 'a5 + a6 + b0 + b1 + b3 + b5 + b6 >= 1', 'a1 + b0 + b1 + b3 + b4 + b5 + b6 >= 1', 'a4 + b1 + b2 + b4 - b5 + b6 + b7 >= 0', '- a0 - a7 - b0 + b2 + b7 >= -2', 'a0 + a4 + a5 + a7 + b1 + b4 + b5 >= 1', '- a3 + b1 - b2 - b4 + b6 + b7 >= -2', '- a0 + a1 - a5 + a7 - b3 + b7 >= -2', 'a4 - b1 + b3 - b4 - b6 >= -2', 'a4 + a5 + a6 + b0 + b4 + b5 + b6 >= 1', 'a1 + a3 - a4 + b2 + b4 + b5 + b6 - b7 >= -1', '- a1 + a5 + b0 + b1 + b2 + b3 - b5 + b6 >= -1', 'a5 + b0 + b1 + b2 + b3 + b4 >= 1', '- a4 - b1 - b2 - b4 >= -3', 'a0 + a1 + a5 + b0 + b1 + b2 + b3 >= 1', '- a1 - b2 - b6 - b7 >= -3', '- a0 - b0 - b2 - b4 >= -3', 'a0 + a1 + b0 + b1 + b2 + b3 + b4 + b6 >= 1', '- a0 - a3 - b1 - b4 + b6 + b7 >= -3', '- a0 + a2 - b0 + b2 - b6 >= -2', '- a1 - a5 - a6 - a7 + b4 + b7 >= -3', '- a1 + a6 - b3 + b5 - b6 - b7 >= -3', 'a0 + a7 + b0 + b1 + b3 + b4 + b7 >= 1', 'a6 - a7 + b1 - b3 - b5 - b6 - b7 >= -4', '- a2 + a6 - a7 + b2 - b6 + b7 >= -2']
        self.q4_4150_ineqs = ['a1 - b5 >= 0', 'a0 - b6 >= 0', '- a6 + b4 >= 0', 'a1 + b0 >= 1', '- a5 - b5 >= -1', '- a4 + a5 + b2 >= 0', '- a4 - a7 - b2 >= -2', '- a3 - b1 - b4 + b7 >= -2', '- a5 + b4 >= 0', 'a3 + a6 + a7 + b7 >= 1', 'a0 + a5 + a6 >= 1', '- a3 + b2 + b6 - b7 >= -1', '- a7 - b1 - b6 >= -2', 'a6 + b2 + b3 - b4 >= 0', '- a6 - b1 >= -1', 'a1 + a7 - b4 >= 0', '- a2 + a6 + b1 - b3 - b4 >= -2', 'a3 - b1 - b7 >= -1', 'a3 - b0 - b4 + b6 + b7 >= -1', 'a3 - b0 + b5 + b6 - b7 >= -1', 'a5 + a6 + a7 - b2 >= 0', 'a2 - b0 + b1 + b3 >= 0', 'a2 - b0 + b1 + b2 >= 0', '- a6 - b0 - b2 >= -2', '- a0 + b0 + b5 + b6 >= 0', '- a3 + a6 + a7 - b4 - b7 >= -2', '- a3 - a5 - a6 - b7 >= -3', 'a4 + b0 + b1 - b3 >= 0', '- a1 + b4 >= 0', '- a1 - b0 + b5 + b6 >= -1', 'a3 + b2 + b6 + b7 >= 1', 'a3 + a5 - a6 - b7 >= -1', '- a3 + a5 - a6 + b7 >= -1', '- a1 + a6 - b2 - b6 >= -2', '- a3 - b0 - b1 + b6 >= -2', '- a7 + b2 + b3 >= 0', '- a3 + b1 - b5 - b7 >= -2', 'a3 + b1 - b5 + b7 >= 0', 'a3 - a5 - a6 + b7 >= -1', '- a5 + a6 - a7 - b2 >= -2', '- a2 - a5 + b2 >= -1', '- a6 + a7 + b0 + b3 >= 0', 'a3 - b0 + b2 - b7 >= -1', '- a3 + a6 - a7 - b6 + b7 >= -2', '- a4 - a5 - b2 >= -2', '- a7 - b0 + b2 >= -1', '- a3 - a7 - b0 - b6 >= -3', 'b1 + b4 + b7 >= 1', '- b2 + b4 - b7 >= -1', '- b1 + b3 - b5 >= -1', '- a2 - b1 - b6 >= -2', 'a3 + a6 - a7 + b2 - b6 - b7 >= -2']
        self.q5_ineqs = ['- a0 + a3 + a5 + a7 - b0 - b2 - b7 >= -3', '- a4 + b0 + b1 + b3 >= 0', 'a4 - a6 + b2 + b4 >= 0', 'a4 + b0 + b1 - b3 >= 0', '- a4 - a5 - b0 - b4 >= -3', '- a1 + a5 + a6 + b5 >= 0', '- a0 + b0 + b5 + b6 >= 0', 'a0 + b0 + b5 - b6 >= 0', 'a4 + a5 - a7 + b2 >= 0', '- a5 + b4 + b6 + b7 >= 0', 'a2 - b0 + b1 + b2 >= 0', 'a5 + b4 + b6 - b7 >= 0', '- a2 + b0 + b1 + b2 >= 0', 'a1 + a5 + a6 - b5 >= 0', 'a4 + a5 + a7 - b2 >= 0', 'a0 + a1 + a3 - b1 >= 0', 'a0 + a1 - a3 + b1 >= 0', '- a1 - a4 - a5 - b0 >= -3', '- a0 + a1 - a5 - b1 - b4 >= -3', '- a6 - b0 - b1 - b2 - b4 >= -4', '- a0 - a4 - a5 - b2 - b5 >= -4', '- a0 - a6 - b2 - b5 - b6 >= -4', 'a0 + a1 + b0 + b2 + b4 >= 1', 'a4 - a5 + a6 - a7 - b4 >= -2', 'a0 - a1 - a6 - b2 - b6 >= -3', 'a4 + a6 + b2 - b4 >= 0', '- a5 - b0 - b1 - b4 >= -3', '- a0 + a1 + a4 - b0 - b1 - b5 >= -3', 'a0 + a1 + a5 + b0 + b2 >= 1', 'a6 + a7 - b1 - b2 + b5 - b6 >= -2', '- a4 + a6 - b0 - b1 - b2 - b5 >= -4', '- a3 - a4 - a5 - b2 - b4 >= -4', '- a0 - a4 + b3 - b5 - b6 >= -3', 'a1 - a3 - a6 - b0 - b2 - b6 >= -4', 'a4 - a6 + a7 - b2 - b4 >= -2', 'a4 - a5 - a6 - a7 + b4 >= -2', 'a4 + a6 + a7 - b2 + b4 >= 0', '- a2 + a4 + b1 - b2 - b3 >= -2', '- a2 - a4 + b1 - b2 + b3 >= -2', '- a1 - b0 - b1 - b4 - b5 - b6 >= -5', 'a2 - a4 - b0 + b1 - b3 >= -2', 'a2 + a4 - b0 + b1 + b3 >= 0', '- a1 - a5 - b0 - b1 >= -3', 'a1 - a6 - b1 - b2 + b5 - b6 >= -3', '- a1 - a5 + a7 - b0 - b2 - b6 >= -4', '- a1 - a6 - b0 - b1 - b2 >= -4', '- a1 - a4 - b2 - b5 - b6 >= -4', '- a1 - a4 + a5 + a7 + b2 + b5 >= -1', '- a1 + a2 - a6 - b0 + b2 - b6 >= -3', 'a1 + a5 - a6 - a7 + b2 + b5 >= -1', '- a1 - a4 + a5 - a7 - b2 + b5 >= -3', '- a0 - a4 - b0 - b5 - b6 >= -4', '- a1 + a5 + a7 + b0 + b2 - b5 + b6 >= -1', '- a1 + a5 - a6 - a7 + b2 - b5 >= -3', '- a0 + a1 - b2 - b4 - b5 >= -3', '- a0 + a5 + a7 - b2 - b4 + b6 >= -2', '- a4 - b0 - b1 - b2 - b7 >= -4', '- a2 - a6 - b0 - b1 + b2 + b4 >= -3', '- a2 - a4 - a6 + b0 + b2 - b4 >= -3', '- a0 + a4 + b0 - b3 - b5 - b6 >= -3', 'a2 - a4 + a6 - b0 + b2 + b4 >= -1', 'a2 + a6 + b0 - b1 + b2 - b4 >= -1', '- a2 - a4 + a6 + b0 + b2 + b4 >= -1', 'a1 + a5 - a6 + a7 - b2 + b5 >= -1', '- a0 + a1 - a5 - b3 - b4 - b5 >= -4', 'a1 - a4 + a5 + a7 + b2 - b5 >= -1', 'a2 - a6 + b0 - b1 + b2 + b4 >= -1', 'a0 + a1 + a4 + b0 + b4 + b6 >= 1', '- a0 - a4 + b0 - b1 - b3 + b6 >= -3', 'a1 - a4 + a5 - a7 - b2 - b5 >= -3', 'a0 - a4 + b0 - b1 - b3 - b6 >= -3', '- a0 + a4 + b0 - b1 + b3 + b6 >= -1', 'a6 + b0 + b1 + b3 + b4 + b5 >= 1', 'a0 + a4 + b0 - b1 + b3 - b6 >= -1', 'a0 + a4 + b0 - b3 - b5 + b6 >= -1', 'a5 - a6 + a7 + b0 + b3 - b4 + b6 >= -1', 'a0 - a4 + b0 + b3 - b5 + b6 >= -1', '- a1 - a5 - a7 + b1 + b2 + b5 - b6 >= -3', '- a6 - b1 - b2 + b4 + b5 - b6 >= -3', '- a0 + a5 - a7 - b0 + b2 - b4 + b6 >= -3', 'a1 - a3 - a5 - b0 + b1 + b5 - b6 >= -3', '- a1 - a4 - a5 - b3 - b4 - b6 >= -5', '- a4 - a7 - b1 - b2 + b5 - b6 >= -4', 'a1 - a5 + a7 + b2 + b4 + b5 + b7 >= 0', '- a1 - a3 - a5 - b0 - b4 + b5 - b7 >= -5', 'a0 - a1 - a4 - b0 - b6 >= -3', '- a2 + a6 - b0 - b1 + b2 - b4 >= -3', 'a1 - a4 - a5 + a6 + b4 + b5 + b7 >= -1', 'a1 - a5 - a7 - b2 + b4 + b5 + b7 >= -2', '- a0 - a1 + a3 - b0 - b1 + b6 - b7 >= -4', '- a0 - a3 - b0 - b1 - b4 + b6 + b7 >= -4', 'a2 - a4 - a6 - b0 + b2 - b4 >= -3', '- a1 - a5 + a7 + b4 - b5 + b7 >= -2', '- a1 - a5 - b0 - b5 - b6 + b7 >= -4', 'a1 + a7 + b2 + b4 - b5 - b6 - b7 >= -2', 'b0 + b2 + b4 + b6 + b7 >= 1', '- a0 - a1 + a3 - a5 + b1 - b4 + b6 - b7 >= -4', '- a0 - a1 - a3 - a5 + b1 + b6 + b7 >= -3', 'a0 - a1 + a4 - a5 - b1 - b3 - b4 >= -4', 'a1 - a4 + a6 + b4 - b5 - b6 - b7 >= -3', 'a4 + a5 + a6 + b0 + b6 >= 1', 'a1 - a5 - a7 - b2 + b4 - b5 - b6 - b7 >= -5', '- a0 + a1 + a3 - a6 + b1 + b5 + b6 >= -1', 'a0 - a1 - a4 - a5 + b3 - b4 >= -3', '- a1 + a5 - a6 + a7 - b2 - b5 >= -3', '- a0 - a3 + a5 - a7 - b0 - b1 - b7 >= -5', 'a0 + a1 + a4 + b1 + b4 + b6 >= 1', 'b0 + b1 - b2 + b3 + b5 + b6 >= 0', '- a1 - a6 - b0 + b4 - b6 >= -3', 'a1 + a3 - b0 - b1 - b4 - b6 >= -3', 'a0 + a1 + a4 + a6 - a7 + b1 - b2 >= -1', '- a1 - a6 + b0 + b1 - b2 - b4 - b6 >= -4', 'a3 - a5 - b0 - b1 - b6 >= -3', '- a4 - a5 - b2 - b4 - b6 >= -4', 'a4 - a5 - b1 + b3 - b4 - b6 >= -3', '- a1 - a4 - a5 - b1 - b2 >= -4', 'a4 + a5 + b0 + b2 + b4 >= 1', '- a1 + a3 - a5 - b0 - b4 + b5 + b7 >= -3', '- a1 + a3 - b0 - b1 - b4 + b5 + b7 >= -3', '- a3 - a4 - b0 + b1 - b6 + b7 >= -3', '- a2 - a5 - b0 - b1 - b5 - b6 - b7 >= -6', '- a0 - b0 - b1 - b2 - b4 >= -4', '- a0 + a3 - a5 - b1 + b6 + b7 >= -2', '- a0 - a3 - a5 - b1 - b4 + b6 - b7 >= -5', 'a1 + a3 - a4 + a5 + a7 - b0 - b1 + b4 >= -2', '- a0 + a3 - a4 - b0 + b1 - b4 + b6 + b7 >= -3', '- a1 - a2 - a7 + b2 + b4 - b5 - b6 - b7 >= -5', '- a3 - a4 - a7 - b0 - b2 - b6 >= -5', 'a3 - b0 - b1 - b2 - b6 >= -3', '- a0 + a1 - a3 - a4 + a7 - b0 - b1 + b6 >= -4', '- a1 - a4 - b2 + b4 - b5 - b7 >= -4', 'a4 + a5 + a6 + b1 - b5 + b6 >= 0', 'a0 + a3 - a5 - b1 - b4 - b7 >= -3', 'a0 - a1 - a3 - a5 - b1 + b6 + b7 >= -3', '- a0 + a3 + a5 - b1 - b2 + b6 - b7 >= -3', '- a0 + a1 + a3 + b1 + b5 + b6 - b7 >= -1', '- a1 + a3 - a5 + b0 - b2 - b3 - b4 + b5 - b7 >= -5', 'a0 + a1 + b0 + b4 + b6 + b7 >= 1', 'a0 + a3 + a5 - b1 - b4 - b5 + b6 + b7 >= -2', 'a0 - a1 - a3 + a5 - b1 - b5 + b6 - b7 >= -4', 'a5 + b0 + b1 - b2 + b5 + b6 >= 0', '- a1 + a3 + b0 + b1 - b3 - b4 + b5 + b7 >= -2', 'a0 - a1 + a3 - a5 + b1 - b5 + b6 + b7 >= -2', 'a0 - a3 - a5 + b1 - b4 - b5 + b6 - b7 >= -4', 'a0 - a1 + a3 + a5 + b1 - b5 + b6 - b7 >= -2', 'a0 - a3 + a5 + b1 - b4 - b5 + b6 + b7 >= -2', '- a0 + a3 + a4 + a6 + a7 + b5 + b6 + b7 >= 0', '- a0 + a6 + a7 + b0 + b1 + b3 - b5 - b6 >= -2', '- a4 - a5 - b2 - b4 - b5 >= -4', '- a0 + a4 + a5 + b1 + b2 + b5 - b6 >= -1', '- a1 + a6 - b2 + b4 + b5 - b6 - b7 >= -3', '- a1 - a3 - b0 - b1 + b5 - b7 >= -4', '- a0 - a4 - b0 + b4 - b5 - b7 >= -4', 'a4 + a6 - a7 + b1 - b4 + b5 >= -1', '- a0 + a1 - a3 - b0 - b1 + b6 - b7 >= -4', '- a1 + a3 + a5 - b1 - b2 - b4 + b5 + b7 >= -3', '- a1 - a3 + a5 - b1 - b2 + b5 - b7 >= -4', '- a1 + a3 + a5 - b0 - b2 + b5 - b7 >= -3', 'a1 - a5 - a6 - a7 + b2 + b4 - b5 + b7 >= -3', '- a1 - a3 + a5 - a7 - b0 + b1 - b4 + b5 + b7 >= -4', '- a1 + a4 + a5 + b1 + b2 - b5 + b6 >= -1', 'b0 + b1 + b2 + b4 + b5 >= 1', 'a0 + a1 + b2 + b4 + b6 + b7 >= 1', '- a0 + a3 + a5 + b1 - b2 - b4 + b6 + b7 >= -2', 'a0 - a3 - a4 - b0 - b2 - b4 + b7 >= -4', '- a0 - a1 - a3 + a5 + b1 - b2 + b6 - b7 >= -4', '- a1 + a2 + a3 - a5 + b2 - b4 + b5 - b7 >= -3', '- a1 + a2 - a3 - a5 + b2 - b4 + b5 + b7 >= -3', '- a0 + a1 - a5 - b0 - b4 - b5 >= -4', '- a1 - a5 + a6 + b1 - b3 - b5 - b6 + b7 >= -4', 'a0 + a1 + b1 + b4 + b6 + b7 >= 1', '- a1 + b0 + b1 + b2 + b3 - b5 + b6 >= -1', '- a5 + b0 + b1 + b2 - b3 + b5 + b6 >= -1', 'a0 - a1 + a4 + a6 + a7 + b0 + b3 - b6 >= -1', '- a0 + a6 - a7 - b0 + b2 - b4 >= -3', 'a4 + a5 + a6 + b1 + b5 - b6 + b7 >= 0', 'a3 - b0 - b1 + b5 - b6 + b7 >= -2', '- a1 + a5 - a7 + b0 + b3 - b4 + b5 - b6 >= -3', 'a4 - a5 + a6 + b1 - b2 + b4 + b5 - b6 - b7 >= -3', 'a1 + a4 + b1 + b4 + b5 + b6 - b7 >= 0', '- a2 - a5 - b0 - b1 + b5 + b7 >= -3', 'a1 - a4 - a6 + a7 - b2 + b5 - b6 - b7 >= -4', '- a0 + a1 - a3 - a7 - b2 + b4 + b5 + b6 + b7 >= -3', 'a4 + a6 + a7 + b1 + b4 + b5 - b6 - b7 >= -1', '- a1 + a5 - a7 + b0 - b1 - b3 - b4 + b5 + b6 >= -4', '- a1 - a5 - a6 - a7 + b1 + b4 - b6 - b7 >= -5', '- a1 - a5 - b2 - b5 - b6 + b7 >= -4', '- a4 - a5 - a6 + a7 - b2 - b5 + b7 >= -4', '- a0 + a1 + a5 + a7 - b0 - b2 - b4 >= -3', 'a4 + a5 + b2 + b4 + b5 - b6 + b7 >= 0', '- a1 + a7 + b2 + b4 + b5 - b6 - b7 >= -2', '- a1 + a2 + b2 + b4 + b5 - b6 - b7 >= -2', 'a1 - a2 - a7 + b0 + b2 + b4 + b5 - b7 >= -2', '- a1 - a5 - b0 - b4 - b5 - b6 >= -5', '- a1 - a2 + a3 - a5 - a7 + b2 + b5 - b6 + b7 >= -4', '- a3 - a5 + a7 - b1 - b4 + b5 - b6 + b7 >= -4', 'a5 + a6 - a7 - b0 - b1 - b5 - b6 >= -4', '- a0 + a1 - a3 + a4 + a5 + b2 - b4 + b5 + b6 >= -2', 'a4 + a5 + a6 + b2 - b5 + b6 >= 0', 'a4 + a6 - b1 - b2 + b4 + b5 + b6 + b7 >= -1', 'a1 + a5 + b0 + b1 + b2 + b5 >= 1', 'a4 + a5 + b1 + b2 + b4 >= 1', 'a7 + b1 + b2 + b4 + b5 + b6 + b7 >= 1', 'a2 - a7 - b0 + b2 + b4 + b5 - b6 - b7 >= -3', '- a1 + a2 - a5 - b1 - b5 - b6 + b7 >= -4', '- a0 - a3 + a5 - b1 - b2 - b4 + b6 + b7 >= -4', '- a0 + a1 - a2 + a6 - a7 + b2 - b5 + b7 >= -3', 'a0 + a5 + b0 + b2 - b5 + b6 >= 0', 'a0 + a1 + a4 + a5 + b1 + b2 >= 1', 'a4 + a5 + b0 + b1 + b2 >= 1', 'a0 + a1 + b0 + b1 + b2 + b3 >= 1', 'a0 - a1 - b1 + b5 - b6 >= -2', '- a2 - a3 - a5 - a7 + b2 - b4 + b5 - b6 - b7 >= -6', '- a4 - b1 - b2 - b3 - b6 >= -4', 'a0 - a1 - a5 - b4 + b5 - b6 >= -3', 'a3 - a5 + a7 - b1 - b4 - b6 - b7 >= -4', '- a1 - a2 - a5 - a7 + b2 + b4 + b5 + b7 >= -3', 'a2 + a4 + a5 + b2 + b4 + b5 - b7 >= 0', 'a0 - a1 + a5 + a7 + b1 + b2 + b5 + b6 >= 0', 'a1 + a4 + b0 + b1 + b2 + b5 >= 1', '- a3 - a4 + a7 - b0 + b1 + b2 - b6 >= -3', '- a1 + a3 + a5 - a7 - b0 + b1 + b5 - b7 >= -3', '- a5 + a6 + b0 - b1 - b2 - b3 + b4 - b5 + b7 >= -4', 'a1 + b0 + b1 + b4 + b5 + b6 >= 1', 'a0 + a1 + a4 + a7 + b1 + b2 + b4 >= 1', 'a1 + a2 - a5 + b0 + b2 + b4 + b5 + b7 >= 0', '- a1 + a2 + a4 + a5 + b2 - b3 + b5 - b6 >= -2', '- a0 - a2 - a7 + b1 + b2 - b5 - b6 >= -4', '- a1 - a5 - a6 + a7 - b2 - b3 + b7 >= -4', '- a6 - a7 - b0 + b2 + b4 + b5 - b6 - b7 >= -4', '- a4 - a7 + b1 - b2 + b4 + b5 + b6 + b7 >= -2', '- a0 - a1 - a3 - a4 - b0 + b1 + b6 - b7 >= -5', '- a3 + a5 + b0 + b1 + b2 + b5 - b7 >= -1', 'a4 + b0 + b1 + b2 + b4 + b6 >= 1', '- a3 - a5 - b1 - b2 - b4 + b5 - b6 + b7 >= -5', '- a0 + a3 + a5 - a7 - b0 + b1 + b2 - b7 >= -3', 'a0 + a4 + a5 + b2 + b4 + b5 >= 1', '- a0 + a1 + a2 - b1 + b4 - b5 - b6 - b7 >= -4', 'a2 - a5 - a7 - b0 + b2 - b5 + b7 >= -3']
        self.q5_4150_ineqs = ['- a3 - a6 - b7 >= -2', 'a2 + a3 + b3 - b6 + b7 >= 0', 'a3 - a6 + b7 >= 0', 'b2 >= 1', 'b4 >= 1', 'a1 - b5 >= 0', 'a0 - b6 >= 0', 'a4 - a5 >= 0', 'b0 - b1 >= 0', 'a5 + b1 >= 1', '- a1 - b0 + b5 >= -1', '- a4 + b3 >= 0', 'a1 - a4 >= 0', '- a4 - b5 >= -1', '- a6 - b1 >= -1', '- a3 + b5 + b6 - b7 >= -1', 'a7 - b1 >= 0', 'a0 - b1 >= 0', '- a3 - b1 + b6 + b7 >= -1', '- a0 + b1 + b6 >= 0', 'a1 + a3 - b6 >= 0', 'a3 - b5 + b6 - b7 >= -1', 'a3 - a7 + b1 + b7 >= 0', '- a2 - a3 - b3 - b5 - b6 - b7 >= -5', 'a2 + a3 - b3 - b5 - b7 >= -2', '- a2 + a3 - b3 - b5 - b6 + b7 >= -3', '- a1 - a3 - a7 + b5 - b7 >= -3', 'a2 - a3 - b3 - b5 + b7 >= -2', '- a2 + a3 + b3 - b6 - b7 >= -2', 'a2 - a3 + b3 - b5 - b6 - b7 >= -3', '- a2 - a3 + b3 - b5 + b7 >= -2', 'a3 + a6 + a7 - b6 - b7 >= -1', '- a3 + a6 + a7 - b6 + b7 >= -1', 'a3 + b1 + b6 + b7 >= 1']
        self.q6_ineqs = ['a0 + a5 - b0 + b1 + b6 >= 0', 'a4 + b0 + b1 - b3 >= 0', '- a4 + b0 + b1 + b3 >= 0', 'b0 + b1 + b4 + b5 >= 1', 'a4 - a6 + b2 + b4 >= 0', 'a4 + a6 + b2 - b4 >= 0', '- a1 + a5 + a6 + b5 >= 0', 'a1 + a5 + a6 - b5 >= 0', 'a0 + b0 + b5 - b6 >= 0', '- a5 - a6 - a7 + b2 + b4 + b5 + b7 >= -2', 'b0 + b2 + b4 >= 1', 'a0 + a1 + a3 - b1 >= 0', 'a0 + a1 - a3 + b1 >= 0', 'a1 + a5 - a6 + a7 + b5 >= 0', '- a1 + a5 - a6 + a7 - b2 - b5 >= -3', 'a2 + a4 - b0 + b1 + b3 >= 0', '- a1 + a5 - a6 - a7 + b2 - b5 >= -3', 'a2 - a4 - b0 + b1 - b3 >= -2', 'a4 - a6 + a7 - b2 - b4 >= -2', '- a5 + b4 + b6 + b7 >= 0', 'a4 + a5 + a7 - b2 >= 0', '- a0 + b0 + b5 + b6 >= 0', 'a2 - b0 + b1 + b2 >= 0', '- a4 - a5 - b0 - b1 - b2 - b4 >= -5', 'a5 + b4 + b6 - b7 >= 0', 'a4 + a5 - a7 + b2 >= 0', 'a1 + a4 - a5 + b1 + b5 >= 0', 'a5 + b0 + b2 >= 1', '- a4 + a5 + a7 + b2 + b5 >= 0', 'a4 + b0 - b1 + b3 + b6 >= 0', 'a4 - a5 + a6 - a7 - b4 >= -2', '- a0 + a1 - b0 - b1 - b2 - b4 - b5 >= -5', 'a1 - a4 + b1 + b4 + b5 >= 0', 'a4 - a5 - a6 - a7 + b4 >= -2', '- a1 - a4 - b0 - b1 - b2 + b4 - b7 >= -5', '- a1 - a6 - b0 - b1 - b2 + b4 - b6 >= -5', 'a0 + b0 + b3 - b5 + b6 >= 0', '- a0 + a1 - a4 - a5 - b2 - b4 - b5 >= -5', '- a2 - a4 + b1 - b2 + b3 >= -2', 'a4 + a6 - a7 + b0 - b6 >= -1', 'a0 + a1 + b2 + b4 >= 1', '- a2 + a4 + b1 - b2 - b3 >= -2', 'a4 + b1 + b4 + b6 >= 1', 'a0 + a1 + b0 + b2 >= 1', '- a4 + a5 - a7 + b1 - b2 + b6 >= -2', 'b2 + b4 + b6 + b7 >= 1', 'a4 + a6 + a7 - b2 + b4 >= 0', '- a4 + a5 - a7 + b0 + b6 >= -1', '- a1 - a5 - b0 - b1 + b2 - b4 - b5 - b6 >= -6', '- a2 + a6 - b0 - b1 + b2 - b4 >= -3', '- a0 - a4 + b0 + b3 - b5 - b6 >= -3', 'a0 + a5 + a6 + b0 + b6 >= 1', 'a2 - a4 - a6 - b0 + b2 - b4 >= -3', '- a0 + a1 - a5 - b0 - b1 - b4 - b5 >= -5', '- a0 + a4 + b0 - b3 - b5 - b6 >= -3', 'a1 + a3 - a5 - b0 - b1 + b5 - b6 >= -3', '- a1 - a4 - a5 - b0 - b4 - b5 - b6 >= -6', 'a2 - a4 + a6 + b2 + b4 >= 0', '- a0 - a1 - a4 - a5 - b4 + b5 + b6 >= -4', '- a2 - a6 - b1 + b2 + b4 >= -2', '- a4 + a5 - a7 + b1 - b2 + b5 >= -2', 'a0 - a1 - a6 - b0 - b1 - b2 - b6 >= -5', 'a0 + a1 + a5 + b2 >= 1', 'a4 - a5 + a6 + a7 + b1 + b4 >= 0', 'a0 + a1 + a4 + a6 + b4 >= 1', '- a0 - a4 - a5 - b1 - b2 - b3 - b4 >= -6', 'a0 - a4 + b0 - b1 - b3 - b6 >= -3', 'b0 + b4 + b6 + b7 >= 1', 'a0 + a1 + b0 + b4 >= 1', 'a1 - a4 + a5 - a7 - b2 - b5 >= -3', '- a0 + a1 - a3 - a5 - b1 + b5 + b6 >= -3', '- a0 - a1 - a3 - a5 - b1 - b4 + b6 - b7 >= -6', 'b1 + b4 + b6 + b7 >= 1', '- a1 + a5 + a7 + b2 - b5 + b6 >= -1', '- a1 - a5 - a7 - b2 + b4 + b5 - b6 - b7 >= -5', '- a2 - a4 - a6 + b0 + b2 >= -2', '- a0 - a1 + a3 - a5 - b1 + b6 + b7 >= -3', '- a1 - a5 - a7 - b2 + b4 - b5 + b7 >= -4', 'a0 + a4 + b0 - b1 + b3 >= 0', 'a5 + a7 + b0 - b1 - b3 + b6 >= -1', '- a0 - a7 - b0 - b1 - b2 - b4 - b5 - b6 >= -7', 'a1 - a5 - a7 - b2 + b4 - b5 - b6 - b7 >= -5', 'a0 + a1 + b1 + b4 >= 1', 'a0 + a1 + a5 + b1 >= 1', '- a1 - a4 + a6 + b4 + b5 - b6 - b7 >= -3', '- a1 - a4 - a5 + a6 + b4 - b5 + b7 >= -3', 'a1 - a5 - a7 + b4 + b5 + b7 >= -1', 'a1 - a4 + a6 + b4 - b5 - b6 - b7 >= -3', 'a1 - a4 + a5 + a7 + b2 >= 0', '- a1 + a4 - a5 + b1 - b5 + b6 >= -2', '- a0 - a2 + a5 - b1 + b2 + b5 - b6 >= -3', '- a1 - a4 + a5 - a7 - b2 + b5 >= -3', 'a4 + a6 + b1 - b2 + b4 >= 0', '- a1 - a4 - b0 - b1 - b2 + b4 - b6 >= -5', '- a4 + b0 - b1 + b2 - b3 + b6 >= -2', 'a4 + a5 + a6 + b1 - b5 - b6 >= -1', 'a2 + a6 + b0 - b1 + b2 >= 0', 'a0 - a1 - a5 - b1 + b2 - b4 + b5 - b6 >= -4', '- a0 - a1 + a4 - a6 + b0 - b3 - b4 >= -4', '- a0 + a5 + a7 - b0 - b1 - b2 - b4 + b6 >= -4', 'a1 - a5 + b2 + b4 + b5 >= 0', 'a0 + a5 + b2 + b6 >= 1', 'a3 + a5 - b0 - b1 - b2 + b5 - b6 + b7 >= -3', 'a1 + a3 + a4 + b1 + b5 - b6 >= 0', 'a0 - a1 - a4 - a5 - b4 + b5 - b6 >= -4', 'a0 + a1 + a4 + b1 >= 1', '- a5 + a7 + b2 + b4 + b5 - b6 - b7 >= -2', '- a1 - a5 + a7 + b2 + b4 - b5 + b7 >= -2', '- a1 - a5 + b0 + b1 - b2 - b3 - b4 - b6 >= -5', 'a0 - a1 - a5 + b0 - b1 - b2 + b3 - b4 >= -4', '- a0 - a1 - a4 + b0 + b2 + b3 >= -2', 'a1 - a5 + a6 + b4 + b5 + b7 >= 0', 'b0 + b1 + b2 + b3 >= 1', 'a0 + a3 + a4 - a5 - b0 - b4 + b6 - b7 >= -3', 'a0 - a3 - b0 + b1 - b4 + b6 - b7 >= -3', 'a0 - a1 - a3 + a4 - a5 - b0 + b6 + b7 >= -3', 'a0 + a3 - b0 - b1 + b2 - b4 + b6 - b7 >= -3', 'a0 + a3 + a5 - b0 - b4 + b6 + b7 >= -1', 'a0 - a1 + a3 - b0 + b1 + b6 + b7 >= -1', 'a1 - a3 - a5 - b0 + b1 + b5 - b6 >= -3', 'a1 + a5 - a6 + b2 + b5 >= 0', 'a1 + a4 - a5 + a6 + b4 + b5 >= 0', '- a1 - a3 - a5 + a7 - b0 - b1 + b2 - b4 + b5 + b7 >= -5', 'a0 + a1 + a4 + b0 >= 1', '- a1 - a4 - a6 + a7 - b2 - b5 - b6 - b7 >= -6', '- a1 - a3 - a5 - a6 + b0 + b1 + b5 + b7 >= -3', '- a1 - a3 + a5 - b0 - b1 - b2 + b5 - b7 >= -5', 'a1 + a7 + b2 + b4 - b5 - b6 - b7 >= -2', 'a1 + a3 + a4 + b4 + b5 + b6 >= 1', '- a0 - a1 + a4 - a7 - b1 - b4 + b5 + b6 >= -4', '- a1 - a4 - a5 - a6 + a7 - b2 + b4 + b5 + b7 >= -4', 'a4 + a6 - a7 - b1 - b4 + b5 >= -2', '- a0 + a1 + a3 - a5 + b1 + b5 + b6 >= -1', 'a1 + a5 - a6 + b1 + b5 >= 0', '- a0 - a4 + a5 - a6 - b0 + b1 - b4 + b5 - b6 >= -5', '- a0 - a1 + a4 + a7 - b0 - b1 - b2 - b4 + b5 >= -5', '- a0 + b0 - b1 - b3 + b4 + b6 >= -2', 'a4 + a5 + a6 - b0 - b1 - b5 + b6 >= -2', 'a1 - a4 - a5 - a6 + a7 - b2 + b4 - b5 + b7 >= -4', '- a0 + a1 - a4 - a5 - b0 - b4 - b5 >= -5', 'a0 - a1 - a3 - a5 - b1 - b5 + b6 + b7 >= -4', '- a0 - a1 + a3 - a5 + b1 - b4 - b5 + b6 - b7 >= -5', '- a0 + a1 - a3 + a5 - a7 - b2 - b4 + b5 + b6 >= -4', '- a2 + b0 + b1 + b2 >= 0', '- a0 - a1 - a3 - a5 + b1 - b5 + b6 + b7 >= -4', 'a5 + a7 + b1 + b2 + b6 >= 1', '- a1 + a4 + a7 + b0 - b5 + b6 >= -1', 'a0 + a1 + a4 + b4 + b6 >= 1', 'a5 - a6 + a7 + b0 + b3 - b4 - b6 >= -2', 'a0 - a1 - a4 - b0 - b1 - b2 - b6 >= -5', '- a0 + a1 - a4 - a5 - b1 - b2 - b4 >= -5', 'a0 + a1 + b4 + b6 + b7 >= 1', '- a1 + a3 - a5 + a7 - b0 - b1 + b2 - b4 + b5 - b7 >= -5', 'a1 - a4 - a6 + a7 + b4 + b5 - b6 - b7 >= -3', '- a5 + b0 + b1 - b2 - b3 + b5 + b6 >= -2', '- a0 - a3 + a7 - b0 + b1 + b2 + b5 - b6 - b7 >= -4', '- a1 - a3 + a6 + a7 + b0 + b1 + b5 + b7 >= -1', '- a0 + a4 - a6 - b0 + b1 - b2 - b4 + b5 - b6 >= -5', 'a2 + a3 - a5 + a6 - a7 + b2 + b5 - b6 + b7 >= -2', '- a3 + a5 + b0 + b1 + b5 - b7 >= -1', '- a1 - a6 - a7 + b2 + b4 - b5 - b6 - b7 >= -5', 'a0 - a1 - a3 + a5 - b5 + b6 - b7 >= -3', '- a2 + a3 - a5 - b0 - b1 + b2 + b5 - b6 - b7 >= -5', 'a3 + a5 + b0 + b1 + b5 + b7 >= 1', '- a0 - a1 - a3 + a5 - a7 - b0 - b2 - b4 - b5 + b6 + b7 >= -7', 'a4 + a5 + a6 + b2 - b5 >= 0', '- a0 + a5 + a6 + a7 - b0 - b1 - b4 + b5 >= -3', 'a0 + a5 + a7 + b1 + b2 + b5 >= 1', 'a4 + b0 + b4 + b6 >= 1', '- a3 - a4 - a5 - a6 - b0 + b1 - b4 - b6 - b7 >= -7', '- a1 + a5 - a6 + b1 - b5 + b6 >= -2', 'a3 - a4 - a7 - b0 - b1 - b2 + b5 - b6 >= -5', 'a3 - a5 + b0 + b1 + b3 + b5 - b7 >= -1', '- a0 + a3 + a5 - b0 - b1 - b2 - b5 + b6 - b7 >= -5', '- a1 + a3 - a4 - a5 - a6 - b0 + b1 - b4 - b6 + b7 >= -6', '- a2 + a3 + a4 + a7 - b0 - b2 - b3 - b5 - b6 - b7 >= -6', 'a3 - a4 - a5 + b0 - b3 - b4 + b5 + b6 - b7 >= -4', '- a4 - a7 + b4 + b5 + b6 + b7 >= -1', 'a2 + a3 + a4 + a7 - b0 - b2 + b3 - b5 - b6 - b7 >= -4', 'a4 + a5 + b1 + b2 - b5 >= 0', 'a2 + a3 + a4 + a7 - b0 - b1 - b2 - b3 - b5 - b6 + b7 >= -5', 'a1 - a5 - a6 - a7 + b2 + b4 + b7 >= -2', '- a1 + b0 + b2 - b5 + b6 >= -1', '- a0 + a1 - a3 + a5 + a7 - b0 + b4 + b5 - b7 >= -3', '- a1 + a4 - a6 + b0 - b5 + b6 >= -2', '- a3 + a4 + a5 + a6 - b1 + b5 - b6 + b7 >= -2', '- a1 - a2 - a3 - a5 - a6 - b0 - b1 + b5 + b7 >= -6', '- a0 - a1 + a3 + a7 - b0 + b1 + b2 - b4 + b5 - b6 + b7 >= -4', '- a0 - a2 - a3 + a4 + a7 - b0 - b1 - b2 + b3 - b5 - b6 - b7 >= -8', 'a1 + b0 + b1 + b2 + b5 >= 1', '- a1 - a2 - a3 + a7 - b0 - b1 - b2 - b3 - b5 - b6 + b7 >= -8', '- a1 + a2 - a3 + a7 - b0 - b1 - b2 + b3 - b5 - b6 + b7 >= -6', '- a0 + a2 - a3 + a5 + a7 - b0 - b2 - b3 - b7 >= -5', '- a2 + a3 + a7 - b0 - b1 - b2 + b3 - b4 - b5 - b6 + b7 >= -6', '- a0 - a2 + a3 + a5 + a7 - b0 - b1 - b2 - b3 - b5 - b7 >= -7', '- a0 - a2 - a3 + a5 + a7 - b0 - b2 + b3 - b7 >= -5', '- a1 + a2 - a7 + b2 + b4 - b5 - b6 - b7 >= -4', 'a1 + a3 - a6 - b0 - b1 + b5 - b6 >= -3', 'a2 + a3 + a5 + a7 - b0 - b1 - b2 + b3 - b5 - b6 - b7 >= -5', 'a2 + a3 + a5 + a7 - b0 - b2 - b3 - b6 + b7 >= -3', '- a1 - a2 - a5 - b0 - b1 + b4 - b5 + b7 >= -5', 'a3 - a5 - a7 - b0 - b1 - b2 + b5 - b6 - b7 >= -6', '- a0 + a4 - a5 + a7 + b1 + b2 + b5 - b6 >= -2', '- a1 - a3 - a5 - a6 - b0 - b1 - b2 + b5 + b7 >= -6', 'a7 + b0 + b1 + b3 + b5 - b6 >= 0', '- a1 + a3 - a5 + b0 - b1 - b3 - b4 - b5 + b6 - b7 >= -6', '- a1 - a3 - a4 - a5 - b1 - b3 + b5 + b6 + b7 >= -5', '- a1 + a2 - a3 + a6 - a7 + b2 - b4 + b5 - b6 - b7 >= -5', '- a1 + a3 - a4 + a6 + a7 + b1 - b2 + b5 - b6 - b7 >= -4', '- a3 - a4 - a7 - b0 + b1 - b2 + b5 - b6 - b7 >= -6', '- a3 - a4 - a5 + a6 + a7 - b0 - b2 - b4 - b6 + b7 >= -6', '- a0 - a2 - a3 - a6 - a7 - b0 - b1 - b3 + b4 - b5 - b7 >= -9', 'a2 + a3 - a6 - a7 - b0 - b1 - b2 - b3 + b4 - b5 - b7 >= -7', '- a0 + a2 - a3 - a6 - a7 - b0 - b1 - b2 + b3 + b4 - b5 - b7 >= -8', '- a1 + a3 + a6 - a7 + b1 - b2 - b4 + b5 + b7 >= -3', '- a2 + a3 - a6 - a7 - b0 - b1 + b3 + b4 - b5 - b7 >= -6', 'a3 - a4 - a5 - a7 - b1 - b2 - b4 - b6 - b7 >= -7', 'a5 + a6 + b0 + b1 + b5 >= 1', '- a1 - a3 - a4 - a7 - b1 - b2 - b4 + b5 + b7 >= -6', 'a0 - a3 + b1 - b4 - b5 + b6 - b7 >= -3', '- a1 + a3 + a4 + b1 - b5 + b6 - b7 >= -2', 'a0 - a1 + a3 + b1 - b5 + b6 + b7 >= -1', 'a1 - a2 - b1 + b2 + b4 - b6 - b7 >= -3', 'a1 + a2 + a4 - a7 + b2 + b4 + b7 >= 0', '- a0 - a2 - a3 - a6 + a7 - b0 - b1 - b3 + b4 - b5 - b6 + b7 >= -8', '- a2 - b1 + b2 + b4 + b5 - b6 - b7 >= -3', '- a1 + a2 - a3 + a6 + b2 + b5 + b6 + b7 >= -1', '- a0 + a2 - a3 - a6 - a7 - b0 - b1 - b2 - b3 - b5 - b6 + b7 >= -9', '- a0 + a2 - a3 - a6 + a7 - b0 - b1 - b2 + b3 - b5 - b6 + b7 >= -7', '- a2 + a3 - a6 - a7 - b0 - b1 - b3 + b4 - b6 + b7 >= -6', '- a2 + a3 - a6 + a7 - b0 - b1 + b3 + b4 - b6 + b7 >= -4', '- a0 - a2 - a3 - a6 - a7 - b0 - b1 + b3 + b4 - b5 - b6 + b7 >= -8', 'a2 + a6 - a7 + b2 + b4 + b5 + b7 >= 0', 'a2 + a3 - a6 - a7 - b0 - b1 - b2 + b3 - b5 - b6 + b7 >= -6', 'a1 + a5 - a6 + b4 + b5 + b6 >= 0', '- a1 + a2 - a3 - a5 - b0 - b1 - b3 - b4 - b5 - b6 - b7 >= -9', '- a1 - a3 - a4 + a6 + a7 + b0 + b3 + b5 - b6 - b7 >= -4', 'a3 - a4 - a5 + a6 + a7 - b1 - b2 + b3 - b4 + b7 >= -4', 'a3 - a6 + a7 + b0 - b2 + b3 - b4 - b6 - b7 >= -4', '- a3 - a5 - a6 + a7 - b1 - b2 - b4 + b5 - b6 + b7 >= -6', '- a1 + a2 - a3 + a4 - a7 - b0 + b2 - b4 - b6 - b7 >= -6', 'a2 + a3 + a4 - a7 - b0 + b2 - b4 - b6 + b7 >= -3', '- a1 + a3 + a6 - a7 - b0 + b1 + b2 - b4 + b5 - b6 - b7 >= -5', '- a3 - a5 + a6 - a7 - b0 + b1 + b2 - b4 - b6 + b7 >= -5', '- a3 + a4 + a5 + a6 - b1 + b6 - b7 >= -2', '- a0 - a2 - a3 - a4 - a5 - a6 - b0 - b1 - b3 - b5 - b6 - b7 >= -11', '- a0 + a2 - a3 + a6 + a7 - b0 - b2 - b3 + b4 - b5 - b6 >= -6', '- a2 + a3 - a4 - a5 + a7 - b0 - b1 - b2 - b3 + b7 >= -6', '- a0 - a2 - a3 - a4 - a5 + a6 - a7 - b0 - b1 - b2 - b3 + b7 >= -9', '- a0 - a2 - a3 - a4 - a5 + a7 - b2 + b3 - b5 - b6 + b7 >= -7', 'a2 + a3 - a4 - a5 - b0 - b2 - b3 - b6 - b7 >= -6', '- a0 + a2 - a3 - a4 - a5 - b1 - b2 + b3 - b5 - b6 - b7 >= -8', 'a3 + a5 + a6 - a7 + b0 - b3 + b6 + b7 >= -1', '- a2 + a3 - a4 - a5 - b0 - b2 + b3 - b6 - b7 >= -6', 'a2 + a3 - a4 + a6 - a7 - b0 - b3 + b4 - b6 >= -4', 'a2 + a3 - a4 - a5 + a7 - b0 - b1 - b2 + b3 + b7 >= -4', '- a0 + a2 - a3 - a4 + a6 - a7 - b1 + b3 + b4 - b5 - b6 >= -6', '- a2 + a3 - a4 + a6 - a7 - b0 - b2 + b3 - b6 >= -5', 'a3 + a7 + b0 + b1 + b2 + b5 - b7 >= 0', '- a0 + a2 - a3 + a4 + a7 - b1 - b2 - b3 - b5 - b6 - b7 >= -7', '- a1 - a2 - a3 - a5 - b0 - b1 + b3 - b4 - b5 - b6 - b7 >= -9', 'a0 - a1 - a2 - a3 - b1 - b2 - b3 + b5 - b6 - b7 >= -7', '- a0 - a2 - a3 + a6 + a7 - b1 - b2 - b3 + b4 + b6 - b7 >= -6', 'a0 + a2 + a3 - b1 - b2 - b3 + b5 - b6 - b7 >= -4', 'a1 + a2 + a3 - a4 + a6 + a7 - b0 - b3 - b5 - b7 >= -4', 'a0 - a1 + a2 - a3 + a6 - b2 + b3 + b5 - b6 - b7 >= -4', 'a0 - a2 + a3 - a5 - b1 + b3 + b5 - b6 - b7 >= -4', '- a0 + a2 - a3 - a4 - a5 + a6 - a7 - b0 - b3 + b6 - b7 >= -7', '- a0 + a2 - a3 - a4 + a6 + a7 - b0 - b1 + b3 + b6 - b7 >= -5', 'a1 - a2 + a3 - a4 + a6 - a7 - b1 - b2 - b3 - b5 - b7 >= -7', '- a2 + a3 + a6 + a7 - b0 - b2 + b3 + b4 - b5 - b7 >= -4', '- a1 + a2 - a3 + a6 + a7 - b0 - b1 - b3 - b4 + b5 + b7 >= -5', '- a0 - a2 - a3 - a4 - a5 + a6 - a7 - b0 - b2 + b3 + b6 >= -7', 'a0 - a2 + a3 - b1 - b2 - b3 - b4 + b5 - b6 + b7 >= -5', '- a0 + a2 - a3 - a4 - a5 - a6 + a7 - b1 - b2 - b3 + b6 >= -7', 'a1 - a2 + a3 - a4 - a6 + a7 - b1 - b3 - b5 + b6 - b7 >= -6', '- a1 - a2 - a3 + a6 - b0 - b1 + b3 - b4 + b5 + b7 >= -5', '- a0 - a2 - a3 - a4 - a6 + a7 - b0 - b2 + b3 + b6 - b7 >= -7', 'a1 + a2 + a3 - a4 + a6 - a7 - b0 - b1 + b3 - b5 - b7 >= -5', 'a0 + a2 + a3 - b1 - b2 + b3 - b4 + b5 - b6 + b7 >= -3', 'a2 + a3 - a4 - a6 + a7 - b0 - b1 - b2 + b3 - b5 + b6 - b7 >= -6', '- a3 + a4 + a6 - a7 + b3 - b5 + b6 + b7 >= -2', 'a3 - a6 + b0 + b1 + b2 + b5 - b7 >= -1']
        self.q7_ineqs = ['a4 + a5 + a7 >= 1', 'a5 + b4 + b6 >= 1', 'a4 + a6 + b2 >= 1', 'b0 + b1 + b3 >= 1', 'a4 + a6 + b4 >= 1', 'a1 + b1 + b5 >= 1', 'a1 + b2 + b5 >= 1', 'a1 + a5 + a6 - b5 >= 0', 'a2 + b1 + b2 >= 1', 'a0 + a5 + b6 >= 1', 'a0 - b0 + b1 + b6 >= 0', 'b0 - b1 - b3 + b6 >= -1', 'a0 + b2 + b6 >= 1', 'a5 + b0 >= 1', 'b0 + b4 >= 1', 'a0 + a4 + b6 >= 1', 'b0 + b2 >= 1', '- a1 + a5 + a6 + b5 >= 0', 'a4 + b0 >= 1', 'a5 + b1 >= 1', 'b1 + b4 >= 1', 'a1 + a5 - a6 + b5 >= 0', 'a0 + b0 + b5 - b6 >= 0', 'a0 + a1 + b1 >= 1', 'a5 + b2 >= 1', 'b2 + b4 >= 1', 'a0 + a4 + a6 >= 1', 'a0 + a1 + b2 >= 1', 'a4 - a5 - a7 + b4 >= -1', 'a0 + a1 + a4 >= 1', 'a4 + b1 >= 1', 'a6 + b4 + b5 - b6 - b7 >= -1', '- a0 + a1 - a3 - a5 + b5 + b6 >= -2', 'a1 + a2 + a3 - a4 + a6 + a7 - b0 - b1 - b2 + b3 - b5 + b6 >= -4', 'a1 - a4 + a5 - a7 >= -1', 'a1 + b4 >= 1', 'b4 + b6 + b7 >= 1', '- a4 + a5 - a7 + b6 >= -1', '- a1 + b1 - b5 + b6 >= -1', 'a0 + b0 - b1 - b3 >= -1', '- a1 + b2 - b5 + b6 >= -1', '- a4 - a5 - a6 + a7 + b4 + b5 + b7 >= -2', 'a1 - a2 + a3 - a4 + a6 + a7 - b1 - b3 - b5 + b6 >= -4', '- a0 - a1 + a2 + a3 + a6 - a7 - b1 - b2 + b3 + b6 + b7 >= -4', 'a0 + a3 - b0 - b4 + b6 - b7 >= -2', 'a0 - a1 - a3 - b0 + b6 + b7 >= -2', '- a5 + a6 + b4 - b5 + b7 >= -1', 'a1 + a2 + a3 - a4 - a6 - a7 - b0 - b1 + b3 - b5 + b6 >= -5', '- a4 + a5 - a7 + b5 >= -1', '- a0 - b0 + b1 + b5 - b6 >= -2', 'a1 - a2 + a3 - a5 - a6 + a7 - b0 - b2 + b3 - b5 + b6 >= -5', '- a0 + b2 + b5 - b6 >= -1', '- a2 + a6 - b1 + b2 >= -1', 'a0 + a2 + a3 + a6 - b2 - b3 - b4 + b5 - b6 + b7 >= -3', '- a0 - a1 - a2 + a3 + a6 - a7 - b1 - b3 + b6 + b7 >= -5', '- a1 - a2 + a3 - a4 + a6 + a7 - b1 - b3 - b4 + b5 + b6 - b7 >= -6', '- a0 + a1 - a2 - a3 - a5 - a6 + a7 - b1 - b2 - b3 + b6 >= -7', '- a0 + a1 - a2 - a3 - a4 - a6 - a7 - b0 - b2 + b3 + b6 >= -7', '- a5 - a7 + b4 - b5 + b7 >= -2', 'a2 - b0 + b1 - b3 >= -1', 'a1 - a2 + a3 - a4 - a6 - a7 - b1 - b2 - b3 - b5 + b6 >= -7', '- a2 + b1 - b2 + b3 >= -1', 'a0 + a1 + a3 >= 1', 'a2 - a4 - a6 + b2 >= -1', 'a0 - a1 + a2 - a3 + a6 - b2 - b3 + b5 - b6 - b7 >= -5', 'a0 + a2 + a3 - a4 - a6 - a7 - b1 + b3 - b4 + b5 - b6 + b7 >= -5', '- a0 - a1 + a2 + a3 - a4 - a6 - a7 - b3 + b6 + b7 >= -5', '- a0 + a1 + a2 - a3 - a4 + a6 + a7 - b1 - b2 + b3 - b5 - b6 >= -6', '- a0 - a1 - a2 + a3 - a4 - a6 - a7 - b2 + b3 + b6 + b7 >= -6', '- a4 - a6 + a7 + b4 - b5 - b6 - b7 >= -4', 'a1 + a3 - a5 - b0 + b5 - b6 >= -2', '- a0 - a1 - a2 + a3 - a5 - a6 + a7 - b1 - b2 - b3 + b6 + b7 >= -7', 'a0 - a1 + a2 - a3 - a4 - a6 - a7 - b1 + b3 + b5 - b6 - b7 >= -7', '- a0 + a1 + a2 - a3 + a6 - a7 - b0 - b2 - b3 - b5 - b6 >= -7', 'a0 - a1 - a2 - a3 - a5 + a7 - b2 + b3 - b4 + b5 - b6 - b7 >= -7', '- a0 - a2 - a3 - a5 - a6 + a7 - b1 - b2 - b3 - b4 + b6 - b7 >= -9', 'a0 - a2 + a3 - a4 - a6 - a7 - b1 - b2 - b3 - b4 + b5 - b6 + b7 >= -8', '- a0 + a1 - a2 - a3 - a4 + a6 + a7 - b0 - b1 - b3 - b5 - b6 >= -8', '- a1 + a2 - a3 - a5 + a6 - b0 - b1 - b2 + b3 - b4 - b5 - b6 - b7 >= -9', '- a0 + a1 + a2 - a3 - a4 - a6 - a7 - b1 + b3 - b5 - b6 >= -7', 'a1 + a2 + a3 - a4 - a6 - a7 - b0 - b3 - b6 >= -5', 'a0 - a1 - a2 - a3 - a4 - a6 - a7 - b1 - b2 - b3 + b5 - b6 - b7 >= -10', '- a0 + a1 - a2 - a3 - a5 - a6 + a7 - b2 + b3 - b5 - b6 >= -7', 'a1 - a2 + a3 - a5 - a6 + a7 - b0 - b1 - b2 - b3 - b6 >= -7', '- a0 + a1 - a2 - a3 - a4 - a6 - a7 - b0 - b1 - b2 - b3 - b5 - b6 >= -11', '- a1 - a2 - a3 - a4 - a5 - a6 - a7 - b0 - b2 + b3 - b4 - b5 - b6 - b7 >= -12', '- a2 + a3 - a4 - a5 - a6 - a7 - b0 - b2 + b3 - b5 - b6 + b7 >= -8', 'a4 - a6 + a7 - b2 - b4 >= -2', '- a0 - a1 + b0 + b6 >= -1', 'a4 - a5 + a6 - a7 >= -1', '- a0 - a1 + a5 + a7 - b4 - b6 >= -3', '- a0 - a1 + b0 + b3 >= -1', '- a1 + a5 - a6 + a7 - b5 >= -2', '- a0 - a1 - a3 - a5 - b4 - b5 + b6 - b7 >= -6', '- a1 + a4 - a6 - b5 + b6 >= -2', '- a1 + a4 + a6 + a7 - b5 >= -1', '- a0 - a1 + a3 - a5 - b5 + b6 + b7 >= -3', '- a0 + a4 - a6 - b4 + b5 - b6 >= -3', 'a1 + b0 + b3 - b5 - b6 >= -1', 'a1 + b0 + b5 + b6 >= 1', '- a0 - a1 - a3 - a7 - b0 - b4 + b5 - b6 + b7 >= -6', '- a0 + a3 - a6 - b0 - b4 + b5 - b6 - b7 >= -5', 'a0 + b0 - b5 + b6 >= 0', 'a1 + a3 + a4 + b5 + b6 >= 1', 'a1 - a3 + a4 + b5 - b6 >= -1', '- a0 - a1 - a3 - a4 + a6 + a7 - b0 + b5 - b6 - b7 >= -6', '- a5 - a7 + b4 + b5 - b6 - b7 >= -3', '- a0 + a3 - a4 - a5 + a6 + a7 - b0 - b4 + b5 - b6 + b7 >= -5', 'a0 + a1 + a5 >= 1', '- a0 - a1 - a3 - a6 - b0 - b4 + b5 - b6 + b7 >= -6', '- a1 + a2 + a3 - a5 + a6 - b0 - b2 - b3 - b4 - b5 - b6 - b7 >= -8', '- a1 + a2 - a3 - a5 + a6 - b0 - b2 - b3 - b5 - b6 + b7 >= -7', '- a1 - a2 - a3 - a5 + a6 - b0 - b1 - b3 - b4 - b5 - b6 - b7 >= -10', '- a1 - a2 + a3 - a5 + a6 - b0 - b2 + b3 - b4 - b5 - b6 - b7 >= -8', '- a1 - a2 - a3 - a5 + a6 - b0 - b2 + b3 - b5 - b6 + b7 >= -7', '- a1 + a2 + a3 - a5 + a7 - b0 - b1 - b2 + b3 - b4 - b5 - b6 + b7 >= -7', '- a1 - a2 + a3 - a5 + a7 - b0 - b1 - b2 - b3 - b4 - b5 - b6 + b7 >= -9', '- a0 - a1 + a2 - a3 + a6 - a7 - b1 - b2 + b3 - b4 + b6 - b7 >= -7', '- a0 + a3 - a5 - a7 - b0 + b5 - b6 - b7 >= -5', '- a0 - a1 - a2 - a3 + a6 - a7 - b1 - b3 - b4 + b6 - b7 >= -8', 'a2 + a3 - a5 + a6 - a7 - b0 - b1 - b2 + b3 - b5 - b6 + b7 >= -6', '- a0 + a2 - a3 - a4 - a6 - a7 - b1 - b3 - b4 + b6 - b7 >= -8', '- a2 + a3 - a5 + a6 - a7 - b0 - b1 - b3 - b5 - b6 + b7 >= -7', 'a3 - a7 + b0 + b1 + b5 - b7 >= -1', '- a1 + a2 + a3 + a6 - a7 - b1 - b2 + b3 + b5 - b6 - b7 >= -5', '- a0 - a1 - a2 + a3 + a6 - a7 - b2 + b3 - b4 + b5 - b7 >= -6', '- a3 - a7 + b0 + b1 + b5 + b7 >= -1', '- a1 + a2 - a3 - a4 - a5 - a6 - a7 - b0 - b3 - b4 - b5 - b6 - b7 >= -11', '- a1 + a2 + a3 - a4 - a6 + a7 - b0 - b3 - b5 - b6 - b7 >= -7', '- a1 + a2 - a3 - a4 - a6 + a7 - b0 - b1 + b3 - b5 - b6 - b7 >= -8', '- a1 + a2 + a3 - a4 - a5 - a6 - a7 - b0 - b1 + b3 - b4 - b5 - b6 - b7 >= -10', '- a1 + a2 - a3 - a6 + a7 - b0 - b2 - b3 - b4 - b5 - b6 + b7 >= -8', '- a1 - a2 - a3 - a6 + a7 - b0 - b1 - b2 - b3 - b4 - b5 - b6 - b7 >= -11', 'a2 + a3 - a4 - a5 - a6 - a7 - b0 - b3 - b5 - b6 + b7 >= -7', '- a1 + a2 - a3 - a4 - a5 - a6 - a7 - b0 - b1 + b3 - b5 - b6 + b7 >= -9', '- a1 - a2 + a3 - a4 - a5 - a6 - a7 - b0 - b1 - b2 - b3 - b4 - b5 - b6 - b7 >= -13', '- a1 - a2 - a3 - a4 - a5 - a6 - a7 - b0 - b1 - b2 - b3 - b5 - b6 + b7 >= -12', '- a1 - a2 + a3 - a6 + a7 - b0 - b2 + b3 - b4 - b5 - b6 - b7 >= -8', '- a1 - a2 - a3 - a6 + a7 - b0 - b2 + b3 - b4 - b5 - b6 + b7 >= -8', 'a0 - a1 + a2 - a3 + a6 - b1 - b2 + b3 - b4 + b5 - b6 + b7 >= -5', 'a0 + a2 + a3 - a5 + a7 - b1 - b2 + b3 - b4 + b5 - b6 - b7 >= -5', 'a0 - a2 + a3 - a5 + a7 - b1 - b2 - b3 - b4 + b5 - b7 >= -6', 'a0 - a1 - a2 - a3 - a5 + a7 - b1 - b2 - b3 - b4 + b5 + b7 >= -7', 'a0 - a2 + a3 - a5 + a7 - b2 + b3 - b4 + b5 - b6 + b7 >= -4', 'a1 + a2 + a3 - a4 + a6 + a7 - b0 - b2 - b3 - b5 - b6 >= -5', '- a0 + a1 - a2 - a3 + a6 - a7 - b2 + b3 - b5 - b6 >= -6', '- a0 + a1 + a2 - a3 - a5 - a6 + a7 - b0 - b2 - b3 - b5 - b6 >= -8', 'a1 - a2 + a3 - a4 + a6 + a7 - b2 + b3 - b5 - b6 >= -4', 'a1 + a2 + a3 - a5 - a6 + a7 - b1 - b2 + b3 - b5 - b6 >= -5', '- a0 - a1 + a2 - a3 - a4 + a6 + a7 - b2 - b3 - b4 + b5 + b6 - b7 >= -7', '- a1 + a2 + a3 + a6 - a7 - b2 - b3 - b4 + b5 + b6 - b7 >= -5', 'a4 + b4 + b6 >= 1', '- a1 + a2 - a3 + a6 - a7 - b2 - b3 + b5 + b6 + b7 >= -4', '- a0 + a1 + a2 - a3 - a4 + a6 + a7 - b1 - b2 - b3 - b5 + b6 >= -6', 'a1 + a2 + a3 + a6 - a7 - b1 - b2 - b3 - b5 + b6 >= -4', '- a0 + a1 + a2 - a3 + a6 - a7 - b0 - b1 - b2 + b3 - b5 + b6 >= -6', '- a1 + a2 + a3 - a4 + a6 + a7 - b0 - b1 - b2 + b3 - b4 + b5 + b6 - b7 >= -6', 'a3 - a6 + b0 + b1 + b5 - b7 >= -1', '- a0 + a1 - a2 - a3 + a6 - a7 - b1 - b3 - b5 + b6 >= -6', '- a0 - a1 + a2 + a3 - a4 + a6 + a7 - b2 - b3 + b5 + b6 + b7 >= -4', '- a0 - a1 + a2 - a3 - a4 + a6 + a7 - b1 - b2 + b3 + b5 + b6 + b7 >= -5', '- a0 - a1 - a2 - a3 - a4 + a6 + a7 - b2 + b3 - b4 + b5 - b7 >= -7', '- a3 - a6 + b0 + b1 + b5 + b7 >= -1', '- a1 + a2 + a3 - a5 - a6 + a7 - b2 - b3 - b4 + b5 + b6 - b7 >= -6', '- a0 + a2 - a3 - a5 - a6 + a7 - b1 - b2 + b3 - b4 + b5 + b6 - b7 >= -7', '- a1 - a2 - a3 - a4 + a6 + a7 - b1 - b3 + b5 + b6 + b7 >= -5', '- a0 - a1 + a2 + a3 - a4 - a6 - a7 - b1 + b3 - b4 + b5 - b7 >= -7', '- a1 - a2 - a3 + a6 - a7 - b0 - b2 + b3 + b5 + b6 + b7 >= -5', '- a0 + a1 - a2 - a3 - a4 + a6 + a7 - b0 - b2 + b3 - b5 + b6 >= -6', '- a1 + a2 - a3 - a4 - a5 - a6 + a7 - b3 + b5 + b6 + b7 >= -5', 'a1 - a2 + a3 + a6 - a7 - b0 - b2 + b3 - b5 + b6 >= -4', '- a0 + a2 - a3 - a4 - a6 - a7 - b1 + b3 + b5 + b6 + b7 >= -5', 'a1 + a2 + a3 - a5 - a6 + a7 - b1 - b2 - b3 - b5 + b6 >= -5', '- a0 + a1 + a2 - a3 - a5 - a6 + a7 - b0 - b1 - b2 + b3 + b6 >= -6', '- a1 - a2 + a3 - a4 - a6 - a7 - b1 - b2 - b3 - b4 + b5 + b6 - b7 >= -9', '- a0 - a2 - a3 - a4 - a6 - a7 - b2 + b3 - b4 + b5 + b6 - b7 >= -8', '- a1 - a2 - a3 - a4 - a6 - a7 - b1 - b2 - b3 + b5 + b6 + b7 >= -8', '- a0 - a1 - a2 + a3 - a4 + a6 + a7 - b2 + b3 + b5 + b6 + b7 >= -4', '- a0 - a1 + a2 + a3 - a5 - a6 + a7 - b1 - b2 + b3 + b6 + b7 >= -5', '- a0 - a1 - a2 + a3 - a5 - a6 + a7 - b2 + b3 - b4 + b5 - b7 >= -7', '- a0 - a2 - a3 - a5 - a6 + a7 - b2 + b3 + b5 + b6 + b7 >= -5', 'a0 - a2 + a3 + a6 - b1 - b3 + b5 - b6 - b7 >= -4', 'a0 - a1 - a2 - a3 + a6 - b2 + b3 + b5 - b6 - b7 >= -5', 'a0 - a1 + a2 - a3 - a5 + a7 - b2 - b3 - b4 + b5 - b6 - b7 >= -7', 'a0 + a2 + a3 - a4 - a6 - a7 - b3 + b5 - b6 - b7 >= -5', '- a1 - a2 - a3 + a6 - a7 - b0 - b1 - b3 - b4 + b5 - b6 + b7 >= -8', 'a0 - a1 + a2 - a3 - a4 - a6 - a7 - b3 - b4 + b5 + b7 >= -6', 'a0 - a2 + a3 + a6 - b2 + b3 - b4 + b5 - b6 + b7 >= -3', 'a0 + a2 + a3 - a5 + a7 - b2 - b3 - b4 + b5 - b6 + b7 >= -4', '- a1 + a2 - a3 - a4 - a5 - a6 + a7 - b1 + b3 + b5 - b6 + b7 >= -6', '- a2 + a3 - a4 - a6 - a7 - b0 - b2 + b3 + b5 - b6 - b7 >= -7', '- a1 - a2 - a3 - a4 - a6 - a7 - b2 + b3 - b4 + b5 - b6 + b7 >= -8', 'a1 + a2 + a3 + a6 - a7 - b1 - b2 + b3 - b5 - b6 >= -4', 'a1 - a2 + a3 + a6 - a7 - b0 - b1 - b3 - b5 - b6 >= -6', 'a1 - a2 + a3 - a4 - a6 - a7 - b2 + b3 - b5 - b6 >= -6', '- a0 + a1 + a2 - a3 - a4 - a6 - a7 - b1 - b3 + b6 >= -6', '- a3 + a6 + a7 + b0 + b1 + b5 - b6 - b7 >= -2', 'a2 - a3 + a4 + a6 - a7 - b3 - b5 - b7 >= -4', 'a3 + a6 + a7 + b0 + b1 + b5 - b6 + b7 >= 0', 'a2 + a3 + a4 + a6 - a7 - b3 - b5 + b7 >= -2', '- a2 - a3 + a4 + a6 - a7 + b3 - b5 - b7 >= -4', '- a2 + a3 + a4 + a6 - a7 + b3 - b5 + b7 >= -2', 'a2 + a3 + a4 + a6 - a7 + b3 - b5 - b6 - b7 >= -3', 'a2 - a3 + a4 + a6 - a7 + b3 - b6 + b7 >= -2', '- a2 + a3 + a4 + a6 - a7 - b3 - b5 - b6 - b7 >= -5', '- a2 - a3 + a4 + a6 - a7 - b3 - b6 + b7 >= -4', 'a0 + a3 + b1 + b6 - b7 >= 0', 'a0 - a3 + b1 + b6 + b7 >= 0']
        self.possible_probabilities = ['2', '2_4150', '2_6781', '3', '3_1926', '3_4150', '3_6781', '4', '4_4150', '5', '5_4150', '6', '7']
        self.sbox_inequalties = {'2' : self.q2_ineqs, '2_4150' : self.q2_4150_ineqs, '2_6781' : self.q2_6781_ineqs, '3' : self.q3_ineqs,\
                                 '3_1926' : self.q3_1926_ineqs, '3_4150' : self.q3_4150_ineqs, '3_6781' : self.q3_6781_ineqs, '4' : self.q4_ineqs,\
                                 '4_4150' : self.q4_4150_ineqs, '5' : self.q5_ineqs, '5_4150' : self.q5_4150_ineqs, '6' : self.q6_ineqs, '7' : self.q7_ineqs}
    
    def create_objective_function(self):
        '''
        Create the objective function of the MILP problem
        '''

        fileobj = open(self.model_filename, "a")
        fileobj.write('Minimize\n')
        minus_log2_p = []
        for r in range(self.rounds):
            for byte_number in range(16):                
                for pr in self.possible_probabilities[0:7]:
                    minus_log2_p.append(pr.replace('_', '.') + ' ' + 'q' + pr + '_' + str(r) + '_' + str(byte_number))
                if self.exact == True:
                    for pr in self.possible_probabilities[7:]:
                        minus_log2_p.append(pr.replace('_', '.') + ' ' + 'q' + pr + '_' + str(r) + '_' + str(byte_number))
        self.obj_func = ' + '.join(minus_log2_p)
        fileobj.write(self.obj_func)
        fileobj.write("\n")
        fileobj.close()

    #@staticmethod
    def create_state_variables(self, r, s):
        '''
        Generate the variables used in the state matrix
        '''

        array = [['' for i in range(0, 8)] for j in range(0, 16)]
        for i in range(0, 16):
            for j in range(0, 8):
                array[i][j] = s + "_" + str(r) + "_" + str(i) + "_" + str(j)
                self.used_variables.append(array[i][j])
        return array
    
    def flatten(self, state_array):
        '''
        Get a state array, and output a flatten list
        '''    
        flat_list = []
        for byte_number in range(16):
            for bit_number in range(8):
                flat_list.append(state_array[byte_number][bit_number])
        return flat_list

    def create_half_state_variables(self, r, s):
        '''
        Generate the variables used in the first half of the state matrix
        '''

        array = [['' for i in range(0, 8)] for j in range(0, 16)]
        for i in range(0, 8):
            for j in range(0, 8):
                array[i][j] = s + "_" + str(r) + "_" + str(i) + "_" + str(j)
                self.used_variables.append(array[i][j])
        return array

    def xor(self, a, b, c):
        '''
        Generate the constraints of a binary XOR (An XOR with two inputs)
        a xor b = c can be modeled with 4 inequalities (without definition of dummy variable) by removing each impossible (a, b, c)
        '''

        fileobj = open(self.model_filename, "a")        
        ineq1 = a + " + " + b + " - " + c + " >= 0\n"
        ineq2 = a + " - " + b + " + " + c + " >= 0\n"
        ineq3 = str(-1) + " " + a + " + " + b + " + " + c + " >= 0\n"
        ineq4 = str(-1) + " " + " - ".join([a, b, c]) + " >= -2\n"
        fileobj.write(ineq1)
        fileobj.write(ineq2)
        fileobj.write(ineq3)
        fileobj.write(ineq4)
        fileobj.close()

    def xor3(self, b, a2, a1, a0):
        '''
        Generate the constraints of a three-input XOR  (b = a0 xor a1 xor a2)    
        b - a2 - a1 - a0 >= -2
        - b + a2 - a1 - a0 >= -2
        - b - a2 + a1 - a0 >= -2
        b + a2 + a1 - a0 >= 0
        - b - a2 - a1 + a0 >= -2
        b + a2 - a1 + a0 >= 0
        b - a2 + a1 + a0 >= 0
        - b + a2 + a1 + a0 >= 0
        The above inequalities are obtained with QuineMcCluskey algorithm
        '''

        fileobj = open(self.model_filename, "a")        
        ineq1 = b + " - " + a2 + " - " + a1 + " - " + a0 + " >= -2\n"
        ineq2 = " - " + b + " + " + a2 + " - " + a1 + " - " + a0 + " >= -2\n"
        ineq3 = " - " + b + " - " + a2 + " + " + a1 + " - " + a0 + " >= -2\n"
        ineq4 = b + " + " + a2 + " + " + a1 + " - " + a0 + " >= 0\n"
        ineq5 = " - " + b + " - " + a2 + " - " + a1 + " + " + a0 + " >= -2\n"
        ineq6 = b + " + " + a2 + " - " + a1 + " + " + a0 + " >= 0\n"
        ineq7 = b + " - " + a2 + " + " + a1 + " + " + a0 + " >= 0\n"
        ineq8 = " - " + b + " + " + a2 + " + " + a1 + " + " + a0 + " >= 0\n"
        fileobj.write(ineq1)
        fileobj.write(ineq2)
        fileobj.write(ineq3)
        fileobj.write(ineq4)
        fileobj.write(ineq5)
        fileobj.write(ineq6)
        fileobj.write(ineq7)
        fileobj.write(ineq8)
        fileobj.close()
    
    def equality(self, x, y):
        '''
        Generate the MILP constraints modeling the equality of two bits
        '''

        fileobj = open(self.model_filename, 'a')
        ineq = x + ' - ' + y + ' = 0\n'
        fileobj.write(ineq)
        fileobj.close()

    def mix_columns(self, x, y):
        '''
        Generate constraints related to mixing layer (MixColumns)
        '''

        for byte_number in range(4):            
            for bit_number in range(8):
                self.xor3(y[byte_number][bit_number], x[byte_number][bit_number], x[byte_number + 8][bit_number], x[byte_number + 12][bit_number])
                self.equality(y[byte_number + 4][bit_number], x[byte_number][bit_number])
                self.xor(x[byte_number + 4][bit_number], x[byte_number + 8][bit_number], y[byte_number + 8][bit_number])
                self.xor(x[byte_number][bit_number], x[byte_number + 8][bit_number], y[byte_number + 12][bit_number])

    def add_tweakey(self, tk, x, y):
        '''
        Generate the constraints concerning the AddTweaey
        tk xor x = y
        '''

        for byte_number in range(8):
            for bit_number in range(8):
                self.xor(tk[byte_number][bit_number], x[byte_number][bit_number], y[byte_number][bit_number])
        for byte_number in range(8, 16):
            for bit_number in range(8):
                self.equality(x[byte_number][bit_number], y[byte_number][bit_number])

    def shift_rows(self, state):
        '''
        Implementing the ShiftRows operation
        No MILP constraint is generated by this operation
        '''
        
        temp = [0]*16
        for i in range(16):
            temp[i] = state[self.permuteation[i]]
        return temp
    
    def permute_tweakey(self, state):
        '''
        implementing the tweak permutation (Q)
        No MILP constraint is generated by this operation
        '''

        temp = [0]*16
        for i in range(16):
            temp[i] = state[self.tk_permutation[i]]
        return temp
    
    def subcells(self, x, y, r):
        '''
        Generate the Sbox constraints
        x: input state
        y: output state
        S(x) = y
        r: depicts the round number
        '''

        fileobj = open(self.model_filename, 'a')
        for byte_number in range(16):
            q_byte_variables = []           
            for pr in self.possible_probabilities[0:7]:
                q = 'q' + pr + '_' + str(r) + '_' + str(byte_number)
                q_byte_variables.append(q)
                for ineq in self.sbox_inequalties[pr]:
                    for i in range(8):
                        ineq = ineq.replace('a' + str(i), x[byte_number][i])
                        ineq = ineq.replace('b' + str(i), y[byte_number][i])
                    # Big-M Method:
                    ineq = ineq.split(' >= ')
                    ineq = ineq[0] + ' - ' + str(self.big_m) + ' ' + q + ' >= ' + str(int(ineq[1]) - self.big_m) + '\n'
                    # Indicator constraint:
                    # ineq  = q + ' = 1'+ ' -> ' + ineq + '\n'
                    fileobj.write(ineq)
            if self.exact == True:                            
                for pr in self.possible_probabilities[7:]:
                    q = 'q' + pr + '_' + str(r) + '_' + str(byte_number)
                    q_byte_variables.append(q)
                    for ineq in self.sbox_inequalties[pr]:
                        for i in range(8):
                            ineq = ineq.replace('a' + str(i), x[byte_number][i])
                            ineq = ineq.replace('b' + str(i), y[byte_number][i])
                        # Big-M method:
                        ineq = ineq.split(' >= ')
                        ineq = ineq[0] + ' - ' + str(self.big_m) + ' ' + q + ' >= ' + str(int(ineq[1]) - self.big_m) + '\n'
                        # Indicator constraint:
                        # ineq  = q + ' = 1'+ ' -> ' + ineq + '\n'
                        fileobj.write(ineq)
            else:
                pass
            # q = sum(qi)
            self.used_variables.extend(q_byte_variables)
            q_byte = 'q_' + str(r) + '_' + str(byte_number)
            self.used_variables.append(q_byte)
            ineq = q_byte + ' - ' + ' - '.join(q_byte_variables) + ' = 0\n'
            fileobj.write(ineq)
            # q[byte_number] >= x[byte_number][i] for i in range(8)
            for i in range(8):
                ineq = q_byte + ' - ' + x[byte_number][i] + ' >= 0\n'
                fileobj.write(ineq)
            # sum(x[byte_number][i] for i in range(8)) >= q[byte_number]
            ineq = ' + '.join(x[byte_number]) + ' - ' + q_byte + ' >= 0\n'
            fileobj.write(ineq)
            # Model the bijectivity of Sbox (x = 0 => y = 0, y = 0 => x = 0)
            ineq = '8 ' + ' + 8 '.join(y[byte_number]) + ' - ' + ' - '.join(x[byte_number]) + ' >= 0\n'
            fileobj.write(ineq)
            ineq = '8 ' + ' + 8 '.join(x[byte_number]) + ' - ' + ' - '.join(y[byte_number]) + ' >= 0\n'
            fileobj.write(ineq)
        fileobj.close()
    
    def lfsr_8bit_tk2(self, a, b):
        '''
        Generate the MILP constraints corresponding to the 8-bit LFSR used in the path of TK2
        It is supposed that a, and b, are 8-bit vectors
        Main paper: (x7||x6||x5||x4||x3||x2||x1||x0) -> (x6||x5||x4||x3||x2||x1||x0||x7 xor x5) where x0 is the LSB
        In this implementation a[0] is the MSB, and a[7] is the LSB
        (a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7]) -> (a[1], a[2], a[3], a[4], a[5], a[6], a[0] xor a[2]) = (b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7])
        '''

        for i in range(7):
           self.equality(a[i + 1], b[i])
        self.xor(a[0], a[2], b[7])

    def tweakey_schedule(self):
        '''
        Generate the MILP constraints modeling the propagation of differences through the tweakey schedule
        '''

        tk1 = self.create_state_variables(0, 'tk1')
        tk2 = self.create_state_variables(0, 'tk2')
        tk = self.create_half_state_variables(0, 'tk')
        # Constraints concerning the generation of round tweakey TK = FirstHalf(TK1) xor FirstHalf(TK2)
        for byte_number in range(8):
            for bit_number in range(8):
                self.xor(tk1[byte_number][bit_number], tk2[byte_number][bit_number], tk[byte_number][bit_number])
        for r in range(1, self.rounds):
            # Perform tweakey permutation on TK1, and TK2
            ptk1 = self.permute_tweakey(tk1)
            ptk2 = self.permute_tweakey(tk2)
            # TK1 doesn't have LFSR in it's path
            #tk1 = ptk1
            tk1 = self.create_state_variables(r, 'tk1')          
            tk2 = self.create_state_variables(r, 'tk2')
            # tk1 = ptk1
            for byte_number in range(16):
                for bit_number in range(8):
                    self.equality(tk1[byte_number][bit_number], ptk1[byte_number][bit_number])
            # The 8-bit LFSR is performed on each byte of the first half of ptk2
            for byte_number in range(8):
                self.lfsr_8bit_tk2(ptk2[byte_number], tk2[byte_number])
            # The second half of the next round tk2 must be the same as the ptk2
            for byte_number in range(8, 16):
                for bit_number in range(8):
                    self.equality(ptk2[byte_number][bit_number], tk2[byte_number][bit_number])            
            tk = self.create_half_state_variables(r, 'tk')
            # Constraints concerning the generation of next round tweakey
            for byte_number in range(8):
                for bit_number in range(8):
                    self.xor(tk1[byte_number][bit_number], tk2[byte_number][bit_number], tk[byte_number][bit_number])
    
    def encryption(self):
        '''
        Generate the MILP constraints modeling the propagation of differences through the encryption data path
        '''

        for r in range(self.rounds):
            x = self.create_state_variables(r, 'x')
            y = self.create_state_variables(r, 'y')
            z = self.create_state_variables(r, 'z')
            tk = self.create_half_state_variables(r, 'tk')
            x_next = self.create_state_variables(r + 1, 'x')
            self.subcells(x, y, r)
            self.add_tweakey(tk, y, z)
            pz = self.shift_rows(z)
            self.mix_columns(pz, x_next)
    
    def exclude_trivial_trail(self):
        fileobj = open(self.model_filename, 'a')
        x = self.create_state_variables(0, 'x')
        tk1 = self.create_state_variables(0, 'tk1')
        tk2 = self.create_state_variables(0, 'tk2')
        temp = []
        for byte_number in range(16):
            for bit_number in range(8):
                temp.append(x[byte_number][bit_number])
                temp.append(tk1[byte_number][bit_number])
                temp.append(tk2[byte_number][bit_number])
        ineq = ' + '.join(temp) + ' >= 1\n'
        fileobj.write(ineq)
        fileobj.close()
    
    def declare_fixed_variables(self):
        fileobj = open(self.model_filename, 'a')
        for cond in self.fixed_variables.items():            
            var = cond[0]
            val = cond[1]
            var = var.split('_')
            if len(var) == 2:
                state_vars = self.create_state_variables(var[1], var[0])
                state_vars = self.flatten(state_vars)
                state_values = list(bin(int(val, 16))[2:].zfill(128))
                for i in range(128):
                    equality = state_vars[i] + ' = ' + state_values[i] + '\n'
                    fileobj.write(equality)
            elif len(var) == 3:
                state_vars = [var[0] + '_' + var[1] + '_' + var[2] + '_' + str(i) for i in range(8)]
                state_values = list(bin(int(val, 16))[2:].zfill(8))
                for i in range(8):
                    equality = state_vars[i] + ' = ' + state_values[i] + '\n'
                    fileobj.write(equality)
            else: 
                pass
        fileobj.close()

    def declare_variables_type(self):
        '''
        Specifying variables' type in the LP file
        '''

        fileobj = open(self.model_filename, 'a')
        fileobj.write('Bin\n')
        self.used_variables = list(set(self.used_variables))
        for var in self.used_variables:
            fileobj.write(var)
            fileobj.write('\n')
        fileobj.write('End')
        fileobj.close()

    def make_model(self):
        '''
        Generate the MILP model of Skinny-128-256 for differential cryptanalysis
        '''
        print('Generating the MILP model ...')
        self.create_objective_function()
        fileobj = open(self.model_filename, 'a')
        fileobj.write('Subject to\n')
        fileobj.close()
        self.exclude_trivial_trail()
        self.tweakey_schedule()
        self.encryption()
        self.declare_fixed_variables()
        self.declare_variables_type()
        print('MILP model generation was finished!\n')
    
    def find_characteristic(self):
        '''
        Find the best differential trail for the given number of rounds (and the given fixed input/output differences)
        '''

        if self.time_limit != -1:
            self.model.Params.TIME_LIMIT = self.time_limit
        obj = self.model.getObjective()
        # Consider the start_weight
        if self.start_weight != None:
            self.model.addConstr(obj >= self.start_weight, 'start_weight_constraint')        
        time_start = time.time()
        #m.setParam(GRB.Param.Threads, 16)
        self.model.optimize()
        # Gurobi syntax: m.Status == 2 represents the model is feasible. 
        if (self.model.Status == GRB.OPTIMAL or self.model.Status == GRB.TIME_LIMIT or self.model.Status == GRB.INTERRUPTED):
            # obj = self.model.getObjective()
            # objVal = obj.getValue()
            self.total_weight = self.model.objVal
            print("\nThe probability of the best differential characteristic: 2^-(%s)" % self.total_weight)
            print("\nDifferential trail:\n")
            diff_trail = self.parse_solver_output()
            self.print_trail(diff_trail)
        # Gurobi syntax: m.Status == 3 represents the model is infeasible. (GRB.Status.INFEASIBLE)
        elif self.model.Status == GRB.INFEASIBLE:
            print("The model is infeasible!")
        else:
            print("Unknown error!")
        time_end = time.time()
        print(('Time used = ' + str(time_end - time_start)))
    
    def find_multiple_characteristics(self):
        '''
        Find multiple differential trails for the given number of rounds (and the given fixed input/output differences)
        '''

        if self.time_limit != -1:
            self.model.Params.TIME_LIMIT = self.time_limit
        #m.setParam(GRB.Param.Threads, 16)
        obj = self.model.getObjective()
        # Consider the start_weight
        if self.start_weight != None:
            self.model.addConstr(obj >= self.start_weight, 'start_weight_constraint')
        self.model.Params.OutputFlag = False
        # You can use the PoolSearchMode parameter to control the approach used to find solutions. In its default setting (0), the MIP search simply aims to find one optimal solution. Setting the parameter
        # to 1 causes the MIP search to expend additional effort to find more solutions, but in a non-systematic way. 
        # You will get more solutions, but not necessarily the best solutions. Setting the parameter to 2 causes the MIP to do a systematic search for the n best solutions. For both non-default settings, 
        # the PoolSolutions parameter sets the target for the number of solutions to find.
        self.model.Params.PoolSearchMode = 2
        # Limit how many solutions to collect
        self.model.Params.PoolSolutions = 10
        time_start = time.time()
        self.model.optimize()
        if (self.model.Status == GRB.OPTIMAL or self.model.Status == GRB.TIME_LIMIT or self.model.Status == GRB.INTERRUPTED):
            # First Method:
            number_of_trails = 10
            for sol_number in range(number_of_trails):
                if (self.model.Status == GRB.OPTIMAL):
                    self.total_weight = self.model.PoolObjVal
                    diff_trail = self.parse_solver_output()
                    self.print_trail(diff_trail)
                elif (self.model.Status == GRB.TIME_LIMIT or self.model.Status == GRB.INTERRUPTED):
                    self.total_weight = self.model.PoolObjVal
                    diff_trail = self.parse_solver_output()
                    self.print_trail(diff_trail)
                    break
                else:
                    break
                self.exclude_the_previous_sol()
                self.model.optimize()
            # Second Method:
            # number_of_trails = self.model.SolCount
            # for sol_number in range(number_of_trails):
            #     self.model.Params.SolutionNumber = sol_number
            #     # PoolObjVal : This attribute is used to query the objective value of the <span>$</span>k<span>$</span>-th solution stored in the pool of feasible solutions found so far for the problem
            #     self.total_weight = self.model.PoolObjVal                
            #     diff_trail = self.parse_solver_output()
            #     self.print_trail(diff_trail)
        # Gurobi syntax: m.Status == 3 represents the model is infeasible. (GRB.INFEASIBLE)
        elif self.model.Status == GRB.INFEASIBLE:
            print("The model is infeasible!")
        else:
            print("Unknown error!")
        time_end = time.time()
        print(('Time used = ' + str(time_end - time_start)))        
    
    def compute_differential_effect(self):
        '''
        Compute the differential effect for a given input/output differences

        Some general information about Gurobi:

        PoolSolutions: It controls the size of the solution pool. Changing this parameter won't affect the number of solutions that are found - 
        it simply determines how many of those are retained

        You can use the PoolSearchMode parameter to control the approach used to find solutions. In its default setting (0), the MIP search simply aims to find one optimal solution. 
        Setting the parameter to 2 causes the MIP to do a systematic search for the n best solutions. With a setting of 2, it will find the n best solutions, 
        where n is determined by the value of the PoolSolutions parameter        

        SolCount: Number of solutions found during the most recent optimization.
        
        Model status:
        LOADED	1	Model is loaded, but no solution information is available.
        OPTIMAL	2	Model was solved to optimality (subject to tolerances), and an optimal solution is available.
        INFEASIBLE	3	Model was proven to be infeasible.
        '''

        if self.time_limit != -1:
            self.model.Params.TIME_LIMIT = self.time_limit
        #self.model.Params.PreSolve = 0 # Activating this flag causes the performance to be decreased, but the accuracy will be increased  
        self.model.Params.PoolSearchMode = 2
        self.model.Params.PoolSolutions = 1
        self.model.Params.OutputFlag = False
        
        self.model.printStats()

        # Consider the start_weight
        obj = self.model.getObjective()
        if self.start_weight != None:            
            self.model.addConstr(obj >= self.start_weight, 'start_weight_constraint')       
        time_start = time.time()
        self.model.optimize()
        if (self.model.Status == GRB.OPTIMAL):
            self.total_weight = self.model.objVal
            diff_prob = 0
            print('\n')
            while (self.model.Status == GRB.OPTIMAL and self.total_weight <= self.end_weight):
                #self.total_weight = self.model.objVal
                self.total_weight = self.model.PoolObjVal 
                self.model.Params.PoolSolutions = 2000000000 #GRB.MAXIN, Default value‎ for PoolSolutions: ‎10                
                temp_constraint = self.model.addConstr(obj == self.total_weight, name='temp_constraint')
                # self.model.Params.PoolGap = 0
                # self.model.Params.PreSolve = 0
                #self.model.printStats()
                self.model.update()
                self.model.optimize()
                diff_prob += math.pow(2, -self.total_weight) * self.model.SolCount
                print('Current weight: %s' % str(self.total_weight))
                print('Number of trails: %s' % str(self.model.SolCount))
                print('\tCurrent Probability: 2^(' + str(math.log(diff_prob, 2)) + ')')
                time_end = time.time()
                print('Time used = %0.4f seconds\n' % (time_end - time_start))
                self.model.remove(temp_constraint)
                self.model.Params.PoolSolutions = 1                
                self.model.addConstr(obj >= (self.total_weight + self.eps), name='temp_cond')
                #self.model.Params.PreSolve = 0
                self.model.optimize()
        elif (self.model.Status == GRB.INFEASIBLE):
            print('The model is infeasible!')
        else: 
            print('Unknown Error!')

    def compute_differential_effect_classic_method(self):
        if self.time_limit != -1:
            self.model.Params.TIME_LIMIT = self.time_limit
        self.model.Params.OutputFlag = False
        # self.model.printStats()
        # Consider the start_weight
        obj = self.model.getObjective()
        if self.start_weight != None:            
            self.model.addConstr(obj >= self.start_weight, 'start_weight_constraint')       
        time_start = time.time()
        self.model.optimize()
        self.model.Params.Quad = 1
        sol_dict = dict()
        if (self.model.Status == GRB.OPTIMAL):
            self.total_weight = self.model.objVal
            diff_prob = 0
            print('\n')
            while (self.model.Status == GRB.OPTIMAL and self.total_weight <= self.end_weight):  
                self.total_weight = self.model.objVal
                diff_prob += math.pow(2, -self.total_weight)
                total_weight_st = 'ntrails_%0.2f' % self.total_weight
                sol_dict[total_weight_st] = sol_dict.get(total_weight_st, 0) + 1
                print('Current weight: %s' % str(self.total_weight))
                print('Number of trails: %d' % sol_dict[total_weight_st])
                print('\tCurrent Probability: 2^(' + str(math.log(diff_prob, 2)) + ')')
                time_end = time.time()
                print('Time used = %0.4f seconds\n' % (time_end - time_start))           
                self.exclude_the_previous_sol()
                self.model.optimize()
        elif (self.model.Status == GRB.INFEASIBLE):
            print('The model is infeasible!')
        else: 
            print('Unknown Error!')

    def exclude_the_previous_sol(self):
        '''
        Let x{S} be the binary variables. Suppose you have a binary solution x* in available from the most recent optimization. 
        Let N be the subset of S such that x*[n] = 1 for all n in N
        Then, add the following constraint:
        sum{n in N} x[n] - sum{s in S-N} x[s] <= |N|-1
        '''

        all_vars = self.model.getVars()
        nonzero_vars = [v for v in all_vars if v.x == 1]
        zero_vars = [v for v in all_vars if v.x == 0]
        support = len(nonzero_vars)
        first_term = sum(nonzero_vars)
        second_term = sum(zero_vars)
        lhs = first_term - second_term
        self.model.addConstr(lhs <= support - 1)


    def solve(self):
        self.model = read(self.model_filename)
        if self.mode == 0:
            self.find_characteristic()
        elif self.mode == 1:                     
            self.find_multiple_characteristics()
        elif self.mode == 2:
            self.compute_differential_effect()
            #self.compute_differential_effect_classic_method()
        else:
            print('Enter a number in [0, 1, 2], for the mode parameter please!')

    def parse_solver_output(self):
        '''
        Extract the differential characteristic from the solver output
        '''

        characteristic = dict()
        for r in range(self.rounds + 1):
            x = self.flatten(self.create_state_variables(r, 'x'))            
            x_value = hex(int('0b' + ''.join(list(map(lambda t: str(int(self.model.getVarByName(t).Xn)), x))), 2))[2:].zfill(32)
            characteristic['x_' + str(r)] = x_value
        tk1 = self.create_state_variables(0, 'tk1')
        for r in range(self.rounds):
            y = self.flatten(self.create_state_variables(r, 'y'))
            y_value = hex(int('0b' + ''.join(list(map(lambda t: str(int(self.model.getVarByName(t).Xn)), y))), 2))[2:].zfill(32)
            characteristic['y_' + str(r)] = y_value
            z = self.flatten(self.create_state_variables(r, 'z'))
            z_value = hex(int('0b' + ''.join(list(map(lambda t: str(int(self.model.getVarByName(t).Xn)), z))), 2))[2:].zfill(32)        
            characteristic['z_' + str(r)] = z_value
            tk1_flat = self.flatten(tk1)
            tk1_value = hex(int('0b' + ''.join(list(map(lambda t: str(int(self.model.getVarByName(t).Xn)), tk1_flat))), 2))[2:].zfill(32)
            characteristic['tk1_' + str(r)] = tk1_value
            tk1 = self.permute_tweakey(tk1)
            tk2 = self.flatten(self.create_state_variables(r, 'tk2'))
            tk2_value = hex(int('0b' + ''.join(list(map(lambda t: str(int(self.model.getVarByName(t).Xn)), tk2))), 2))[2:].zfill(32)
            characteristic['tk2_' + str(r)] = tk2_value            
            tk = self.flatten(self.create_half_state_variables(r, 'tk'))[0:64]
            tk_value = hex(int('0b' + ''.join(list(map(lambda t: str(int(self.model.getVarByName(t).Xn)), tk))), 2))[2:].zfill(16)
            characteristic['tk_' + str(r)] = tk_value        
            round_probability = 0
            for byte_number in range(16):
                for pr in self.possible_probabilities:
                    q = 'q' + pr + '_' + str(r) + '_' + str(byte_number)
                    round_probability += float(pr.replace('_', '.')) * int(self.model.getVarByName(q).Xn)
            characteristic['pr_' +str(r)] = '-' + str(round_probability)
        
        return characteristic
    
    def print_trail(self, diff_trail):
        '''
        Print out the obtained differential trail
        '''
        
        header = ['x', 'y', 'z', 'tk1', 'tk2', 'tk', 'pr']
        # Print everthing        
        col_width = max(len(s) for s in diff_trail.values()) + 2
        header_str = "Rounds\t"
        data_str = ""
        current_row = 0
        for entry in header[0:-2]:
            header_str += entry.ljust(col_width)
        header_str += header[-2].ljust(col_width//2)
        header_str += header[-1].ljust(7)
        for r in range(self.rounds + 1):
            data_str += str(current_row) + '\t'            
            data_str += diff_trail.get('x_' + str(r), 'none').ljust(col_width)
            data_str += diff_trail.get('y_' + str(r), 'none').ljust(col_width)
            data_str += diff_trail.get('z_' + str(r), 'none').ljust(col_width)
            data_str += diff_trail.get('tk1_' + str(r), 'none').ljust(col_width)
            data_str += diff_trail.get('tk2_' + str(r), 'none').ljust(col_width)            
            data_str += diff_trail.get('tk_' + str(r), 'none').ljust(col_width//2)
            data_str += diff_trail.get('pr_' + str(r), 'none').ljust(7)
            data_str += '\n'
            current_row += 1
        print(header_str)
        print("-"*len(header_str))
        print(data_str)        
        print("Weight: " + '-' + str(self.total_weight))
        return
