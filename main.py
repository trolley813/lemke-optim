import numpy as np
from fractions import Fraction

import solver
import plotter
import reporter

if __name__ == '__main__':
    z = np.array([[1, 1], [1, 2], [2, 2]], dtype=Fraction)
    p = np.array([[-1, -1], [-1, -2], [-2, -2]], dtype=Fraction)
    s = solver.Solver(z, p, reporter.Reporter())
    s.solve()
    # Plotting
    s.plot(plotter.Plotter)
