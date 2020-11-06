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
        IIR = IIRDesign.ellip(self.n, self.Rp, self.Rs, self.Wp1)
        iir = signal.ellip(self.n, self.Rp, self.Rs, self.Wp1, btype='lowpass', fs=2)
        self.assertTrue((IIR[0] == iir[0]).all() and (IIR[1] == iir[1]).all())
        
    def test_ellip_2(self):
        # Test case for lowpass filter without default
        IIR = IIRDesign.ellip(self.n, self.Rp, self.Rs, self.Wp1, ftype = 'low')
        iir = signal.ellip(self.n, self.Rp, self.Rs, self.Wp1, btype='lowpass', fs=2)
        self.assertTrue((IIR[0] == iir[0]).all() and (IIR[1] == iir[1]).all())
        
    def test_ellip_3(self):
        # Test case for highpass filter
        IIR = IIRDesign.ellip(self.n, self.Rp, self.Rs, self.Wp1, ftype = 'high')
        iir = signal.ellip(self.n, self.Rp, self.Rs, self.Wp1, btype='highpass', fs=2)
        self.assertTrue((IIR[0] == iir[0]).all() and (IIR[1] == iir[1]).all())
       　
    def test_ellip_4(self):
        # Test case for bandpass filter with default
        IIR = IIRDesign.ellip(self.n, self.Rp, self.Rs, self.Wp2)
        iir = ignal.ellip(self.n, self.Rp, self.Rs, self.Wp2, btype='bandpass', fs=2)
        self.assertTrue((IIR[0] == iir[0]).all() and (IIR[1] == iir[1]).all())
        
    def test_ellip_5(self):
        # Test case for bandpass filter without default
        IIR = IIRDesign.ellip(self.n, self.Rp, self.Rs, self.Wp2, ftype = 'bandpass')
        iir = signal.ellip(self.n, self.Rp, self.Rs, self.Wp2, btype='bandpass', fs=2)
        self.assertTrue((IIR[0] == iir[0]).all() and (IIR[1] == iir[1]).all())
        
    def test_ellip_6(self):
        # Test case for bandstop filter
        IIR = IIRDesign.ellip(self.n, self.Rp, self.Rs, self.Wp2, ftype = 'stop')
        iir = signal.ellip(self.n, self.Rp, self.Rs, self.Wp2, btype='bandstop', fs=2)
        self.assertTrue((IIR[0] == iir[0]).all() and (IIR[1] == iir[1]).all())
        
    def test_ellip_7(self):
        # Test case for analog filter
        IIR = IIRDesign.ellip(self.n, self.Rp, self.Rs, self.Wps, zs='s')
        iir = signal.ellip(self.n, self.Rp, self.Rs, self.Wps, btype='lowpass', analog=True)
        self.assertTrue((IIR[0] == iir[0]).all() and (IIR[1] == iir[1]).all())
        
