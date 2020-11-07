import unittest
import filterdesigner.IIRDesign as IIRDesign
import scipy.signal as signal
import numpy as np

class TestCheby1(unittest.TestCase):

    def setUp(self):
        self.n = 3
        self.Rp = 1
        self.Wp1 = 0.3
        self.Wp2 = [0.25, 0.75]
        self.Wps = np.pi/2

    def test_cheby1_1(self):
        # Test case for lowpass filter with default
        IIR = IIRDesign.cheby1(self.n, self.Rp, self.Wp1)
        iir = signal.cheby1(self.n, self.Rp, self.Wp1, fs=2)
        self.assertTrue((IIR[0] == iir[0]).all() and (IIR[1] == iir[1]).all())
    
    def test_cheby1_2(self):
        # Test case for lowpass filter without default
        IIR = IIRDesign.cheby1(self.n, self.Rp, self.Wp1, ftype='low')
        iir = signal.cheby1(self.n, self.Rp, self.Wp1, fs=2)
        self.assertTrue((IIR[0] == iir[0]).all() and (IIR[1] == iir[1]).all())
        
    def test_cheby1_3(self):
        # Test case for highpass filter
        IIR = IIRDesign.cheby1(self.n, self.Rp, self.Wp1, ftype='high')
        iir = signal.cheby1(self.n, self.Rp, self.Wp1, btype='highpass', fs=2)
        self.assertTrue((IIR[0] == iir[0]).all() and (IIR[1] == iir[1]).all())
       
    def test_cheby1_4(self):
        # Test case for bandpass filter with default
        IIR = IIRDesign.cheby1(self.n, self.Rp, self.Wp2)
        iir = signal.cheby1(self.n, self.Rp, self.Wp2, btype='bandpass', fs=2)
        self.assertTrue((IIR[0] == iir[0]).all() and (IIR[1] == iir[1]).all())

    def test_cheby1_5(self):
        # Test case for bandpass filter without default
        IIR = IIRDesign.cheby1(self.n, self.Rp, self.Wp2, ftype='bandpass')
        iir = signal.cheby1(self.n, self.Rp, self.Wp2, btype='bandpass', fs=2)
        self.assertTrue((IIR[0] == iir[0]).all() and (IIR[1] == iir[1]).all())
        
    def test_cheby1_6(self):
        # Test case for bandstop filter
        IIR = IIRDesign.cheby1(self.n, self.Rp, self.Wp2, ftype='stop')
        iir = signal.cheby1(self.n, self.Rp, self.Wp2, btype='bandstop', fs=2)
        self.assertTrue((IIR[0] == iir[0]).all() and (IIR[1] == iir[1]).all())
        
    def test_cheby1_7(self):
        # Test case for analog filter
        IIR = IIRDesign.cheby1(self.n, self.Rp, self.Wps, zs='s')
        iir = signal.cheby1(self.n, self.Rp, self.Wps, analog=True)
        self.assertTrue((IIR[0] == iir[0]).all() and (IIR[1] == iir[1]).all())
        
    def test_cheby1_8(self):
        # Test case for exception 1
        with self.assertRaises(ValueError):
            IIRDesign.cheby1(self.n, self.Rp, self.Wp2, ftype='x')

    def test_cheby1_9(self):
        # Test case for exception 2
        with self.assertRaises(ValueError):
            IIRDesign.cheby1(self.n, self.Rp, self.Wps, zs='x')

    def test_cheby1_10(self):
        # Test case for exception 3
        with self.assertRaises(ValueError):
            IIRDesign.cheby1(2.5, self.Rp, self.Wp2, ftype='bandpass')

    def test_cheby1_11(self):
        # Test case for exception 4
        with self.assertRaises(ValueError):
            IIRDesign.cheby1(self.n, self.Rp, self.Wps, ftype='low')

    def test_cheby1_12(self):
        # Test case for exception 5
        with self.assertRaises(ValueError):
            IIRDesign.cheby1(self.n, self.Rp, [2, 4], ftype='stop')

    def test_cheby1_13(self):
        # Test case for exception 6
        with self.assertRaises(ValueError):
            IIRDesign.cheby1(self.n, self.Rp, self.Wp2, ftype='low')

    def test_cheby1_14(self):
        # Test case for exception 7
        with self.assertRaises(ValueError):
            IIRDesign.cheby1(self.n, self.Rp, self.Wp2, ftype='high')

    def test_cheby1_15(self):
        # Test case for exception 8
        with self.assertRaises(ValueError):
            IIRDesign.cheby1(self.n, self.Rp, self.Wp1, ftype='stop')

    def test_cheby1_16(self):
        # Test case for exception 9
        with self.assertRaises(ValueError):
            IIRDesign.cheby1(self.n, self.Rp, self.Wp1, ftype='bandpass')
