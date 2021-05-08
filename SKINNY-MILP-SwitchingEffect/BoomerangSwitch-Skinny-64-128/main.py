# H. Hadipour
# Jan 17, 2020
# 27 Day, 1398
# Applying the MILP-based method to find an optimum boomerang differential distinguisher for Skinny-64-128

from skinnyrk import Skinnyrk

if __name__ == "__main__":
        
    r0, w0 = 8, 4
    r1, w1 = 8, 4
    rm, wm = 2, 2
    number_of_patterns = 1

    time_limit = 400
    skinny = Skinnyrk(r0, r1, rm, w0, w1, wm, number_of_patterns, time_limit)
    skinny.make_model()
    skinny.solve_model()
