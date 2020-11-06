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
        
