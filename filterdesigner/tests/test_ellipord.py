import unittest
import filterdesigner.IIRDesign as IIRDesign
import scipy.signal as signal
import numpy as np

class TestEllipord(unittest.TestCase):

    def setUp(self):
        self.f1 = 0.2
        self.f2 = 0.3
        self.f3 = [0.2, 0.5]
        self.f4 = [0.1, 0.6]
        self.Rp = 1
        self.Rs = 1

    def test_ellipord_1(self):
        # Test case for lowpass filter
        ORD = IIRDesign.ellipord(self.f1, self.f2, self.Rp, self.Rs)
        ord = signal.ellipord(self.f1, self.f2, self.Rp, self.Rs, analog=False, fs=2)
        self.assertTrue((ORD[0] == ord[0]) and np.all(ORD[1] == ord[1]))

    def test_ellipord_2(self):
        # Test case for highpass filter
        ORD = IIRDesign.ellipord(self.f2, self.f1, self.Rp, self.Rs)
        ord = signal.ellipord(self.f2, self.f1, self.Rp, self.Rs, analog=False,fs=2)
        self.assertTrue((ORD[0] == ord[0]) and np.all(ORD[1] == ord[1]))
        
    def test_ellipord_3(self):
        # Test case for bandpass filter
        ORD = IIRDesign.ellipord(self.f3, self.f4, self.Rp, self.Rs)
        ord = signal.ellipord(self.f3, self.f4, self.Rp, self.Rs, analog=False, fs=2)
        self.assertTrue((ORD[0] == ord[0]) and np.all(ORD[1] == ord[1]))
        
    def test_ellipord_4(self):
        # Test case for bandstop filter
        ORD = IIRDesign.ellipord(self.f4, self.f3, self.Rp, self.Rs)
        ord = signal.ellipord(self.f4, self.f3, self.Rp, self.Rs, analog=False, fs=2)
        self.assertTrue((ORD[0] == ord[0]) and np.all(ORD[1] == ord[1]))
        
    def test_ellipord_5(self):
        # Test case for analog filter
        ORD = IIRDesign.ellipord(60, 75, self.Rp, self.Rs, zs='s')
        ord = signal.ellipord(60, 75, self.Rp, self.Rs, analog=True, fs=None)
        self.assertTrue((ORD[0] == ord[0]) and np.all(ORD[1] == ord[1]))
        
