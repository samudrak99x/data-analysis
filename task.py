#!/usr/bin/env python3
"""
Customer Churn Visualization - Task Implementation

Generates 10 professional charts for customer churn analysis.
Based on specification: customer-churn-chart-spec.md

Author: DataJames (@data-dev)
Date: January 2, 2026
"""

# ============================================================================
# TASK 1: SETUP & CONFIGURATION
# ============================================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Color Palette (Task 1.2)
CHURN_RED = '#e74c3c'
RETAIN_GREEN = '#2ecc71'
NEUTRAL_BLUE = '#3498db'
WARNING_ORANGE = '#f39c12'

# Output Configuration (Task 1.3)
OUTPUT_DIR = Path('outputs')
DATA_PATH = 'data/customer_churn.csv'

# Matplotlib Defaults (Task 1.4)
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.size'] = 11
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.titleweight'] = 'bold'

# Create output directory (Task 1.5)
OUTPUT_DIR.mkdir(exist_ok=True)

print("[OK] Task 1: Setup & Configuration complete")


# ============================================================================
# TASK 2: DATA LOADING & VALIDATION
# ============================================================================

def load_data(filepath: str) -> pd.DataFrame:
    """
    Load and validate customer churn dataset.
    
    Args:
        filepath: Path to CSV file
        
    Returns:
        pd.DataFrame: Validated customer churn data
        
    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If required columns are missing
    """
    # Task 2.2: Read CSV file
    df = pd.read_csv(filepath)
    
    # Task 2.3: Verify expected columns
    required_cols = [
        'customer_id', 'age', 'tenure_months', 'monthly_charges',
        'total_charges', 'num_products', 'num_support_calls',
        'contract_type', 'payment_method', 'churned'
    ]
    
    missing_cols = set(required_cols) - set(df.columns)
    if missing_cols:
        raise ValueError(f"Missing columns: {missing_cols}")
    
    # Task 2.4: Check for missing values
    null_counts = df[required_cols].isnull().sum()
    if null_counts.any():
        print(f"Warning: Found missing values:\n{null_counts[null_counts > 0]}")
    
    # Task 2.5: Convert data types
    df['churned'] = df['churned'].astype(int)
    df['num_products'] = df['num_products'].astype(int)
    df['num_support_calls'] = df['num_support_calls'].astype(int)
    df['age'] = df['age'].astype(int)
    df['tenure_months'] = df['tenure_months'].astype(int)
    
    # Task 2.6: Print data summary
    print(f"\n[OK] Task 2: Data loaded successfully")
    print(f"  - Shape: {df.shape[0]} rows x {df.shape[1]} columns")
    print(f"  - Churn Rate: {df['churned'].mean()*100:.1f}%")
    print(f"  - Date Range: {df['tenure_months'].min()}-{df['tenure_months'].max()} months")
    
    # Task 2.7: Return validated DataFrame
    return df


print("[OK] Task 2: Data Loading Function defined")
