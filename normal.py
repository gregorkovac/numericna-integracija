import numpy as np

"""
std_normal(x): vrne vrednost standardne normalne porazdelitve v točki x
"""
def std_normal(x):
    return 1 / np.sqrt(2 * np.pi) * np.exp(-x**2 / 2)

"""
std_normal_integral(x, n, lower_limit): vrne aproksimacijo integrala standardne normalne porazdelitve na intervalu [-neskončno, x] z uporabo trapeznega pravila

Vhod:
    x (float) ... zgornja meja integrala
    n (int) ... število podintervalov
    lower_limit (float) ... spodnja meja integrala, ki se uporabi namesto -neskončno

Izhod: (float) aproksimacija integrala
"""
def std_normal_integral(x, n=1000000, lower_limit=-10, upper_limit=10):
    # Nastavimo meje integrala. Pazimo, da nimamo -inf ali inf
    a = lower_limit
    b = max(min(x, upper_limit), lower_limit)

    # Izračunamo dolžino koraka
    h = (b - a) / n

    # Izračunamo vrednosti funkcije v točkah
    t_vals = np.linspace(a, b, n + 1)
    f_vals = std_normal(t_vals)

    # Izračunamo integral s trapeznim pravilom
    integral = h * (np.sum(f_vals) - 0.5 * (f_vals[0] + f_vals[-1]))

    return integral
