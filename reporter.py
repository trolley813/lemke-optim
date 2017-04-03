from tabulate import tabulate
import numpy as np

class Reporter:
    def __init__(self, file_name = 'tex/_report.tex'):
        self.file = open(file_name, 'w')

    def print_numpy(self, lable, nums):
        self.file.write(lable + "\n\n" + tabulate(nums, tablefmt="latex", floatfmt=".2f") + "\n\n")

    def print_simplex_table(self, iter_no, simplex_table):
        self.file.write("\nsimplex table at iter " + str(iter_no) + " = \n\n" +  tabulate(simplex_table, tablefmt="latex", floatfmt=".2f") + "\n\n")

    def print_changes(self, base_from, base_to):
        self.file.write(str(base_from) + " -> " + str(base_to) + "\n\n")

    def print_results(self, pt, ss, scs, fs, ys):
        self.file.write(str(pt))
        self.file.write("s* = " + str(ss) + "\n\ns*' =" + str(scs) + "\n\n")
        self.file.write("f* = " + str(fs) + "\n\n")
        self.file.write("y* = " + str(ys) + "\n\n")
