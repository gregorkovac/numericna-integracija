import numpy as np
import matplotlib.pyplot as plt

def hx(t, a = 1, b = -11/7):
    return (a + b) * np.cos(t) + b * np.cos((a + b) / b * t)

def hy(t, a = 1, b = -11/7):
    return (a + b) * np.sin(t) + b * np.sin((a + b) / b * t)

def h(t, a = 1, b = -11/7):
    return np.array([hx(t, a, b),
                     hy(t, a, b)])

def dhx(t, a = 1, b = -11/7):
    return -(a + b) * (np.sin(t) + np.sin(t) * (((a + b) * t)/b))

def dhy(t, a = 1, b = -11/7):
    return (a + b) * (np.cos(t) + np.cos(((a + b) * t)/b))

def trikotnik(x, y, dx, dy, t1, t2, n = 1000):
    h = (t2 - t1) / n

    t_vals = np.linspace(t1, t2, n + 1)
    f_vals = x(t_vals) * dy(t_vals) - dx(t_vals) * y(t_vals)

    integral = h * (np.sum(f_vals) - 0.5 * (f_vals[0] + f_vals[-1]))

    return 1/2 * integral

def hipotrohoida(a, b, period):
    t_vals = np.linspace(0, period, 10)

    P = 0

    x = lambda t: hx(t, a, b)
    y = lambda t: hy(t, a, b)
    dx = lambda t: dhx(t, a, b)
    dy = lambda t: dhy(t, a, b)

    t_prev = 0
    for t in t_vals:
        P += trikotnik(x, y, dx, dy, t_prev, t)
        # print( trikotnik(x, y, dx, dy, t_prev, t))
        # break
        t_prev = t

    return P