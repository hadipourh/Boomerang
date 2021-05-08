# Author: Hosein Hadippour
# Date: June 13, 2019
#       23 Khordad, 1398

import time
from gurobipy import *

"""
x_roundNumber_nibbleNumber_bitNumber
x_roundNumber_nibbleNumber_0: msb
x_roundNumber_nibbleNumber_3: lsb

Input of (i + 1)-th round:
u vs d
x_i_0	x_i_1	x_i_2	x_i_3
x_i_4	x_i_5	x_i_6	x_i_7
x_i_8	x_i_9	x_i_10	x_i_11
x_i_12	x_i_13	x_i_14	x_i_15

Output of MC in (i + 1)-th round:
u vs d
y_i_0	y_i_1	y_i_2	y_i_3
y_i_4	y_i_5	y_i_6	y_i_7
x_i_8	x_i_9	x_i_10	x_i_11
x_i_12	x_i_13	x_i_14	x_i_15

R1 - R - 1: Number of Sbox layres covered by the upper trail only
R2 - R: Number of Sbox layers covered by the lower trail only
R + 1: Number of Sbox layers covered by both upper and lower trails (where the upper and lower trails overlap)

linking variables:
s_i_0	s_i_1	s_i_2	s_i_3
s_i_4	s_i_5	s_i_6	s_i_7
s_i_8	s_i_9	s_i_10	s_i_11
s_i_12	s_i_13	s_i_14	s_i_15
"""

class Craft:
    def __init__(self, r0, r1, rm, w0, w1, wm, number_of_patterns):
        self.xor_counter = 0
        self.dummy_var_counter = 0
        self.R1 = r0 + rm
        self.R2 = r1 + rm - 1
        self.R = rm - 1
        self.w0 = w0
        self.w1 = w1
        self.wm = wm
        self.number_of_patterns = number_of_patterns
        self.p_permute_nibbles = [
            0xf, 0xc, 0xd, 0xe, 0xa, 0x9, 0x8, 0xb, 0x6, 0x5, 0x4, 0x7, 0x1, 0x2, 0x3, 0x0]
        self.q_permute_teakey_nibbles = [
            0xc, 0xa, 0xf, 0x5, 0xe, 0x8, 0x9, 0x2, 0xb, 0x3, 0x7, 0x4, 0x6, 0x0, 0x1, 0xd]                
        self.filename_model = "craft.lp"
        self.filename_result = "craft.txt"
        fileobj = open(self.filename_model, "w")
        fileobj.close()

    @staticmethod
    def create_variables(r, s):
        """
        Generate the variables used in the model.
        """
        array = ["" for i in range(0, 16)]
        for i in range(0, 16):
            array[i] = "%s_%d_%d" % (s, r, i)
        return array

    @staticmethod
    def create_variables_after_mc(r, s1, s2):
        """
        Generate the variables used in the model.
        """
        array = [["" for i in range(0, 4)] for j in range(0, 16)]
        for i in range(0, 8):
            array[i] = "%s_%d_%d" % (s1, r, i)
        for i in range(8, 16):
            array[i] = "%s_%d_%d" % (s2, r, i)
        return array

    def constraints_by_truncxor(self, a, b, c):
        fileobj = open(self.filename_model, "a")
        """
        a + b + c >= 2 d
        d >= a
        d >= b
        d >= c
        """
        d = "d_%d" % self.xor_counter
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

    def constraints_by_equality(self, s1, s2):
        fileobj = open(self.filename_model, "a")
        for i in range(16):
            constraint = "%s - %s = 0\n" % (s1[i], s2[i])
            fileobj.write(constraint)
        fileobj.close() 

    def constraints_by_mixing_layer(self, x, y):
        """
        Generate constraints related to mixing layer (MC)
        """
        for nibble_number in range(4):
            dummy_var = "dv_%d" % self.dummy_var_counter
            self.constraints_by_truncxor(
                x[nibble_number], x[nibble_number + 8], dummy_var)
            self.constraints_by_truncxor(
                dummy_var, x[nibble_number + 12], y[nibble_number])
            self.constraints_by_truncxor(x[nibble_number + 4], x[nibble_number + 12],
                                         y[nibble_number + 4])
            self.dummy_var_counter += 1

    def permute_nibbles(self, state):
        temp = [0]*16
        for i in range(16):
            temp[self.p_permute_nibbles[i]] = state[i]
        return temp

    def initial_state_constraint(self, x):        
        fileobj = open(self.filename_model, "a")        
        fileobj.write("\ Exclude the trivial solution:\n")
        temp = " + ".join(x) + " >= 1\n"
        fileobj.write(temp)
        fileobj.close()
    
    def create_objective_function(self):
        """
        Create objective function of the MILP model.
        """

        fileobj = open(self.filename_model, "a")
        fileobj.write("Minimize\n")
        A = ["%f xu_%d_%d" % (self.w0, r, i) for r in range(1, (self.R1 - self.R)) for i in range(16)]
        #A1 = [str(self.R1 - r) + " xu_%d_%d" % (r, i) for r in range(1, self.R1 + 1) for i in range(16)]
        B = ["%f xl_%d_%d" % (self.w1, r, i) for r in range(self.R + 1, self.R2 + 1) for i in range(16)]
        #B1 = [str(r) + " xl_%d_%d" % (r, i) for r in range(0, self.R2 + 1) for i in range(16)]
        C = ["%f s_%d_%d" % (self.wm, r, i) for r in range(self.R + 1) for i in range(16)]
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
    
    def constraints_upper_trail(self):
        """
        Generating the constraints related to the upper trail
        """
        fileobj = open(self.filename_model, "a")
        fileobj.write("Subject To\n")
        zero_link = ["s_%d_%d" % (r, i) for r in range(self.R + 1) for i in range(16)]
        zero_link = " + ".join(zero_link) + " = 0\n"
        # fileobj.write(zero_link)
        fileobj.close()        
        
        rounds = self.R1 # - self.R
        x_in = self.create_variables(0, "xu")
        self.initial_state_constraint(x_in)
        y = self.create_variables_after_mc(0, "yu", "xu")
        x_out = self.create_variables(1, "xu")
        if (rounds == 1):
            self.constraints_by_mixing_layer(x_in, y)
            self.constraints_by_equality(self.permute_nibbles(y), x_out)
        else:
            self.constraints_by_mixing_layer(x_in, y)
            self.constraints_by_equality(self.permute_nibbles(y), x_out)
        for r in range(1, rounds):
            x_in = x_out
            y = self.create_variables_after_mc(r, "yu", "xu")
            x_out = self.create_variables(r + 1, "xu")
            self.constraints_by_mixing_layer(x_in, y)
            self.constraints_by_equality(self.permute_nibbles(y), x_out)
        
    def constraints_lower_trail(self):
        """
        Generating the constraints related to the lower trail
        """

        rounds = self.R2 # - self.R
        x_in = self.create_variables(0, "xl")
        self.initial_state_constraint(x_in)
        y = self.create_variables_after_mc(0, "yl", "xl")
        x_out = self.create_variables(1, "xl")
        if (rounds == 1):
            self.constraints_by_mixing_layer(x_in, y)
            self.constraints_by_equality(self.permute_nibbles(y), x_out)
        else:
            self.constraints_by_mixing_layer(x_in, y)
            self.constraints_by_equality(self.permute_nibbles(y), x_out)
        for r in range(1, rounds):
            x_in = x_out
            y = self.create_variables_after_mc(r, "yl", "xl")
            x_out = self.create_variables(r + 1, "xl")
            self.constraints_by_mixing_layer(x_in, y)
            self.constraints_by_equality(self.permute_nibbles(y), x_out)
        
    def linking_constraints(self):
        fileobj = open(self.filename_model, "a")
        for r in range(self.R + 1):
            uppder_vars = self.create_variables(r + (self.R1 - self.R), "xu")
            lower_vars = self.create_variables(r, "xl")
            link_vars = self.create_variables(r, "s")
            for i in range(16):
                fileobj.write("\ Linking constraints:\n")
                ineq1 = "%s - %s >= 0\n" % (uppder_vars[i], link_vars[i])
                ineq2 = "%s - %s >= 0\n" % (lower_vars[i], link_vars[i])
                ineq3 = "- %s - %s + %s >= -1\n" % (uppder_vars[i], lower_vars[i], link_vars[i])
                fileobj.write(ineq1)
                fileobj.write(ineq2)
                fileobj.write(ineq3)
        fileobj.close()

    # Variables declaration
    def binary_variables(self):
        """
        Specifying variables type.
        """
        fileobj = open(self.filename_model, "a")        
        fileobj.write("Binary\n")     
        # xu
        for round_number in range(self.R1 + 1):
            for nibble_number in range(16):
                fileobj.write("xu_%s_%s\n" % (round_number, nibble_number))
        # xl
        for round_number in range(self.R2 + 1):
            for nibble_number in range(16):
                fileobj.write("xl_%s_%s\n" % (round_number, nibble_number))
        
        # yu
        for round_number in range(self.R1):
            for nibble_number in range(8):
                fileobj.write("yu_%s_%s\n" % (round_number, nibble_number))
        # yl
        for round_number in range(self.R2):
            for nibble_number in range(8):
                fileobj.write("yl_%s_%s\n" % (round_number, nibble_number))
        
        # s
        for round_number in range(self.R + 1):
            for nibble_number in range(16):
                fileobj.write("s_%s_%s\n" % (round_number, nibble_number))

        # dummy variables used in xor operations
        for i in range(self.xor_counter):
            fileobj.write("d_%d\n" % i)

        # dummy variables used in mixing layers
        for i in range(self.dummy_var_counter):
            fileobj.write("dv_%d\n" % i)

        fileobj.write("END")
        fileobj.close()

    def make_model(self):
        """
        Generate the MILP model of CRAFT
        """
        fileobj = open(self.filename_model, "w")
        fileobj.close()        
        self.create_objective_function()
        self.constraints_upper_trail()
        self.constraints_lower_trail()
        self.linking_constraints()
        self.binary_variables()

    def get_state_values_at_round(self, s, r, m, updown):
        v_names = ["%s%s_%d_%d" % (s, updown, r, nibble_number)
                           for nibble_number in range(16)]
        #v_names.reverse()
        temp = map(m.getVarByName, v_names)                
        v_values = "".join([str(int(e.X)) for e in temp])
        return v_values
    
    def get_state_values_output_of_mixing(self, r, m, updown):
        v_names1 = self.create_variables_after_mc(r, "y%s" % updown, "x%s" % updown)
        #v_names1.reverse()
        temp1 = map(m.getVarByName, v_names1)                    
        v_values1 = "".join([str(int(e.X)) for e in temp1])
        return v_values1

    def exclude_the_previous_sol(self, m):
        '''
        Let x{S} be the binary variables. Suppose you have a binary solution x* in available from the most recent optimization. 
        Let N be the subset of S such that x*[n] = 1 for all n in N
        Then, add the following constraint:
        sum{n in N} x[n] - sum{s in S-N} x[s] <= |N|-1
        '''

        all_vars = m.getVars()
        nonzero_vars = [v for v in all_vars if v.x == 1]
        zero_vars = [v for v in all_vars if v.x == 0]
        support = len(nonzero_vars)
        first_term = sum(nonzero_vars)
        second_term = sum(zero_vars)
        lhs = first_term - second_term
        m.addConstr(lhs <= support - 1)
    
    def solve_model(self):
        """
        Solve the MILP model to search optimized boomerang distinguisher using the switching effect
        """
        time_start = time.time()
        m = read(self.filename_model)
        m.setParam(GRB.Param.OutputFlag, 0)
        # m.setParam(GRB.Param.Threads, 12)
        # m.setParam(GRB.Param.Presolve, 0)
        # do a systematic search for the k-best solutions
        # m.setParam(GRB.Param.PoolSearchMode, 2)
        # Limit how many solutions to collect
        sol_count = 0
        # m.setParam(GRB.Param.PoolSolutions, self.number_of_patterns)
        m.optimize()
        # Gurobi syntax: m.Status == 2 represents the model is feasible.
        if m.Status == 2:
            while (m.Status == 2 and sol_count < self.number_of_patterns):
                #m.setParam(GRB.Param.SolutionNumber, e)
                # with open("solution_%d.sol" % e, "w"):
                #     m.write("solution_%d.sol" % e)            
                obj = m.getObjective()
                print("Solution number %d\n" % sol_count)
                # print upper trail
                print("Upper activeness pattern:")        
                for r in range(self.R1 + 1):
                    state1 = self.get_state_values_at_round("x", r, m, 'u')
                    if (r < self.R1):
                        state2 = self.get_state_values_output_of_mixing(r, m, 'u')
                        print("xu%d: %s\t\t\tyu%d: %s" %
                            (r, state1, r, state2))
                        # print(state1[2:])
                    else:
                        print("xu%d: %s" % (r, state1))
                        # print(state1[2:])

                # print lower trail
                print("Lower activeness pattern:")
                for r in range(self.R2 + 1):
                    state1 = self.get_state_values_at_round("x", r, m, 'l')
                    if (r < self.R2):
                        state2 = self.get_state_values_output_of_mixing(r, m, 'l')
                        print("xl%d: %s\t\t\tyl%d: %s" %
                            (r, state1, r, state2))
                        # print(state1[2:])
                    else:
                        print("xl%d: %s" % (r, state1))
                        # print(state1[2:])

                #print linking vars
                print("\nLinking variables:")
                for r in range(self.R + 1):
                    state1 = self.get_state_values_at_round("s", r, m, '')                
                    print("s%d: %s" % (r, state1[2:]))
                sol_count += 1
                self.exclude_the_previous_sol(m)
                if (sol_count < self.number_of_patterns):
                    m.optimize()
                    print("#"*20 + "\n\n")
        # Gurobi syntax: m.Status == 3 represents the model is infeasible.
        elif m.Status == 3:           
            print("The model is infeasible!")
        else:
            print("Unknown error!")
        time_end = time.time()
        print(("Time used = " + str(time_end - time_start)))        
