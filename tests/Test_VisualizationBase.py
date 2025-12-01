"""
Unit Tests for VisualizationBase (Abstract Base Class)
This file verifies the abstract nature, inheritance, and core non-abstract
methods of the VisualizationBase class.
"""
import unittest
import pandas as pd
from abc import ABC
# Import the class being tested and a concrete class for instantiation checks
from plotease import VisualizationBase, PlotEase, DiagnosticPlotter 

def load_mtcars():
    """Load mtcars dataset for testing"""
    # NOTE: This data is copied locally to ensure the test is self-contained.
    mtcars = pd.DataFrame({
        'mpg': [21.0, 21.0, 22.8, 21.4, 18.7, 18.1, 14.3, 24.4, 22.8, 19.2, 
                17.8, 16.4, 17.3, 15.2, 10.4, 10.4, 14.7, 32.4, 30.4, 33.9,
                21.5, 15.5, 15.2, 13.3, 19.2, 27.3, 26.0, 30.4, 15.8, 19.7, 15.0, 21.4],
        'cyl': [6, 6, 4, 6, 8, 6, 8, 4, 4, 6, 
                6, 8, 8, 8, 8, 8, 8, 4, 4, 4,
                4, 8, 8, 8, 8, 4, 4, 4, 8, 6, 8, 4],
        'hp': [110, 110, 93, 110, 175, 105, 245, 62, 95, 123,
               123, 180, 180, 180, 205, 215, 230, 66, 52, 65,
               97, 150, 150, 245, 175, 66, 91, 113, 264, 175, 335, 109],
        'wt': [2.620, 2.875, 2.320, 3.215, 3.440, 3.460, 3.570, 3.190, 3.150, 3.440,
               3.440, 4.070, 3.730, 3.780, 5.250, 5.424, 5.345, 2.200, 1.615, 1.835,
               2.465, 3.520, 3.435, 3.840, 3.845, 1.935, 2.140, 1.513, 3.170, 2.770, 3.570, 2.780]
    })
    return mtcars
    
class TestVisualizationBase(unittest.TestCase):
    """Test the abstract base class"""
    
    def test_cannot_instantiate_abstract_class(self):
        """Test that abstract class cannot be instantiated directly"""
        with self.assertRaises(TypeError):
            VisualizationBase(self.mtcars)
    
    def test_inheritance(self):
        """Test that subclasses inherit from base"""
        pe = PlotEase(self.mtcars)
        self.assertIsInstance(pe, VisualizationBase)
        
        dp = DiagnosticPlotter(self.mtcars)
        self.assertIsInstance(dp, VisualizationBase)


if __name__ == '__main__':
    # Run with verbose output when executed directly
    unittest.main(verbosity=2)
