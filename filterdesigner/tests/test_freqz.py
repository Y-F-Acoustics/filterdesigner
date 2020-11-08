import unittest
import filterdesigner.FilterSpec as FilterSpec
import filterdesigner.FIRDesign as FIRDesign
import filterdesigner.IIRDesign as IIRDesign
import scipy.signal as signal
import numpy as np

class TestFreqz(unittest.TestCase):
    def setUp(self):
        self.order = 80
        self.cut = 0.5
        self.fc = 300
        self.fs = 1000

    def test_freqz_1(self):
        # Testcase for return complex form
        fil = FIRDesign.fir1(self.order, self.cut)
        w1, h1 = FilterSpec.freqz(fil)
        w2, h2 = signal.freqz(fil[0], fil[1], worN=512, fs=2*np.pi)
        self.assertTrue(np.all(w1 == w2) and np.all(h1 == h2))
    
    def test_freqz_2(self):
        # Testcase for return dB form
        fil = FIRDesign.fir1(self.order, self.cut)
        w1, h1 = FilterSpec.freqz(fil, outform='dB')
        w2, h2 = signal.freqz(fil[0], fil[1], worN=512, fs=2*np.pi)
        h2 = 20*np.log10(np.abs(h2))
        self.assertTrue(np.all(w1 == w2) and np.all(h1 == h2))

    def test_freqz_3(self):
        # Testcase for return real form
        fil = FIRDesign.fir1(self.order, self.cut)
        w1, h1 = FilterSpec.freqz(fil, outform='abs')
        w2, h2 = signal.freqz(fil[0], fil[1], worN=512, fs=2*np.pi)
        h2 = np.abs(h2)
        self.assertTrue(np.all(w1 == w2) and np.all(h1 == h2))

    def test_freqz_4(self):
        # Testcase for IIR filter
        fil = IIRDesign.butter(6, self.fc/(self.fs/2))
        w1, h1 = FilterSpec.freqz(fil)
        w2, h2 = signal.freqz(fil[0], fil[1], worN=512, fs=2*np.pi)
        self.assertTrue(np.all(w1 == w2) and np.all(h1 == h2))

    def test_freqz_5(self):
        # Test case for exception
        with self.assertRaises(ValueError):
            FilterSpec.freqz(fil, outform='x')

        
