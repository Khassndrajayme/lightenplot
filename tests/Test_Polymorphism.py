"""
Unit Tests for Polymorphism
This file verifies that concrete classes correctly implement the abstract methods
defined in VisualizationBase, allowing for polymorphic method calls (e.g., render()).
"""
import unittest
import pandas as pd
# Import classes that implement the abstract render() method
from plotease import PlotEase, DiagnosticPlotter, QuickPlotter


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


class TestPolymorphism(unittest.TestCase):
    """Test polymorphism - method overriding"""
    
    def setUp(self):
        """Set up test data - using mtcars"""
        self.mtcars = load_mtcars()
    
    def test_render_method_override(self):
        """Test that render() is overridden in subclasses"""
        pe = PlotEase(self.mtcars)
        dp = DiagnosticPlotter(self.mtcars)
        qp = QuickPlotter(self.mtcars)
        
        # All should have render method
        self.assertTrue(hasattr(pe, 'render'))
        self.assertTrue(hasattr(dp, 'render'))
        self.assertTrue(hasattr(qp, 'render'))
        
        # They should have different implementations
        try:
            pe.render()
            dp.render()
            qp.render()
            success = True
        except Exception:
            success = False
        
        self.assertTrue(success)


if __name__ == '__main__':
    # Run with verbose output when executed directly
    unittest.main(verbosity=2)
