"""
Unit Tests for Polymorphism
This file verifies that subclasses correctly implement and override the
abstract methods (specifically render()) defined in VisualizationBase.
Run with: pytest test_polymorphism.py -v
"""

import unittest
import pandas as pd
import io
import sys
# Import the classes that demonstrate polymorphism
from plotease import PlotEase, DiagnosticPlotter, QuickPlotter, VisualizationBase


class TestPolymorphism(unittest.TestCase):
    """Test polymorphism - method overriding and abstract method implementation."""
    
    def setUp(self):
        """Set up test data."""
        self.data = pd.DataFrame({
            'age': [25, 30, 35, 40, 45],
            'salary': [50000, 60000, 70000, 80000, 90000]
        })
    
    def test_subclasses_implement_render(self):
        """
        Test that PlotEase, DiagnosticPlotter, and QuickPlotter all have a 'render' method,
        fulfilling the contract of the abstract base class.
        """
        pe = PlotEase(self.data)
        dp = DiagnosticPlotter(self.data)
        qp = QuickPlotter(self.data)
        
        # Check that the methods exist
        self.assertTrue(hasattr(pe, 'render'))
        self.assertTrue(hasattr(dp, 'render'))
        self.assertTrue(hasattr(qp, 'render'))

    def test_render_method_is_polymorphic(self):
        """
        Test that each subclass's render() method produces distinct output,
        demonstrating different behavior (polymorphism).
        We capture print output to verify content differences.
        """
        pe = PlotEase(self.data)
        dp = DiagnosticPlotter(self.data)
        qp = QuickPlotter(self.data)
        
        # Helper to capture print output
        def capture_render_output(obj):
            old_stdout = sys.stdout
            new_stdout = io.StringIO()
            sys.stdout = new_stdout
            try:
                obj.render()
            finally:
                sys.stdout = old_stdout
            return new_stdout.getvalue()

        pe_output = capture_render_output(pe)
        dp_output = capture_render_output(dp)
        qp_output = capture_render_output(qp)

        # 1. Check distinct messages (Behavioral Polymorphism)
        # PlotEase should contain 'Facade'
        self.assertIn("Facade", pe_output) 
        # DiagnosticPlotter and QuickPlotter should contain their own specific names (or functions)
        self.assertIn("Diagnostic Plotter", dp_output)
        self.assertIn("QuickPlotter", qp_output)
        
        # 2. Ensure all three outputs are different from each other
        self.assertNotEqual(pe_output, dp_output)
        self.assertNotEqual(pe_output, qp_output)
        self.assertNotEqual(dp_output, qp_output)


if __name__ == '__main__':
    # Run with verbose output when executed directly
    unittest.main(verbosity=2)