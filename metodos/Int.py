import numpy as np


class Integral:
    @staticmethod
    def SumaInferior(a, b, dom, *args):
        """
        a -> es el valor donde inicia el intervalo
        b -> el valor donde termina el intervalo
        dom -> es el dominio o el intervalo sobre el que se integra
        f -> es la función que se desea integrar
        k -> Argumerntos opcionales
        """
        area = 0
        h = (self.b - self.a) / (len(self.dom) - 1)
        for i in range(len(self.dom) - 1):
            area += h * self.f(self.dom[i], *args)
        # print(self.k)
        return np.array(area)

    def SumaSuperior(self, *args):
        """
        a -> es el valor donde inicia el intervalo
        b -> el valor donde termina el intervalo
        dom -> es el dominio o el intervalo sobre el que se integra
        f -> es la función que se desea integrar
        k -> Argumentos opcionales
        Es necesario colocar k en su función aún cuando no sea necesaria
        """
        area = 0
        h = (self.b - self.a) / (len(self.dom) - 1)

        for i in range(1, len(self.dom)):
            area += h * self.f(self.dom[i - 1], *args)
        return np.array(area)

    def ReglaTrapezoidal(self, *args):
        """
        a -> es el valor donde inicia el intervalo
        b -> el valor donde termina el intervalo
        dom -> es el dominio o el intervalo sobre el que se integra
        f -> es la función que se desea integrar
        k -> Argumentos opcionales
        Es necesario colocar k en su función aún cuando no sea necesaria
        """
        area = 0
        h = (self.b - self.a) / (len(self.dom) - 1)
        for i in range(1, len(self.dom)):
            area += (
                h / 2 * (self.f(self.dom[i], *args) +
                         self.f(self.dom[i - 1], *args))
            )
        return np.array(area)

    def ReglaSimpson(self, N, *args):
        """
        a -> el valor inicial del intervalo en que se está integrando
        b -> valor final del intervalo
        N -> Número de particiones donde N tiene que ser par
        f -> es la función que se va integrar
        """

        if N % 2 != 0:
            raise ValueError('El número de subintervalos "N" debe ser par')
        else:
            h = (self.b - self.a) / (N - 1)
            x = np.float64(np.linspace(self.a, self.b, N + 1))
            suma_par = 0
            suma_impar = 0

            for i in range(len(x)):
                if i == 0 or x[i] == 0:
                    continue
                elif i % 2 == 0:
                    suma_par += self.f(x[i], *args)
                else:
                    suma_impar += self.f(x[i], *args)
            integral = (
                h
                / 3
                * (
                    self.f(x[0], *args)
                    + 4 * suma_impar
                    + 2 * suma_par
                    + self.f(x[-1], *args)
                )
            )
            return np.array(integral)
