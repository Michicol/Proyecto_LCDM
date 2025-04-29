import numpy as np


class EDO:
    def MetodoEuler(y0, X, f, args):
        """
        y0 -> Condiciones iniciales
        X -> Dominio
        f -> Función del lado derecho de la EDO
        args -> posibles valores de los que dependa la f
        """
        h = X[1] - X[0]  # tamaño de paso
        # se inicializa el arreglo contenedor de los valores del codominio
        Y = np.zeros(len(X))
        # se asigna el valor de las condiciones iniciales a la primera entrada del arreglo
        Y[0] = y0
        for i in range(len(X) - 1):
            Y[i + 1] = Y[i] + h * f(Y[i], X[i], args)
        return Y

    def MetodoRungeKutta(y0, X, f, args):
        """
         y0 -> Condiciones iniciales
        X -> Dominio
        f -> Función del lado derecho de la EDO
        args -> posibles valores de los que dependa la f
        """
        h = X[1] - X[0]
        Y = np.zeros(len(X))
        Y[0] = y0
        for i in range(len(X) - 1):
            k1 = f(Y[i], X[i], args)
            k2 = f(Y[i] + k1 / 2, X[i] + h / 2, args)
            Y[i + 1] = Y[i] + h / 2 * (k1 + 2 * k2)
        return Y

    def rk4Solve(X, F, U0, **args):
        n = len(X)
        h = (X[n - 1] - X[0]) / n
        U = np.zeros((n, len(U0)))

        U[0] = U0

        for i in range(0, n - 1):
            k1 = F(U[i], **args)
            k2 = F(U[i] + k1 * h / 2, X[i], args)
            k3 = F(U[i] + k2 * h / 2, X[i], args)
            k4 = F(U[i] + k3 * h, args, X[i], args)
            U[i + 1] = U[i] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        return U
