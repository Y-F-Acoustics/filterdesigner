import unittest
import filterdesigner.IIRDesign as IIRDesign
import scipy.signal as signal

class TestIirnotch(unittest.TestCase):

    def setUp(self):
        self.w0 = 0.4
        self.bw = 0.4/35

    def test_iirnotch(self):
        # Test case
        self.assertTrue(IIRDesign.iirnotch(self.w0, self.bw) == signal.iirnotch(self.w0, self.w0/self.bw, fs=2))
