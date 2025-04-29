import numpy as np


class EDO:
    def __init__(self, y0, x, f):
        self.y0 = y0
        self.x = x
        self.f = f

    def MetodoEuler(self, **args):
        """
        y0: Condiciones iniciales
        X:  Domino tipo varieblea array
        f: Fucnion lado derecho de la EDO
        args: posibles valores de los que dependa la f

        """

        h = self.x[1] - self.x[0]
        Y = np.zeros(self.x.size)
        Y[0] = self.y0

        Y[1:] = Y[:-1] + h * self.f(Y[:1], self.x[:-1], **args)

        return Y

    def MetodoRungeKutta(self):
        h = self.x[1] - self.x[0]
        Y = np.zeros(self.x.size)
        Y[0] = self.y0

        k1 = self.f(Y[:-1], self.x[:-1])
        k2 = self.f(Y[:-1] + k1 / 2, self.x[:-1] + h / 2)
        Y[1:] = Y[:-1] + h / 2 * (k1 + 2 * k2)

        return Y

    def rk4Solve(self, u0):
        self.u0 = u0

        n = self.x.size
        h = self.x[n - 1] - self.x[0]
        U = np.zeros((n, len(self.u0)))

        U[0] = u0

        k1 = self.f(U[:-1])
        k2 = self.f(U[:-1] + k1 * h / 2, self.x[:-1])
        k3 = self.f(U[:-1] + k2 * h / 2, self.x[:-1])
        k4 = self.f(U[:-1] + k3 * h, self.x[:-1])
        U[1:-1] = U[:-1] + (h / 6) * (k1 + k2 + 2 * k3 + k4)
        return U
