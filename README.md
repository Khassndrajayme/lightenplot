# PlotEase

**Simplify data visualization with elegant, one-line commands.**

PlotEase is a Python library designed to dramatically reduce syntax complexity compared to matplotlib, seaborn, and ggplot. Built with Object-Oriented Programming principles, PlotEase makes data visualization accessible and intuitive while maintaining the power and flexibility you need.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![PlotEase UML Class Diagram](PlotEase_UMLDiagram/PlotEase_UMLDiagram.png)

---

## 📑 Table of Contents

- [Why PlotEase?](#why-plotease)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage Examples](#usage-examples)
- [Themes](#themes)
- [Testing](#testing)
- [Documentation](#documentation)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

---

## Why PlotEase?

Traditional plotting libraries require extensive code for simple visualizations. PlotEase changes that.

### Traditional Approach (matplotlib/seaborn)
```python
import matplotlib.pyplot as plt
import seaborn as sns

# 10+ lines for a simple scatter plot
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=df, x='age', y='salary', ax=ax, color='blue')
ax.set_title('Age vs Salary', fontsize=14)
ax.set_xlabel('Age', fontsize=12)
ax.set_ylabel('Salary', fontsize=12)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### PlotEase Approach
```python
from plotease import PlotEase
pe = PlotEase(data)

# Just 1 line!
pe.quick_plot('age', 'salary', color='blue', title='Age vs Salary')
```

**Result: 90% less code, same beautiful visualizations.**


## Features

### **AutoPlot Diagnostics**
Automatically generate comprehensive diagnostic plots based on your data types:
- Distribution plots for numeric variables
- Correlation heatmaps
- Missing value analysis
- Outlier detection with boxplots
- Target variable analysis

### **Tabular Summary**
Generate detailed statistical summaries with a single command:
- Comprehensive statistics for numeric columns
- Category analysis for categorical data
- Missing value reports
- Export to CSV/Excel

### **Model Comparison**
Visualize machine learning model performance:
- Grouped bar charts comparing metrics
- Radar charts showing model profiles
- Best model identification
- Side-by-side performance comparison

### **Quick Plotting**
Create beautiful plots with minimal syntax:
- Automatic plot type detection
- Scatter, line, bar, histogram, and box plots
- Custom styling and themes
- One-line plot generation

## Installation

### From PyPI
```bash
pip install plotease
```

### From Source
```bash
git clone https://github.com/Khassndrajayme/PlotEase.git
cd PlotEase
pip install -e .
```

### Verify Installation
```bash
python -c "from plotease import PlotEase; print('PlotEase installed successfully!')"
```

### Requirements
- Python 3.8+
- pandas >= 1.3.0
- numpy >= 1.21.0
- matplotlib >= 3.4.0
- seaborn >= 0.11.0
- scipy >= 1.7.0


## Quick Start

### Basic Usage

```python
import pandas as pd
from plotease import PlotEase

# Load your data
data = pd.read_csv('your_data.csv')

# Initialize PlotEase
pe = PlotEase(data, theme='minimal')

# That's it! You're ready to visualize
```

## Usage Examples

### 1. AutoPlot Diagnostics

Generate comprehensive diagnostic plots automatically:

```python
# Analyze your entire dataset with one command
pe.autoplot()

# Focus on specific target variable
pe.autoplot(target='sales')
```

This automatically creates:
- Distribution plots for all numeric variables
- Correlation heatmap
- Missing value visualization
- Outlier detection plots

### 2. Tabular Summary

```python
# Full summary (numeric + categorical)
summary = pe.tabular_summary(style='full')

# Only numeric columns
numeric_summary = pe.tabular_summary(style='numeric')

# Only categorical columns
cat_summary = pe.tabular_summary(style='categorical')

# Export to file
pe.tabular_summary(style='full', export_to='summary.csv')
```

**Output includes:**
- Count, Missing values, Mean, Std, Min, Max
- Unique values, Top category, Frequency
- Memory usage statistics

### 3. Model Comparison

```python
models_results = {
    'Linear Regression': {
        'Accuracy': 0.85, 
        'Precision': 0.82, 
        'Recall': 0.84,
        'F1-Score': 0.83
    },
    'Random Forest': {
        'Accuracy': 0.92, 
        'Precision': 0.90, 
        'Recall': 0.91,
        'F1-Score': 0.90
    },
    'XGBoost': {
        'Accuracy': 0.94, 
        'Precision': 0.93, 
        'Recall': 0.94,
        'F1-Score': 0.93
    }
}

# Compare all metrics
pe.compare_models(models_results)

# Compare specific metrics only
pe.compare_models(models_results, metrics=['Accuracy', 'F1-Score'])
```

### 4. Quick Plotting

```python
# Automatic plot type detection
pe.quick_plot('age', 'salary')  # Auto-detects scatter plot

# Specific plot types
pe.quick_plot('age', 'salary', kind='scatter', color='blue')
pe.quick_plot('category', kind='bar', color='green')
pe.quick_plot('values', kind='hist', color='orange')
pe.quick_plot('var1', 'var2', kind='line', color='red')

# Custom styling
pe.quick_plot('x', 'y', kind='scatter', 
              color='coral', 
              title='My Custom Title',
              figsize=(12, 6))
```

### 5. Custom Styling

```python
# Apply custom style globally
custom_style = {
    'font_size': 14,
    'figure_facecolor': '#f9f9f9',
    'axes_facecolor': 'white',
    'grid_alpha': 0.3
}
pe.set_style(custom_style)

# All subsequent plots will use this style
pe.quick_plot('x', 'y')
```

## Themes

PlotEase comes with 4 built-in themes:

```python
# Available themes
pe = PlotEase(data, theme='default')    # Classic scientific
pe = PlotEase(data, theme='minimal')    # Clean and simple
pe = PlotEase(data, theme='dark')       # Dark mode
pe = PlotEase(data, theme='colorful')   # Vibrant colors

# Change theme after initialization
pe.set_theme('dark')
```


## Testing

Run the test suite:

```bash
# Run all tests
pytest tests/test_plotease.py -v

# Run specific test class
pytest tests/test_plotease.py::TestDunderMethods -v

# Run with coverage
pytest tests/test_plotease.py --cov=plotease --cov-report=html
```

Run the demo:

```bash
python demo.py
```

---

## Documentation

### Helper Functions

PlotEase includes utility functions in `plotease.utils`:

```python
from plotease.utils import (
    load_mtcars,                    # Load example dataset
    validate_dataframe,             # Validate data
    get_numeric_columns,            # Get numeric column names
    get_categorical_columns,        # Get categorical column names
    calculate_statistics,           # Comprehensive statistics
    find_highly_correlated_pairs,   # Correlation analysis
    detect_outliers_iqr,            # Outlier detection
    export_summary_to_csv,          # Export to CSV
    print_data_info                 # Print data information
)
```

### Example: Using Utility Functions

```python
from plotease.utils import load_mtcars, get_numeric_columns

# Load example dataset
data = load_mtcars()

# Get numeric columns
numeric_cols = get_numeric_columns(data)
print(f"Numeric columns: {numeric_cols}")
```

## 🔧 Troubleshooting

### Common Issues

**Issue: `ModuleNotFoundError: No module named 'plotease'`**
- **Solution:** Ensure you've installed the package: `pip install plotease`

**Issue: Plots not displaying**
- **Solution:** Make sure you're running in an environment that supports plotting (Jupyter, IDE with plot support)
- Try adding `plt.show()` if in a script

**Issue: `ValueError: DataFrame is empty`**
- **Solution:** Verify your data is loaded correctly before creating PlotEase instance
- Use `print(data.head())` to check

**Issue: Import errors for dependencies**
- **Solution:** Install missing dependencies: `pip install pandas numpy matplotlib seaborn scipy`

**Issue: Theme not applying**
- **Solution:** Set theme during initialization: `pe = PlotEase(data, theme='dark')`
- Or use: `pe.set_theme('dark')`

## Contributors

This project was developed as part of an Object-Oriented Programming course.

### Team Members

- **Khassandra Louise C. Jayme** - Lead Developer - [GitHub](https://github.com/Khassndrajayme)
- **Sheena Angela T. Janog** - Developer - [GitHub](https://github.com/Sheena06J)
- **Xavier Neo Mahilum** - Developer - [GitHub](https://github.com/MysteriousHotdog)
- **Allen Floro Ventura** - Developer - [GitHub](https://github.com/AllenKalbo)
- **Genetyron Zamoranos** - Developer - [GitHub](https://github.com/noryt-py)

### Acknowledgments

- Thanks to our instructor for guidance and support
- Inspired by matplotlib, seaborn, and ggplot2
- mtcars dataset from R's datasets package

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

We welcome contributions! Please feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

**Made with ❤️ by the PlotEase Team**
