# -*- coding: utf-8 -*-
"""
Created on May 25 2020

@author: Hosein Hadipour
"""


import math
import time
#import numpy as np

S = [0xc, 0x6, 0x9, 0x0, 0x1, 0xa, 0x2, 0xb, 0x3, 0x8, 0x5, 0xd, 0x4, 0xe, 0x7, 0xf]     # skinny 4-bit s-box

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
        self.x_ddt2_y = self.get_x_2ddt_y()
        self.x_ddt3_y = self.get_x_3ddt_y()
        self.x_ddt2i_y = self.get_x_2ddti_y()
        self.x_ddt3i_y = self.get_x_3ddti_y()
        self.DBT_star = self.get_DBT_star(S, Sinv)
        self.BDT_star = self.get_BDT_star(S, Sinv)
        self.BCTDI = self.get_BCTDI(S, Sinv)


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

    def get_BCTDI(self, S, Sinv):
        bctdi = [[[0 for inDiff1 in range(self.size)] for inDiff2 in range(self.size)] for outDiff in range(self.size)]
        for inDiff1 in range(self.size):
            for inDiff2 in range(self.size):
                for outDiff in range(self.size):
                    for x in range(self.size):
                        y1 = S[x]
                        y2 = S[x ^ inDiff1]
                        x3 = Sinv[y1 ^ outDiff]
                        x4 = Sinv[y2 ^ outDiff]
                        if x3 ^ x4 == inDiff2:
                            bctdi[inDiff1][inDiff2][outDiff] += 1
        return bctdi

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
        print('Memory complexity = 2^(%0.2f)' % math.log(self.size**4, 2))
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
        dXbct = [[[[set([]) for k in range(self.size)] for outDiff in range(self.size)] for inDiff2 in range(self.size)] for inDiff1 in range(self.size)]
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

    def get_DBTDO(self, S, Sinv):
        dXbct = [[[[set([]) for yDiff2 in range(self.size)] for yDiff1 in range(self.size)] for outDiff in range(self.size)] for inDiff in range(self.size)]
        for inDiff in range(self.size):
            for outDiff in range(self.size):
                for x in range(self.size):
                    y1 = S[x]
                    y2 = S[x^inDiff]
                    x3 = Sinv[y1^outDiff]
                    x4 = Sinv[y2^outDiff]
                    if x3^x4 == inDiff:
                        dXbct[inDiff][outDiff][yDiff] |= set([y1])
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
        
    def compute_probability_3r(self, B11, Cp10, e1, ep13):
        num = 0
        # for dp14 in range(self.size):
        #     for C91 in range(self.size):
        #         for C92 in range(self.size):
        #             for dp4 in range(self.size):
        #                 for C13 in range(self.size):
        #                     # for dp11 in range(self.size):
        #                     #     # for dp12 in range(self.size):
        #                     num += self.DBCT[B11][dp14] * self.ddt[B11][C91] * self.ddt[B11][C92] * \
        #                         self.DBCT_vd[B11][C13][dp4] * self.BCTDI[C91][C92][dp14] * self.DBCT_dv[C13][dp4][ep13] * \
        #                             self.bct[Cp10][dp4] * self.ddt[dp11][e1] * self.ddt[dp11][e1] * self.ddt[dp14][ep13]
        for dp14 in range(self.size):
            for C91 in range(self.size):
                for dp4 in range(self.size):
                    for C13 in range(self.size):
                        for dp11 in range(self.size):
                            for dp12 in range(self.size):
                                num += self.DBCT[B11][dp14] * self.ddt[B11][C91] * self.ddt[B11][C91] * \
                                    self.DBCT_vd[B11][C13][dp4] * self.bct[C91][dp14] * self.DBCT_dv[C13][dp4][ep13] * \
                                        self.bct[Cp10][dp4] * self.ddt[dp11][e1] * self.ddt[dp12][e1] * self.ddt[dp14][ep13]
        print(num)
        print("self.size = %d" % self.size)
        if num != 0:
            return (math.log(num, 2) - (13 * 4))
        else:
            return '-inf'

BCT = BCT_Analyzer(S)
print('computation started ...')
print(BCT.compute_probability_3r(B11=0x2, Cp10=0xD, e1=0x5, ep13=0x5))

