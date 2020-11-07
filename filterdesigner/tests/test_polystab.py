import unittest
import filterdesigner.IIRDesign as IIRDesign
import numpy as np

class TestPolystab(unittest.TestCase):
    def setUp(self):
        self.a = 4
    
    def test_polystab(self):
        # test case
        x = self.a
        v = np.roots(x)
        vs = 0.5 * (np.sign(np.abs(v) - 1) + 1)
        v = (1 - vs) * v + vs / np.conj(v)
        b = a[0] * np.poly(v)
        self.assertTrue(IIRDesign.polystab(a) == b)