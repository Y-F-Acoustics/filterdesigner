import unittest
import filterdesigner.IIRDesign as IIRDesign
import numpy as np

class TestPolyscale(unittest.TestCase):
    def setUp(self):
        self.a = [1, -2, -3]
        self.alpha = 0.5

    def test_polyscale(self):
        # Test case
        self.assertTrue(IIRDesign.polyscale(self.a, self.alpha) == (self.alpha * np.roots(self.a)))
        