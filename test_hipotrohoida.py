import unittest

from hipotrohoida import *
import numpy as np

class TestHipotrohoida(unittest.TestCase):
    def test_x(self):
        # Tu preverimo nekaj izracunanih vrednosti x koordinate hipotrohoide
        self.assertAlmostEqual(hx(0), -15/7, places=10)
        self.assertAlmostEqual(hx(np.pi), -0.0813664490, places=10)
        self.assertAlmostEqual(hx(2*np.pi), 0.4576382962, places=10)

    def test_y(self):
        # Tu preverimo nekaj izracunanih vrednosti y koordinate hipotrohoide
        self.assertAlmostEqual(hy(0), 0, places=10)
        self.assertAlmostEqual(hy(np.pi), -1.4294217070, places=10)
        self.assertAlmostEqual(hy(2*np.pi), -1.1876064740, places=10)

    def test_odvod_x(self):
        # Tu preverimo, da je numerični odvod x koordinate hipotrohoide enak analitičnemu
        eps = 1e-6

        for t in [0, 1, np.pi, 2*np.pi]:
            dhx_t = dhx(t)
            dhx_t_approx = (hx(t + eps) - hx(t - eps)) / (2 * eps)
            self.assertAlmostEqual(dhx_t, dhx_t_approx, places=6)

    def test_odvod_y(self):
        # Tu preverimo, da je numerični odvod y koordinate hipotrohoide enak analitičnemu
        eps = 1e-6
        
        for t in [0, 1, np.pi, 2*np.pi]:
            dhy_t = dhy(t)
            dhy_t_approx = (hy(t + eps) - hy(t - eps)) / (2 * eps)
            self.assertAlmostEqual(dhy_t, dhy_t_approx, places=6)

    def test_trikotnik(self):
        # Tu prevermi, da lahko ploscino kroga korektno izracunamo s ploscino trikotnikov, ki jih krog omejuje
        x = lambda t: np.cos(t)
        y = lambda t: np.sin(t)
        dx = lambda t: -np.sin(t)
        dy = lambda t: np.cos(t)

        P = trikotnik(x, y, dx, dy, 0, 2 * np.pi, n = 5)

        self.assertAlmostEqual(P, np.pi, places=10)

    def test_omejenost_ploscine_s_kvadratom(self):
        # Tu preverimo omejenost ploscine hipotrohoide s kvadratom [-2, 2] x [-2, 2]
        P = hipotrohoida()
        self.assertGreaterEqual(4 * 4, P)

    def test_omejenost_ploscine_s_krogom(self):
        # Tu preverimo omejenost ploscine hipotrohoide s krogom z radijem, ki je enak normi najbolj oddaljene tocke na hipotrohoidi od izhodisca
        P = hipotrohoida()
        r = 2.1428571429
        self.assertGreaterEqual(np.pi * r ** 2, P)


        

if __name__ == "__main__":
    unittest.main()