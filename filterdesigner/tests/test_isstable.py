import unittest
import filterdesigner.FilterSpec as FilterSpec
import filterdesigner.FIRDesign as FIRDesign
import filterdesigner.IIRDesign as IIRDesign

class TestIsstable(unittest.TestCase):

    def setUp(self):
        self.order = 80
        self.cut = 0.5

        self.n = 3
        self.fc = 0.4

    def test_isstable_1(self):
        # Test case for FIR filter
        fil = FIRDesign.fir1(self.order, self.cut)
        self.assertTrue(FilterSpec.isstable(fil) == True)

    def test_isstable_2(self):
        # Test case for IIR filter
        fil = IIRDesign.butter(self.n, self.fc)
        self.assertTrue(FilterSpec.isstable(fil) == False)
