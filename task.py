"""
Customer Churn Visualization - BI Chart Generation
Generated from: customer-churn-chart-spec.md
Date: January 2, 2026
Developer: DevPython (BI & Visualization Developer)

This module implements 10 chart visualizations for customer churn analysis.
"""

# TASK 1: Imports & Configuration
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

# Color scheme constants
CHURN_RED = '#e74c3c'
RETAIN_GREEN = '#2ecc71'
NEUTRAL_BLUE = '#3498db'
WARNING_ORANGE = '#f39c12'

# Output configuration
OUTPUT_DIR = Path('outputs')
OUTPUT_DIR.mkdir(exist_ok=True)

# Matplotlib style configuration
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")


# TASK 2: Data Loading & Validation
def load_data(filepath: str) -> pd.DataFrame:
    """
    Load and validate customer churn dataset.
    
    Args:
        filepath: Path to the customer_churn.csv file
        
    Returns:
        pd.DataFrame: Validated customer churn dataset
        
    Raises:
        FileNotFoundError: If the dataset file doesn't exist
        ValueError: If required columns are missing
    """
    print(f"Loading data from: {filepath}")
    
    # Read CSV file
    df = pd.read_csv(filepath)
    
    # Expected columns
    expected_columns = [
        'customer_id', 'age', 'tenure_months', 'monthly_charges',
        'total_charges', 'num_products', 'num_support_calls',
        'contract_type', 'payment_method', 'churned'
    ]
    
    # Verify columns exist
    missing_cols = set(expected_columns) - set(df.columns)
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")
    
    # Check for missing values
    null_counts = df.isnull().sum()
    if null_counts.sum() > 0:
        print(f"Warning: Found {null_counts.sum()} missing values")
        print(null_counts[null_counts > 0])
    
    # Convert data types
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df['tenure_months'] = pd.to_numeric(df['tenure_months'], errors='coerce')
    df['monthly_charges'] = pd.to_numeric(df['monthly_charges'], errors='coerce')
    df['total_charges'] = pd.to_numeric(df['total_charges'], errors='coerce')
    df['num_products'] = pd.to_numeric(df['num_products'], errors='coerce')
    df['num_support_calls'] = pd.to_numeric(df['num_support_calls'], errors='coerce')
    df['churned'] = pd.to_numeric(df['churned'], errors='coerce')
    
    # Print data summary
    print(f"\nDataset Summary:")
    print(f"  Shape: {df.shape}")
    print(f"  Columns: {list(df.columns)}")
    print(f"  Churn Rate: {df['churned'].mean()*100:.2f}%")
    print(f"  Sample:")
    print(df.head(3))
    
    return df


# TASK 3: Chart Generation Functions
# (To be implemented in next commit)


# TASK 4: Main Execution Function
def main():
    """
    Main execution function for chart generation.
    Orchestrates data loading and all chart generation.
    """
    print("="*60)
    print("  Customer Churn Chart Generation")
    print("  BI Visualization Implementation")
    print("="*60)
    
    # Load data
    try:
        df = load_data('data/customer_churn.csv')
    except Exception as e:
        print(f"[ERROR] Failed to load data: {e}")
        return
    
    # Track successfully created charts
    charts_created = []
    
    print("\n" + "="*60)
    print("  Chart generation will be implemented in next commit")
    print("="*60)
    
    # Summary
    print(f"\n[OK] Setup complete. Ready for chart generation.")
    print(f"[OK] Output directory: {OUTPUT_DIR.absolute()}")


if __name__ == "__main__":
    main()