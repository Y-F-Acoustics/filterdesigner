import unittest
import filterdesigner.FIRDesign as FIRDesign
import filterdesigner.FilterSpec as FilterSpec
import filterdesigner.IIRDesign as IIRDesign

class TestIsminphase(unittest.TestCase):

    def setUp(self):
        self.order = 80
        self.cut = 0.5

        self.n = 3
        self.fc = 0.4

    def test_isminphase_1(self):
        # Test case
        fil = FIRDesign.fir1(self.order, self.cut)
        self.assertTrue(FilterSpec.isminphase(fil) == False)

    def test_isminphase_2(self):
        # Test case
        fil = IIRDesign.butter(self.n, self.fc)
        self.assertTrue(FilterSpec.isminphase(fil) == False)
