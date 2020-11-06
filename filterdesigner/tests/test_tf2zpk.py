import unittest
import filterdesigner.Transform as Transform
import scipy.signal as signal
import numpy as np

class TestTf2zpk(unittest.TestCase):
    def setUp(self):
        self.firfil = (np.array([1.84796815e-18, 2.03712369e-01, 5.92575262e-01, 2.03712369e-01, 1.84796815e-18]), 1)
        self.iirfil = (np.array([0.09853116, 0.29559348, 0.29559348, 0.09853116]), np.array([ 1, -0.57724052,  0.42178705, -0.05629724]))

    def test_tf2zpk_1(self):
        # Test case for FIR
        Z, P, K = Transform.tf2zpk(self.firfil)
        z, p, k = signal.tf2zpk(self.firfil[0], self.firfil[1])
        self.assertTrue(np.all(Z == z) and np.all(P == p) and (K == k))

    def test_tf2zpk_2(self):
        # Test case for IIR
        Z, P, K = Transform.tf2zpk(self.iirfil)
        z, p, k = signal.tf2zpk(self.iirfil[0], self.iirfil[1])
        self.assertTrue(np.all(Z == z) and np.all(P == p) and (K == k))
