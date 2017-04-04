import numpy as np
from fractions import Fraction


class Solver:

    def __init__(self, z, p, reporter):
        self.z = z
        self.p = p
        self.zmp = np.array([zi - pj for zi in z for pj in p], dtype=Fraction)
        self.reporter = reporter

    def zw(self, j):
        return ("w_{%d}" % (j + 1) if j < self.m else
                ("z_{%d}" % (j + 1 - self.m) if j != 2 * self.m else "z_0"))

    def solve(self):
        E = np.eye(4, dtype=Fraction) - \
            (np.eye(4, dtype=Fraction, k=-2) + np.eye(4, dtype=Fraction, k=2))
        self.reporter.print_numpy("E =", E)
        e = np.size(E, 0)
        z = self.z
        self.reporter.print_numpy("z =", z)
        p = self.p
        self.reporter.print_numpy("p =", p)
        zmp = self.zmp
        self.reporter.print_numpy("zmp =", zmp)
        A = np.hstack((zmp, -zmp))
        self.reporter.print_numpy("A =", A)
        a = np.size(A, 0)
        b = np.ones((np.size(A, 0), 1), dtype=Fraction)
        self.reporter.print_numpy("b =0", b)
        M = np.zeros((np.size(E, 0) + np.size(A, 0),
                      np.size(E, 0) + np.size(A, 0)), dtype=Fraction)
        M[0:e, 0:e] = E + np.transpose(E)
        M[0:e, e:a + e] = -np.transpose(A)
        M[e:a + e, 0:e] = A
        self.m = np.size(M, 0)
        m = self.m
        self.reporter.print_numpy("M =", M)
        q = np.vstack([np.zeros((e, 1), dtype=Fraction), -b])
        self.reporter.print_numpy("q =", q)
        iter_no = 1
        simplex_table = np.zeros((m, 2 * m + 2), dtype=Fraction)
        simplex_table[:, 0:m] = np.eye(m, dtype=Fraction)
        simplex_table[:, m:2 * m] = -M
        simplex_table[:, -2] = -1
        simplex_table[:, -1] = np.transpose(q)
        base = np.arange(m)
        base_str = np.array([self.zw(j) for j in base])
        base_from_index = np.argmin(simplex_table[:, -1])
        base_from = base[base_from_index]
        base_to = 2 * m
        self.reporter.print_simplex_table(iter_no, base_str, simplex_table)
        self.reporter.print_base(base_str)
        self.reporter.print_changes(self.zw(base_from), self.zw(base_to))
        while 1:
            iter_no += 1
            # Replace in base
            base[base_from_index] = base_to
            base_str = np.array([self.zw(j) for j in base])
            # Recompute and print simplex_table
            leading_element = simplex_table[base_from_index, base_to]
            simplex_table[base_from_index, :] /= Fraction(leading_element)
            for i in range(m):
                if i == base_from_index:
                    continue
                else:
                    simplex_table[i, :] -= simplex_table[base_from_index, :] \
                        * simplex_table[i, base_to]
            self.reporter.print_simplex_table(iter_no, base_str, simplex_table)
            # If base_from iz z0, break, otherwise determine new base_from and
            # base_to
            if base_from == 2 * m:
                self.reporter.print_base(base_str)
                break
            base_to = base_from + m if base_from < m else base_from - m
            ratios = [simplex_table[i, -1] / simplex_table[i, base_to]
                      if simplex_table[i, base_to] > 0
                      else 10000 for i in range(m)]
            # self.reporter.print_numpy("Ratios:", ratios)
            base_from_index = np.argmin(ratios)
            base_z0_index = np.where(base == 2 * m)[0][0]
            if ratios[base_z0_index] == ratios[base_from_index]:
                base_from = 2 * m
                base_from_index = base_z0_index
            else:
                base_from = base[base_from_index]
            self.reporter.print_base(base_str)
            self.reporter.print_changes(self.zw(base_from), self.zw(base_to))

        pt = np.zeros(2 * m, dtype=Fraction)
        for i in range(len(base)):
            pt[base[i]] = simplex_table[i, -1]
        ss, scs = pt[m:m + e], pt[m + e:]
        fs = np.dot(ss, np.dot(E, np.transpose(ss)))
        ys = np.array([ss[i] - ss[i + 2] for i in range(2)])
        self.reporter.print_results(pt, ss, scs, fs, ys)

    def plot(self, plotter):
        plotter.plot(self.z, self.p, self.zmp)
