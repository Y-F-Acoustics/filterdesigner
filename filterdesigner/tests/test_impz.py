import unittest
import filterdesigner.FilterSpec as FilterSpec
import filterdesigner.FIRDesign as FIRDesign
import filterdesigner.IIRDesign as IIRDesign
import scipy.signal as signal
import numpy as np

class TestImpz(unittest.TestCase):

    def setUp(self):
        self.order = 80
        self.cut = 0.5
        self.fc = 300
        self.fs = 1000
        self.n = 1000

    def test_impz_1(self):
        # Test case for FIR filter without n
        fil = FIRDesign.fir1(self.order, self.cut)
        _, yout = FilterSpec.impz(fil)
        self.assertTrue(np.all(yout == fil[0]))

    def test_impz_2(self):
        # Test case for FIR filter with n
        fil = FIRDesign.fir1(self.order, self.cut)
        T = np.arange(0, self.n, 1)
        x = np.zeros(len(T))
        x[0] = 1
        yout = signal.lfilter(fil[0], fil[1], x)
        tt, y = FilterSpec.impz(fil, n=self.n)
        self.assertTrue(np.all(tt == T) and np.all(y == yout))

    def test_impz_3(self):
        # Test case for IIR filter without n
        fil = IIRDesign.butter(6, self.fc/(self.fs/2))
        dl = signal.dlti(fil[0], fil[1], dt=1/self.fs)
        i_d = signal.dimpulse(dl)
        T = i_d[0]
        yout = i_d[1][0]
        tt, y = FilterSpec.impz(fil, fs=self.fs)
        self.assertTrue(np.all(tt == T) and np.all(y == yout))
        
    def test_impz_4(self):
        # Test case for IIR filter with n
        fil = IIRDesign.butter(6, self.fc/(self.fs/2))
        dl = signal.dlti(fil[0], fil[1], dt=1/self.fs)
        i_d = signal.dimpulse(dl, n=self.n)
        T = i_d[0]
        yout = i_d[1][0]
        tt, y = FilterSpec.impz(fil, n=self.n, fs=self.fs)
        self.assertTrue(np.all(tt == T) and np.all(y == yout))
