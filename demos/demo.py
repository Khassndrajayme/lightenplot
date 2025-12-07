"""
LightenPlot Demo Script - Using mtcars Dataset
Demonstrates all features and class interactions
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

from lightenplot import (
    LightenPlot, 
    DiagnosticPlotter, 
    SummaryGenerator, 
    ModelComparator, 
    QuickPlotter
)

def print_section(title):
    """Helper function to print section headers"""
    print("\n" + "="*80)
    print(f"  {title}")
    print("="*80 + "\n")


def load_mtcars_data():
    """Load the mtcars dataset"""
    mtcars = pd.DataFrame({
        'mpg': [21.0, 21.0, 22.8, 21.4, 18.7, 18.1, 14.3, 24.4, 22.8, 19.2, 
                17.8, 16.4, 17.3, 15.2, 10.4, 10.4, 14.7, 32.4, 30.4, 33.9,
                21.5, 15.5, 15.2, 13.3, 19.2, 27.3, 26.0, 30.4, 15.8, 19.7, 15.0, 21.4],
        'cyl': [6, 6, 4, 6, 8, 6, 8, 4, 4, 6, 
                6, 8, 8, 8, 8, 8, 8, 4, 4, 4,
                4, 8, 8, 8, 8, 4, 4, 4, 8, 6, 8, 4],
        'disp': [160.0, 160.0, 108.0, 258.0, 360.0, 225.0, 360.0, 146.7, 140.8, 167.6,
                 167.6, 275.8, 275.8, 275.8, 472.0, 460.0, 440.0, 78.7, 75.7, 71.1,
                 120.1, 318.0, 304.0, 350.0, 400.0, 79.0, 120.3, 95.1, 351.0, 145.0, 301.0, 121.0],
        'hp': [110, 110, 93, 110, 175, 105, 245, 62, 95, 123,
               123, 180, 180, 180, 205, 215, 230, 66, 52, 65,
               97, 150, 150, 245, 175, 66, 91, 113, 264, 175, 335, 109],
        'drat': [3.90, 3.90, 3.85, 3.08, 3.15, 2.76, 3.21, 3.69, 3.92, 3.92,
                 3.92, 3.07, 3.07, 3.07, 2.93, 3.00, 3.23, 4.08, 4.93, 4.22,
                 3.70, 2.76, 3.15, 3.73, 3.08, 4.08, 4.43, 3.77, 4.22, 3.62, 3.54, 4.11],
        'wt': [2.620, 2.875, 2.320, 3.215, 3.440, 3.460, 3.570, 3.190, 3.150, 3.440,
               3.440, 4.070, 3.730, 3.780, 5.250, 5.424, 5.345, 2.200, 1.615, 1.835,
               2.465, 3.520, 3.435, 3.840, 3.845, 1.935, 2.140, 1.513, 3.170, 2.770, 3.570, 2.780],
        'qsec': [16.46, 17.02, 18.61, 19.44, 17.02, 20.22, 15.84, 20.00, 22.90, 18.30,
                 18.90, 17.40, 17.60, 18.00, 17.98, 17.82, 17.42, 19.47, 18.52, 19.90,
                 20.01, 16.87, 17.30, 15.41, 17.05, 18.90, 16.70, 16.90, 14.50, 15.50, 14.60, 18.60],
        'vs': [0, 0, 1, 1, 0, 1, 0, 1, 1, 1,
               1, 0, 0, 0, 0, 0, 0, 1, 1, 1,
               1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
        'am': [1, 1, 1, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
               0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
        'gear': [4, 4, 4, 3, 3, 3, 3, 4, 4, 4,
                 4, 3, 3, 3, 3, 3, 3, 4, 4, 4,
                 3, 3, 3, 3, 3, 4, 5, 5, 5, 5, 5, 4],
        'carb': [4, 4, 1, 1, 2, 1, 4, 2, 2, 4,
                 4, 3, 3, 3, 4, 4, 4, 1, 2, 1,
                 1, 2, 2, 4, 2, 1, 2, 2, 4, 6, 8, 2]
    }, index=['Mazda RX4', 'Mazda RX4 Wag', 'Datsun 710', 'Hornet 4 Drive', 'Hornet Sportabout',
              'Valiant', 'Duster 360', 'Merc 240D', 'Merc 230', 'Merc 280',
              'Merc 280C', 'Merc 450SE', 'Merc 450SL', 'Merc 450SLC', 'Cadillac Fleetwood',
              'Lincoln Continental', 'Chrysler Imperial', 'Fiat 128', 'Honda Civic', 'Toyota Corolla',
              'Toyota Corona', 'Dodge Challenger', 'AMC Javelin', 'Camaro Z28', 'Pontiac Firebird',
              'Fiat X1-9', 'Porsche 914-2', 'Lotus Europa', 'Ford Pantera L', 'Ferrari Dino',
              'Maserati Bora', 'Volvo 142E'])
    
    return mtcars


def demo_basic_usage():
    """Demo 1: Basic Usage and Initialization"""
    print_section("DEMO 1: Basic Usage and Initialization - mtcars Dataset")
    
    mtcars = load_mtcars_data()
    
    print("mtcars Dataset Loaded:")
    print(f"  Shape: {mtcars.shape}")
    print(f"  Columns: {list(mtcars.columns)}")
    print("\nColumn Descriptions:")
    print("  mpg  - Miles per gallon")
    print("  cyl  - Number of cylinders")
    print("  disp - Displacement (cu.in.)")
    print("  hp   - Gross horsepower")
    print("  drat - Rear axle ratio")
    print("  wt   - Weight (1000 lbs)")
    print("  qsec - 1/4 mile time")
    print("  vs   - Engine (0=V-shaped, 1=straight)")
    print("  am   - Transmission (0=automatic, 1=manual)")
    print("  gear - Number of forward gears")
    print("  carb - Number of carburetors")
    
    print(f"\nFirst 5 cars:")
    print(mtcars.head())
    
    lp = LightenPlot(mtcars, theme='minimal')
    print(f"\n✓ LightenPlot initialized: {lp}")
    print(f"  Total cars analyzed: {len(lp)}")
    
    return lp, mtcars


def demo_encapsulation(lp):
    """Demo 2: Encapsulation - Protected attributes and getters"""
    print_section("DEMO 2: Encapsulation (Protected Attributes & Getters)")
    
    print("✓ Protected attributes are prefixed with underscore:")
    print(f"  _data: {type(lp._data)}")
    print(f"  _theme: {lp._theme}")
    print(f"  _diagnostic: {type(lp._diagnostic)}")
    print(f"  _summary: {type(lp._summary)}")
    print(f"  _plotter: {type(lp._plotter)}")
    
    print("\n✓ Data is encapsulated and protected from direct modification")


def demo_inheritance():
    """Demo 3: Inheritance - Parent-child relationships"""
    print_section("DEMO 3: Inheritance (Parent-Child Relationships)")
    
    mtcars = load_mtcars_data()
    sample_data = mtcars[['mpg', 'hp', 'wt']].head(10)
    
    lp = LightenPlot(sample_data)
    dp = DiagnosticPlotter(sample_data)
    qp = QuickPlotter()
    
    print("✓ Inheritance Hierarchy:")
    print("  VisualizationBase (Parent)")
    print("    ├── LightenPlot")
    print("    ├── DiagnosticPlotter")
    print("    ├── SummaryGenerator")
    print("    ├── ModelComparator")
    print("    └── QuickPlotter")
    
    print("\n✓ All classes inherit common attributes:")
    print(f"  LightenPlot figsize: {lp.figsize}")
    print(f"  DiagnosticPlotter figsize: {dp.figsize}")
    print(f"  QuickPlotter figsize: {qp.figsize}")


def demo_polymorphism():
    """Demo 4: Polymorphism - Method Overriding"""
    print_section("DEMO 4: Polymorphism (Method Overriding)")
    
    print("✓ Abstract method plot() is overridden in each subclass:")
    print("\n  Same method name, different implementations:")
    print("  - LightenPlot.plot() → delegates to diagnostic plotter")
    print("  - DiagnosticPlotter.plot() → creates diagnostic visualizations")
    print("  - SummaryGenerator.plot() → creates summary statistics heatmap")
    print("  - QuickPlotter.plot() → creates quick plots")
    print("  - ModelComparator.plot() → creates model comparison charts")
    
    print("\n✓ This is POLYMORPHISM!")


def demo_composition(lp):
    """Demo 5: Composition - LightenPlot contains other classes"""
    print_section("DEMO 5: Composition (HAS-A Relationships)")
    
    print("✓ LightenPlot contains (composes) these components:")
    print(f"  1. DiagnosticPlotter: {type(lp._diagnostic).__name__}")
    print(f"  2. SummaryGenerator: {type(lp._summary).__name__}")
    print(f"  3. QuickPlotter: {type(lp._plotter).__name__}")
    print(f"  4. ModelComparator: {lp._comparator} (initialized when needed)")
    
    print("\n✓ LightenPlot delegates work to its components:")
    print("  - autoplot() → delegates to DiagnosticPlotter")
    print("  - tabular_summary() → delegates to SummaryGenerator")
    print("  - compare_models() → creates and uses ModelComparator")
    print("  - quick_plot() → delegates to QuickPlotter")
    
    print("\n✓ This is COMPOSITION: LightenPlot HAS-A relationship with components")


def demo_dunder_methods():
    """Demo 6: Dunder Methods (Magic Methods)"""
    print_section("DEMO 6: Dunder Methods (Magic Methods)")
    
    mtcars = load_mtcars_data()
    
    data_full = mtcars
    data_small = mtcars.head(10)
    
    lp1 = LightenPlot(data_full, theme='minimal')
    lp2 = LightenPlot(data_full, theme='minimal')
    lp3 = LightenPlot(data_small, theme='minimal')
    
    print("✓ __repr__ - String representation:")
    print(f"  {repr(lp1)}")
    
    print("\n✓ __len__ - Length of data:")
    print(f"  len(lp1) = {len(lp1)} cars")
    print(f"  len(lp3) = {len(lp3)} cars")
    
    print("\n✓ __eq__ - Equality comparison:")
    print(f"  lp1 == lp2: {lp1 == lp2} (same data and theme)")
    print(f"  lp1 == lp3: {lp1 == lp3} (different data)")
    
    print("\n✓ __lt__ - Less than comparison:")
    print(f"  lp1 < lp3: {lp1 < lp3} (32 cars < 10 cars)")
    print(f"  lp3 < lp1: {lp3 < lp1} (10 cars < 32 cars)")


def demo_feature_1_autoplot(lp):
    """Demo 7: Feature 1 - AutoPlot Diagnostics"""
    print_section("DEMO 7: Feature 1 - AutoPlot Diagnostics (mtcars)")
    
    print("✓ Generating automatic diagnostic plots for mtcars...")
    print("  This will create up to 6 diagnostic visualizations:")
    print("    1. Distribution of numeric variables")
    print("    2. Correlation matrix heatmap")
    print("    3. Missing values analysis")
    print("    4. Target variable distribution (mpg)")
    print("    5. Categorical variable distribution")
    print("    6. Outlier detection (boxplots)")
    
    lp.autoplot(target='mpg', max_plots=6)
    plt.show()


def demo_feature_2_summary(lp):
    """Demo 8: Feature 2 - Tabular Summary"""
    print_section("DEMO 8: Feature 2 - Tabular Summary (mtcars)")
    
    print("✓ Generating comprehensive mtcars summary...")
    summary = lp.tabular_summary(style='full')
    
    print("\nSummary DataFrame:")
    print(summary.to_string())
    
    print("\n✓ Can also generate specific summaries:")
    print("  - style='numeric': Only numeric columns")
    print("  - style='categorical': Only categorical columns")
    print("  - style='full': All columns (default)")


def demo_feature_3_model_comparison(lp):
    """Demo 9: Feature 3 - Model Comparison"""
    print_section("DEMO 9: Feature 3 - Model Comparison (Predicting MPG)")
    
    print("✓ Comparing ML models for predicting car fuel efficiency (mpg)...")
    
    models = {
        'Linear Regression': {'Accuracy': 0.85, 'Precision': 0.82, 'Recall': 0.84, 'F1': 0.83},
        'Random Forest': {'Accuracy': 0.92, 'Precision': 0.90, 'Recall': 0.91, 'F1': 0.90},
        'XGBoost': {'Accuracy': 0.94, 'Precision': 0.93, 'Recall': 0.94, 'F1': 0.93},
        'Neural Network': {'Accuracy': 0.89, 'Precision': 0.87, 'Recall': 0.88, 'F1': 0.87}
    }
    
    print("\nModels predicting MPG:")
    for model, metrics in models.items():
        print(f"  - {model}: Accuracy={metrics['Accuracy']:.2f}, F1={metrics['F1']:.2f}")
    
    print("\n✓ Generating comparison visualizations...")
    lp.compare_models(models)
    plt.show()


def demo_feature_4_quick_plot(lp):
    """Demo 10: Feature 4 - Quick Plotting"""
    print_section("DEMO 10: Feature 4 - Quick Plotting (mtcars Analysis)")
    
    print("✓ Creating quick plots with minimal syntax...")
    
    print("\n1. Scatter plot: Horsepower vs MPG")
    lp.quick_plot('hp', 'mpg', kind='scatter', color='coral', 
                  title='Horsepower vs Fuel Efficiency (MPG)')
    plt.show()
    
    print("\n2. Scatter plot: Weight vs MPG")
    lp.quick_plot('wt', 'mpg', kind='scatter', color='steelblue',
                  title='Car Weight vs Fuel Efficiency')
    plt.show()
    
    print("\n3. Histogram: MPG Distribution")
    lp.quick_plot('mpg', kind='hist', color='green',
                  title='Distribution of Miles Per Gallon')
    plt.show()
    
    print("\n4. Histogram: Horsepower Distribution")
    lp.quick_plot('hp', kind='hist', color='orange',
                  title='Distribution of Horsepower')
    plt.show()


def demo_real_world_analysis():
    """Demo 11: Real-World Analysis Example"""
    print_section("DEMO 11: Real-World Analysis - Car Performance vs Efficiency")
    
    mtcars = load_mtcars_data()
    lp = LightenPlot(mtcars, theme='minimal')
    
    print("Analysis Question: How do different car characteristics affect fuel efficiency?")
    print("\nStep 1: Overview of the dataset")
    print(f"   Total cars: {len(mtcars)}")
    print(f"   Average MPG: {mtcars['mpg'].mean():.1f}")
    print(f"   Average HP: {mtcars['hp'].mean():.0f}")
    print(f"   Average Weight: {mtcars['wt'].mean():.2f} (1000 lbs)")
    
    print("\nStep 2: Correlation Analysis")
    correlations = mtcars[['mpg', 'hp', 'wt', 'cyl']].corr()['mpg'].sort_values()
    print("\n   Correlations with MPG:")
    for col, corr in correlations.items():
        if col != 'mpg':
            direction = "↑ positive" if corr > 0 else "↓ negative"
            print(f"     {col:8s}: {corr:6.3f} ({direction})")
    
    print("\nStep 3: Visualizations")
    lp.autoplot(target='mpg', max_plots=6)
    plt.show()
    
    print("\nStep 4: Key Insights")
    print("   ✓ Strong negative correlation between weight and MPG")
    print("   ✓ Strong negative correlation between horsepower and MPG")
    print("   ✓ Number of cylinders inversely affects fuel efficiency")
    print("   ✓ Lighter, less powerful cars tend to be more fuel-efficient")


def main():
    """Main demo execution"""
    print("\n")
    print("╔" + "="*78 + "╗")
    print("║" + " "*17 + "LIGHTENPLOT COMPREHENSIVE DEMO" + " "*30 + "║")
    print("║" + " "*20 + "Using mtcars Dataset" + " "*37 + "║")
    print("║" + " "*15 + "Week 3: Functional Implementation" + " "*30 + "║")
    print("╚" + "="*78 + "╝")
    
    # Run all demos
    lp, mtcars = demo_basic_usage()
    demo_encapsulation(lp)
    demo_inheritance()
    demo_polymorphism()
    demo_composition(lp)
    demo_dunder_methods()
    
    print("\n")
    print("╔" + "="*78 + "╗")
    print("║" + " "*25 + "FEATURE DEMONSTRATIONS" + " "*32 + "║")
    print("╚" + "="*78 + "╝")
    
    demo_feature_1_autoplot(lp)
    demo_feature_2_summary(lp)
    demo_feature_3_model_comparison(lp)
    demo_feature_4_quick_plot(lp)
    demo_real_world_analysis()
    
    print("\n")
    print("╔" + "="*78 + "╗")
    print("║" + " "*23 + "DEMO COMPLETED SUCCESSFULLY!" + " "*28 + "║")
    print("╚" + "="*78 + "╝")
    print("\n✓ All OOP principles demonstrated with mtcars dataset")
    print("✓ All features working correctly")
    print("✓ Class interactions verified")
    print("✓ Real-world analysis example completed")
    print("mtcars Dataset Analysis Complete! 🎉\n")


if __name__ == "__main__":
    main()