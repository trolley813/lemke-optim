#!/usr/bin/env python3

import separator
import plotter
import numpy as np

if __name__ == "__main__":
    z = np.array([[2, 6], [1, 7], [8, 5]])
    p = np.array([[4, 3], [6, 4], [1, 0]])
    separator.separator(z, p)
    plotter.Plotter.plot(z, p, figurefile="./tex/sep.png")
    
    z = np.array([[2, 6], [6, 4], [8, 5]])
    p = np.array([[4, 3], [5, 7], [1, 0]])
    separator.separator(z, p)
    plotter.Plotter.plot(z, p, figurefile="./tex/psep.png")
