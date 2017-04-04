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
        if isinstance(x, float):
            return ("%5.3f" % x).replace(".", "{,}")
        if isinstance(x, Fraction):
            if x.denominator == 1:
                return "%s" % x
            else:
                return "%s\\frac{%s}{%s}" % ("-" if x.numerator < 0 else "",
                                             abs(x.numerator), x.denominator)
        else:
            return "%s" % x

    def latexise(self, table):
        table = self.latexstr(table)
        if table.ndim == 1:
            table = np.reshape(table, (-1, 1))
        res = "\\begin{array}{%s}\n" % ("c" * np.size(table, 1))
        for i in range(np.size(table, 0)):
            res += (" & ".join(table[i, :]))
            res += "\\\\" + "\n"
        res += "\\end{array}"
        return res

    def print_numpy(self, table, nums):
        self.file.write("\\[ %s  \\left( \n %s \\right) \\]" %
                        (table, self.latexise(nums)))

    def print_base(self, base):
        self.file.write("Base is: $\\{%s\\}$\n\n" % ",".join(base))

    def print_simplex_table(self, iter_no, base, simplex_table):

        self.file.write("\\[  S_{%s} = %s \\left( \n %s \\right) \\]"
                        % (iter_no, self.latexise(np.transpose(base)),
                            self.latexise(simplex_table)))

    def print_changes(self, base_from, base_to):
        self.file.write("$%s \\rightarrow %s$\n\n" % (base_from, base_to))

    def print_results(self, pt, ss, scs, fs, ys):
        self.file.write("$\\{%s\\}$\n\n" % ",".join(self.latexstr(pt)))
        self.file.write("$$s* = \\{%s\\}$$ \n\n $$s*' = \\{%s\\}$$ \n\n"
                        % (",".join(self.latexstr(ss)),
                           ",".join(self.latexstr(scs))))
        self.file.write("$$f* = \\{%s\\}$$ \n\n"
                        % ((self.latexstr(fs))))
        self.file.write("$$y* = \\{%s\\}$$ \n\n"
                        % (",".join(self.latexstr(ys))))
        self.file.write("$$\\mathrm{normal} = \\{%s\\} \\approx \\{%s\\}$$\n\n"
                        % (",".join(self.latexstr(ys / fs)),
                           ",".join(self.latexstr(ys / float(fs))
                                    )))
        self.file.write("$$\\mathrm{normal\\ length} \approx %s $$\n\n"
        % (self.latexstr(np.sum((ys / float(fs)) ** 2) ** 0.5)
        ))
