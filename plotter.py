import numpy as np
import numpy.linalg as nplin
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

class Plotter:
    @staticmethod
    def plot(z, p, zmp=None, normal=None, thickness=None, gammas=None, figurefile='./tex/figure.png'):
        if zmp is None:
            zmp = np.array([zi - pj for zi in z for pj in p])
        hull_z = ConvexHull(z)
        hull_p = ConvexHull(p)
        hull_zmp = ConvexHull(zmp)
        f = plt.figure(figsize=(20,10))
        a1 = f.add_subplot(121)
        plt.plot(z[:, 0], z[:, 1], 'go')
        for simplex in hull_z.simplices:
            plt.plot(z[simplex, 0], z[simplex, 1], 'g--')
        plt.plot(p[:, 0], p[:, 1], 'bo')
        for simplex in hull_p.simplices:
            plt.plot(p[simplex, 0], p[simplex, 1], 'b--')
        if gammas:
            old_x, old_y = a1.get_xlim(), a1.get_ylim()
            if thickness is None:
                thickness = nplin.norm(normal * 1.0)
                c = normal / thickness
            else:
                c = normal
            gammaL = gammas[0]
            gammaM = gammas[1]
            gamma_star = sum(gammas) / 2
            for (g, col) in ((gammaL, "g"), (gammaM, "b"), (gamma_star, "y")):
                points = ([[x, (g - c[0] * x) / c[1]] for x in (-100, 100)]
                          if c[1] else [[g / c[0], y] for y in (-100, 100)])
                points_x = [p[0] for p in points]
                points_y = [p[1] for p in points]
                plt.plot(points_x, points_y, col)
            a1.set_xlim(old_x)
            a1.set_ylim(old_y)
        a2 = f.add_subplot(122)
        plt.plot(zmp[:, 0], zmp[:, 1], 'ro')
        for simplex in hull_zmp.simplices:
            plt.plot(zmp[simplex, 0], zmp[simplex, 1], 'r--')
        plt.plot((0, normal[0]), (0, normal[1]), 'ko--')
        a2.grid(True, ls="--")
        a1.grid(True, ls="--")
        a1.xaxis.set_major_locator(ticker.MultipleLocator(1))
        a1.yaxis.set_major_locator(ticker.MultipleLocator(1))
        a2.xaxis.set_major_locator(ticker.MultipleLocator(1))
        a2.yaxis.set_major_locator(ticker.MultipleLocator(1))
        a1.set_aspect('equal', 'datalim')
        a2.set_aspect('equal', 'datalim')
        plt.savefig(figurefile)
