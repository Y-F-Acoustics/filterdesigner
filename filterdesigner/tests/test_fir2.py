import unittest
import filterdesigner.FIRDesign as FIRDesign
import scipy.signal as signal
import numpy as np

class TestFIR2(unittest.TestCase):
    def setUp(self):
        self.nhi = 33
        self.fhi = [0, 0.48, 0.48, 1]
        self.mhi = [0, 0, 1, 1]
        self.nlo = 30
        self.flo = [0, 0.6, 0.6, 1]
        self.mlo = [1, 1, 0, 0]
        self.nA = 50

    def test_fir2_1(self):
        # Highpass filter with bad filter order.
        FIR = FIRDesign.fir2(self.nhi, self.fhi, self.mhi)
        fir = signal.firwin2(35, self.fhi, self.mhi, nfreqs=1024, window='hamming')
        self.assertTrue(np.all(FIR[0] == fir))

    def test_fir2_2(self):
        # Lowpass filter
        FIR = FIRDesign.fir2(self.nlo, self.flo, self.mlo)
        fir = signal.firwin2(31, self.flo, self.mlo, nfreqs=1024, window='hamming')
        self.assertTrue(np.all(FIR[0] == fir))

    def test_fir2_3(self):
        # Arbitrary Magnitude filter
        F1 = np.arange(0, 0.181, 0.01)
        A1 = 0.5 + np.sin(2*np.pi*7.5*F1)/4
        F2 = [0.2, 0.38, 0.4, 0.55, 0.562, 0.585, 0.6, 0.78]
        A2 = [0.5, 2.3, 1, 1, -0.2, -0.2, 1, 1]
        F3 = np.arange(0.79, 1.01, 0.01)
        A3 = 0.2 + 18 * (1-F3) ** 2
        FA = np.hstack((F1, F2, F3))
        AA = np.hstack((A1, A2, A3))
        FIR = FIRDesign.fir2(self.nA, FA, AA)
        fir = signal.firwin2(51, FA, AA, nfreqs=1024, window='hamming')
        self.assertTrue(np.all(FIR[0] == fir))
        
