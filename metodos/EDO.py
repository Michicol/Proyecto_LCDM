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

    def rk4Solve(dYdX, Y0, X, args):
        """
        dYdX: Derivada de la Función
        Y0: float valor inicial
        X: arr dominio
        args: posibles parametros que requiera la derivada
        """
        n = len(X)
        h = X[1] - X[0]  # Paso de integración
        Y = np.zeros((n, len(Y0)))
        Y[0] = Y0
        for i in range(n - 1):
            k1 = dYdX(Y[i], X[i], args)
            k2 = dYdX(Y[i] + k1 * h / 2.0, X[i] + h / 2.0, args)
            k3 = dYdX(Y[i] + k2 * h / 2.0, X[i] + h / 2.0, args)
            k4 = dYdX(Y[i] + k3 * h, X[i] + h, args)
            Y[i + 1] = Y[i] + (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        return Y
