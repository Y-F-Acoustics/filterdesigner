import unittest
import filterdesigner.IIRDesign as IIRDesign
import scipy.signal as signal

class TestCheb2ord(unittest.TestCase):
    def setUp(self):
        self.f1 = 0.2
        self.f2 = 0.3
        self.f3 = [0.2, 0.5]
        self.f4 = [0.1, 0.6]
        self.Rp = 1
        self.Rs = 100

    def test_cheb2ord_1(self):
        # Test case for lowpass filter
        self.assertTrue(IIRDesign.cheb2ord(self.f1, self.f2, self.Rp, self.Rs) == signal.cheb2ord(self.f1, self.f2, self.Rp, self.Rs, analog=False, fs=2))

    def test_cheb2ord_2(self):
        # Test case for highpass filter
        self.assertTrue(IIRDesign.cheb2ord(self.f2, self.f1, self.Rp, self.Rs) == signal.cheb2ord(self.f2, self.f1, self.Rp, self.Rs, analog=False, fs=2))

    def test_cheb2ord_3(self):
        # Test case for bandpass filter
        ORD = IIRDesign.cheb2ord(self.f3, self.f4, self.Rp, self.Rs)
        ord = signal.cheb2ord(self.f3, self.f4, self.Rp, self.Rs, analog=False, fs=2)
        self.assertTrue((ORD[0] == ord[0]) and (ORD[1] == ord[1]).all())

    def test_cheb2ord_4(self):
        # Test case for bandstop filter
        ORD = IIRDesign.cheb2ord(self.f4, self.f3, self.Rp, self.Rs)
        ord = signal.cheb2ord(self.f4, self.f3, self.Rp, self.Rs, analog=False, fs=2)
        self.assertTrue((ORD[0] == ord[0]) and (ORD[1] == ord[1]).all())
       
    def test_cheb2ord_5(self):
        # Test case for analog filter
        self.assertTrue(IIRDesign.cheb2ord(60, 75, self.Rp, self.Rs, zs='s') == signal.cheb2ord(60, 75, self.Rp, self.Rs, analog=True, fs=None))
