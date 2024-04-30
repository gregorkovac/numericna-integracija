import unittest

from normal import *

class TestNormalIntegral(unittest.TestCase):
    def test_std_normal(self):
        self.assertEqual(std_normal(0), 1 / np.sqrt(2 * np.pi))
        self.assertEqual(std_normal(1), 1 / np.sqrt(2 * np.pi) * np.exp(-1 / 2))
        self.assertEqual(std_normal(-1), 1 / np.sqrt(2 * np.pi) * np.exp(-1 / 2))
        self.assertEqual(std_normal(np.inf), 0)
        self.assertEqual(std_normal(-np.inf), 0)

    def test_std_normal_integral(self):
        self.assertAlmostEqual(std_normal_integral(0), 0.5, places=10)
        self.assertAlmostEqual(std_normal_integral(1), 0.8413447461, places=10)
        self.assertAlmostEqual(std_normal_integral(-1), 0.1586552539, places=10)
        self.assertAlmostEqual(std_normal_integral(2), 0.9772498681, places=10)
        self.assertAlmostEqual(std_normal_integral(-2), 0.0227501319, places=10)
        self.assertAlmostEqual(std_normal_integral(np.inf), 1, places=10)
        self.assertAlmostEqual(std_normal_integral(-np.inf), 0, places=10)

if __name__ == "__main__":
    unittest.main()