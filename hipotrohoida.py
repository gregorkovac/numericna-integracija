import numpy as np
from gauss_quadrature import gauss_quadrature

"""
hx(t, a, b): vrne x koordinato parametrično podane hipotrohoide

Vhod:
    t (float) ... parameter, pri katerem računamo x koordinato
    a (float) ... prvi parameter, ki definira hipotrohoido
    b (float) ... drugi parameter, ki definira hipotrohoido

Izhod: (float) x koordinata hipotrohoide
"""
def hx(t, a = 1, b = -11/7):
    return (a + b) * np.cos(t) + b * np.cos((a + b) / b * t)

"""
hy(t, a, b): vrne y koordinato parametrično podane hipotrohoide

Vhod:
    t (float) ... parameter, pri katerem računamo y koordinato
    a (float) ... prvi parameter, ki definira hipotrohoido
    b (float) ... drugi parameter, ki definira hipotrohoido

Izhod: (float) y koordinata hipotrohoide
"""
def hy(t, a = 1, b = -11/7):
    return (a + b) * np.sin(t) + b * np.sin((a + b) / b * t)

"""
h(t, a, b): vrne točko na hipotrohoidi pri parametru t

Vhod:
    t (float) ... parameter, pri katerem računamo točko na hipotrohoidi
    a (float) ... prvi parameter, ki definira hipotrohoido
    b (float) ... drugi parameter, ki definira hipotrohoido

Izhod: (numpy.ndarray) točka na hipotrohoidi pri parametru t
"""
def h(t, a = 1, b = -11/7):
    return np.array([hx(t, a, b),
                     hy(t, a, b)])

"""
dhx(t, a, b): vrne odvod x koordinate hipotrohoide, definirane z a in b, pri parametru t

Vhod:
    t (float) ... parameter, pri katerem računamo odvod x koordinate
    a (float) ... prvi parameter, ki definira hipotrohoido
    b (float) ... drugi parameter, ki definira hipotrohoido

Izhod: (float) odvod x koordinate hipotrohoide
"""
def dhx(t, a = 1, b = -11/7):
    return (a + b) * (-np.sin(t)) - b * np.sin((a + b) / b * t) * (a + b) / b

"""
dhy(t, a, b): vrne odvod y koordinate hipotrohoide, definirane z a in b, pri parametru t

Vhod:
    t (float) ... parameter, pri katerem računamo odvod y koordinate
    a (float) ... prvi parameter, ki definira hipotrohoido
    b (float) ... drugi parameter, ki definira hipotrohoido
"""
def dhy(t, a = 1, b = -11/7):
    return (a + b) * (np.cos(t) + np.cos(((a + b) * t)/b))

"""
trikotnik_integrand(x, y, dx, dy, t): vrne vrednost integranda, ki se uporabi pri izračunu ploščine krivočrtnega trikotnika pod krivuljo

Vhod:
    x (function(t)) ... funkcija, ki parametrično določa x koordinato krivulje
    y (function(t)) ... funkcija, ki parametrično določa y koordinato krivulje
    dx (function(t)) ... odvod funkcije x
    dy (function(t)) ... odvod funkcije y
    t (float) ... parameter, pri katerem računamo vrednost integranda

Izhod: (float) vrednost integranda pri parametru t
"""
def trikotnik_integrand(x, y, dx, dy, t):
    return 0.5 * (x(t) * dy(t) - dx(t) * y(t))

"""
trikotnik(x, y, dx, dy, t1, t2, n): izračuna ploščino krivočrtnega trikotnika pod krivuljo z Gaussovimi kvadraturami
Vhod:
    x (function(t)) ... funkcija, ki parametrično določa x koordinato krivulje
    y (function(t)) ... funkcija, ki parametrično določa y koordinato krivulje
    dx (function(t)) ... odvod funkcije x
    dy (function(t)) ... odvod funkcije y
    t1 (float) ... spodnja meja integrala
    t2 (float) ... zgornja meja integrala
    n (int) ... stopnja Gauss-Legendrove kvadrature

Izhod: (float) ploščina krivočrtnega trikotnika pod krivuljo
"""
def trikotnik(x, y, dx, dy, t1, t2, n = 3):
    f = lambda t: trikotnik_integrand(x, y, dx, dy, t)
    integral = gauss_quadrature(f, t1, t2, n)

    return integral

"""
hipotrohoida(n, a, b): vrne ploščino območja, ki ga omejuje hipotrohoida, definirana z a in b.                    
                       Ploščino izračuna s pomočjo ploščine krivočrtnega trikotnika pod zunanjimi loki hipotrohoide.

Vhod:
    n (int) ... stopnja Gauss-Legendrove kvadrature
    a (float) ... prvi parameter hipotrohoide
    b (float) ... drugi parameter hipotrohoide

Izhod: (float) ploščina območja, ki ga omejuje hipotrohoida
"""
def hipotrohoida(n = 3, a = 1, b = -11/7):
    # Definiramo meje integrala, ki so meje enega od zunanjih lokov hipotrohoide
    t_1 = -11/(7 * 2)
    t_2 = 11/(7 * 2)

    # Zaradi preglednosti redefiniramo funkcije x, y, dx, dy
    x = lambda t: hx(t, a, b)
    y = lambda t: hy(t, a, b)
    dx = lambda t: dhx(t, a, b)
    dy = lambda t: dhy(t, a, b)

    # Ploščino izračunamo s pomočjo funkcije trikotnik in rezultat pomnožimo z 7 (število zunanjih lokov)
    return 7 * trikotnik(x, y, dx, dy, t_1, t_2, n = n)