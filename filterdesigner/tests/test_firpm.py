import unittest
import numpy as np
import scipy.signal as signal
import scipy.interpolate as ip
import filterdesigner.FIRDesign as FIRDesign

class TestFIRpm(unittest.TestCase):
    def setUp(self):
        self.n1 = 17
        self.f1 = np.array([0, 0.3, 0.4, 0.6, 0.7, 1])
        self.a1 = [0, 0, 1, 1, 0, 0]
        self.n2 = 50
        self.fs = 1000
        self.f2 = np.array([0, 150, 200, 300, 350, 500])
        self.a2 = [0, 0, 1, 1, 0, 0]
        self.w = [3, 1, 100]

    def test_firpm_1(self):
        x = [i for i in range(len(self.f1))]
        ipf = ip.interp1d(x, self.f1)
        f1_new = ipf(np.linspace(x[0], x[-1], 2*len(x)))
        FIR = FIRDesign.firpm(self.n1, self.f1, self.a1)
        fir = signal.remez(self.n1+1, f1_new, self.a1, fs=2)
        self.assertTrue(np.all(FIR[0] == fir))

    def test_firpm_2(self):
        x = [i for i in range(len(self.f2))]
        ipf = ip.interp1d(x, self.f2)
        f2_new = ipf(np.linspace(x[0], x[-1], 2*len(x)))
        f2_2 = self.f2/(self.fs/2)
        f2_2[0] = 0
        f2_2[-1] = 1
        x_w = [i for i in range(len(w))]
        ipw = ip.interp1d(x_w, w)
        w_new = ipw(np.linspace(x_w[0], x_w[-1], 2*len(x_w)))
        FIR = FIRDesign.firpm(self.n2, f2_2, self.a2, self.w)
        fir = signal.remez(self.n2+1, f2_new, self.a2, w_new, fs=2)
        self.assertTrue(np.all(FIR[0] == fir))
