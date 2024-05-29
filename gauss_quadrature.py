import numpy as np

"""
gauss_legendre_points_and_weights(n): vrne vozlišča in uteži za Gauss-Legendrovo kvadraturo stopnje n

Viri za točke in uteži:
    - https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_quadrature
    - https://pomax.github.io/bezierinfo/legendre-gauss.html
"""

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
gauss_quadrature(f, a, b, n): izračuna integral funkcije s pomočjo Gaussovih kvadraturnih formul

Vhod:
    f (function(t)) ... funkcija, katere integral računamo
    a ... spodnja meja integrala
    b ... zgornja meja integrala
    n ... stopnja kvadrature
"""
def gauss_quadrature(f, a, b, n):
    # Določimo vozlišča in uteži za Gaussovo kvadraturo
    nodes, weights = gauss_legendre_points_and_weights(n)

    # Izračunamo integral
    integral = 0
    for i in range(n):
        # Sproti izvedemo transformacijo iz intervala [a, b] na interval [-1, 1]
        integral += f(((b - a) * nodes[i] + b + a) / 2) * (b - a) / 2 * weights[i]

    return integral