from tabulate import tabulate
import numpy as np


class Reporter:

    def __init__(self, file_name='tex/_report.tex'):
        self.file = open(file_name, 'w')

    def print_numpy(self, table, nums):
        self.file.write("%s\n\n%s\n\n" % (table, tabulate(nums,
                                                          tablefmt="latex",
                                                          floatfmt=".2f")))

    def print_simplex_table(self, iter_no, simplex_table):
        self.file.write("\nsimplex table at iter %s = \n\n%s\n\n"
                        % (iter_no, tabulate(simplex_table,
                                             tablefmt="latex",
                                             floatfmt=".1f")))

    def print_changes(self, base_from, base_to):
        self.file.write("%s -> %s\n\n" % (base_from, base_to))

    def print_results(self, pt, ss, scs, fs, ys):
        self.file.write(str(pt))
        self.file.write("s* = %s\n\ns*' = %s\n\n" % (ss, scs))
        self.file.write("f* = %s\n\n" % fs)
        self.file.write("y* = %s\n\n" % ys)
