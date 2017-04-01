from tabulate import tabulate
import numpy as np

class Reporter:
    @staticmethod
    def print_numpy(lable, nums):
        np.set_printoptions(formatter={'all': lambda x: "$%s$" % x}, linewidth=200)
        print(lable + "\n%s\n" % nums)

    @staticmethod
    def print_simplex_table(iter_no, simplex_table):
        np.set_printoptions(formatter={'all': lambda x: "$%s$" % x}, linewidth=200)
        print("simplex_table at iter %d = \n%s\n" % (iter_no, simplex_table))


    @staticmethod
    def print_changes(base_from, base_to):
        print("%s -> %s" % (base_from, base_to))

    @staticmethod
    def print_results(pt, ss, scs, fs, ys):
        print(pt)
        print("s* =", ss, "s*' =", scs)
        print("f* =", fs)
        print("y* =", ys)
