import unittest
import filterdesigner.IIRDesign as IIRDesign
import scipy.signal as signal
import numpy as np

class TestButter(unittest.TestCase):

    def setUp(self):
        self.n = 3
        self.fc = 0.4

        self.n2 = 6
        self.fc2 = [0.25, 0.75]

        self.fcs = 75

    def test_butter_1(self):
        # Test case for lowpass filter with default
        IIR = IIRDesign.butter(self.n, self.fc)
        iir = signal.butter(self.n, self.fc, fs=2)
        self.assertTrue((IIR[0] == iir[0]).all and (IIR[1] == iir[1]).all)
    
    def test_butter_2(self):
        # Test case for lowpass filter without default
        IIR = IIRDesign.butter(self.n, self.fc, ftype='low')
        iir = signal.butter(self.n, self.fc, fs=2)
        self.assertTrue((IIR[0] == iir[0]).all and (IIR[1] == iir[1]).all)
        
    def test_butter_3(self):
        # Test case for highpass filter
        IIR = IIRDesign.butter(self.n, self.fc, ftype='high')
        iir = signal.butter(self.n, self.fc, btype='highpass', fs=2)
        self.assertTrue((IIR[0] == iir[0]).all and (IIR[1] == iir[1]).all)
       
    def test_butter_4(self):
        # Test case for bandpass filter with default
        IIR = IIRDesign.butter(self.n2, self.fc2)
        iir = signal.butter(self.n2, self.fc2, fs=2)
        self.assertTrue((IIR[0] == iir[0]).all and (IIR[1] == iir[1]).all)
        
    def test_butter_5(self):
        # Test case for bandpass filter without default
        IIR = IIRDesign.butter(self.n2, self.fc2, ftype='bandpass')
        iir = signal.butter(self.n2, self.fc2, fs=2)
        self.assertTrue((IIR[0] == iir[0]).all and (IIR[1] == iir[1]).all)

    def test_butter_6(self):
        # Test case for bandstop filter
        IIR = IIRDesign.butter(self.n2, self.fc2, ftype='stop')
        iir = signal.butter(self.n2, self.fc2, btype='bandstop', fs=2)
        self.assertTrue((IIR[0] == iir[0]).all and (IIR[1] == iir[1]).all)

    def test_butter_7(self):
        # Test case for analog filter
        IIR = IIRDesign.butter(self.n, self.fcs, zs='s')
        iir = signal.butter(self.n, self.fcs, analog=True)
        self.assertTrue((IIR[0] == iir[0]).all and (IIR[1] == iir[1]).all)
        
