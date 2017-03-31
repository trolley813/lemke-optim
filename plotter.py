import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

class Plotter:
	@staticmethod
	def plot(z, p, zmp):
		hull_z = ConvexHull(z)
		hull_p = ConvexHull(p)
		hull_zmp = ConvexHull(zmp)
		plt.figure(1)
		plt.subplot(121)
		plt.plot(z[:, 0], z[:, 1], 'go')
		for simplex in hull_z.simplices:
		    plt.plot(z[simplex, 0], z[simplex, 1], 'g--')
		plt.plot(p[:, 0], p[:, 1], 'bo')
		for simplex in hull_p.simplices:
		    plt.plot(p[simplex, 0], p[simplex, 1], 'b--')
		plt.subplot(122)
		plt.plot(zmp[:, 0], zmp[:, 1], 'ro')
		for simplex in hull_zmp.simplices:
		    plt.plot(zmp[simplex, 0], zmp[simplex, 1], 'r--')
		plt.show()