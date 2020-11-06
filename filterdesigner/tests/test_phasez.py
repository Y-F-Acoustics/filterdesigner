import unittest
import filterdesigner.FilterSpec as FilterSpec
import filterdesigner.FIRDesign as FIRDesign
import scipy.signal as signal
import numpy as np
import scipy as sp

class TestPhasez(unittest.TestCase):

    def setUp(self):
        self.order = 80
        self.cut = 0.5

    def test_phasez_1(self):
        # Testcase for return radian form
        fil = FIRDesign.fir1(self.order, self.cut)
        w, h = signal.freqz(fil[0], fil[1], worN=512, fs=2*np.pi)
        phase = sp.unwrap(sp.angle(h))
        ww, pp = FilterSpec.phasez(fil)
        self.assertTrue(np.all(w == ww) and np.all(pp == phase))

    def test_phasez_2(self):
        # Testcase for return degree form
        fil = FIRDesign.fir1(self.order, self.cut)
        w, h = signal.freqz(fil[0], fil[1], worN=512, fs=2*np.pi)
        phase = sp.unwrap(sp.angle(h))
        phase=np.rad2deg(phase)
        ww, pp = FilterSpec.phasez(fil, deg=True)
        self.assertTrue(np.all(w == ww) and np.all(pp == phase))
        
