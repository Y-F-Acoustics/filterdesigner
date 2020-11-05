import unittest
import filterdesigner.IIRDesign as IIRDesign
import scipy.signal as signal

class TestIirpeak(unittest.TestCase):

    def setUp(self):
        self.w0 = 0.4
        self.bw = 0.4/35

    def test_iirpeak(self):
        # Test case
        self.assertTrue(IIRDesign.iirpeak(self.w0, self.bw) == signal.iirpeak(self.w0, self.w0/self.bw, fs=2))
