#!/usr/bin/env python3

import separator
import plotter
import numpy as np

if __name__ == "__main__":
    z = np.array([[2, 6], [1, 7], [8, 5]])
    p = np.array([[4, 3], [6, 4], [1, 0]])
    c, t = separator.separator(z, p)
    plotter.Plotter.plot(z, p, normal=c * t, figurefile="./tex/sep.png")

    z = np.array([[2, 6], [6, 4], [8, 5]])
    p = np.array([[4, 3], [5, 7], [1, 0]])
    c, t = separator.separator(z, p)
    plotter.Plotter.plot(z, p, normal=c * t, figurefile="./tex/psep.png")

    z = np.array([[2, 6], [6, 7], [8, 6]])
    p = np.array([[4, 3], [5, 6], [1, 0]])
    c, t = separator.separator(z, p)
    plotter.Plotter.plot(z, p, normal=c * t, figurefile="./tex/zero.png")
