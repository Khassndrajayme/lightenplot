"""
Unit Tests for Composition
This file verifies that the PlotEase Facade class is composed of 
and correctly delegates tasks to its specialized component classes.
"""
import unittest
import pandas as pd
import numpy as np
from plotease import (
    PlotEase, 
    VisualizationBase,
    DiagnosticPlotter, 
    SummaryGenerator,
    ModelComparator,
    QuickPlotter
)


class TestComposition(unittest.TestCase):
    """Test composition - PlotEase contains other classes"""
    
    def setUp(self):
        """Set up test data - using mtcars"""
        self.mtcars = load_mtcars()
    
    def test_plotease_contains_diagnostic_plotter(self):
        """Test that PlotEase contains DiagnosticPlotter"""
        pe = PlotEase(self.mtcars)
        self.assertIsInstance(pe._diagnostic, DiagnosticPlotter)
    
    def test_plotease_contains_summary_generator(self):
        """Test that PlotEase contains SummaryGenerator"""
        pe = PlotEase(self.mtcars)
        self.assertIsInstance(pe._summary, SummaryGenerator)
    
    def test_plotease_contains_quick_plotter(self):
        """Test that PlotEase contains QuickPlotter"""
        pe = PlotEase(self.mtcars)
        self.assertIsInstance(pe._plotter, QuickPlotter)
    
    def test_delegation_to_components(self):
        """Test that PlotEase delegates to its components"""
        pe = PlotEase(self.mtcars)
        
        # Test delegation to SummaryGenerator
        summary = pe.tabular_summary(style='numeric')
        self.assertIsInstance(summary, pd.DataFrame)
        self.assertEqual(len(summary), 11)  # All mtcars columns

if __name__ == '__main__':
    # Run with verbose output
    print("="*80)
    print("PLOTEASE UNIT TESTS - Using mtcars Dataset")
    print("="*80)
    unittest.main(verbosity=2)
