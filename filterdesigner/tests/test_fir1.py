import unittest
import filterdesigner.FIRDesign as FIRDesign
import scipy.signal as signal
import numpy as np

class TestFIR1(unittest.TestCase):
    def setUp(self):
        self.n = 2
        self.f1 = 0.1
        self.f2 = 0.2
        self.f3 = 0.3
        self.f4 = 0.4

    def test_fir1_1(self):
        # Test for lowpass filter with hamming window.
        FIR = FIRDesign.fir1(self.n, self.f1)
        fir = signal.firwin(self.n, self.f1, window='hamming', pass_zero=True, scale=True)
        self.assertTrue(np.all(FIR[0] == fir[0]))

    def test_fir1_2(self):
        # Test for highpass filter with hamming window.
        FIR = FIRDesign.fir1(self.n, self.f1, ftype='high')
        fir = signal.firwin(self.n, self.f1, window='hamming', pass_zero=False, scale=True)
        self.assertTrue(np.all(FIR[0] == fir[0]))

    def test_fir1_3(self):
        # Test for bandpass filter with hamming window.
        FIR = FIRDesign.fir1(self.n, [self.f1, self.f2])
        self.assertTrue(np.all(FIR[0] == np.array([ 0.06301614,  0.88770441,  0.06301614])))

    def test_fir1_4(self):
        # Test for bandstop filter with hamming window.
        FIR = FIRDesign.fir1(self.n, [self.f1, self.f2], ftype='stop')
        self.assertTrue(np.all(FIR[0] == np.array([-0.00801395,  1.0160279 , -0.00801395])))

    def test_fir1_5(self):
        # Test for DC-0 filter with hamming window.
        FIR = FIRDesign.fir1(self.n, [self.f1, self.f2, self.f3, self.f4])
        self.assertTrue(np.all(FIR[0] == np.array([ 0.04890915,  0.91284326,  0.04890915])))

    def test_fir1_6(self):
        # Test for DC-1 filter with hamming window.
        FIR = FIRDesign.fir1(self.n, [self.f1, self.f2, self.f3, self.f4], ftype='DC-1')
        self.assertTrue(np.all(FIR[0] == np.array([-0.01376344,  1.02752689, -0.01376344])))
