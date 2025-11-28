"""
Unit Tests for PlotEase Initialization and Data Validation
This file verifies correct object creation and input data handling.
Run with: pytest test_plotease_initialization.py -v
"""

import unittest
import pandas as pd
# Only PlotEase is needed for initialization tests
from plotease import PlotEase


class TestPlotEaseInitialization(unittest.TestCase):
    """Test PlotEase initialization, data validation, and basic getters/setters."""
    
    def setUp(self):
        """Set up valid test data."""
        self.valid_data = pd.DataFrame({
            'age': [25, 30, 35, 40, 45],
            'salary': [50000, 60000, 70000, 80000, 90000],
            'department': ['Sales', 'HR', 'IT', 'Sales', 'HR']
        })
    

    # Initialization and Validation Tests


    def test_valid_initialization(self):
        """Test successful initialization with valid data and a custom theme."""
        pe = PlotEase(self.valid_data, theme='minimal')
        self.assertIsNotNone(pe)
        # Check if the protected attribute is set correctly
        self.assertEqual(pe._theme, 'minimal')
    
    def test_invalid_data_type(self):
        """Test TypeError when passing non-DataFrame data."""
        # Test list
        with self.assertRaises(TypeError):
            PlotEase([1, 2, 3])
        # Test dictionary
        with self.assertRaises(TypeError):
            PlotEase({'a': [1, 2]})
        # Test None
        with self.assertRaises(TypeError):
            PlotEase(None)
    
    def test_empty_dataframe(self):
        """Test ValueError when passing an empty DataFrame, as required by _validate_data."""
        with self.assertRaises(ValueError):
            PlotEase(pd.DataFrame())


    # Encapsulation Tests (Theme & Data Management)


    def test_get_data(self):
        """Test data getter method (get_data) to verify Encapsulation."""
        pe = PlotEase(self.valid_data)
        retrieved_data = pe.get_data()
        self.assertTrue(retrieved_data.equals(self.valid_data))
    
    def test_set_theme(self):
        """Test theme setter method (set_theme) and attribute change."""
        pe = PlotEase(self.valid_data, theme='default')
        
        # Change the theme and check the internal attribute
        pe.set_theme('dark')
        self.assertEqual(pe._theme, 'dark')


if __name__ == '__main__':
    # Run with verbose output when executed directly
    unittest.main(verbosity=2)