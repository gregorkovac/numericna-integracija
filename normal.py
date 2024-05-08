import numpy as np

"""
std_normal(x): vrne vrednost standardne normalne porazdelitve v točki x
"""
def std_normal(x):
    return 1 / np.sqrt(2 * np.pi) * np.exp(-x**2 / 2)

def transf(x):
    return np.tanh(x)

def inv_transf(x):
    x[x == -1] = -1 + 1e-11
    x[x == 1] = 1 - 1e-11
    return np.arctanh(x)

"""
std_normal_integral(x, n, lower_limit): vrne aproksimacijo integrala standardne normalne porazdelitve na intervalu [-neskončno, x] z uporabo trapeznega pravila

Vhod:
    x (float) ... zgornja meja integrala
    n (int) ... število podintervalov
    lower_limit (float) ... spodnja meja integrala, ki se uporabi namesto -neskončno

Izhod: (float) aproksimacija integrala
"""
def std_normal_integral(x, n=1000000):

    a = -1
    b = transf(x)

    # Izračunamo dolžino koraka
    h = (b - a) / n

    # Izračunamo vrednosti funkcije v točkah
    t_vals = np.linspace(a, b, n + 1)
    f_vals = std_normal(inv_transf(t_vals)) / (1 - t_vals**2 + 1e-20)

    # Izračunamo integral s trapeznim pravilom
    integral = h * (np.sum(f_vals) - 0.5 * (f_vals[0] + f_vals[-1]))

    return integral
