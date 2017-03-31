import numpy as np
from fractions import Fraction

import solver
import plotter

z = np.array([[2, 6], [1, 7], [8, 5]], dtype=Fraction)
p = np.array([[4, 3], [6, 4], [1, 0]], dtype=Fraction)

s = solver.Solver(z, p)
s.solve()
# Plotting
s.plot(plotter.Plotter)
