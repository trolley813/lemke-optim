import numpy as np
from fractions import Fraction


class Reporter:

    def __init__(self, file_name='tex/_report.tex'):
        self.file = open(file_name, 'w')

    @np.vectorize
    def latexstr(x):
        # Convert to LaTeX fraction
        if isinstance(x, int):
            return "%s" % x
        if isinstance(x, Fraction):
            if x.denominator == 1:
                return "%s" % x
            else:
                return "%s\\frac{%s}{%s}" % ("-" if x.numerator < 0 else "",
                                             abs(x.numerator), x.denominator)

    def latexise(self, table):
        table = self.latexstr(table)
        res = "\\[ \\left( \\begin{array}{%s}\n" % ("c" * np.size(table, 1))
        for i in range(np.size(table, 0)):
            res += (" & ".join(table[i, :]))
            res += "\\\\" + "\n"
        res += "\\end{array} \\right) \\]"
        return res

    def print_numpy(self, table, nums):
        self.file.write("%s\n\n%s\n\n" % (table, self.latexise(nums)))

    def print_base(self, base):
        self.file.write("Base is: $\\{%s\\}$\n\n" % ",".join(base))

    def print_simplex_table(self, iter_no, simplex_table):

        self.file.write("\nsimplex table at iter %s = \n\n%s\n\n"
                        % (iter_no,
                            self.latexise(simplex_table)))

    def print_changes(self, base_from, base_to):
        self.file.write("$%s \\rightarrow %s$\n\n" % (base_from, base_to))

    def print_results(self, pt, ss, scs, fs, ys):
        self.file.write(str(pt))
        self.file.write("s* = %s\n\ns*' = %s\n\n" % (ss, scs))
        self.file.write("f* = %s\n\n" % fs)
        self.file.write("y* = %s\n\n" % ys)
