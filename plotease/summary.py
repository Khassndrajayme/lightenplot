import pandas as pd
import numpy as np 
from typing import List, Dict 

class SummaryGenerator:
    """
    Generates comprehensive data summaries.
    
    Demonstrates: Encapsulation (using _data), Dunder Methods (__repr__, __len__).
    """

    def __init__(self, data: pd.DataFrame):
        # Encapsulation: Use of a protected attribute for the DataFrame
        self._data = data

    def summarize_numeric(self) -> List[Dict]:
        """Summarize numeric columns"""
        summaries = []
        # Use np.number to select all numeric dtypes
        numeric_cols = self._data.select_dtypes(include=[np.number]).columns

        for col in numeric_cols:
            summary = {
                'Column': col,
                'Type': 'Numeric',
                # NOTE: The code correctly uses the protected attribute self._data[col]
                'Count': self._data[col].count(), 
                'Missing': self._data[col].isnull().sum(),
                'Missing %': f"{self._data[col].isnull().sum() / len(self._data) * 100:.1f}%",
                'Mean': f"{self._data[col].mean():.2f}",
                'Std': f"{self._data[col].std():.2f}",
                'Min': f"{self._data[col].min():.2f}",
                'Max': f"{self._data[col].max():.2f}",
                'Unique': self._data[col].nunique()
            }
            summaries.append(summary)
        return summaries

    def summarize_categorical(self) -> List[Dict]:
        """Summarize categorical columns"""
        summaries = []
        # Include 'object' (strings) and 'category' (explicitly casted)
        categorical_cols = self._data.select_dtypes(include=['object', 'category']).columns

        for col in categorical_cols:
            # Safely get the mode (top value)
            top_val = self._data[col].mode()[0] if not self._data[col].mode().empty else 'N/A'
            
            # Use value_counts() to safely get top frequency
            value_counts = self._data[col].value_counts()
            top_freq = value_counts.iloc[0] if not value_counts.empty else 0
            
            summary = {
                'Column': col,
                'Type': 'Categorical',
                'Count': self._data[col].count(),
                'Missing': self._data[col].isnull().sum(),
                'Missing %': f"{self._data[col].isnull().sum() / len(self._data) * 100:.1f}%",
                'Unique': self._data[col].nunique(),
                'Top Value': str(top_val),
                'Top Freq': top_freq
            }
            summaries.append(summary)
        return summaries

    def tabular_summary(self, style: str = 'full') -> pd.DataFrame:
        """
        Generate comprehensive tabular summary

        Args:
            style: 'full' (numeric & categorical), 'numeric', or 'categorical'

        Returns:
            DataFrame with summary statistics
        """
        summaries = []

        if style in ['full', 'numeric']:
            summaries.extend(self.summarize_numeric())

        if style in ['full', 'categorical']:
            summaries.extend(self.summarize_categorical())
            
        summary_df = pd.DataFrame(summaries) # FIX: Added missing assignment operator '='

        print("\n" + "="*80)
        print(f"DATASET SUMMARY - {style.upper()} VIEW")
        print("="*80)
        print(f"Total Rows: {len(self._data):,}")
        # Calculate memory usage in MB
        memory_mb = self._data.memory_usage(deep=True).sum() / 1024**2
        print(f"Memory Usage: {memory_mb:.2f} MB")
        print("="*80 + "\n")

        return summary_df

    # Dunder Methods
    def __repr__(self) -> str:
        """String representation: How the object looks when printed"""
        return f"SummaryGenerator(rows={len(self._data)}, cols={len(self._data.columns)})"

    def __len__(self) -> int:
        """Return number of rows, allowing len(instance)"""
        return len(self._data)
