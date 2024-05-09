import numpy as np

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

# Sources: https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_quadrature
#          https://pomax.github.io/bezierinfo/legendre-gauss.html
def gauss_legendre_points_and_weights(n):
    if n == 3:
        points = [-np.sqrt(3/5), 0, np.sqrt(3/5)]
        weights = [5/9, 8/9, 5/9]
    elif n == 4:
        points = [-np.sqrt((3 + 2 * np.sqrt(6/5)) / 7), -np.sqrt((3 - 2 * np.sqrt(6/5)) / 7), np.sqrt((3 - 2 * np.sqrt(6/5)) / 7), np.sqrt((3 + 2 * np.sqrt(6/5)) / 7)]
        weights = [(18 - np.sqrt(30)) / 36, (18 + np.sqrt(30)) / 36, (18 + np.sqrt(30)) / 36, (18 - np.sqrt(30)) / 36]
    elif n == 5:
        points = [-1/3 * np.sqrt(5 + 2 * np.sqrt(10/7)), -1/3 * np.sqrt(5 - 2 * np.sqrt(10/7)), 0, 1/3 * np.sqrt(5 - 2 * np.sqrt(10/7)), 1/3 * np.sqrt(5 + 2 * np.sqrt(10/7))]
        weights = [(322 - 13 * np.sqrt(70)) / 900, (322 + 13 * np.sqrt(70)) / 900, 128/225, (322 + 13 * np.sqrt(70)) / 900, (322 - 13 * np.sqrt(70)) / 900]
    elif n == 8:
        points = [0.183434642495650, 0.525532409916329, 0.796666477413627, 0.960289856497536, -0.183434642495650, -0.525532409916329, -0.796666477413627, -0.960289856497536]
        weights = [0.362683783378362, 0.313706645877887, 0.222381034453374, 0.101228536290376, 0.362683783378362, 0.313706645877887, 0.222381034453374, 0.101228536290376]

    return points, weights

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

    # Določimo vozlišča in uteži za Gaussovo kvadraturo
    nodes, weights = gauss_legendre_points_and_weights(n)

    # Izračunamo integral
    integral = 0
    for i in range(n):
        integral += std_normal(((b - a) * nodes[i] + b + a) / 2) * (b - a) / 2 * weights[i]

    # Upoštevamo, da računamo integral simetrične gostote verjetnosti, ki ima srednjo vrednost v 0
    integral = 0.5 + sgn * integral

    return integral
