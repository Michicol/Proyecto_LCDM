from metodos.EDO import EDO
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")


def friedmann(a, t, params):
    omega_co, omega_ro = params
    omega_Ao = 1 - omega_co - omega_ro
    return a * np.sqrt(omega_co * a ** (-3) + omega_ro * a ** (-4) + omega_Ao)


t_i = 1e-10
t_f = 2
t_valores = np.linspace(t_i, t_f, 1000)
omega_co = 0.3
omega_ro = 0
a_i = 1

a_valores = EDO.rk4Solve(friedmann, [a_i], t_valores, (omega_co, omega_ro))

plt.figure()

plt.plot(t_valores, a_valores)
plt.xlim(0, 1.5)

plt.show()

1
