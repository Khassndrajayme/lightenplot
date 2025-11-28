"""
Unit Tests for QuickPlotter Component
This file verifies the functionality of the simple, single-plot visualization component.
Run with: pytest test_quickplotter.py -v
"""

import unittest
import pandas as pd
# Import the classes specific to this component's tests
from plotease import QuickPlotter, VisualizationBase


class TestQuickPlotter(unittest.TestCase):
    """Test QuickPlotter functionality, focusing on plot type detection and execution."""
    
    def setUp(self):
        """Set up test data with different types for plot detection."""
        self.data = pd.DataFrame({
            'age': [25, 30, 35, 40, 45], # Numeric
            'salary': [50000, 60000, 70000, 80000, 90000], # Numeric
            'department': ['Sales', 'HR', 'IT', 'Sales', 'HR'], # Categorical
            'is_manager': [True, False, True, False, True] # Boolean/Categorical
        })
    
    def test_initialization(self):
        """Test QuickPlotter initialization."""
        qp = QuickPlotter(self.data)
        self.assertIsNotNone(qp)
        self.assertIsInstance(qp, QuickPlotter)
    
    def test_inheritance_from_base(self):
        """Test that QuickPlotter inherits from VisualizationBase (Inheritance)."""
        qp = QuickPlotter(self.data)
        self.assertIsInstance(qp, VisualizationBase)


    # Plot Type Detection Logic

        
    def test_detect_plot_type_single_numeric(self):
        """Test detection for a single numeric column (should be 'hist')."""
        qp = QuickPlotter(self.data)
        plot_type = qp.detect_plot_type('age', None)
        self.assertEqual(plot_type, 'hist')
        
    def test_detect_plot_type_single_categorical(self):
        """Test detection for a single categorical column (should be 'bar')."""
        qp = QuickPlotter(self.data)
        plot_type = qp.detect_plot_type('department', None)
        self.assertEqual(plot_type, 'bar')

    def test_detect_plot_type_two_numeric(self):
        """Test detection for two numeric columns (should be 'scatter')."""
        qp = QuickPlotter(self.data)
        plot_type = qp.detect_plot_type('age', 'salary')
        self.assertEqual(plot_type, 'scatter')

    def test_detect_plot_type_numeric_vs_categorical(self):
        """Test detection for one numeric and one categorical column (should be 'box')."""
        qp = QuickPlotter(self.data)
        plot_type = qp.detect_plot_type('department', 'salary')
        self.assertEqual(plot_type, 'box')
        

    # Execution Test

        
    def test_quick_plot_runs_without_error(self):
        """
        Test that quick_plot executes various plots without raising exceptions.
        This verifies successful delegation and setup of plotting parameters.
        """
        qp = QuickPlotter(self.data)
        try:
            # Test scatter plot
            qp.quick_plot('age', 'salary', kind='scatter')
            # Test bar plot (categorical)
            qp.quick_plot('department', None)
            # Test explicit box plot
            qp.quick_plot('department', 'salary', kind='box')
            
            success = True
        except Exception as e:
            print(f"QuickPlotter's quick_plot method raised an exception: {e}")
            success = False
        
        self.assertTrue(success, "The quick_plot method failed during execution.")

    def test_set_style_runs_without_error(self):
        """Test that setting a custom style dictionary runs without crashing."""
        qp = QuickPlotter(self.data)
        try:
            qp.set_style({'axes.labelsize': 14, 'figure.figsize': (8, 6)})
            success = True
        except Exception:
            success = False
        self.assertTrue(success)


if __name__ == '__main__':
    # Run with verbose output when executed directly
    unittest.main(verbosity=2)