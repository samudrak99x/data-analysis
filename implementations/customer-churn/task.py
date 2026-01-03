"""
Customer Churn Visualization Task

Generates 10 visualizations from customer churn dataset to analyze
churn patterns, contract types, payment methods, and customer demographics.

Generated from specification: customer-churn-chart-spec.md
Author: DataDev Agent
Date: 2026-01-02
"""

# Standard library imports
from pathlib import Path
import os

# Third-party imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================================
# TASK 1: Setup & Configuration
# ============================================================================

# Path resolution: Works for both local and container environments
BASE_DIR = Path(os.getenv('TASK_BASE_DIR', '.'))
DATA_DIR = BASE_DIR / 'data'
OUTPUT_DIR = BASE_DIR / 'outputs'
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Input file path
INPUT_FILE = DATA_DIR / 'customer_churn.csv'

# Visualization constants
DPI = 300

# Color palette dictionary
COLORS = {
    'retained': '#6BCF7F',      # Green for retained
    'churned': '#FF6B6B',       # Red for churned
    'warning': '#FFD93D',       # Yellow for medium risk
    'primary': '#4A90E2',       # Blue for neutral
    'secondary': '#9B59B6',     # Purple for accent
    'accent1': '#FF9800',       # Orange
    'accent2': '#26A69A'        # Teal
}

# Matplotlib style configuration
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.dpi'] = DPI

# ============================================================================
# TASK 2: Data Loading Function
# ============================================================================

def load_data(input_file=None):
    """
    Load and prepare customer churn dataset.
    
    Args:
        input_file: Path to CSV file (defaults to INPUT_FILE)
    
    Returns:
        DataFrame with numeric types converted
    """
    if input_file is None:
        input_file = INPUT_FILE
    else:
        input_file = Path(input_file)
        if not input_file.is_absolute():
            input_file = BASE_DIR / input_file
    
    if not input_file.exists():
        raise FileNotFoundError(f"File not found: {input_file}")
    
    # Read CSV
    df = pd.read_csv(input_file)
    
    # Convert string columns to numeric types
    numeric_cols = ['age', 'tenure_months', 'monthly_charges', 'total_charges', 
                    'num_products', 'num_support_calls', 'churned']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    return df

# ============================================================================
# TASK 3: Chart Generation Functions
# ============================================================================

def create_customer_distribution(df):
    """TASK 3.1: Create customer churn overview pie chart."""
    churn_counts = df['churned'].value_counts().sort_index()
    
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.pie(churn_counts.values, 
           labels=['Retained', 'Churned'],
           autopct='%1.1f%%',
           colors=[COLORS['retained'], COLORS['churned']],
           explode=(0, 0.1),
           startangle=90)
    ax.set_title('Customer Churn Overview\n1,000 Total Customers', 
                 fontsize=16, fontweight='bold')
    
    plt.savefig(OUTPUT_DIR / '01_customer_distribution.png', dpi=DPI, bbox_inches='tight')
    plt.close()
    print('  [OK] Saved: 01_customer_distribution.png')

def create_churn_by_contract(df):
    """TASK 3.2: Create churn rate by contract type bar chart."""
    churn_by_contract = df.groupby('contract_type')['churned'].agg(['mean', 'count'])
    churn_by_contract['churn_rate'] = churn_by_contract['mean'] * 100
    churn_by_contract = churn_by_contract.reindex(['Month-to-month', 'One year', 'Two year'])
    
    fig, ax = plt.subplots(figsize=(12, 8))
    bars = ax.bar(churn_by_contract.index, 
                  churn_by_contract['churn_rate'],
                  color=[COLORS['churned'], COLORS['warning'], COLORS['retained']])
    
    # Add percentage labels on bars
    for i, (idx, row) in enumerate(churn_by_contract.iterrows()):
        ax.text(i, row['churn_rate'] + 1, f"{row['churn_rate']:.1f}%",
                ha='center', va='bottom', fontweight='bold')
        ax.text(i, -2, f"n={int(row['count'])}",
                ha='center', va='top', fontsize=9)
    
    ax.set_title('Churn Rate by Contract Type', fontsize=14, fontweight='bold')
    ax.set_xlabel('Contract Type', fontsize=12)
    ax.set_ylabel('Churn Rate (%)', fontsize=12)
    ax.set_ylim(0, max(churn_by_contract['churn_rate']) * 1.2)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    plt.xticks(rotation=0)
    
    plt.savefig(OUTPUT_DIR / '02_churn_by_contract.png', dpi=DPI, bbox_inches='tight')
    plt.close()
    print('  [OK] Saved: 02_churn_by_contract.png')

def create_churn_by_payment(df):
    """TASK 3.3: Create churn rate by payment method horizontal bar chart."""
    churn_by_payment = df.groupby('payment_method')['churned'].mean() * 100
    churn_by_payment = churn_by_payment.sort_values(ascending=False)
    
    # Create gradient colors based on churn rate
    gradient_colors = []
    max_churn = churn_by_payment.max()
    min_churn = churn_by_payment.min()
    for val in churn_by_payment.values:
        # Interpolate between red (high) and green (low)
        ratio = (val - min_churn) / (max_churn - min_churn) if max_churn > min_churn else 0.5
        if ratio > 0.5:
            gradient_colors.append(COLORS['churned'])
        else:
            gradient_colors.append(COLORS['retained'])
    
    fig, ax = plt.subplots(figsize=(12, 8))
    bars = ax.barh(churn_by_payment.index, churn_by_payment.values, color=gradient_colors)
    
    # Add percentage labels at end of bars
    for i, (idx, val) in enumerate(churn_by_payment.items()):
        ax.text(val + 0.5, i, f"{val:.1f}%",
                va='center', fontweight='bold')
    
    ax.set_title('Churn Rate by Payment Method', fontsize=14, fontweight='bold')
    ax.set_xlabel('Churn Rate (%)', fontsize=12)
    ax.set_ylabel('Payment Method', fontsize=12)
    ax.set_xlim(0, max(churn_by_payment.values) * 1.15)
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    
    plt.savefig(OUTPUT_DIR / '03_churn_by_payment.png', dpi=DPI, bbox_inches='tight')
    plt.close()
    print('  [OK] Saved: 03_churn_by_payment.png')

def create_churn_by_tenure(df):
    """TASK 3.4: Create churn rate by tenure line chart."""
    df_copy = df.copy()
    df_copy['tenure_group'] = pd.cut(df_copy['tenure_months'], 
                                     bins=[0, 12, 24, 36, 72], 
                                     labels=['0-12', '13-24', '25-36', '37-72'])
    churn_by_tenure = df_copy.groupby('tenure_group')['churned'].mean() * 100
    
    fig, ax = plt.subplots(figsize=(12, 8))
    line = ax.plot(churn_by_tenure.index.astype(str), 
                   churn_by_tenure.values,
                   marker='o', linewidth=2, markersize=10, color=COLORS['primary'])
    
    # Highlight first point with larger marker
    ax.plot(churn_by_tenure.index[0], churn_by_tenure.iloc[0],
            marker='o', markersize=15, color=COLORS['warning'], 
            markeredgecolor='black', markeredgewidth=2)
    
    # Add percentage labels above points
    for i, (idx, val) in enumerate(churn_by_tenure.items()):
        ax.text(i, val + 2, f"{val:.1f}%",
                ha='center', va='bottom', fontweight='bold')
    
    ax.set_title('Churn Rate by Customer Tenure', fontsize=14, fontweight='bold')
    ax.set_xlabel('Tenure Group (months)', fontsize=12)
    ax.set_ylabel('Churn Rate (%)', fontsize=12)
    ax.set_ylim(0, max(churn_by_tenure.values) * 1.3)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.savefig(OUTPUT_DIR / '04_churn_by_tenure.png', dpi=DPI, bbox_inches='tight')
    plt.close()
    print('  [OK] Saved: 04_churn_by_tenure.png')

def create_churn_by_products(df):
    """TASK 3.5: Create churn rate by number of products bar chart."""
    churn_by_products = df.groupby('num_products')['churned'].agg(['mean', 'count'])
    churn_by_products['churn_rate'] = churn_by_products['mean'] * 100
    
    fig, ax = plt.subplots(figsize=(12, 8))
    bars = ax.bar(churn_by_products.index.astype(str),
                  churn_by_products['churn_rate'],
                  color=COLORS['secondary'])
    
    # Add percentage labels on bars
    for i, (idx, row) in enumerate(churn_by_products.iterrows()):
        ax.text(i, row['churn_rate'] + 1, f"{row['churn_rate']:.1f}%",
                ha='center', va='bottom', fontweight='bold')
        ax.text(i, -1, f"n={int(row['count'])}",
                ha='center', va='top', fontsize=9)
    
    ax.set_title('Churn Rate by Number of Products', fontsize=14, fontweight='bold')
    ax.set_xlabel('Number of Products', fontsize=12)
    ax.set_ylabel('Churn Rate (%)', fontsize=12)
    ax.set_ylim(0, max(churn_by_products['churn_rate']) * 1.2)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.savefig(OUTPUT_DIR / '05_churn_by_products.png', dpi=DPI, bbox_inches='tight')
    plt.close()
    print('  [OK] Saved: 05_churn_by_products.png')

def create_age_distribution(df):
    """TASK 3.6: Create age distribution overlapping histograms."""
    age_bins = [18, 30, 40, 50, 60, 70, 80]
    churned_ages = df[df['churned'] == 1]['age']
    retained_ages = df[df['churned'] == 0]['age']
    
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.hist([retained_ages, churned_ages],
            bins=age_bins,
            label=['Retained', 'Churned'],
            color=[COLORS['retained'], COLORS['churned']],
            alpha=0.7,
            edgecolor='black')
    
    ax.set_title('Age Distribution: Churned vs Retained', fontsize=14, fontweight='bold')
    ax.set_xlabel('Age (years)', fontsize=12)
    ax.set_ylabel('Number of Customers', fontsize=12)
    ax.legend(loc='upper right')
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.savefig(OUTPUT_DIR / '06_age_distribution.png', dpi=DPI, bbox_inches='tight')
    plt.close()
    print('  [OK] Saved: 06_age_distribution.png')

def create_charges_distribution(df):
    """TASK 3.7: Create monthly charges distribution box plot."""
    retained_charges = df[df['churned'] == 0]['monthly_charges']
    churned_charges = df[df['churned'] == 1]['monthly_charges']
    
    fig, ax = plt.subplots(figsize=(12, 8))
    bp = ax.boxplot([retained_charges, churned_charges],
                    labels=['Retained', 'Churned'],
                    patch_artist=True)
    
    # Set colors for boxes
    bp['boxes'][0].set_facecolor(COLORS['retained'])
    bp['boxes'][1].set_facecolor(COLORS['churned'])
    bp['boxes'][0].set_alpha(0.7)
    bp['boxes'][1].set_alpha(0.7)
    
    # Add mean value annotations
    ax.text(1, retained_charges.mean(), f"Mean: ${retained_charges.mean():.2f}",
            ha='center', va='bottom', fontweight='bold')
    ax.text(2, churned_charges.mean(), f"Mean: ${churned_charges.mean():.2f}",
            ha='center', va='bottom', fontweight='bold')
    
    ax.set_title('Monthly Charges Distribution', fontsize=14, fontweight='bold')
    ax.set_ylabel('Monthly Charges ($)', fontsize=12)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.savefig(OUTPUT_DIR / '07_charges_distribution.png', dpi=DPI, bbox_inches='tight')
    plt.close()
    print('  [OK] Saved: 07_charges_distribution.png')

def create_support_calls_churn(df):
    """TASK 3.8: Create support calls distribution stacked bar chart."""
    support_churn = df.groupby(['num_support_calls', 'churned']).size().unstack(fill_value=0)
    if 0 not in support_churn.columns:
        support_churn[0] = 0
    if 1 not in support_churn.columns:
        support_churn[1] = 0
    support_churn = support_churn[[0, 1]]
    support_churn.columns = ['Retained', 'Churned']
    
    fig, ax = plt.subplots(figsize=(12, 8))
    support_churn.plot(kind='bar', stacked=True, ax=ax,
                      color=[COLORS['retained'], COLORS['churned']])
    
    # Add count labels on segments
    for container in ax.containers:
        ax.bar_label(container, label_type='center', fontsize=9)
    
    ax.set_title('Support Calls Distribution by Churn Status', fontsize=14, fontweight='bold')
    ax.set_xlabel('Number of Support Calls', fontsize=12)
    ax.set_ylabel('Customer Count', fontsize=12)
    ax.legend(title='Status', loc='upper right')
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    plt.xticks(rotation=0)
    
    plt.savefig(OUTPUT_DIR / '08_support_calls_churn.png', dpi=DPI, bbox_inches='tight')
    plt.close()
    print('  [OK] Saved: 08_support_calls_churn.png')

def create_contract_distribution(df):
    """TASK 3.9: Create contract type distribution pie chart."""
    contract_counts = df['contract_type'].value_counts()
    contract_counts = contract_counts.reindex(['Month-to-month', 'One year', 'Two year'])
    
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.pie(contract_counts.values,
           labels=contract_counts.index,
           autopct='%1.1f%%',
           colors=[COLORS['churned'], COLORS['warning'], COLORS['retained']])
    ax.set_title('Customer Base by Contract Type\nContract distribution across 1,000 customers',
                 fontsize=14, fontweight='bold')
    
    plt.savefig(OUTPUT_DIR / '09_contract_distribution.png', dpi=DPI, bbox_inches='tight')
    plt.close()
    print('  [OK] Saved: 09_contract_distribution.png')

def create_payment_distribution(df):
    """TASK 3.10: Create payment method distribution pie chart."""
    payment_counts = df['payment_method'].value_counts()
    
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.pie(payment_counts.values,
           labels=payment_counts.index,
           autopct='%1.1f%%',
           colors=[COLORS['primary'], COLORS['secondary'], COLORS['accent1'], COLORS['accent2']])
    ax.set_title('Customer Base by Payment Method\nPayment preference distribution',
                 fontsize=14, fontweight='bold')
    
    plt.savefig(OUTPUT_DIR / '10_payment_distribution.png', dpi=DPI, bbox_inches='tight')
    plt.close()
    print('  [OK] Saved: 10_payment_distribution.png')

# ============================================================================
# TASK 4: Main Execution Function
# ============================================================================

def main():
    """Main execution function."""
    print("=" * 50)
    print("CUSTOMER CHURN VISUALIZATION TASK")
    print("=" * 50)
    
    print("\n[1/2] Loading data...")
    df = load_data()
    print(f"  Loaded {len(df):,} rows")
    
    print("\n[2/2] Generating charts...")
    create_customer_distribution(df)
    create_churn_by_contract(df)
    create_churn_by_payment(df)
    create_churn_by_tenure(df)
    create_churn_by_products(df)
    create_age_distribution(df)
    create_charges_distribution(df)
    create_support_calls_churn(df)
    create_contract_distribution(df)
    create_payment_distribution(df)
    
    print("\n" + "=" * 50)
    print(f"COMPLETED - Generated 10 charts in {OUTPUT_DIR}")
    print("=" * 50)

if __name__ == '__main__':
    main()
