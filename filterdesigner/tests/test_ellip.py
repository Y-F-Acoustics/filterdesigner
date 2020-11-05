import unittest
import filterdesigner.IIRDesign as IIRDesign
import scipy.signal as signal
import numpy as np

class TestEllip(unittest.TestCase):

    def setUp(self):
        self.n = 3
        self.Rp = 1
        self.Rs = 120
        self.Wp1 = 0.5
        self.Wp2 = [0.25, 0.75]
        self.Wps = np.pi/2

    def test_ellip_1(self):
        # Test case for lowpass filter with default
        self.assertTrue(IIRDesign.ellip(self.n, self.Rp, self.Rs, self.Wp1) == signal.ellip(self.n, self.Rp, self.Rs, self.Wp1, btype='lowpass', fs=2))

    def test_ellip_2(self):
        # Test case for lowpass filter without default
        self.assertTrue(IIRDesign.ellip(self.n, self.Rp, self.Rs, self.Wp1, ftype = 'low') == signal.ellip(self.n, self.Rp, self.Rs, self.Wp1, btype='lowpass', fs=2))

    def test_ellip_3(self):
        # Test case for highpass filter
        self.assertTrue(IIRDesign.ellip(self.n, self.Rp, self.Rs, self.Wp1, ftype = 'high') == signal.ellip(self.n, self.Rp, self.Rs, self.Wp1, btype='highpass', fs=2))

    def test_ellip_4(self):
        # Test case for bandpass filter with default
        self.assertTrue(IIRDesign.ellip(self.n, self.Rp, self.Rs, self.Wp2) == signal.ellip(self.n, self.Rp, self.Rs, self.Wp2, btype='bandpass', fs=2))

    def test_ellip_5(self):
        # Test case for bandpass filter without default
        self.assertTrue(IIRDesign.ellip(self.n, self.Rp, self.Rs, self.Wp2, ftype = 'bandpass') == signal.ellip(self.n, self.Rp, self.Rs, self.Wp2, btype='bandpass', fs=2))

    def test_ellip_6(self):
        # Test case for bandstop filter
        self.assertTrue(IIRDesign.ellip(self.n, self.Rp, self.Rs, self.Wp2, ftype = 'stop') == signal.ellip(self.n, self.Rp, self.Rs, self.Wp2, btype='bandstop', fs=2))

    def test_ellip_7(self):
        # Test case for analog filter
        self.assertTrue(IIRDesign.ellip(self.n, self.Rp, self.Rs, self.Wps, zs='s') == signal.ellip(self.n, self.Rp, self.Rs, self.Wps, btype='lowpass', analog=True))
