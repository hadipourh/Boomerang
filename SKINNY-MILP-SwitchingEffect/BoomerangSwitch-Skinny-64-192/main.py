# H. Hadipour
# Feb 11, 2020
# 22 Bahman, 1398
# Applying the MILP-based method to find an optimum boomerang differential distinguisher for Skinny-64-192 

from skinnyrk import Skinnyrk

if __name__ == "__main__":

    # R1 = 12
    # R = 3
    # R2 = 13
    r0, w0 = 9, 4
    r1, w1 = 10, 4
    rm, wm = 3, 2
    # number_of_pattern = 1
    time_limit = -1
    skinny = Skinnyrk(r0, r1, rm, w0, w1, wm, 1, time_limit)
    skinny.make_model()
    skinny.solve_model()
