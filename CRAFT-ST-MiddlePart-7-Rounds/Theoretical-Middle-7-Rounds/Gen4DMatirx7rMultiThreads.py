# -*- coding: utf-8 -*-
"""
Created on May 25 2020

@authors: Hosein Hadipour and Ling Song
"""

from multiprocessing import Pool, current_process, Process
import math
import time
#import numpy as np

S = [0xc, 0xa, 0xd, 0x3, 0xe, 0xb, 0xf, 0x7, 0x8, 0x9, 0x1, 0x5, 0x0, 0x2, 0x4, 0x6]     # craft 4-bit s-box

def print2Dlist(D):
    size = len(D[0])
    for i in range(size):
        print(str(i)+': ', end = "")
        for j in range(size):
            print(D[i][j], ' ', end = "")
        print('')

class BCT_Analyzer:
    def __init__(self, S):
        self.initialization(S)

    def initialization(self, S):
        Sinv = [0 for i in range(len(S))]
        for i in range(len(S)):
            Sinv[S[i]] = i
        print('S   : ', S)
        print('Sinv: ', Sinv)
        self.size = len(S)
        self.ddt = self.get_DDT(S)       # ddt[alpha][beta] = int
        self.bct = self.get_BCT(S, Sinv) # bct[alpha][beta] = int
        self.Yddt = self.get_Yddt(S)     # Yddt[alpha][beta] = {y0,y1,y2,y3}, the set of possible outputs
        self.dYddt = self.get_dYddt(S)   # dYddt[alpha][beta] = {0,y1 xor y0, y2 xor y0, y3 xor y0}, the set of possible crossing differences
        self.Xddt = self.get_Xddt(S)     # Xddt[alpha][beta] = {x0,x1,x2,x3}, the set of possible inputs
        self.dXddt = self.get_dXddt(S)   # dXddt[alpha][beta] = {0,x1 xor x0, x2 xor x0, x3 xor x0}, the set of possible crossing differences
        self.Xbct = self.get_Xbct(S, Sinv) # Xbct[alpha][beta] = {x0,x1,..}, the set of possible inputs
        self.DBT = self.get_DBT(S, Sinv) # dXbct[alpha][beta][y1^y2] = {y0, y1, ..}
        self.BDT = self.get_BDT(S, Sinv) # DXbct[alpha][beta][x1^x3] = {x0, x1, ..}
        self.SD = self.get_SD(S)      # SD[i]  = {d | ddt[i][d] > 0 }
        #self.SDi = self.get_SD(Sinv)  # SDi[i] = {d | ddt[d][i] > 0 }
        self.SDi = self.get_SDi(Sinv)  # SDi[i] = {d | ddt[d][i] > 0 }
        self.SB = self.get_SB(S)      # SB[i]  = {d | bct[i][d] > 0 } 
        self.SBi = self.get_SB(Sinv)  # SBi[i] = {d | bct[d][i] > 0 }
        # alpha --- *
        #       -    -
        #        -    -
        #         -    -
        #           *--- beta
        self.DBCT = self.get_DBCT()  # DBCT[alpha][beta] = int
        self.DBCT_dv = self.get_DBCT_dashv()  # DBCT_dv[alpha][beta][gamma] = int or float
        self.DBCT_vd = self.get_DBCT_vdash()  # DBCT_vd[alpha][beta][gamma] = int or float
        self.C12_2ddt_Ep1_table = self.x_ddt2_y = self.get_x_2ddt_y()
        self.C12_3ddt_Fp5_table = self.x_ddt3_y = self.get_x_3ddt_y()
        self.fp12_2ddti_d1_table = self.x_ddt2i_y = self.get_x_2ddti_y()
        self.fp12_3ddti_c5_table = self.x_ddt3i_y = self.get_x_3ddti_y()
        self.DBT_star = self.get_DBT_star(S, Sinv)
        self.BDT_star = self.get_BDT_star(S, Sinv)
        self.M12_table = self.get_M12()
        self.M34_table = self.get_M34()

    def get_DDT(self, S):
        ddt = []
        for i in range(self.size):
            ddt.append( [0 for j in range(self.size)] )
        for inDiff in range(self.size):
            for x in range(self.size):
                ddt[inDiff][S[x]^S[x^inDiff]] += 1
        #print2Dlist(ddt)
        return ddt

    def get_BCT(self, S, Sinv):
        bct = []
        for i in range(self.size):
            bct.append( [0 for j in range(self.size)] )
        for inDiff in range(self.size):
            for outDiff in range(self.size):
                for x in range(self.size):
                    y1 = S[x]
                    y2 = S[x^inDiff]
                    x3 = Sinv[y1^outDiff]
                    x4 = Sinv[y2^outDiff]
                    if x3^x4 == inDiff:
                        bct[inDiff][outDiff] += 1
        #print2Dlist(bct)
        return bct

    def get_Yddt(self, S):
        Yddt = []
        for i in range(self.size):
            Yddt.append( [set([]) for j in range(self.size)] )
        for inDiff in range(self.size):
            for x in range(self.size):
                outDiff = S[x]^S[x^inDiff]
                Yddt[inDiff][outDiff] |= set([S[x]])
        return Yddt

    def get_Xddt(self, S):
        Xddt = []
        for i in range(self.size):
            Xddt.append( [set([]) for j in range(self.size)] )
        for inDiff in range(self.size):
            for x in range(self.size):
                outDiff = S[x]^S[x^inDiff]
                Xddt[inDiff][outDiff] |= set([x])
        return Xddt

    def get_dYddt(self, S):
        dYddt = []
        for i in range(self.size):
            dYddt.append( [set([]) for j in range(self.size)] )
        for inDiff in range(self.size):
            for outDiff in range(self.size):
                if len(self.Yddt[inDiff][outDiff])>0:
                    ls = []
                    for y in self.Yddt[inDiff][outDiff]:
                        ls.append(y)
                    lls = [ls[i]^ls[0] for i in range(len(ls))]
                    dYddt[inDiff][outDiff] = set(lls)
        return dYddt

    def get_dXddt(self, S):
        dXddt = []
        for i in range(self.size):
            dXddt.append( [set([]) for j in range(self.size)] )
        for inDiff in range(self.size):
            for outDiff in range(self.size):
                if len(self.Xddt[inDiff][outDiff])>0:
                    ls = []
                    for x in self.Xddt[inDiff][outDiff]:
                        ls.append(x)
                    lls = [ls[i]^ls[0] for i in range(len(ls))]
                    dXddt[inDiff][outDiff] = set(lls)
        return dXddt
    
    def get_Xbct(self, S, Sinv):
        Xbct = []
        for i in range(self.size):
            Xbct.append( [set([]) for j in range(self.size)] )
        for inDiff in range(self.size):
            for outDiff in range(self.size):
                for x in range(self.size):
                    y1 = S[x]
                    y2 = S[x^inDiff]
                    x3 = Sinv[y1^outDiff]
                    x4 = Sinv[y2^outDiff]
                    if x3^x4 == inDiff:
                        Xbct[inDiff][outDiff] |= set([x])
        return Xbct
    
    def get_BDT(self, S, Sinv):
        dXbct = []
        for i in range(self.size):
            matrix = []
            for j in range(self.size):
                matrix.append( [set([]) for k in range(self.size)] )
            dXbct.append(matrix)
        for inDiff in range(self.size):
            for outDiff in range(self.size):
                for x in range(self.size):
                    y1 = S[x]
                    y2 = S[x^inDiff]
                    x3 = Sinv[y1^outDiff]
                    x4 = Sinv[y2^outDiff]
                    if x3^x4 == inDiff:
                        dXbct[inDiff][outDiff][x^x3] |= set([x])
        return dXbct

    def get_BDT_star(self, S, Sinv):
        print('\nComputing the BDT* was started ...')
        print('Time complexity = 2^(%0.2f)' % math.log(self.size**4, 2))
        print('Memory complexity = 2^(%0.2fd)' % math.log(self.size**4, 2))
        dXbct = [[[[set([]) for k in range(self.size)] for outDiff2 in range(self.size)] for outDiff1 in range(self.size)] for inDiff in range(self.size)]
        for inDiff in range(self.size):
            for outDiff1 in range(self.size):
                for outDiff2 in range(self.size):
                    for x in range(self.size):
                        y1 = S[x]
                        y2 = S[x^inDiff]
                        x3 = Sinv[y1^outDiff1]
                        x4 = Sinv[y2^outDiff2]
                        if x3^x4 == inDiff:
                            dXbct[inDiff][outDiff1][outDiff2][x^x3] |= set([x])
        print('Construction of BDT* was finished ...\n')
        return dXbct
    
    def get_DBT(self, S, Sinv):
        dXbct = []
        for i in range(self.size):
            matrix = []
            for j in range(self.size):
                matrix.append( [set([]) for k in range(self.size)] )
            dXbct.append(matrix)
        for inDiff in range(self.size):
            for outDiff in range(self.size):
                for x in range(self.size):
                    y1 = S[x]
                    y2 = S[x^inDiff]
                    x3 = Sinv[y1^outDiff]
                    x4 = Sinv[y2^outDiff]
                    if x3^x4 == inDiff:
                        dXbct[inDiff][outDiff][y1^y2] |= set([y1])
        return dXbct
    
    def get_DBT_star(self, S, Sinv):
        print('\nComputing the DBT* was started ...')
        print('Time complexity = 2^(%0.2f)' % math.log(self.size**4, 2))
        print('Memory complexity = 2^(%0.2fd)' % math.log(self.size**4, 2))
        dXbct = [[[[set([]) for k in range(self.size)] for outDiff in range(self.size)] for inDiff1 in range(self.size)] for inDiff2 in range(self.size)]
        for i in range(self.size):
            matrix = []
            for j in range(self.size):
                matrix.append( [set([]) for k in range(self.size)] )
            dXbct.append(matrix)
        for inDiff1 in range(self.size):
            for inDiff2 in range(self.size):
                for outDiff in range(self.size):
                    for x in range(self.size):
                        y1 = S[x]
                        y2 = S[x^inDiff1]
                        x3 = Sinv[y1^outDiff]
                        x4 = Sinv[y2^outDiff]
                        if x3^x4 == inDiff2:
                            dXbct[inDiff1][inDiff2][outDiff][y1^y2] |= set([y1])
        print('Construction of DBT* was finished ...\n')
        return dXbct
    

    def get_SD(self, S):
        Sd = [set([]) for i in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                if self.ddt[i][j]>0:
                    Sd[i] |= set([j])
        return Sd

    def get_SDi(self, S):
        SDi_table = [set() for i in range(self.size)]
        for j in range(self.size):
            for i in range(self.size):
                if self.ddt[i][j] > 0:
                    SDi_table[j] |= set([i])
        return SDi_table

    def get_SB(self, S):
        Sb = [set([]) for i in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                if self.bct[j][i]>0:
                    Sb[i] |= set([j])
        return Sb
    
    def get_DBCT(self):
        DBCT = []
        for i in range(self.size):
            DBCT.append( [float(0) for j in range(self.size)] )
        for alpha in range(self.size):
            for beta in range(self.size):
                alist = self.SD[alpha] & self.SBi[beta]
                if len(alist) == 0:
                    DBCT[alpha][beta] = 0
                else:
                    for a in alist:
                        for b in range(self.size):
                            s = self.BDT[a][beta][b]
                            if len(s) and b in self.dYddt[alpha][a]:                            
                                DBCT[alpha][beta] += len(s)*self.ddt[alpha][a]
        return DBCT

    def get_DBCT_dashv(self):
        """
        alpha -------- *
               -         -
                -          -
                 beta -----gamma
        """
        pgram = []
        for i in range(self.size):
            submat = []
            for j in range(self.size):
                submat.append( [float(0) for k in range(self.size)] )
            pgram.append(submat)
        for alpha in range(self.size):
            for beta in range(self.size):
                for gamma in range(self.size):
                    alist = self.SD[alpha] & self.SBi[gamma]
                    num = 0
                    if len(alist) > 0:
                        for a in alist:
                            s = self.BDT[a][gamma][beta]
                            if len(s) and beta in self.dYddt[alpha][a]:                            
                                num += len(s)*self.ddt[alpha][a]
                    pgram[alpha][beta][gamma] = num
        return pgram

    def get_DBCT_vdash(self):
        """
        alpha -------- beta
               -         -
                -          -
                 * -----  gamma
        """
        pgram = []
        for i in range(self.size):
            submat = []
            for j in range(self.size):
                submat.append( [float(0) for k in range(self.size)] )
            pgram.append(submat)
        for alpha in range(self.size):
            for beta in range(self.size):
                for gamma in range(self.size):        
                    blist = self.SB[alpha] & self.SDi[gamma]
                    num = 0
                    if len(blist) > 0:
                        for b in blist:
                            s = self.DBT[alpha][b][beta]
                            if len(s) and beta in self.dXddt[b][gamma]:                            
                                num += len(s)*self.ddt[b][gamma]
                    pgram[alpha][beta][gamma] = num
        return pgram
    
    def accumulativeDDT(self, d1):
        d2 = dict()
        for i in range(self.size) :
            num = 0
            for j in range(self.size) :
                num += d1[j]*self.ddt[j][i]
            d2[i] = num
        return  d2

    def accumulativeDDTinv(self, d1):
        d2 = dict()
        for i in range(self.size) :
            num = 0
            for j in range(self.size) :
                num += d1[j]*self.ddt[i][j]
            d2[i] = num
        return  d2

    
    def get_x_2ddt_y(self):
        x_ddt2_y_table = [[float(0) for i in range(self.size)] for j in range(self.size)]
        for x in range(0, self.size):
            for y in range(0, self.size):
                temp = float(0)
                for k in range(0, self.size):
                    temp += self.ddt[x][k] * self.ddt[k][y]
                x_ddt2_y_table[x][y] = temp
        return x_ddt2_y_table
    
    def get_x_3ddt_y(self):
        x_ddt3_y_table = [[float(0) for i in range(self.size)] for j in range(self.size)]
        for x in range(0, self.size):
            for y in range(0, self.size):
                temp = float(0)
                for k1 in range(0, self.size):
                    for k2 in range(0, self.size):
                        temp += self.ddt[x][k1] * self.ddt[k1][k2] * self.ddt[k2][y]
                x_ddt3_y_table[x][y] = temp
        return x_ddt3_y_table

    def get_x_2ddti_y(self):
        x_ddt2i_y_table = [[float(0) for i in range(self.size)] for j in range(self.size)]
        for x in range(0, self.size):
            for y in range(0, self.size):
                temp = float(0)
                for k in range(0, self.size):
                    temp += self.ddt[y][k] * self.ddt[k][x] 
                x_ddt2i_y_table[x][y] = temp
        return x_ddt2i_y_table
    
    def get_x_3ddti_y(self):
        x_ddt3i_y_table = [[float(0) for i in range(self.size)] for j in range(self.size)]
        for x in range(0, self.size):
            for y in range(0, self.size):
                temp = float(0)
                for k1 in range(0, self.size):
                    for k2 in range(0, self.size):
                        temp += self.ddt[y][k2] * self.ddt[k2][k1] * self.ddt[k1][x]
                x_ddt3i_y_table[x][y] = temp
        return x_ddt3i_y_table
    
    # def get_M0(self, Xp9):
    #     M0_table = [[0 for B9 in range(self.size)] for b9 in range(self.size)]
    #     for b9 in range(self.size):
    #         for B9 in range(self.size):
    #             num = 0
    #             for A51 in range(self.size):
    #                 for A52 in range(self.size):
    #                     num += len(self.DBT_star[A51][A52][b9][B9]) * self.ddt[Xp9][A51] * self.ddt[Xp9][A52]
    #             M0_table[b9][B9] = num
    #     return M0_table
    
    def get_M1(self):
        M1_table = [[[[0 for c5 in range(self.size)] for B9 in range(self.size)] for A52 in range(self.size)] for A51 in range(self.size)]
        for A51 in range(self.size):
            for A52 in range(self.size):
                for B9 in range(self.size):
                    for c5 in range(self.size):
                        num = 0
                        for b9 in range(self.size):
                            num += len(self.DBT_star[A51][A52][b9][B9]) * len(self.BDT[B9][c5][b9])
                        M1_table[A51][A52][B9][c5] = num
        return M1_table
    
    def get_M2(self):
        M2_table = [[[0 for d1 in range(self.size)] for C12 in range(self.size)] for B9 in range(self.size)]
        for B9 in range(self.size):
            for C12 in range(self.size):
                for d1 in range(self.size):
                    num = 0
                    for c12 in range(self.size):
                        num += len(self.DBT[B9][c12][C12]) * len(self.BDT[C12][d1][c12])
                    M2_table[B9][C12][d1] = num
        return M2_table

    def get_M3(self):
        M3_table = [[[0 for gp9 in range(self.size)] for fp12 in range(self.size)] for Ep1 in range(self.size)]
        for Ep1 in range(self.size):
            for fp12 in range(self.size):
                for gp9 in range(self.size):
                    num = 0
                    for F12 in range(self.size):
                        num += len(self.DBT[Ep1][fp12][F12]) * len(self.BDT[F12][gp9][fp12])
                    M3_table[Ep1][fp12][gp9] = num
        return M3_table
    
    # def get_M5(self, y9):
    #     M5_table = [[0 for gp9 in range(self.size)] for G9 in range(self.size)]
    #     for G9 in range(self.size):
    #         for gp9 in range(self.size):
    #             num = 0
    #             for h51 in range(self.size):
    #                 for h52 in range(self.size):
    #                     num += len(self.BDT_star[G9][h51][h52][gp9]) * self.ddt[h51][y9] * self.ddt[h52][y9]
    #             M5_table[G9][gp9] = num
    #     return M5_table
    
    def get_M4(self):
        M4_table = [[[[0 for h52 in range(self.size)] for h51 in range(self.size)] for gp9 in range(self.size)] for Fp5 in range(self.size)]
        for Fp5 in range(self.size):
            for gp9 in range(self.size):
                for h51 in range(self.size):
                    for h52 in range(self.size):
                        num = 0
                        for G9 in range(self.size):
                            num += len(self.DBT[Fp5][gp9][G9]) * len(self.BDT_star[G9][h51][h52][gp9])
                        M4_table[Fp5][gp9][h51][h52] = num
        return M4_table
    
    def get_M12(self):
        M1_table = self.get_M1()
        M2_table = self.get_M2()
        M12_table = [[[[[0 for d1 in range(self.size)] for C12 in range(self.size)] for c5 in range(self.size)] for A52 in range(self.size)] for A51 in range(self.size)]
        for A51 in range(self.size):
            for A52 in range(self.size):
                for c5 in range(self.size):
                    for C12 in range(self.size):
                        for d1 in range(self.size):
                            num = 0
                            for B9 in range(self.size):
                                num += M1_table[A51][A52][B9][c5] * M2_table[B9][C12][d1]
                            M12_table[A51][A52][c5][C12][d1] = num
        return M12_table

    def get_M34(self):
        M3_table = self.get_M3()
        M4_table = self.get_M4()
        M34_table = [[[[[0 for h52 in range(self.size)] for h51 in range(self.size)] for Fp5 in range(self.size)] for fp12 in range(self.size)] for Ep1 in range(self.size)]
        for Ep1 in range(self.size):
            for fp12 in range(self.size):
                for Fp5 in range(self.size):
                    for h51 in range(self.size):
                        for h52 in range(self.size):
                            num = 0
                            for gp9 in range(self.size):
                                num += M3_table[Ep1][fp12][gp9] * M4_table[Fp5][gp9][h51][h52]
                            M34_table[Ep1][fp12][Fp5][h51][h52] = num
        return M34_table

    def probability_7r(self, A51, A52, h51, h52):
        print('Computing the probability of 7-round middle part for (%d, %d, %d, %d)' % (A51, A52, h51, h52))
        print('Time complexity = 2^(%0.2f)' % math.log(self.size**6, 2))
        num = 0
        for c5 in range(self.size):
            for C12 in range(self.size):
                for d1 in range(self.size):
                    for Ep1 in range(self.size):
                        for fp12 in range(self.size):
                            for Fp5 in range(self.size):
                                num += self.M12_table[A51][A52][c5][C12][d1] * self.M34_table[Ep1][fp12][Fp5][h51][h52] * \
                                    self.fp12_2ddti_d1_table[fp12][d1] * self.fp12_3ddti_c5_table[fp12][c5] * \
                                    self.C12_2ddt_Ep1_table[C12][Ep1] * self.C12_3ddt_Fp5_table[C12][Fp5]
        if num == 0:
            return '-inf'
        else:
            return math.log(num, 2) - 18*4
# Serial execution
#print(BCT.probability_7r(0xA, 0xA, 0xA, 0xA))
# print("\nGenerating the 4-dimensional probability matrix of 7-round middle part ...\n")
# start_time = time.time()
# pr_matrix = [[[[0 for i in range(1, BCT.size)] for j in range(1, BCT.size)] for k in range(1, BCT.size)] for L in range(1, BCT.size)]
# n = BCT.size
# for i in range(1, n):
#     for j in range(1, n):
#         for k in range(1, n):
#             for L in range(1, n):
#                 pr = BCT.probability_7r(i, j, k, L)
#                 if pr != '-inf':
#                     pr_matrix[i - 1][j - 1][k - 1][L - 1] = pr
#                     print('pr(%01X, %01X, %01X, %01X) = 2^(%0.2f)' % (i, j, k, L, pr))
#                 else:
#                     pr_matrix[i - 1][j - 1][k - 1][L - 1] = 0
#                     print('pr(%01X, %01X, %01X, %01X) = 0' % (i, j, k, L))
# elapsed_time = time.time() - start_time
# print("Elapsed time : %d seconds\n" % elapsed_time)

# with open('R7r4DSage.txt', 'w') as matrix_file:
#     matrix_file.write('[')
#     for i in range(1, n):
#         matrix_file.write('[')
#         for j in range(1, n):
#             matrix_file.write('[')
#             for k in range(1, n):
#                 matrix_file.write('[')
#                 for L in range(1, n):
#                     if L == n - 1:
#                         if pr_matrix[i - 1][j - 1][k - 1][L - 1] != 0:
#                             temp = '2^(%0.4f)' % pr_matrix[i - 1][j - 1][k - 1][L - 1]
#                         else:
#                             temp = '0'
#                     else:
#                         if pr_matrix[i - 1][j - 1][k - 1][L - 1] != 0:
#                             temp = '2^(%0.4f), ' % pr_matrix[i - 1][j - 1][k - 1][L - 1]
#                         else:
#                             temp = '0, '
#                     matrix_file.write(temp)
#                 if k == n - 1:
#                     matrix_file.write(']')
#                 else:
#                     matrix_file.write('], ')
#             if j == n - 1:
#                 matrix_file.write(']')
#             else: 
#                 matrix_file.write('], ')
#         if i == n - 1:
#             matrix_file.write(']]')
#         else:
#             matrix_file.write('], ')
        
### Parallel execution
    def compute_a_part_of_matrix(self, part_number):
        pid = current_process().name
        print(f"\nProcess {pid} started, part {part_number} out of {16}")
        print("\nGenerating row %d of 4-dimensional probability matrix of 7-round middle part ...\n" % part_number)
        pr_matrix = [[[0 for L in range(1, self.size)] for k in range(1, self.size)] for j in range(1, self.size)]
        n = self.size
        offset = 1
        i = part_number
        for j in range(offset, n):
            for k in range(offset, n):
                for L in range(offset, n):
                    pr = self.probability_7r(i, j, k, L)
                    if pr != '-inf':
                        pr_matrix[j - 1][k - 1][L - 1] = pr
                        print('pr(%01X, %01X, %01X, %01X) = 2^(%0.2f)' % (i, j, k, L, pr))
                    else:
                        pr_matrix[j - 1][k - 1][L - 1] = 0
                        print('pr(%01X, %01X, %01X, %01X) = 0' % (i, j, k, L))
        # Writing result into a text file
        file_name = 'R7r4DSage%d.txt' % part_number
        with open(file_name, 'w') as matrix_file:
            matrix_file.write('row : %d\n' % part_number)
            matrix_file.write('[')
            for j in range(offset, n):
                matrix_file.write('[')
                for k in range(offset, n):
                    matrix_file.write('[')
                    for L in range(offset, n):
                        if L == n - 1:
                            if pr_matrix[j - 1][k - 1][L - 1] != 0:
                                temp = '2^(%0.4f)' % pr_matrix[j - 1][k - 1][L - 1]
                            else:
                                temp = '0'
                        else:
                            if pr_matrix[j - 1][k - 1][L - 1] != 0:
                                temp = '2^(%0.4f), ' % pr_matrix[j - 1][k - 1][L - 1]
                            else:
                                temp = '0, '
                        matrix_file.write(temp)
                    if k == n - 1:
                        matrix_file.write(']')
                    else:
                        matrix_file.write('], ')
                if j == n - 1:
                    matrix_file.write(']]')
                else: 
                    matrix_file.write('], ')

if __name__ == "__main__":
    start_time = time.time()
    with Pool() as pool:
        BCT = BCT_Analyzer(S)
        arguments = [(part_number, ) for part_number in range(1, 16)]
        results = pool.starmap(BCT.compute_a_part_of_matrix, arguments)
    # processes = [Process(target = compute_a_part_of_matrix, args = (part_number))\
    #     for part_number in range(16)]
    # # Start processes
    # for pr in processes:
    #     pr.start()
    # # Exit the completed processes
    # for pr in processes:
    #     pr.join()
    elapsed_time = time.time() - start_time
    print(f"\nProcesses completed after {elapsed_time} seconds")