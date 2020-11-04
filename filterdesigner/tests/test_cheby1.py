import unittest
import filterdesigner.IIRDesign as IIRDesign
import scipy.signal as signal

class TestCheby1(unittest.TestCase):

    def setUp(self):
        self.n = 3
        self.Rp = 1
        self.Wp1 = 0.3
        self.Wp2 = [0.25, 0.75]
        self.Wps = np.pi/2

    def test_cheby1_1(self):
        # Test case for lowpass filter with default
        self.assertTrue(IIRDesign.cheby1(self.n, self.Rp, self.Wp1) == signal.cheby1(self.n, self.Rp, self.Wp1, fs=2))
    
    def test_cheby1_2(self):
        # Test case for lowpass filter without default
        self.assertTrue(IIRDesign.cheby1(self.n, self.Rp, self.Wp1, ftype='low') == signal.cheby1(self.n, self.Rp, self.Wp1, fs=2))

    def test_cheby1_3(self):
        # Test case for highpass filter
        self.assertTrue(IIRDesign.cheby1(self.n, self.Rp, self.Wp1, ftype='high') == signal.cheby1(self.n, self.Rp, self.Wp1, btype='highpass', fs=2))

    def test_cheby1_4(self):
        # Test case for bandpass filter with default
        self.assertTrue(IIRDesign.cheby1(self.n, self.Rp, self.Wp2) == signal.cheby1(self.n, self.Rp, self.Wp2, fs=2))

    def test_cheby1_5(self):
        # Test case for bandpass filter without default
        self.assertTrue(IIRDesign.cheby1(self.n, self.Rp, self.Wp2, ftype='bandpass') == signal.cheby1(self.n, self.Rp, self.Wp2, fs=2))

    def test_cheby1_6(self):
        # Test case for bandstop filter
        self.assertTrue(IIRDesign.cheby1(self.n, self.Rp, self.Wp2, ftype='stop') == signal.cheby1(self.n, self.Rp, self.Wp2, btype='bandstop', fs=2))

    def test_cheby1_7(self):
        # Test case for analog filter
        self.assertTrue(IIRDesign.cheby1(self.n, self.Rp, self.Wps, zs='s') == signal.cheby1(self.n, self.Rp, self.Wps, analog=True))