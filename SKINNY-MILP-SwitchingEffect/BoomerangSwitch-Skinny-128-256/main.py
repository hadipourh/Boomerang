# H. Hadipour
# March 8, 2020
# 18 Esfand, 1398
# Applying the MILP-based method to find an optimum boomerang differential distinguisher for Skinny-128-256

from skinnyrk import Skinnyrk

def main():
    # R1 = 11
    # R = 3
    # R2 = 11
    r0, w0 = 8, 4
    r1, w1 = 8, 4
    rm, wm = 3, 2
    # number_of_pattern = 1
    time_limit = -1
    skinny = Skinnyrk(r0, r1, rm, w0, w1, wm, 1, time_limit)
    skinny.make_model()
    skinny.solve_model()

if __name__ == "__main__":
    main()
