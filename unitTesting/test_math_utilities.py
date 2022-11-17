import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import math_utilities

class TestMathUtilities(unittest.TestCase):
    
    def test_linearInterpolation(self):
        self.assertEqual(math_utilities.linear_interpolation(0,-1,1,-1,1),0)
        self.assertEqual(math_utilities.linear_interpolation(50,0,100,100,200),150)
    
    
    
if __name__ == '__main__':
    unittest.main()    