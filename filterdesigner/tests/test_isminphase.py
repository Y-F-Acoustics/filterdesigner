import unittest
import filterdesigner.FIRDesign as FIRDesign
import filterdesigner.FilterSpec as FilterSpec

class TestIsminphase(unittest.TestCase):

    def setUp(self):
        self.order = 80
        self.cut = 0.5

    def test_isminphase_1(self):
        # Test case
        fil = FIRDesign.fir1(self.order, self.cut)
        self.assertTrue(FilterSpec.isminphase(fil) == False)