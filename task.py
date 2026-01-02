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


# ============================================================================
# TASK 3: CHART GENERATION FUNCTIONS
# ============================================================================

# Task 3.1: Overall Churn Distribution (Pie Chart)
def create_churn_pie_chart(df: pd.DataFrame) -> str:
    """
    Generate overall churn distribution pie chart.
    
    Args:
        df: Customer churn DataFrame
        
    Returns:
        str: Path to saved chart
    """
    # Calculate churn counts
    churn_counts = df['churned'].value_counts().sort_index()
    labels = ['Retained', 'Churned']
    colors = [RETAIN_GREEN, CHURN_RED]
    
    # Create pie chart
    fig, ax = plt.subplots(figsize=(6, 4))
    wedges, texts, autotexts = ax.pie(
        churn_counts,
        labels=labels,
        colors=colors,
        autopct='%1.1f%%',
        startangle=90,
        explode=(0.05, 0.05)
    )
    
    # Styling
    ax.set_title('Customer Churn Distribution', pad=20)
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(12)
        autotext.set_weight('bold')
    
    # Save
    output_path = OUTPUT_DIR / '01_churn_distribution_pie.png'
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    
    print(f"  [OK] Saved: {output_path}")
    return str(output_path)


# Task 3.2: Churn by Contract Type (Bar Chart)
def create_contract_churn_chart(df: pd.DataFrame) -> str:
    """
    Generate churn rate by contract type bar chart.
    
    Args:
        df: Customer churn DataFrame
        
    Returns:
        str: Path to saved chart
    """
    # Calculate churn rates
    contract_churn = df.groupby('contract_type').agg({
        'churned': ['sum', 'count']
    })
    contract_churn.columns = ['churned', 'total']
    contract_churn['churn_rate'] = (contract_churn['churned'] / contract_churn['total']) * 100
    contract_churn = contract_churn.sort_values('churn_rate', ascending=False)
    
    # Create bar chart
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(
        range(len(contract_churn)),
        contract_churn['churn_rate'],
        color=[CHURN_RED, '#e67e73', '#f1948a']
    )
    
    # Add value labels
    for i, (idx, row) in enumerate(contract_churn.iterrows()):
        ax.text(
            i, row['churn_rate'] + 1,
            f"{row['churn_rate']:.1f}%",
            ha='center', va='bottom', fontweight='bold'
        )
    
    # Styling
    ax.set_xticks(range(len(contract_churn)))
    ax.set_xticklabels(contract_churn.index, rotation=0)
    ax.set_ylabel('Churn Rate (%)')
    ax.set_title('Churn Rate by Contract Type')
    ax.set_ylim(0, 100)
    ax.grid(axis='y', alpha=0.3)
    
    # Save
    output_path = OUTPUT_DIR / '02_churn_by_contract.png'
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    
    print(f"  [OK] Saved: {output_path}")
    return str(output_path)


# Task 3.3: Churn by Support Calls (Bar Chart)
def create_support_calls_chart(df: pd.DataFrame) -> str:
    """
    Generate churn rate by support calls bar chart.
    
    Args:
        df: Customer churn DataFrame
        
    Returns:
        str: Path to saved chart
    """
    # Calculate churn rates
    support_churn = df.groupby('num_support_calls').agg({
        'churned': ['sum', 'count']
    })
    support_churn.columns = ['churned', 'total']
    support_churn['churn_rate'] = (support_churn['churned'] / support_churn['total']) * 100
    
    # Create bar chart with gradient
    fig, ax = plt.subplots(figsize=(8, 5))
    colors_gradient = ['#f39c12', '#e67e22', '#d35400', '#c0392b', '#a93226']
    bars = ax.bar(
        support_churn.index,
        support_churn['churn_rate'],
        color=colors_gradient[:len(support_churn)]
    )
    
    # Add value labels
    for i, (idx, row) in enumerate(support_churn.iterrows()):
        ax.text(
            idx, row['churn_rate'] + 2,
            f"{row['churn_rate']:.1f}%",
            ha='center', va='bottom', fontweight='bold'
        )
    
    # Styling
    ax.set_xlabel('Number of Support Calls')
    ax.set_ylabel('Churn Rate (%)')
    ax.set_title('Churn Rate by Number of Support Calls')
    ax.set_ylim(0, 100)
    ax.grid(axis='y', alpha=0.3)
    
    # Highlight high risk zone (3+ calls)
    ax.axvspan(2.5, support_churn.index.max() + 0.5, alpha=0.1, color='red', label='High Risk Zone')
    ax.legend()
    
    # Save
    output_path = OUTPUT_DIR / '03_churn_by_support_calls.png'
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    
    print(f"  [OK] Saved: {output_path}")
    return str(output_path)


# Task 3.4: Churn by Payment Method (Grouped Bar)
def create_payment_method_chart(df: pd.DataFrame) -> str:
    """
    Generate customer status by payment method grouped bar chart.
    
    Args:
        df: Customer churn DataFrame
        
    Returns:
        str: Path to saved chart
    """
    # Calculate counts
    payment_status = df.groupby(['payment_method', 'churned']).size().unstack(fill_value=0)
    payment_status.columns = ['Retained', 'Churned']
    
    # Create grouped bar chart
    fig, ax = plt.subplots(figsize=(9, 5))
    x = np.arange(len(payment_status))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, payment_status['Retained'], width, 
                   label='Retained', color=RETAIN_GREEN)
    bars2 = ax.bar(x + width/2, payment_status['Churned'], width,
                   label='Churned', color=CHURN_RED)
    
    # Styling
    ax.set_xlabel('Payment Method')
    ax.set_ylabel('Customer Count')
    ax.set_title('Customer Status by Payment Method')
    ax.set_xticks(x)
    ax.set_xticklabels(payment_status.index, rotation=15, ha='right')
    ax.legend(loc='upper right')
    ax.grid(axis='y', alpha=0.3)
    
    # Save
    output_path = OUTPUT_DIR / '04_churn_by_payment.png'
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    
    print(f"  [OK] Saved: {output_path}")
    return str(output_path)


# Task 3.5: Churn by Products (Bar Chart)
def create_products_chart(df: pd.DataFrame) -> str:
    """
    Generate churn rate by number of products bar chart.
    
    Args:
        df: Customer churn DataFrame
        
    Returns:
        str: Path to saved chart
    """
    # Calculate churn rates
    products_churn = df.groupby('num_products').agg({
        'churned': ['sum', 'count']
    })
    products_churn.columns = ['churned', 'total']
    products_churn['churn_rate'] = (products_churn['churned'] / products_churn['total']) * 100
    
    # Create bar chart with green gradient (lower churn = darker green)
    fig, ax = plt.subplots(figsize=(8, 5))
    colors_green = ['#27ae60', '#2ecc71', '#52be80', '#7dcea0', '#a9dfbf']
    bars = ax.bar(
        products_churn.index,
        products_churn['churn_rate'],
        color=colors_green[:len(products_churn)]
    )
    
    # Add value labels
    for i, (idx, row) in enumerate(products_churn.iterrows()):
        ax.text(
            idx, row['churn_rate'] + 1,
            f"{row['churn_rate']:.1f}%",
            ha='center', va='bottom', fontweight='bold'
        )
    
    # Styling
    ax.set_xlabel('Number of Products')
    ax.set_ylabel('Churn Rate (%)')
    ax.set_title('Churn Rate by Product Portfolio Size')
    ax.set_ylim(0, max(products_churn['churn_rate']) * 1.2)
    ax.grid(axis='y', alpha=0.3)
    
    # Save
    output_path = OUTPUT_DIR / '05_churn_by_products.png'
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    
    print(f"  [OK] Saved: {output_path}")
    return str(output_path)


print("[OK] Task 3.1-3.5: First 5 chart functions defined")
