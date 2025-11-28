# 1. Import all primary classes from their new modules 
# The classes are imported relative to the current package ('.')

from .visualization import VisualizationBase # From visualization.py
from .summary import SummaryGenerator       # From summary.py
from .diagnostic import DiagnosticPlotter   # From diagnostic.py
from .quick_plotter import QuickPlotter     # From quick_plotter.py
from .model_comp import ModelComparator     # From model_comp.py

# The main user-facing facade class
from .plotease import PlotEase              # From plotease.py 

# 2. Define __all__ 
# This explicitly lists all public objects to expose when someone runs 'from plotease import *'
__all__ = [
    "PlotEase",
    "VisualizationBase",
    "SummaryGenerator",
    "DiagnosticPlotter",
    "QuickPlotter",
    "ModelComparator",
]

# 3. Package Version 
__version__ = "0.1.0"