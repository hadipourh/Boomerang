# -*- coding: utf-8 -*-
"""
Created on May 25 2020

@authors: Long Song and Hosein Hadipour
"""


import math
import time

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
        print(Sinv)
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
        self.SDi = self.get_SD(Sinv)  # SDi[i] = {d | ddt[d][i] > 0 }
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
    
    def get_SD(self, S):
        Sd = [set([]) for i in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                if self.ddt[i][j]>0:
                    Sd[i] |= set([j])
        return Sd
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
        
    def fixedColors(self, A5p, h9, purple, cyan, blue, green, cyan_ddt2, cyan_ddt3, green_ddti2, green_ddti3):
        num = float(0)
        for c9 in range(1, self.size): # green_ddti3:
            for d12 in range(1, self.size): #green_ddti2:
                for E1p in range(1, self.size): #cyan_ddt2:
                    for F5p in range(1, self.size): #cyan_ddt3:
                        #print(c9, d12, E1p, F5p)
                        this  = self.DBCT_vd[A5p][purple][c9]*green_ddti3[c9] #/(2^4)^5
                        this *= self.DBCT_vd[purple][cyan][d12]*green_ddti2[d12] #/(2^4)^4                        
                        this *= self.DBCT_dv[E1p][green][blue]*cyan_ddt2[E1p] #/(2^4)^4
                        this *= self.DBCT_dv[F5p][blue][h9]*cyan_ddt3[F5p] #/(2^4)^5
                        num += this
        return num
    
    def fiveBirds(self, A5p, h9):
        num = float(0)
        for purple in self.SD[A5p]:
            for cyan in self.SD[purple]:
                cyan_ddt1 = {}       
                for i in range(16):
                    cyan_ddt1[i] = self.ddt[cyan][i] 
                cyan_ddt2 = self.accumulativeDDT(cyan_ddt1)
                cyan_ddt3 = self.accumulativeDDT(cyan_ddt2)
                for blue in self.SDi[h9]:
                    for green in self.SDi[blue]:
                        green_ddti1 = {}       
                        for i in range(16):
                            green_ddti1[i] = self.ddt[i][green] 
                        green_ddti2 = self.accumulativeDDTinv(green_ddti1)
                        green_ddti3 = self.accumulativeDDTinv(green_ddti2)
                        
                        this = self.fixedColors(A5p, h9, purple, cyan, blue, green, cyan_ddt2, cyan_ddt3, green_ddti2, green_ddti3)
                        #print(math.log(this, 2))
                        num += this
        return math.log(num, 2) - 18*4

    
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
    
    def get_M1(self, Ap5):
        M1_table = [[0 for c5 in range(self.size)] for B9 in range(self.size)]
        for B9 in range(self.size):
            for c5 in range(self.size):
                num = 0
                for b9 in range(self.size):
                    num += len(self.DBT[Ap5][b9][B9]) * len(self.BDT[B9][c5][b9])
                M1_table[B9][c5] = num
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
    
    def get_M4(self, h5):
        M4_table = [[0 for gp9 in range(self.size)] for Fp5 in range(self.size)]
        for Fp5 in range(self.size):
            for gp9 in range(self.size):
                num = 0
                for G9 in range(self.size):
                    num += len(self.DBT[Fp5][gp9][G9]) * len(self.BDT[G9][h5][gp9])
                M4_table[Fp5][gp9] = num
        return M4_table

    def get_M12(self, Ap5):
        M1 = self.get_M1(Ap5)
        M2 = self.get_M2()
        M12_table = [[[0 for d1 in range(self.size)] for C12 in range(self.size)] for c5 in range(self.size)]
        for c5 in range(self.size):
            for C12 in range(self.size):
                for d1 in range(self.size):
                    num = 0
                    for B9 in range(self.size):
                        num += M1[B9][c5] * M2[B9][C12][d1]
                    M12_table[c5][C12][d1] = num
        return M12_table
    
    def get_M34(self, h5):
        M3 = self.get_M3()
        M4 = self.get_M4(h5)
        M34_table = [[[0 for Fp5 in range(self.size)] for fp12 in range(self.size)] for Ep1 in range(self.size)]
        for Ep1 in range(self.size):
            for fp12 in range(self.size):
                for Fp5 in range(self.size):
                    num = 0
                    for gp9 in range(self.size):
                        num += M3[Ep1][fp12][gp9] * M4[Fp5][gp9]
                    M34_table[Ep1][fp12][Fp5] = num
        return M34_table
    
    def probability_7r(self, Ap5, h5):
        fp12_2ddti_d1_table = self.get_x_2ddti_y()
        fp12_3ddti_c5_table = self.get_x_3ddti_y()
        C12_2ddt_Ep1_table = self.get_x_2ddt_y()
        C12_3ddt_Fp5_table = self.get_x_3ddt_y()
        M12_table = self.get_M12(Ap5)
        M34_table = self.get_M34(h5)
        num = 0
        for c5 in range(self.size):
            for C12 in range(self.size):
                for d1 in range(self.size):
                    for Ep1 in range(self.size):
                        for fp12 in range(self.size):
                            for Fp5 in range(self.size):
                                num += M12_table[c5][C12][d1] * M34_table[Ep1][fp12][Fp5] * fp12_2ddti_d1_table[fp12][d1] * fp12_3ddti_c5_table[fp12][c5] * \
                                    C12_2ddt_Ep1_table[C12][Ep1] * C12_3ddt_Fp5_table[C12][Fp5]
        if num == 0:
            return '-inf'
        else:
            return math.log(num, 2) - 18*4

BCT = BCT_Analyzer(S)
print("Killing five birds with one stone started :)")
start_time = time.time()
print(BCT.probability_7r(10, 10))
elapsed_time = time.time() - start_time
print("Elapsed time : %d seconds" % elapsed_time)


