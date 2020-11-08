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

    def test_cheb2ord_6(self):
        # Test case for exception 1
        with self.assertRaises(ValueError):
            IIRDesign.cheb2ord(60, 75, self.Rp, self.Rs, zs='x')

    def test_cheb2ord_7(self):
        # test case for exception 2
        with self.assertRaises(ValueError):
            IIRDesign.cheb2ord(60, 0.2, self.Rp, self.Rs, zs='s')

    def test_cheb2ord_8(self):
        # Test case for exception 3
        with self.assertRaises(ValueError):
            IIRDesign.cheb2ord([1, 2], self.f4, self.Rp, self.Rs)

    def test_cheb2ord_9(self):
        # Test case for exception 4
        with self.assertRaises(ValueError):
            IIRDesign.cheb2ord([0.2, 0.5, 0.7], self.f4, self.Rp, self.Rs)

    def test_cheb2ord_10(self):
        # Test case for exception 5
        with self.assertRaises(ValueError):
            IIRDesign.cheb2ord(60, 75, 'x', self.Rs, zs='s')

    def test_cheb2ord_11(self):
        # test case for exception 6
        with self.assertRaises(ValueError):
            IIRDesign.cheb2ord(60, 75, self.Rp, 'x', zs='s')