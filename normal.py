import numpy as np
from gauss_quadrature import gauss_quadrature

"""
std_normal(x): vrne vrednost standardne normalne porazdelitve v točki x
"""
def std_normal(x):
    return 1 / np.sqrt(2 * np.pi) * np.exp(-x**2 / 2)

def transf(x):
    return np.tanh(x)

def inv_transf(x):
    x = np.array(x)
    return np.arctanh(x)

"""
std_normal_integral(x, n, lower_limit): vrne aproksimacijo integrala standardne normalne porazdelitve na intervalu [-neskončno, x] z uporabo Gaussovih kvadraturnih formul

Vhod:
    x (float) ... zgornja meja integrala
    n (int) ... število podintervalov
    lower_limit (float) ... spodnja meja integrala, ki se uporabi namesto -neskončno

Izhod: (float) aproksimacija integrala
"""
def std_normal_integral(x, n=8):

    # Poskrbimo za neskončna primera
    if x == -np.inf:
        return 0
    if x == np.inf:
        return 1

    # Določimo meje integrala. Integriramo bodisi od [x, 0] ali od [0, x]. Zabeležimo si tudi predznak.
    if x < 0:
        a = x
        b = 0
        sgn = -1
    else:
        a = 0
        b = x
        sgn = 1

    # Izračunamo integral
    integral = gauss_quadrature(std_normal, a, b, n)

    # Upoštevamo, da računamo integral simetrične gostote verjetnosti, ki ima srednjo vrednost v 0
    integral = 0.5 + sgn * integral

    return integral
