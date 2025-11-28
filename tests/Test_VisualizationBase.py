"""
Unit Tests for VisualizationBase (Abstract Base Class)
This file verifies the ABC contract, data validation, and encapsulation logic
inherited by all subclasses.
Run with: pytest test_visualizationbase.py -v
"""

import unittest
import pandas as pd
from abc import ABC, abstractmethod
# Import the base class for testing
from plotease import VisualizationBase


#  Helper Mock Class for Testing Inherited Methods 
# Since VisualizationBase cannot be instantiated, we create a concrete subclass
# just to test its non-abstract methods (like validation, getters, and setters).
class MockVisualization(VisualizationBase):
    """Concrete mock class to instantiate VisualizationBase for testing."""
    def render(self):
        """Implement the abstract method to satisfy the ABC contract."""
        pass



class TestVisualizationBase(unittest.TestCase):
    """Test the Abstract Base Class contract and core validation logic."""
    
    def setUp(self):
        """Set up valid test data."""
        self.valid_data = pd.DataFrame({
            'a': [1, 2, 3, 4, 5],
            'b': [10, 20, 30, 40, 50]
        })
    
 
    # ABC Contract Enforcement
 

    def test_cannot_instantiate_abstract_class(self):
        """Test that the ABC itself cannot be instantiated (Polymorphism contract)."""
        with self.assertRaises(TypeError) as cm:
            # Attempting to instantiate an ABC should raise a TypeError
            VisualizationBase(self.valid_data)
        
        # Verify the error message relates to the abstract method 'render'
        self.assertIn("Can't instantiate abstract class", str(cm.exception))


    # Validation Tests (Executed via the base class __init__)


    def test_valid_initialization(self):
        """Test successful initialization using the Mock class."""
        mock_viz = MockVisualization(self.valid_data, theme='dark')
        self.assertIsInstance(mock_viz, VisualizationBase)
        self.assertEqual(mock_viz._theme, 'dark')

    def test_invalid_data_type(self):
        """Test TypeError when passing non-DataFrame data to the base initializer."""
        # The base class's _validate_data method should catch this
        with self.assertRaises(TypeError):
            MockVisualization([1, 2, 3])
        
        with self.assertRaises(TypeError):
            MockVisualization(None)
    
    def test_empty_dataframe(self):
        """Test ValueError when passing an empty DataFrame to the base initializer."""
        # The base class's _validate_data method should catch this
        with self.assertRaises(ValueError):
            MockVisualization(pd.DataFrame())


    # Encapsulation and Property Management Tests


    def test_get_data(self):
        """Test the get_data method (Encapsulation)."""
        mock_viz = MockVisualization(self.valid_data)
        retrieved_data = mock_viz.get_data()
        self.assertTrue(retrieved_data.equals(self.valid_data))
    
    def test_set_theme(self):
        """Test the set_theme method (Encapsulation)."""
        mock_viz = MockVisualization(self.valid_data, theme='default')
        self.assertEqual(mock_viz._theme, 'default')

        # Setting a new theme
        mock_viz.set_theme('minimal')
        self.assertEqual(mock_viz._theme, 'minimal')
        
        
if __name__ == '__main__':
    # Run with verbose output when executed directly
    unittest.main(verbosity=2)