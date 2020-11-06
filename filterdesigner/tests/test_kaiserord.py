import unittest
import filterdesigner.FIRDesign as FIRDesign
import numpy as np

class TestKaiserord(unittest.TestCase):

    def setUp(self):
        self.f1 = 0.2
        self.f2 = 0.3
        self.f3 = 0.4
        self.f4 = 0.5
        self.f5 = 0.6
        self.f6 = 0.7
        self.m1 = 1
        self.m2 = 0
        self.dev1 = 0.05
        self.dev2 = 0.01

    def test_kaiserord_1(self):
        # Test case for lowapass filter
        self.assertTrue(np.all(FIRDesign.kaiserord([self.f1, self.f2], [self.m1, self.m2], self.dev2) == (45, 0.25, 3.3953210522614574, 'low')))

    def test_kaiserord_2(self):
        # Test case for highpass filter
        self.assertTrue(np.all(FIRDesign.kaiserord([self.f1, self.f2], [self.m2, self.m1], self.dev1) == (26, 0.25, 1.509869637041394, 'high')))

    def test_kaiserord_3(self):
        # Test case for bandpass filter
        ORD = FIRDesign.kaiserord([self.f1, self.f2, self.f3, self.f4], [self.m2, self.m1, self.m2], self.dev2)
        self.assertTrue((ORD[0] == 45) and np.all(ORD[1] == [0.25, 0.45]) and (ORD[2] == 3.3953210522614574) and (ORD[3] == 'bandpass'))
        
    def test_kaiserord_4(self):
        # Test case for bandstop filter
        ORD = FIRDesign.kaiserord([self.f1, self.f2, self.f3, self.f4], [self.m1, self.m2, self.m1], self.dev2)
        self.assertTrue((ORD[0] == 46) and np.all(ORD[1] == [0.25, 0.45]) and (ORD[2] == 3.3953210522614574) and (ORD[3] == 'stop'))
        
    def test_kaiserord_5(self):
        # Test case for 'DC-1' filter
        ORD = FIRDesign.kaiserord([self.f1, self.f2, self.f3, self.f4, self.f5, self.f6], [self.m1, self.m2, self.m1, self.m2], self.dev2)
        self.assertTrue((ORD[0] == 45) and np.all(ORD[1] == [0.25, 0.45, 0.6499999999999999]) and (ORD[2] == 3.3953210522614574) and (ORD[3] == 'DC-1'))
        
    def test_kaiserord_6(self):
        # Test case for 'DC-0' filter
        ORD = FIRDesign.kaiserord([self.f1, self.f2, self.f3, self.f4, self.f5, self.f6], [self.m2, self.m1, self.m2, self.m1], self.dev2)
        self.assertTrue((ORD[0] == 46) and np.all(ORD[1] == [0.25, 0.45, 0.6499999999999999]) and (ORD[2] == 3.3953210522614574) and (ORD[3] == 'DC-0'))
        
