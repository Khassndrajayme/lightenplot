"""
Unit Tests for SummaryGenerator Component
This file verifies the data profiling and tabular summary generation logic.
Run with: pytest test_summary_generator.py -v
"""

import unittest
import pandas as pd
# Import the class specific to this component's tests
from plotease import SummaryGenerator


class TestSummaryGenerator(unittest.TestCase):
    """Test SummaryGenerator functionality, focusing on data summarization."""
    
    def setUp(self):
        """Set up test data with both numeric and categorical columns."""
        self.data = pd.DataFrame({
            'age': [25, 30, 35, 40, 45],
            'salary': [50000, 60000, 70000, 80000, 90000],
            'department': ['Sales', 'HR', 'IT', 'Sales', 'HR'],
            'city': ['NYC', 'LA', 'NYC', 'SF', 'LA']
        })
    
    def test_initialization(self):
        """Test SummaryGenerator initialization."""
        sg = SummaryGenerator(self.data)
        self.assertIsNotNone(sg)
        
    def test_summarize_numeric(self):
        """Test the internal method for numeric column summarization."""
        sg = SummaryGenerator(self.data)
        numeric_summary = sg.summarize_numeric()
        
        self.assertIsInstance(numeric_summary, list)
        self.assertEqual(len(numeric_summary), 2) # Should find 'age' and 'salary'
        
        # Check that the necessary statistical keys are present
        first_summary = numeric_summary[0]
        self.assertIn('Column', first_summary)
        self.assertIn('Mean', first_summary)
        self.assertIn('Std', first_summary)
        
    def test_summarize_categorical(self):
        """Test the internal method for categorical column summarization."""
        sg = SummaryGenerator(self.data)
        cat_summary = sg.summarize_categorical()
        
        self.assertIsInstance(cat_summary, list)
        self.assertEqual(len(cat_summary), 2) # Should find 'department' and 'city'
        
        # Check that the necessary categorical keys are present
        first_summary = cat_summary[0]
        self.assertIn('Column', first_summary)
        self.assertIn('Unique', first_summary)
        self.assertIn('Top Value', first_summary)
        
    def test_tabular_summary_full(self):
        """Test the public method to return a full summary DataFrame (numeric + categorical)."""
        sg = SummaryGenerator(self.data)
        summary_df = sg.tabular_summary(style='full')
        
        self.assertIsInstance(summary_df, pd.DataFrame)
        self.assertEqual(len(summary_df), 4) # All 4 columns
        self.assertTrue('Mean' in summary_df.columns)
        self.assertTrue('Top Value' in summary_df.columns)

        
    def test_tabular_summary_numeric_only(self):
        """Test the public method to return a numeric-only summary DataFrame."""
        sg = SummaryGenerator(self.data)
        summary_df = sg.tabular_summary(style='numeric')
        
        self.assertIsInstance(summary_df, pd.DataFrame)
        self.assertEqual(len(summary_df), 2) # Only 2 numeric columns
        self.assertTrue('Mean' in summary_df.columns)
        self.assertTrue('Top Value' not in summary_df.columns) # Should not have cat columns

    def test_len_dunder(self):
        """Test __len__ method, inherited from the base class, to check row count."""
        sg = SummaryGenerator(self.data)
        self.assertEqual(len(sg), 5)


if __name__ == '__main__':
    # Run with verbose output when executed directly
    unittest.main(verbosity=2)