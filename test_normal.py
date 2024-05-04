import unittest

from normal import *
import numpy as np

class TestNormalIntegral(unittest.TestCase):
    def test_std_normal(self):
        # Tu preverimo nekaj izracunanih vrednosti standardne normalne porazdelitve
        self.assertEqual(std_normal(0), 1 / np.sqrt(2 * np.pi))
        self.assertEqual(std_normal(1), 1 / np.sqrt(2 * np.pi) * np.exp(-1 / 2))
        self.assertEqual(std_normal(-1), 1 / np.sqrt(2 * np.pi) * np.exp(-1 / 2))
        self.assertEqual(std_normal(np.inf), 0)
        self.assertEqual(std_normal(-np.inf), 0)

    def test_std_normal_integral(self):
        # Tu preverimo nekaj izracunanih vrednosti integrala standardne normalne porazdelitve
        self.assertAlmostEqual(std_normal_integral(0), 0.5, places=10)
        self.assertAlmostEqual(std_normal_integral(1), 0.8413447461, places=10)
        self.assertAlmostEqual(std_normal_integral(-1), 0.1586552539, places=10)
        self.assertAlmostEqual(std_normal_integral(2), 0.9772498681, places=10)
        self.assertAlmostEqual(std_normal_integral(-2), 0.0227501319, places=10)
        self.assertAlmostEqual(std_normal_integral(np.inf), 1, places=10)
        self.assertAlmostEqual(std_normal_integral(-np.inf), 0, places=10)

    def test_std_normal_integral_vsota_1(self):
        # Iz teorije verjetnosti vemo, da je integral standardne normalne porazdelitve na intervalu [-inf, inf] enak 1. To preverimo tu.
        n1 = std_normal_integral(1)
        n2 = std_normal_integral(-1)
        self.assertAlmostEqual(n1 + n2, 1, places=10)

        n1 = std_normal_integral(2)
        n2 = std_normal_integral(-2)
        self.assertAlmostEqual(n1 + n2, 1, places=10)

        n1 = std_normal_integral(0)
        self.assertAlmostEqual(n1 + n1, 1, places=10)

        np.random.seed(0)
        randnum = np.random.rand()
        n1 = std_normal_integral(randnum)
        n2 = std_normal_integral(-randnum)
        self.assertAlmostEqual(n1 + n2, 1, places=10)


if __name__ == "__main__":
    unittest.main()