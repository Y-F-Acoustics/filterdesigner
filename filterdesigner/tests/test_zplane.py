import unittest
import filterdesigner.FIRDesign as FIRDesign
import filterdesigner.FilterSpec as FilterSpec

class TestZplane(unittest.TestCase):
    def setUp(self):
        self.order = 80
        self.cut = 0.5

    def test_zplane(self):
        # Test case
        fil = FIRDesign.fir1(self.order, self.cut)
        b = fil[0]
        a = fil[1]
        z, p, k = signal.tf2zpk(b, a)

        self.assertTrue(FilterSpec.zplane(fil, show=False) == (z, p, k))

