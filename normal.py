import numpy as np

def std_normal(x):
    return 1 / np.sqrt(2 * np.pi) * np.exp(-x**2 / 2)

def std_normal_integral(x, n=1000):
    a = -10
    b = x

    h = (b - a) / n

    t_vals = np.linspace(a, b, n + 1)
        

    f_vals = std_normal(t_vals)

    integral = h * (np.sum(f_vals) - 0.5 * (f_vals[0] + f_vals[-1]))

    return integral
