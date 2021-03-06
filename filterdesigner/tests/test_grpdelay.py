import unittest
import filterdesigner.FilterSpec as FilterSpec
import filterdesigner.FIRDesign as FIRDesign
import filterdesigner.IIRDesign as IIRDesign
import numpy as np
import scipy.signal as signal

class TestGrpdelay(unittest.TestCase):

    def setUp(self):
        self.order = 80
        self.cut = 0.5
        self.fc = 300
        self.fs = 1000

    def test_grpdelay_1(self):
        # Test case for FIR filter
        fil = FIRDesign.fir1(self.order, self.cut)
        w, gd = signal.group_delay(fil, w=512, fs=2*np.pi)
        gd = np.round(gd)
        ww, gdgd = FilterSpec.grpdelay(fil)
        self.assertTrue(np.all(w == ww) and np.all(gd == gdgd))
    
    def test_grpdelay_2(self):
        # Test case for IIR filter
        fil = IIRDesign.butter(6, self.fc/(self.fs/2))
        w, gd = FilterSpec.grpdelay(fil)
        ww, gdgd = signal.group_delay(fil, w=512, fs=2*np.pi)
        self.assertTrue(np.all(w == ww) and np.all(gd == gdgd))
