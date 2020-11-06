import unittest
import numpy as np
import scipy.signal as signal
import filterdesigner.FIRDesign as FIRDesign

class TestSgolay(unittest.TestCase):
    def setUp(self):
        self.order = 4
        self.framelen = 21

    def test_sgolay(self):
        # Test case for sgolay
        FIR = FIRDesign.sgolay(self.order, self.framelen)
        fir = signal.savgol_coeffs(self.framelen, self.order)
        self.assertTrue(np.all(FIR[0] == fir))
        
