import unittest
import filterdesigner.FIRDesign as FIRDesign
import numpy as np
import scipy.signal as signal

class TestFIRls(unittest.TestCase):
    def setUp(self):
        self.n = 100
        self.f = [0, 0.15, 0.85, 1]
        self.a = [1, 1, 0, 0]
        self.n2 = 101

    def test_firls_1(self):
        # Test for least square method
        FIR = FIRDesign.firls(self.n, self.f, self.a)
        fir = signal.firls(101, self.f, self.a)
        self.assertTrue(np.all(FIR[0] == fir))
        
    def test_firls_2(self):
        # Test for least square method with odd order
        FIR = FIRDesign.firls(self.n2, self.f, self.a)
        fir = signal.firls(103, self.f, self.a)
        self.assertTrue(FIR[0] == fir)
