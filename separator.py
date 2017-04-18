import numpy as np
import numpy.linalg as nplin
import scipy.optimize as sciopt
from fractions import Fraction

if __name__ == '__main__':
    np.set_printoptions(precision=4)
    z = np.array([[2, 6], [1, 7], [8, 5]])
    p = np.array([[4, 3], [6, 4], [1, 0]])
    print("z =\n%s" % z)
    print("p =\n%s" % p)
    zmp = np.array([zi - pj for zi in z for pj in p])
    res = sciopt.minimize(lambda c: -np.min(zmp @ c.T), np.array([1, 0]),
                          constraints=(
                              {"type": "eq", "fun": lambda c: nplin.norm(c) - 1}
                              )
                          )
    print(res)
    c = res.x
    t = -res.fun
    print("c = %s" % c)
    prod = zmp @ c.T
    print("<c, zi - pj> = %s" % prod)
    print("t = %6.4f" % t)
    prod_z = z @ c.T
    prod_p = p @ c.T
    print("<c, zi> = %s" % prod_z)
    print("<c, pj> = %s" % prod_p)
    gammaL = np.min(prod_z)
    print("gammaL = %6.4f" % gammaL)
    gammaM = np.max(prod_p)
    print("gammaM = %6.4f" % gammaM)
    gamma_star = (gammaL + gammaM) / 2
    print("gamma* = %6.4f" % gamma_star)

    def classifier(x): return 1 if (c @ x.T - gamma_star) >= 0 else 2
    for zi in z:
        print(zi, classifier(zi))
    for pj in p:
        print(pj, classifier(pj))