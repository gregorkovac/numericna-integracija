# Numerična integracija

## 2. domača naloga pri predmetu Numerična matematika

Gregor Kovač

## Opis nalog

### 1. Porazdelitvena funkcija normalne slučajne spremenljivke

Cilj naloge je numerično izračunati vrednost integrala standardne normalne porazdelitve $X \sim N(0,1)$, ki je podan s formulo: \
$\Phi(x) = P(X \le x) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^x e^{-\frac{t^2}{2}}$.

### 2. Ploščina hipotrohoide

Cilj naloge je izračunati ploščino hipotrhoide, podane parametrično z: \
$x(t) = (a + b)\cos(t) + b\cos(\frac{a+b}{b}t)$ \
$y(t) = (a + b)\sin(t) + b\sin(\frac{a+b}{b}t)$, \
kjer sta $a = 1$ in $b = - \frac{11}{7}$.

Kot namig je podana formula za ploščino krivočrtnega trikotnika pod krivuljo:
$P = \frac{1}{2} \int_{t_1}^{t_2} (x(t)\dot{y}(t) - \dot{x}(t)y(t)) dt$.

## Struktura projekta

- [normal.py](./normal.py) - Python skripta s kodo za 1. nalogo
- [test_normal.py](test_normal.py) - Python skripta s testi za 1. nalogo
- [hipotrohoida.py](hipotrohoida.py) - Python skripta s kodo za 2. nalogo
- [test_hipotrohoida.py](test_hipotrohoida.py) - Python skripta s testi za 2. nalogo
- [report.pdf](report.pdf) - poročilo projekta
- [demo.ipynb](demo.ipynb) - Jupyter notebook skripta za dinamično generiranje poročila

## Potrebne Python knjižnice

- Numpy
- MatPlotLib
- Scipy

## Uporaba testov

Če želimo pognati teste za projekt, v ukazno vrstico napišemo `python test_normal.py` (za 1. nalogo) ali `python test_hipotrohoida.py` (za 2. nalogo). Lahko uporabimo tudi vgrajeno funkcijo za testiranje v našem razvojnem okolju.

## Generiranje poročila

Za (ponovno) generiranje odpremo datoteko `demo.ipynb`. To lahko storimo v svojem razvojnem okolju, ali pa v ukazni vrstici napišemo `jupyter notebook`. Nato v seznamu poiščemo pravo datoteko, jo odpremo, po želji spremenimo in poženemo vse celice, nato pa v orodni vrstici izberemo `File > Save and Export Notebook As > PDF`.
