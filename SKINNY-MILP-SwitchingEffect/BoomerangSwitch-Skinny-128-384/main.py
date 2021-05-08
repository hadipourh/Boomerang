# H. Hadipour
# March 8, 2020
# 18 Esfand, 1398
# Applying the MILP-based method to find an optimum boomerang differential distinguisher for Skinny-128-384

from skinnyrk import Skinnyrk

def main():
    # R1 = 14
    # R = 4
    # R2 = 13
    r0, w0 = 10, 4
    r1, w1 = 9, 4
    rm, wm = 4, 2
    #number_of_pattern = 1
    time_limit = -1
    skinny = Skinnyrk(r0, r1, rm, w0, w1, wm, 1, time_limit)
    skinny.make_model()
    skinny.solve_model()

if __name__ == "__main__":
    main()
