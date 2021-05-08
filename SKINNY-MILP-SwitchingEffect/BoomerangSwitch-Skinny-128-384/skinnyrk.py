# H. Hadipour
# March 8, 2020
# 18 Esfand, 1398
# Applying the MILP-based method to find an optimum boomerang differential distinguisher for Skinny-128-384

import time
from gurobipy import *

"""
This code has been prepared for boomerang cryptanalysis of Skinny-64-192

x_roundNumber_byteNumber_bitNumber
x_roundNumber_byteNumber_0: msb
x_roundNumber_byteNumber_3: lsb

Input of (i + 1)'th round:
u vs d
x_i_0	x_i_1	x_i_2	x_i_3
x_i_4	x_i_5	x_i_6	x_i_7
x_i_8	x_i_9	x_i_10	x_i_11
x_i_12	x_i_13	x_i_14	x_i_15

Output of ART in (i + 1)'th round:
u vs d
y_i_0	y_i_1	y_i_2	y_i_3
y_i_4	y_i_5	y_i_6	y_i_7
y_i_8	y_i_9	y_i_10	y_i_11
y_i_12	y_i_13	y_i_14	y_i_15

tk1 in (i + 1)'th round
u vs d
tk1_i_0   tk1_i_1   tk1_i_2  tk1_i_3
tk1_i_4   tk1_i_5   tk1_i_6  tk1_i_7
tk1_i_8   tk1_i_9   tk1_i_10 tk1_i_11
tk1_i_12  tk1_i_13  tk1_i_14 tk1_i_15

tk2 in (i + 1)'th round
u vs d
tk2_i_0   tk2_i_1   tk2_i_2  tk2_i_3
tk2_i_4   tk2_i_5   tk2_i_6  tk2_i_7
tk2_i_8   tk2_i_9   tk2_i_10 tk2_i_11
tk2_i_12  tk2_i_13  tk2_i_14 tk2_i_15

tk in (i + 1)'th round
u vs d
tk_i_0   tk_i_1   tk_i_2  tk_i_3
tk_i_4   tk_i_5   tk_i_6  tk_i_7
tk_i_8   tk_i_9   tk_i_10 tk_i_11
tk_i_12  tk_i_13  tk_i_14 tk_i_15

Twakey schedule has been implemented bit-oriented
tk1: bit-wise
tk2: bit-wise
tk3: bit-wise
tk : bit-wise
tkw : word-wise
tk and tkw are linked towgether via the following conditions
u vs d
tkw_i_0 >= tk_i_0_0, tkw_i_0 >= tk_i_0_1, tkw_i_0 >= tk_i_0_2, tkw_i_0 >= tk_i_0_3, tkw_i_0 >= tk_i_0_4, tkw_i_0 >= tkw_i_0_5, tkw_i_0 >= tk_i_0_6, tkw_i_0 >= tk_i_0_7, tkw_i_0 >= tk_i_0_8
tkw_i_0 <= tk_i_0_0 + tk_i_0_1 + tk_i_0_2 + tk_i_0_3 + tk_i_0_4 + tk_i_0_5 + tk_i_0_6 + tk_i_0_7 + tk_i_0_8

R1 - R: Number of Sbox layers covered by the upper trail only
R2 - R: Number of Sbox layers covered by the lower trail only
R: Number of Sbox layers covered by both upper and lower trails (where upper and lower trails overlap)

linking variables:
s_i_0	s_i_1	s_i_2	s_i_3
s_i_4	s_i_5	s_i_6	s_i_7
s_i_8	s_i_9	s_i_10	s_i_11
s_i_12	s_i_13	s_i_14	s_i_15
"""

class Skinnyrk:
    def __init__(self, r0, r1, rm, w0, w1, wm, number_of_pattern, time_limit):
        self.permute_byte_table = [
            0x0, 0x1, 0x2, 0x3, 0x7, 0x4, 0x5, 0x6, 0xa, 0xb, 0x8, 0x9, 0xd, 0xe, 0xf, 0xc]
        self.permute_tweak_byte_table = [
            0x9, 0xf, 0x8, 0xd, 0xa, 0xe, 0xc, 0xb, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7]
        self.xor_counter = 0
        self.dummy_var_counter = 0
        self.used_variables = []
        self.R1 = r0 + rm
        self.R2 = r1 + rm
        self.R = rm
        self.w0 = w0
        self.w1 = w1
        self.wm = wm
        self.number_of_pattern = number_of_pattern
        self.time_limit = time_limit
        self.filename_model = "skinnyrk_%du_%dm_%dd.lp" % (self.R1, self.R, self.R2)
        self.filename_diffpath_up = "diffpath_upper_%dr.yaml" % (r0)
        self.filename_diffpath_down = "diffpath_lower_%dr.yaml" % (r1)
        self.filename_io_middle = "io_diff_middle_%dr.txt" % (rm)

    def gen_variables(self, r, s):
        """
        Generate the state variables
        """
        variables = ["%s_%d_%d" % (s, r, i) for i in range(16)]
        self.used_variables.extend(variables)
        return variables
    
    def gen_bit_wise_variables(self, r, s):
        """
        Generate the bit-wise state variables
        """
        variables = [["%s_%d_%d_%d" % (s, r, i, j) for j in range(8)] for i in range(16)]
        for i in range(16):
            self.used_variables.extend(variables[i])
        return variables
    
    def gen_half_variables(self, r, s):
        """
        Generate the variables corresponding to the half of the state
        """
        variables = ["%s_%d_%d" % (s, r, i) for i in range(8)]
        self.used_variables.extend(variables)
        return variables

    def gen_half_bit_wise_variables(self, r, s):
        """
        Generate bit-wise variables corresponding to the half of the state
        """
        variables = [["%s_%d_%d_%d" % (s, r, i, j) for j in range(8)] for i in range(8)]
        for i in range(8):
            self.used_variables.extend(variables[i])
        return variables
    
    def constraints_of_exact_xor(self, a, b, c):
        """
        Generate the constraints corresponding to XOR
        a XOR b = c can be modeled with 4 inequalities
        (without definition of dummy variable) by removing
        each impossible (a, b, c).
        """
        fileobj = open(self.filename_model, 'a')
        ineq1 = a + " + " + b + " - " + c + " >= 0\n"
        ineq2 = a + " - " + b + " + " + c + " >= 0\n"
        ineq3 = str(-1) + " " + a + " + " + b + " + " + c + " >= 0\n"
        ineq4 = str(-1) + " " + " - ".join([a, b, c]) + " >= -2\n"
        fileobj.write(ineq1)
        fileobj.write(ineq2)
        fileobj.write(ineq3)
        fileobj.write(ineq4)
        fileobj.close()

    def constraints_by_exact_xor3(self, a2, a1, a0, b):
        fileobj = open(self.filename_model, 'a')
        """
        These inequalities have been obtained via LogicFriday(QM algorithm, exact)
        Let b = a2 + a1 + a0
        b - a2 - a1 - a0 >= -2
        - b + a2 - a1 - a0 >= -2
        - b - a2 + a1 - a0 >= -2
        b + a2 + a1 - a0 >= 0
        - b - a2 - a1 + a0 >= -2
        b + a2 - a1 + a0 >= 0
        b - a2 + a1 + a0 >= 0
        - b + a2 + a1 + a0 >= 0
        """
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
    
    def constraints_of_trun_cxor(self, a, b, c):        
        """
        a + b + c >= 2 d
        d >= a
        d >= b
        d >= c
        """
        fileobj = open(self.filename_model, 'a')
        d = "d_%d" % self.xor_counter
        self.used_variables.append(d)
        ineq1 = "%s + %s + %s -  2 %s >= 0\n" % (a, b, c, d)
        ineq2 = "%s - %s >= 0\n" % (d, a)
        ineq3 = "%s - %s >= 0\n" % (d, b)
        ineq4 = "%s - %s >= 0\n" % (d, c)
        fileobj.write(ineq1)
        fileobj.write(ineq2)
        fileobj.write(ineq3)
        fileobj.write(ineq4)
        fileobj.close()
        self.xor_counter += 1

    def constraint_of_equality(self, x, y):
        """
        Generate constraint modeling the equality of x, and y
        """
        fileobj = open(self.filename_model, 'a')
        equality = "%s - %s = 0\n" % (x, y)
        fileobj.write(equality)
        fileobj.close()

    def constraints_of_mixing_layer(self, x, y):
        """
        Generate constraints related to mixing layer (MC)
        """
        for j in range(4):
            dummy_var = "dv_%d" % self.dummy_var_counter
            self.constraints_of_trun_cxor(x[j + 4*0], x[j + 4*2], dummy_var)
            self.used_variables.append(dummy_var)
            self.dummy_var_counter += 1
            self.constraints_of_trun_cxor(dummy_var, x[j + 4*3], y[j + 4*0])
            self.constraint_of_equality(x[j + 4*0], y[j + 4*1])
            self.constraints_of_trun_cxor(x[j + 4*1], x[j + 4*2], y[j + 4*2])
            self.constraint_of_equality(dummy_var, y[j + 4*3])

    def constraints_of_tk2_lfsr8(self, x, y):
        """
        Generate constraints related to LFSR
        It is supposed that x, and y are arrays of lentgh 8, where each entry depicts one bit of difference
        """
        for i in range(7):
            self.constraint_of_equality(y[i], x[i + 1])
        self.constraints_of_exact_xor(x[0], x[2], y[7])
        
    def constraints_of_tk3_lfsr8(self, x, y):
        """
        Generate constraints related to the LFSR
        It is supposed that x, and y are arrays of lentgh 8, where each entry depicts one bit of difference
        """
        for i in range(7):
            self.constraint_of_equality(y[i + 1], x[i])
        self.constraints_of_exact_xor(x[7], x[1], y[0])    

    def constraints_of_linking_word_to_bits(self, w, bits):
        """
        Generate constraints corresponding to linking bits to word
        """
        fileobj = open(self.filename_model, 'a')
        for j in range(8):
            ineq = "%s - %s >= 0\n" % (w, bits[j])
            fileobj.write(ineq)
        ineq = " + ".join(bits) + " - " + w + " >= 0\n"
        fileobj.write(ineq)
        fileobj.close()
    
    def permute_bytes(self, state):
        temp = [0]*16
        for i in range(16):
            temp[i] = state[self.permute_byte_table[i]]
        return temp
    
    def permute_tweakey_bytes(self, state):
        temp = [0]*16
        for i in range(16):
            temp[i] = state[self.permute_tweak_byte_table[i]]
        return temp 
    
    def gen_objective_function(self):
        """
        Create objective function of the MILP model.
        """
        fileobj = open(self.filename_model, "w")
        fileobj.write("Minimize\n")
        A = ["xu_%d_%d" % (r, i) for r in range(0, (self.R1 - self.R)) for i in range(16)]
        B = ["xl_%d_%d" % (r, i) for r in range(self.R, self.R2) for i in range(16)]
        C = ["s_%d_%d" % (r, i) for r in range(self.R) for i in range(16)]
        if (A != []) and (B != []):
            temp = " + ".join(A) + " + " + " + ".join(B) + " + " + " + ".join(C)
        elif (A == []) and (B != []):
            temp = " + ".join(B) + " + " + " + ".join(C)
        elif (A != []) and (B == []):
            temp = " + ".join(A) + " + ".join(C)
        else:
            temp = " + ".join(C) 
        fileobj.write(temp)
        fileobj.write("\n")
        fileobj.close()

########################################################################################################
########################################################################################################
#################################### Upper Differential Trail ##########################################
########################################################################################################
########################################################################################################

    def constraints_of_upper_trail(self):
        """
        Generating the constraints related to the upper trail
        """
        fileobj = open(self.filename_model, "a")
        fileobj.write("Subject To\n")
        zero_link = ["s_%d_%d" % (r, i) for r in range(self.R) for i in range(16)]
        zero_link = " + ".join(zero_link) + " = 0\n"
        #fileobj.write(zero_link)
        
        rounds = self.R1
        x_in = self.gen_variables(0, "xu")
        tk1 = self.gen_bit_wise_variables(0, 'tku1')
        tk2 = self.gen_bit_wise_variables(0, 'tku2')
        tk3 = self.gen_bit_wise_variables(0, 'tku3')
        tk1_flat = [tk1[i][j] for i in range(16) for j in range(4)]
        tk2_flat = [tk2[i][j] for i in range(16) for j in range(4)]
        tk3_flat = [tk3[i][j] for i in range(16) for j in range(4)]
        temp = " + ".join(x_in + tk1_flat + tk2_flat + tk3_flat) + " >= 1\n"
        fileobj.write(temp)
        fileobj.close()
        for r in range(0, rounds):
            x_in = self.gen_variables(r, 'xu')
            y = self.gen_variables(r, 'yu')
            x_out = self.gen_variables(r + 1, 'xu')
            tk1 = self.gen_bit_wise_variables(r, 'tku1')
            tk2 = self.gen_bit_wise_variables(r, 'tku2')
            tk3 = self.gen_bit_wise_variables(r, 'tku3')
            next_tk1 = self.gen_bit_wise_variables(r + 1, 'tku1')
            next_tk2 = self.gen_bit_wise_variables(r + 1, 'tku2')
            next_tk3 = self.gen_bit_wise_variables(r + 1, 'tku3')
            round_tk = self.gen_half_bit_wise_variables(r, 'tku')
            round_tkw = self.gen_half_variables(r, 'tkwu')
            ## Constraints by tweakey-schedule
            tk1p = self.permute_tweakey_bytes(tk1)
            tk2p = self.permute_tweakey_bytes(tk2)
            tk3p = self.permute_tweakey_bytes(tk3)
            for i in range(16):
                for j in range(8):
                    self.constraint_of_equality(tk1p[i][j], next_tk1[i][j])
                if (i < 8):
                    self.constraints_of_tk2_lfsr8(tk2p[i], next_tk2[i])
                    self.constraints_of_tk3_lfsr8(tk3p[i], next_tk3[i])
                    for j in range(8):                        
                        self.constraints_by_exact_xor3(tk1[i][j], tk2[i][j], tk3[i][j], round_tk[i][j])
                else:
                    for j in range(8):
                        self.constraint_of_equality(tk2p[i][j], next_tk2[i][j])           
                        self.constraint_of_equality(tk3p[i][j], next_tk3[i][j])
            ## Linking bit-wise variables to word-wise ones
            for i in range(8):
                self.constraints_of_linking_word_to_bits(round_tkw[i], round_tk[i])
            ## Constraints by ART
            for j in range(4):
                self.constraints_of_trun_cxor(x_in[j + 4*0], round_tkw[j + 4*0], y[j + 4*0])
                self.constraints_of_trun_cxor(x_in[j + 4*1], round_tkw[j + 4*1], y[j + 4*1])
                self.constraint_of_equality(x_in[j + 4*2], y[j + 4*2])
                self.constraint_of_equality(x_in[j + 4*3], y[j + 4*3])
            ## Constraints by MixingLayer
            self.constraints_of_mixing_layer(self.permute_bytes(y), x_out)

########################################################################################################
########################################################################################################
################################### Middle Differential Trail ##########################################
########################################################################################################
########################################################################################################

    def linking_constraints(self):
        fileobj = open(self.filename_model, "a")
        for r in range(self.R):
            uppder_vars = self.gen_variables(r + (self.R1 - self.R), "xu")
            lower_vars = self.gen_variables(r, "xl")
            link_vars = self.gen_variables(r, "s")
            for i in range(16):
                ineq1 = "%s - %s >= 0\n" % (uppder_vars[i], link_vars[i])
                ineq2 = "%s - %s >= 0\n" % (lower_vars[i], link_vars[i])
                ineq3 = "- %s - %s + %s >= -1\n" % (uppder_vars[i], lower_vars[i], link_vars[i])
                fileobj.write(ineq1)
                fileobj.write(ineq2)
                fileobj.write(ineq3)
        fileobj.close()

########################################################################################################
########################################################################################################
#################################### Lower Differential Trail ##########################################
########################################################################################################
########################################################################################################

    def constraints_of_lower_trail(self):
        """
        Generating the constraints related to the lower trail
        """
        fileobj = open(self.filename_model, "a")
        rounds = self.R2
        x_in = self.gen_variables(0, "xl")
        tk1 = self.gen_bit_wise_variables(0, 'tkl1')
        tk2 = self.gen_bit_wise_variables(0, 'tkl2')
        tk3 = self.gen_bit_wise_variables(0, 'tkl3')
        tk1_flat = [tk1[i][j] for i in range(16) for j in range(4)]
        tk2_flat = [tk2[i][j] for i in range(16) for j in range(4)]
        tk3_flat = [tk3[i][j] for i in range(16) for j in range(4)]
        temp = " + ".join(x_in + tk1_flat + tk2_flat + tk3_flat) + " >= 1\n"
        fileobj.write(temp)
        fileobj.close()
        for r in range(0, rounds):
            x_in = self.gen_variables(r, 'xl')
            y = self.gen_variables(r, 'yl')
            x_out = self.gen_variables(r + 1, 'xl')
            tk1 = self.gen_bit_wise_variables(r, 'tkl1')
            tk2 = self.gen_bit_wise_variables(r, 'tkl2')
            tk3 = self.gen_bit_wise_variables(r, 'tkl3')
            next_tk1 = self.gen_bit_wise_variables(r + 1, 'tkl1')
            next_tk2 = self.gen_bit_wise_variables(r + 1, 'tkl2')
            next_tk3 = self.gen_bit_wise_variables(r + 1, 'tkl3')
            round_tk = self.gen_half_bit_wise_variables(r, 'tkl')
            round_tkw = self.gen_half_variables(r, 'tkwl')
            ## Constraints by tweakey-schedule
            tk1p = self.permute_tweakey_bytes(tk1)
            tk2p = self.permute_tweakey_bytes(tk2)
            tk3p = self.permute_tweakey_bytes(tk3)
            for i in range(16):
                for j in range(8):
                    self.constraint_of_equality(tk1p[i][j], next_tk1[i][j])
                if (i < 8):
                    self.constraints_of_tk2_lfsr8(tk2p[i], next_tk2[i])
                    self.constraints_of_tk3_lfsr8(tk3p[i], next_tk3[i])
                    for j in range(8):
                        self.constraints_by_exact_xor3(tk1[i][j], tk2[i][j], tk3[i][j], round_tk[i][j])
                else:
                    for j in range(8):
                        self.constraint_of_equality(tk2p[i][j], next_tk2[i][j])
                        self.constraint_of_equality(tk3p[i][j], next_tk3[i][j])
            ## Linking bit-wise variables to word-wise ones
            for i in range(8):
                self.constraints_of_linking_word_to_bits(round_tkw[i], round_tk[i])
            ## Constraints by ART
            for j in range(4):
                self.constraints_of_trun_cxor(x_in[j + 4*0], round_tkw[j + 4*0], y[j + 4*0])
                self.constraints_of_trun_cxor(x_in[j + 4*1], round_tkw[j + 4*1], y[j + 4*1])
                self.constraint_of_equality(x_in[j + 4*2], y[j + 4*2])
                self.constraint_of_equality(x_in[j + 4*3], y[j + 4*3])
            ## Constraints by MixingLayer
            self.constraints_of_mixing_layer(self.permute_bytes(y), x_out)

    # Variables declaration
    def declare_variable_type(self):
        """
        Specifying variables type.
        """
        fileobj = open(self.filename_model, 'a+')
        fileobj.write("Binary\n")
        for var in self.used_variables:
            fileobj.write(var)
            fileobj.write('\n')
        fileobj.write("END")
        fileobj.close()

    def make_model(self):
        """
        Generate the MILP model of CRAFT
        """
        fileobj = open(self.filename_model, "w")
        fileobj.close()
        self.gen_objective_function()
        self.constraints_of_upper_trail()
        self.constraints_of_lower_trail()
        self.linking_constraints()
        self.declare_variable_type()

    def get_state_values_at_round(self, s, r):
        '''
        Retrive solution corresponding to the word-wise state array
        '''
        v_names = ["%s_%d_%d" % (s, r, byte_number)
                           for byte_number in range(16)]
        #v_names.reverse()
        temp = map(self.model.getVarByName, v_names)                
        v_values = "".join([str(int(e.Xn)) for e in temp])
        return v_values
    
    def get_bitwise_state_values_at_round(self, s, r):
        '''
        Retrive solution corresponding to the bit-wise state array
        '''
        v_names = [["%s_%d_%d_%d" % (s, r, byte_number, bit_number) for bit_number in range(8)] 
                    for byte_number in range(16)]
        #v_names.reverse()
        temp = [map(self.model.getVarByName, v_names[i]) for i in range(16)]
        v_values = [[str(int(e.Xn)) for e in temp[i]] for i in range(16)]
        v_values = [hex(int("".join(v_values[i]), 2))[2:].zfill(2) for i in range(16)]
        v_values = "".join(v_values)
        return v_values
    
    def retrieve_upper_trail(self, fileobj_diffpath_up):
        '''
        Retrieve the uppaer trail from the solver output
        '''        
        cipher_parameters = 'blocksize: 128\n'        
        #cipher_parameters += 'rounds: ' + str(self.R1 - self.R) + '\n'
        cipher_parameters += 'rounds: ' + str(self.R1) + '\n'        
        cipher_parameters += 'mode: 0\n'
        cipher_parameters += 'sweight: 0\n'
        cipher_parameters += 'endweight: 128\n'
        cipher_parameters += 'timelimit: -1\n'
        cipher_parameters += 'fixedVariables:\n'
        fileobj_diffpath_up.write(cipher_parameters)
        ####### upper trail
        print('\n\n Upper Trail: \n')
        rounds = self.R1 #self.R1 - self.R
        for r in range(0, rounds + 1):
            state1_u = self.get_state_values_at_round('xu', r)
            if (r < rounds):
                state2_u = self.get_state_values_at_round('yu', r)
                print("x%d:\t%s\t\t\ty%d: %s" %
                        (r, state1_u, r, state2_u))
                #if (r < self.R1 - self.R + 1):
                temp = list(state1_u)
                for j in range(16):
                    if (temp[j] == '0'):
                        fileobj_diffpath_up.write("- x_%d_%d : \"0x00\"\n" % (r, j))
            else:
                print("x%d:\t%s" % (r, state1_u))
                temp = list(state1_u)
                for j in range(16):
                    if (temp[j] == '0'):
                        fileobj_diffpath_up.write("- x_%d_%d : \"0x00\"\n" % (r, j))
                
        tku1_values = self.get_bitwise_state_values_at_round('tku1', 0)
        tku2_values = self.get_bitwise_state_values_at_round('tku2', 0)
        tku3_values = self.get_bitwise_state_values_at_round('tku3', 0)
        print("tku1:\t%s" % tku1_values)                
        print("tku2:\t%s" % tku2_values)
        print("tku3:\t%s" % tku3_values)
        temp = [''.join(tku1_values[2 * i: 2 * i + 2]) for i in range(16)]
        for j in range(16):
            if (temp[j] == '00'):
                fileobj_diffpath_up.write("- tk1_0_%d: \"0x00\"\n" % j)
        temp = [''.join(tku2_values[2 * i: 2 * i + 2]) for i in range(16)]
        for j in range(16):
            if (temp[j] == '00'):
                fileobj_diffpath_up.write("- tk2_0_%d: \"0x00\"\n" % j)
        temp = [''.join(tku3_values[2 * i: 2 * i + 2]) for i in range(16)]
        for j in range(16):
            if (temp[j] == '00'):
                fileobj_diffpath_up.write("- tk3_0_%d: \"0x00\"\n" % j)
    
    def retrieve_lower_trail(self, fileobj_diffpath_down):
        '''
        Retrieve the lower trail from the solver output
        '''        
        cipher_parameters = 'blocksize: 128\n'        
        #cipher_parameters += 'rounds: ' + str(self.R1 - self.R) + '\n'
        cipher_parameters += 'rounds: ' + str(self.R2) + '\n'        
        cipher_parameters += 'mode: 0\n'
        cipher_parameters += 'sweight: 0\n'
        cipher_parameters += 'endweight: 128\n'
        cipher_parameters += 'timelimit: -1\n'
        cipher_parameters += 'fixedVariables:\n'
        fileobj_diffpath_down.write(cipher_parameters)
        print('\n\n Lower Trail: \n')
        rounds = self.R2 #self.R2 - self.R
        for r in range(0, rounds + 1):
            state1_l = self.get_state_values_at_round('xl', r)
            if (r < rounds):
                state2_l = self.get_state_values_at_round('yl', r)
                print("x%d:\t%s\t\t\ty%d: %s" %
                        (r, state1_l, r, state2_l))                        
                #if (r >= self.R):
                temp = list(state1_l)
                for j in range(16):
                    if (temp[j] == '0'):                        
                        fileobj_diffpath_down.write("- x_%d_%d : \"0x00\"\n" % (r, j))
            else:
                print("x%d:\t%s" % (r, state1_l))
                temp = list(state1_l)
                for j in range(16):
                    if (temp[j] == '0'):
                        fileobj_diffpath_down.write("- x_%d_%d : \"0x00\"\n" % (r, j))
                                                
        # tkl1_values = self.get_bitwise_state_values_at_round('tkl1', self.R)
        # tkl2_values = self.get_bitwise_state_values_at_round('tkl2', self.R)
        tkl1_values = self.get_bitwise_state_values_at_round('tkl1', 0)
        tkl2_values = self.get_bitwise_state_values_at_round('tkl2', 0)
        tkl3_values = self.get_bitwise_state_values_at_round('tkl3', 0)
        print("tkl1:\t%s" % tkl1_values)
        print("tkl2:\t%s" % tkl2_values)
        print("tkl3:\t%s" % tkl3_values)
        temp = [''.join(tkl1_values[2 * i: 2 * i + 2]) for i in range(16)]
        for j in range(16):
            if (temp[j] == '00'):
                fileobj_diffpath_down.write("- tk1_0_%d: \"0x00\"\n" % j)
        temp = [''.join(tkl2_values[2 * i: 2 * i + 2]) for i in range(16)]
        for j in range(16):
            if (temp[j] == '00'):
                fileobj_diffpath_down.write("- tk2_0_%d: \"0x00\"\n" % j)
        temp = [''.join(tkl3_values[2 * i: 2 * i + 2]) for i in range(16)]
        for j in range(16):
            if (temp[j] == '00'):
                fileobj_diffpath_down.write("- tk3_0_%d: \"0x00\"\n" % j)
    
    def retrieve_middle_part(self, fileobj_io_middle):
        print("\n Middle Rounds: \n")        
        midd_first_round = self.R1 - self.R
        state1_u = self.get_state_values_at_round('xu', midd_first_round)
        print("xu%d:\t%s" % (midd_first_round, state1_u))
        fileobj_io_middle.write("xu%d:\t%s" % (midd_first_round, state1_u))
        fileobj_io_middle.write('\n')

        mid_last_round = self.R
        state1_l = self.get_state_values_at_round('xl', mid_last_round)
        print("xl%d:\t%s" % (mid_last_round, state1_l))
        fileobj_io_middle.write("xl%d:\t%s" % (mid_last_round, state1_l))
        fileobj_io_middle.write('\n')

        tku1_values = self.get_bitwise_state_values_at_round('tku1', 0)
        tku2_values = self.get_bitwise_state_values_at_round('tku2', 0)
        tku3_values = self.get_bitwise_state_values_at_round('tku3', 0)
        print("tku1:\t%s" % tku1_values)
        print("tku2:\t%s" % tku2_values)
        print("tku3:\t%s" % tku2_values)
        fileobj_io_middle.write("tku1:\t%s\n" % tku1_values)
        fileobj_io_middle.write("tku2:\t%s\n" % tku2_values)
        fileobj_io_middle.write("tku3:\t%s\n" % tku3_values)

        tkl1_values = self.get_bitwise_state_values_at_round('tkl1', 0)
        tkl2_values = self.get_bitwise_state_values_at_round('tkl2', 0)
        tkl3_values = self.get_bitwise_state_values_at_round('tkl3', 0)
        print("tkl1:\t%s" % tkl1_values)
        print("tkl2:\t%s" % tkl2_values)
        print("tkl3:\t%s" % tkl2_values)
        fileobj_io_middle.write("tkl1:\t%s\n" % tkl1_values)
        fileobj_io_middle.write("tkl2:\t%s\n" % tkl2_values)
        fileobj_io_middle.write("tkl3:\t%s\n" % tkl3_values)        

    def solve_model(self):
        """
        Solve the MILP problem to find an optiumum boomerang distinguisher        
        """
        #self.model.setParam(GRB.Param.OutputFlag, 0)
        #self.model.setParam(GRB.Param.Threads, 16)
        #self.model.setParam(GRB.Param.Presolve, 0)
        time_start = time.time()
        self.model = read(self.filename_model)
        if self.time_limit != -1:
            self.model.Params.TimeLimit = self.time_limit
        # do a systematic search for the k-best solutions
        self.model.Params.PoolSearchMode = 2
        # Limit how many solutions to collect
        self.model.Params.PoolSolutions = self.number_of_pattern
        self.model.optimize()
        number_of_solutions = self.model.SolCount
        print("\nNumber of solutions: %d" % number_of_solutions)
        if (self.model.Status == GRB.OPTIMAL or self.model.Status == GRB.TIME_LIMIT or self.model.Status == GRB.INTERRUPTED):
            status = 2
            with open(self.filename_diffpath_up, 'w') as fileobj_diffpath_up, open(self.filename_diffpath_down, 'w') as fileobj_diffpath_down,\
                 open(self.filename_io_middle, 'w') as fileobj_io_middle:
                for e in range(number_of_solutions):
                    self.model.Params.SolutionNumber = e
                    print('\nObj: %g' % self.model.objVal)
                    # obj = self.model.getObjective()
                    ####### Upper trail                    
                    self.retrieve_upper_trail(fileobj_diffpath_up)
                    ####### lower trail                    
                    self.retrieve_lower_trail(fileobj_diffpath_down)
                    ####### middle rounds
                    self.retrieve_middle_part(fileobj_io_middle)
        # Gurobi syntax: m.Status == 3 represents the model is infeasible.
        elif self.model.Status == 3:
            status = 3
            print("The model is infeasible!")
        else:
            print("Unknown error!")
        time_end = time.time()
        print(("Time used = " + str(time_end - time_start)))
        return status
