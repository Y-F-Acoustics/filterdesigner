import unittest
import filterdesigner.FIRDesign as FIRDesign
import filterdesigner.FilterSpec as FilterSpec

class TestZplane(unittest.TestCase):
    def setUp(self):
        self.order = 80
        self.cut = 0.5

    def test_zplane(self):
        # Test case
        fil = FIRDesign.fir1(self.order, self.cut)
        
        if np.max(b) > 1:
            kn = np.max(b)
            b /= float(kn)
        else:
            kn = 1
    
        if np.max(a) > 1:
            kd = np.max(a)
            a /= float(kd)
        else:
            kd = 1

        # Get the poles, zeros and gains
        p = np.round(np.roots(a), decimals=2)
        z = np.round(np.roots(b), decimals=2)
        k = kn / float(kd)

        self.assertTrue(FilterSpec.zplane(fil) == (z, p, k))

