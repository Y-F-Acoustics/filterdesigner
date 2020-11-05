import unittest
import numpy as np
import scipy.signal as signal
import filterDesigner.FIRDesign as FIRDesign

class TestSgolay(unittest.TestCase):
    def setUp(self):
        self.order = 4
        self.framelen = 21

    def test_sgolay(self):
        # Test case for sgolay
        self.assertTrue(FIRDesign.sgolay(self.order, self.framelen) == (signal.savgol_coeffs(self.framelen, self.order), 1))

    
