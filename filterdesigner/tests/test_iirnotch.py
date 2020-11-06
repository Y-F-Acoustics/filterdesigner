import unittest
import filterdesigner.IIRDesign as IIRDesign
import scipy.signal as signal
import numpy as np

class TestIirnotch(unittest.TestCase):

    def setUp(self):
        self.w0 = 0.4
        self.bw = 0.4/35

    def test_iirnotch(self):
        # Test case
        IIR = IIRDesign.iirnotch(self.w0, self.bw)
        iir = signal.iirnotch(self.w0, self.w0/self.bw, fs=2)
        self.assertTrue(np.all(IIR[0] == iir[0]) and np.all(IIR[1] == iir[1]))
