import unittest
import filterdesigner.IIRDesign as IIRDesign
import scipy.signal as signal
import numpy as np

class TestButtord(unittest.TestCase):

    def setUp(self):
        self.f1 = 0.2
        self.f2 = 0.3
        self.f3 = [0.2, 0.5]
        self.f4 = [0.1, 0.6]
        self.Rp = 1
        self.Rs = 1

    def test_buttord_1(self):
        # Test case for lowpass filter
        self.assertTrue(np.all(IIRDesign.buttord(self.f1, self.f2, self.Rp, self.Rs) == signal.buttord(self.f1, self.f2, self.Rp, self.Rs, analog=False, fs=2)))

    def test_buttord_2(self):
        # Test case for highpass filter
         self.assertTrue(np.all(IIRDesign.buttord(self.f2, self.f1, self.Rp, self.Rs) == signal.buttord(self.f2, self.f1, self.Rp, self.Rs, analog=False, fs=2)))

    def test_buttord_3(self):
        # Test case for bandpass filter
        ORD = IIRDesign.buttord(self.f3, self.f4, self.Rp, self.Rs)
        ord = signal.buttord(self.f3, self.f4, self.Rp, self.Rs, analog=False, fs=2)
        self.assertTrue((ORD[0] == ord[0]) and (ORD[1] == ord[1]).all())
        
    def test_buttord_4(self):
        # Test case for bandstop filter
        ORD = IIRDesign.buttord(self.f4, self.f3, self.Rp, self.Rs)
        ord = signal.buttord(self.f4, self.f3, self.Rp, self.Rs, analog=False, fs=2)
        self.assertTrue((ORD[0] == ord[0]) and (ORD[1] == ord[1]).all())
        
    def test_buttord_5(self):
        # Test case for analog filter
        self.assertTrue(np.all(IIRDesign.buttord(60, 75, self.Rp, self.Rs, zs='s') == signal.buttord(60, 75, self.Rp, self.Rs, analog=True, fs=None)))

    def test_buttord_6(self):
        # Test case for Exception
        with self.assertRaises(ValueError):
            IIRDesign.buttord(self.f1, self.f2, self.Rp, self.Rs, zs='x')
