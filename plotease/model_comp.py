import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Optional, List, Dict 

class ModelComparator:
    """
    Compares machine learning model performance across various metrics.

    This class demonstrates several core object-oriented programming (OOP) principles:
     1. Encapsulation: The model results are stored in a protected attribute (_models_results).
     2. Operator Overloading (Dunder Methods): Customizing behavior for operators like == (equality) and > (greater than).

    Attributes:
        _models_results (Dict[str, Dict[str, float]]): The raw input dictionary.
        _df (pd.DataFrame): A pandas DataFrame representation of the results,
            with models as the index and metrics as the columns.
    """
    
    def __init__(self, models_results: Dict[str, Dict[str, float]]):
        """
        Initializes the ModelComparator with a dictionary of model results.

        Args:
            models_results: A dictionary containing model performance scores.
                            Format: {'Model_A': {'Metric1': 0.9, 'Metric2': 0.8}, ...}
        """
        # Protected attribute to store the raw results
        self._models_results = models_results  
        
        if not models_results:
             # Handle empty input gracefully to avoid errors during plotting/comparison
            self._df = pd.DataFrame()
        else:
            # Convert results to a DataFrame (models as index, metrics as columns)
            # .T is the transpose operation, ensuring models are rows (index)
            self._df = pd.DataFrame(models_results).T
    
    def create_bar_chart(self, ax: plt.Axes, df: pd.DataFrame):
        """
        Creates and formats a grouped bar chart for model performance.
        """
        # FIX: Ensure there is data before plotting
        if df.empty:
            ax.text(0.5, 0.5, 'No Data to Plot', ha='center', va='center', fontsize=16)
            ax.set_title('Model Performance Comparison (Bar Chart)')
            return
            
        df.plot(kind='bar', ax=ax, width=0.8, edgecolor='black')
        ax.set_title('Model Performance Comparison (Bar Chart)', fontsize=16, fontweight='bold')
        ax.set_xlabel('Models', fontsize=12)
        ax.set_ylabel('Score', fontsize=12)
        ax.legend(title='Metrics', bbox_to_anchor=(1.05, 1), loc='upper left')
        ax.grid(axis='y', alpha=0.3)
        ax.set_xticklabels(df.index, rotation=45, ha='right')
        # Setting y-limit ensures consistency across plots
        ax.set_ylim(0, 1.0)
        
        # Add score labels on top of each bar
        for container in ax.containers:
            ax.bar_label(container, fmt='%.3f', padding=3, fontsize=9)
    
    def create_radar_chart(self, ax: plt.Axes, df: pd.DataFrame):
        """
        Creates and formats a radar chart for model performance.
        """
        if df.empty or len(df.columns) < 3:
             # Radar charts require at least 3 axes/metrics to be meaningful
            ax.text(0.5, 0.5, 'Requires at least 3 Metrics', ha='center', va='center', fontsize=16)
            ax.set_title('Model Performance Radar')
            ax.axis('off') # Hide polar axis if no plot is made
            return

        n_metrics = len(df.columns)
        # Calculate angles for the radar axes
        angles = np.linspace(0, 2 * np.pi, n_metrics, endpoint=False).tolist()
        # Complete the loop for plotting (closing the circle)
        angles += angles[:1]
        
        # Plot each model's performance on the radar chart
        for model_name, values in df.iterrows():
            values_list = values.tolist()
            values_list += values_list[:1] # Close the circle
            ax.plot(angles, values_list, 'o-', linewidth=2, label=model_name)
            ax.fill(angles, values_list, alpha=0.15)
        
        # Set the labels for each metric
        ax.set_xticks(angles[:-1])
