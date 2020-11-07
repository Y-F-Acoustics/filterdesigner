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
        IIR = IIRDesign.ellip(self.n, self.Rp, self.Rs, self.Wp1, ftype='low')
        iir = signal.ellip(self.n, self.Rp, self.Rs, self.Wp1, btype='lowpass', fs=2)
        self.assertTrue((IIR[0] == iir[0]).all() and (IIR[1] == iir[1]).all())
        
    def test_ellip_3(self):
        # Test case for highpass filter
        IIR = IIRDesign.ellip(self.n, self.Rp, self.Rs, self.Wp1, ftype='high')
        iir = signal.ellip(self.n, self.Rp, self.Rs, self.Wp1, btype='highpass', fs=2)
        self.assertTrue((IIR[0] == iir[0]).all() and (IIR[1] == iir[1]).all())
        
    def test_ellip_4(self):
        # Test case for bandpass filter with default
        IIR = IIRDesign.ellip(self.n, self.Rp, self.Rs, self.Wp2)
        iir = signal.ellip(self.n, self.Rp, self.Rs, self.Wp2, btype='bandpass', fs=2)
        self.assertTrue((IIR[0] == iir[0]).all() and (IIR[1] == iir[1]).all())
        
    def test_ellip_5(self):
        # Test case for bandpass filter without default
        IIR = IIRDesign.ellip(self.n, self.Rp, self.Rs, self.Wp2, ftype='bandpass')
        iir = signal.ellip(self.n, self.Rp, self.Rs, self.Wp2, btype='bandpass', fs=2)
        self.assertTrue((IIR[0] == iir[0]).all() and (IIR[1] == iir[1]).all())
        
    def test_ellip_6(self):
        # Test case for bandstop filter
        IIR = IIRDesign.ellip(self.n, self.Rp, self.Rs, self.Wp2, ftype='stop')
        iir = signal.ellip(self.n, self.Rp, self.Rs, self.Wp2, btype='bandstop', fs=2)
        self.assertTrue((IIR[0] == iir[0]).all() and (IIR[1] == iir[1]).all())
        
    def test_ellip_7(self):
        # Test case for analog filter
        IIR = IIRDesign.ellip(self.n, self.Rp, self.Rs, self.Wps, zs='s')
        iir = signal.ellip(self.n, self.Rp, self.Rs, self.Wps, btype='lowpass', analog=True)
        self.assertTrue((IIR[0] == iir[0]).all() and (IIR[1] == iir[1]).all())

    def test_ellip_8(self):
        # test case for Exception 1
        with self.assertRaises(ValueError):
            IIRDesign.ellip(self.n, self.Rp, self.Rs, self.Wps, zs='x')

    def test_ellip_9(self):
        # test case for Exception 2
        with self.assertRaises(ValueError):
            IIRDesign.ellip(2.5, self.Rp, self.Rs, self.Wp1)

    def test_ellip_10(self):
        # test case for Exception 3
        with self.assertRaises(ValueError):
            IIRDesign.ellip(self.n, self.Rp, self.Rs, self.Wp1, ftype='x')

    def test_ellip_11(self):
        # test case for Exception 4
        with self.assertRaises(ValueError):
            IIRDesign.ellip(self.n, self.Rp, self.Rs, 1.4, zs='z')

    def test_ellip_12(self):
        # test case for Exception 5
        with self.assertRaises(ValueError):
            IIRDesign.ellip(self.n, self.Rp, self.Rs, [0.5, 1.5], zs='z')

    def test_ellip_13(self):
        # test case for Exception 6
        with self.assertRaises(ValueError):
            IIRDesign.ellip(self.n, self.Rp, self.Rs, self.Wp2, ftype='low')

    def test_ellip_14(self):
        # test case for Exception 7
        with self.assertRaises(ValueError):
            IIRDesign.ellip(self.n, self.Rp, self.Rs, self.Wp2, ftype='high')

    def test_ellip_15(self):
        # test case for Exception 8
        with self.assertRaises(ValueError):
            IIRDesign.ellip(self.n, self.Rp, self.Rs, self.Wp1, ftype='stop')

    def test_ellip_16(self):
        # test case for Exception 9
        with self.assertRaises(ValueError):
            IIRDesign.ellip(self.n, self.Rp, self.Rs, self.Wp1, ftype='bandpass')