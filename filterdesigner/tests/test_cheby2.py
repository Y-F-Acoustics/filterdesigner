import unittest
import filterdesigner.IIRDesign as IIRDesign
import scipy.signal as signal
import numpy as np

class TestCheby2(unittest.TestCase):

    def setUp(self):
        self.n = 3
        self.Rs = 1
        self.Ws1 = 0.3
        self.Ws2 = [0.25, 0.75]
        self.Wss = np.pi/2

    def test_cheby2_1(self):
        # Test case for lowpass filter with default
        IIR = IIRDesign.cheby2(self.n, self.Rs, self.Ws1)
        iir = signal.cheby2(self.n, self.Rs, self.Ws1, fs=2)
        self.assertTrue((IIR[0] == iir[0]).all() and (IIR[1] == iir[1]).all)
    
    def test_cheby2_2(self):
        # Test case for lowpass filter without default
        IIR = IIRDesign.cheby2(self.n, self.Rs, self.Ws1, ftype='low')
        iir = signal.cheby2(self.n, self.Rs, self.Ws1, fs=2)
        self.assertTrue((IIR[0] == iir[0]).all() and (IIR[1] == iir[1]).all)
        
    def test_cheby2_3(self):
        # Test case for highpass filter
        IIR = IIRDesign.cheby2(self.n, self.Rs, self.Ws1, ftype='high')
        iir = signal.cheby2(self.n, self.Rs, self.Ws1, btype='highpass', fs=2)
        self.assertTrue((IIR[0] == iir[0]).all() and (IIR[1] == iir[1]).all)
       
    def test_cheby2_4(self):
        # Test case for bandpass filter with default
        IIR = IIRDesign.cheby2(self.n, self.Rs, self.Ws2)
        iir = signal.cheby2(self.n, self.Rs, self.Ws2, btype='bandpass', fs=2)
        self.assertTrue((IIR[0] == iir[0]).all() and (IIR[1] == iir[1]).all)
        
    def test_cheby2_5(self):
        # Test case for bandpass filter without default
        IIR = IIRDesign.cheby2(self.n, self.Rs, self.Ws2, ftype='bandpass')
        iir = signal.cheby2(self.n, self.Rs, self.Ws2, btype='bandpass', fs=2)
        self.assertTrue((IIR[0] == iir[0]).all() and (IIR[1] == iir[1]).all)
        
    def test_cheby2_6(self):
        # Test case for bandstop filter
        IIR = IIRDesign.cheby2(self.n, self.Rs, self.Ws2, ftype='stop')
        iir = signal.cheby2(self.n, self.Rs, self.Ws2, btype='bandstop', fs=2)
        self.assertTrue((IIR[0] == iir[0]).all() and (IIR[1] == iir[1]).all)
        
    def test_cheby2_7(self):
        # Test case for analog filter
        IIR = IIRDesign.cheby2(self.n, self.Rs, self.Wss, zs='s')
        iir = signal.cheby2(self.n, self.Rs, self.Wss, analog=True)
        self.assertTrue((IIR[0] == iir[0]).all() and (IIR[1] == iir[1]).all)
    
