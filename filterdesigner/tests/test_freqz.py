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
        self.assertTrue(FilterSpec.freqz(fil) == signal.freqz(fil[0], fil[1], worN=512, fs=2*np.py))
    
    def test_freqz_2(self):
        # Testcase for return dB form
        fil = FIRDesign.fir1(self.order, self.cut)
        w1, h1 = FilterSpec.freqz(fil, outform='dB')
        w2, h2 = signal.freqz(fil[0], fil[1], worN=512, fs=2*np.py)
        h2 = 20*np.log10(np.abs(h2))
        self.assertTrue((w1, h1) == (w2, h2))

    def test_freqz_3(self):
        # Testcase for return real form
        fil = FIRDesign.fir1(self.order, self.cut)
        w1, h1 = FilterSpec.freqz(fil, outform='abs')
        w2, h2 = signal.freqz(fil[0], fil[1], worN=512, fs=2*np.py)
        h2 = np.abs(h2)
        self.assertTrue((w1, h1) == (w2, h2))

    def test_freqz_4(self):
        # Testcase for IIR filter
        fil = IIRDesign.butter(6, self.fc/(self.fs/2))
        self.assertTrue(FilterSpec.freqz(fil) == signal.freqz(fil[0], fil[1], worN=512, fs=2*np.py))