import unittest
import filterdesigner.FIRDesign as FIRDesign
import filterdesigner.FilterSpec as FilterSpec
import scipy.signal as signal

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
        Z, P, K = FilterSpec.zplane(fil, show=False)

        self.assertTrue(np.all(Z == z) and np.all(P == p) and (K == k))
        
