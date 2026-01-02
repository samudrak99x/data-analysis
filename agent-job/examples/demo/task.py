"""
Customer Churn Visualization Task

This script generates 9 visualizations for customer churn analysis based on
the specification in customer-churn-chart-spec.md.

Generated: January 2, 2026
Author: DataDev Agent
"""

# Standard library imports
from pathlib import Path
import sys
import os
from datetime import datetime

# Third-party imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================================
# CONFIGURATION AND CONSTANTS
# ============================================================================

# Path resolution: Works for both local and container environments
# - Local: Uses current directory structure
# - Container: Uses /app/ as base (set by Kubernetes pod)
BASE_DIR = Path(os.getenv('TASK_BASE_DIR', '.'))
DATA_DIR = BASE_DIR / 'data'
OUTPUT_DIR = BASE_DIR / 'outputs'

# Input and output paths (relative to BASE_DIR)
INPUT_FILE = DATA_DIR / 'customer_churn.csv'
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# DPI setting
DPI = 300

# Color palette
colors = {
    'danger': '#FF6B6B',      # Red for high churn
    'warning': '#FFD93D',     # Yellow for medium
    'success': '#6BCF7F',     # Green for low churn
    'primary': '#4A90E2',     # Blue for neutral
    'secondary': '#9B59B6'    # Purple for accent
}

# Matplotlib style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# ============================================================================
# DATA LOADING FUNCTION
# ============================================================================

def load_data():
    """
    Load and prepare customer churn dataset.
    
    Returns:
        pd.DataFrame: Cleaned and validated DataFrame
    """
    # Convert Path object to string for pandas
    input_path = str(INPUT_FILE)
    print(f"Loading data from: {input_path}")
    print(f"Base directory: {BASE_DIR.absolute()}")
    
    # Verify file exists
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Data file not found: {input_path}. Current directory: {os.getcwd()}")
    
    # Read CSV file
    df = pd.read_csv(input_path)
    
    # Convert string columns to numeric
    numeric_columns = ['age', 'tenure_months', 'monthly_charges', 
                       'total_charges', 'num_products', 'num_support_calls', 'churned']
    
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    print(f"  Loaded {len(df):,} rows, {len(df.columns)} columns")
    return df

# ============================================================================
# CHART GENERATION FUNCTIONS
# ============================================================================

def create_customer_distribution(df):
    """
    Chart 1: Customer Churn Overview (Pie chart)
    """
    print("  Creating: 01_customer_distribution.png")
    
    # Group by churned field
    churn_counts = df['churned'].value_counts()
    labels = ['Retained', 'Churned']
    sizes = [churn_counts.get(0, 0), churn_counts.get(1, 0)]
    colors_pie = [colors['success'], colors['danger']]
    explode = (0, 0.1)  # Explode churned segment
    
    # Calculate percentages
    total = sum(sizes)
    percentages = [f'{s/total*100:.1f}%' for s in sizes]
    
    # Create pie chart
    fig, ax = plt.subplots(figsize=(10, 10))
    wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors_pie,
                                       autopct='%1.1f%%', explode=explode,
                                       startangle=90, textprops={'fontsize': 12})
    
    # Styling
    ax.set_title('Customer Churn Overview', fontsize=16, fontweight='bold', pad=20)
    ax.text(0, -1.3, '1,000 Total Customers', ha='center', fontsize=12, style='italic')
    
    # Save
    output_path = OUTPUT_DIR / '01_customer_distribution.png'
    plt.tight_layout()
    plt.savefig(output_path, dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"    [OK] Saved: {output_path.name}")


def create_churn_by_contract(df):
    """
    Chart 2: Churn Rate by Contract Type (Vertical bar chart)
    """
    print("  Creating: 02_churn_by_contract.png")
    
    # Group by contract_type and calculate churn rate
    contract_churn = df.groupby('contract_type')['churned'].agg(['mean', 'count'])
    contract_churn['churn_rate'] = contract_churn['mean'] * 100
    
    # Order: Month-to-month, One year, Two year
    order = ['Month-to-month', 'One year', 'Two year']
    contract_churn = contract_churn.reindex(order)
    
    # Colors for each contract type
    bar_colors = [colors['danger'], colors['warning'], colors['success']]
    
    # Create bar chart
    fig, ax = plt.subplots(figsize=(12, 8))
    bars = ax.bar(range(len(contract_churn)), contract_churn['churn_rate'], 
                  color=bar_colors)
    
    # Add percentage labels on top of bars
    for i, (bar, rate) in enumerate(zip(bars, contract_churn['churn_rate'])):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{rate:.1f}%', ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    # Add customer count labels below x-axis
    for i, count in enumerate(contract_churn['count']):
        ax.text(i, -2, f'n={count}', ha='center', va='top', fontsize=10)
    
    # Styling
    ax.set_title('Churn Rate by Contract Type', fontsize=16, fontweight='bold', pad=20)
    ax.text(0.5, -0.15, 'Month-to-month contracts show higher churn', 
            ha='center', transform=ax.transAxes, fontsize=12, style='italic')
    ax.set_xlabel('Contract Type', fontsize=12)
    ax.set_ylabel('Churn Rate (%)', fontsize=12)
    ax.set_xticks(range(len(contract_churn)))
    ax.set_xticklabels(contract_churn.index, fontsize=11)
    ax.set_ylim(0, max(contract_churn['churn_rate']) * 1.2)
    ax.grid(axis='y', alpha=0.3, linestyle='--', color='#EEEEEE')
    ax.set_axisbelow(True)
    
    # Save
    output_path = OUTPUT_DIR / '02_churn_by_contract.png'
    plt.tight_layout()
    plt.savefig(output_path, dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"    [OK] Saved: {output_path.name}")


def create_churn_by_payment(df):
    """
    Chart 3: Churn Rate by Payment Method (Horizontal bar chart)
    """
    print("  Creating: 03_churn_by_payment.png")
    
    # Group by payment_method and calculate churn rate
    payment_churn = df.groupby('payment_method')['churned'].agg(['mean', 'count'])
    payment_churn['churn_rate'] = payment_churn['mean'] * 100
    
    # Sort by churn rate descending
    payment_churn = payment_churn.sort_values('churn_rate', ascending=True)
    
    # Create color gradient from red to green
    n = len(payment_churn)
    color_list = [colors['danger'] if i < n/2 else colors['success'] 
                  for i in range(n)]
    
    # Create horizontal bar chart
    fig, ax = plt.subplots(figsize=(12, 8))
    bars = ax.barh(range(len(payment_churn)), payment_churn['churn_rate'], 
                   color=color_list)
    
    # Add percentage labels at end of each bar
    for i, (bar, rate) in enumerate(zip(bars, payment_churn['churn_rate'])):
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height()/2.,
                f' {rate:.1f}%', ha='left', va='center', fontsize=11, fontweight='bold')
    
    # Styling
    ax.set_title('Churn Rate by Payment Method', fontsize=16, fontweight='bold', pad=20)
    ax.text(0.5, -0.1, 'Manual payment methods show higher churn', 
            ha='center', transform=ax.transAxes, fontsize=12, style='italic')
    ax.set_xlabel('Churn Rate (%)', fontsize=12)
    ax.set_ylabel('Payment Method', fontsize=12)
    ax.set_yticks(range(len(payment_churn)))
    ax.set_yticklabels(payment_churn.index, fontsize=11)
    ax.set_xlim(0, max(payment_churn['churn_rate']) * 1.2)
    ax.grid(axis='x', alpha=0.3, linestyle='--', color='#EEEEEE')
    ax.set_axisbelow(True)
    
    # Save
    output_path = OUTPUT_DIR / '03_churn_by_payment.png'
    plt.tight_layout()
    plt.savefig(output_path, dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"    [OK] Saved: {output_path.name}")


def create_churn_by_tenure(df):
    """
    Chart 4: Churn Rate by Tenure Group (Line chart with markers)
    """
    print("  Creating: 04_churn_by_tenure.png")
    
    # Create tenure bins
    df['tenure_group'] = pd.cut(df['tenure_months'], 
                                bins=[0, 12, 24, 36, 72], 
                                labels=['0-12', '13-24', '25-36', '37-72'])
    
    # Group by tenure bins and calculate churn rate
    tenure_churn = df.groupby('tenure_group')['churned'].agg(['mean', 'count'])
    tenure_churn['churn_rate'] = tenure_churn['mean'] * 100
    
    # Create line chart
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Plot line with markers
    line = ax.plot(range(len(tenure_churn)), tenure_churn['churn_rate'],
                   marker='o', markersize=12, linewidth=2.5, 
                   color=colors['primary'], label='Churn Rate')
    
    # Highlight 0-12 months group
    ax.plot(0, tenure_churn.iloc[0]['churn_rate'], 
            marker='o', markersize=18, color=colors['danger'], 
            markeredgewidth=3, markeredgecolor='black', zorder=5)
    
    # Add percentage labels above each point
    for i, rate in enumerate(tenure_churn['churn_rate']):
        ax.text(i, rate + 1, f'{rate:.1f}%', ha='center', va='bottom', 
                fontsize=11, fontweight='bold')
    
    # Styling
    ax.set_title('Churn Rate by Customer Tenure', fontsize=16, fontweight='bold', pad=20)
    ax.text(0.5, -0.1, 'First year is critical period', 
            ha='center', transform=ax.transAxes, fontsize=12, style='italic')
    ax.set_xlabel('Tenure Group (months)', fontsize=12)
    ax.set_ylabel('Churn Rate (%)', fontsize=12)
    ax.set_xticks(range(len(tenure_churn)))
    ax.set_xticklabels(tenure_churn.index, fontsize=11)
    ax.set_ylim(0, max(tenure_churn['churn_rate']) * 1.3)
    ax.grid(axis='y', alpha=0.3, linestyle='--', color='#EEEEEE')
    ax.set_axisbelow(True)
    
    # Save
    output_path = OUTPUT_DIR / '04_churn_by_tenure.png'
    plt.tight_layout()
    plt.savefig(output_path, dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"    [OK] Saved: {output_path.name}")


def create_churn_by_products(df):
    """
    Chart 5: Churn Rate by Number of Products (Column chart)
    """
    print("  Creating: 05_churn_by_products.png")
    
    # Group by num_products and calculate churn rate
    products_churn = df.groupby('num_products')['churned'].agg(['mean', 'count'])
    products_churn['churn_rate'] = products_churn['mean'] * 100
    products_churn = products_churn.sort_index()
    
    # Create column chart
    fig, ax = plt.subplots(figsize=(12, 8))
    bars = ax.bar(products_churn.index, products_churn['churn_rate'], 
                  color=colors['secondary'])
    
    # Add percentage labels on bars
    for bar, rate in zip(bars, products_churn['churn_rate']):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{rate:.1f}%', ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    # Add customer count labels below x-axis
    for prod, count in products_churn['count'].items():
        ax.text(prod, -1, f'n={count}', ha='center', va='top', fontsize=10)
    
    # Styling
    ax.set_title('Churn Rate by Product Count', fontsize=16, fontweight='bold', pad=20)
    ax.text(0.5, -0.1, '3-4 products show lowest churn', 
            ha='center', transform=ax.transAxes, fontsize=12, style='italic')
    ax.set_xlabel('Number of Products', fontsize=12)
    ax.set_ylabel('Churn Rate (%)', fontsize=12)
    ax.set_ylim(0, max(products_churn['churn_rate']) * 1.2)
    ax.grid(axis='y', alpha=0.3, linestyle='--', color='#EEEEEE')
    ax.set_axisbelow(True)
    
    # Save
    output_path = OUTPUT_DIR / '05_churn_by_products.png'
    plt.tight_layout()
    plt.savefig(output_path, dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"    [OK] Saved: {output_path.name}")


def create_age_distribution(df):
    """
    Chart 6: Age Distribution Comparison (Overlapping histogram)
    """
    print("  Creating: 06_age_distribution.png")
    
    # Filter by churned status
    retained = df[df['churned'] == 0]['age']
    churned = df[df['churned'] == 1]['age']
    
    # Create age bins
    bins = [18, 30, 40, 50, 60, 70, 80]
    
    # Create overlapping histograms
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.hist(retained, bins=bins, alpha=0.7, color=colors['success'], 
            label='Retained', edgecolor='black', linewidth=1.5)
    ax.hist(churned, bins=bins, alpha=0.7, color=colors['danger'], 
            label='Churned', edgecolor='black', linewidth=1.5)
    
    # Styling
    ax.set_title('Age Distribution: Churned vs Retained', fontsize=16, fontweight='bold', pad=20)
    ax.text(0.5, -0.1, 'Comparison of customer age patterns', 
            ha='center', transform=ax.transAxes, fontsize=12, style='italic')
    ax.set_xlabel('Age', fontsize=12)
    ax.set_ylabel('Customer Count', fontsize=12)
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(axis='y', alpha=0.3, linestyle='--', color='#EEEEEE')
    ax.set_axisbelow(True)
    
    # Save
    output_path = OUTPUT_DIR / '06_age_distribution.png'
    plt.tight_layout()
    plt.savefig(output_path, dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"    [OK] Saved: {output_path.name}")


def create_charges_distribution(df):
    """
    Chart 7: Monthly Charges Distribution (Box plot)
    """
    print("  Creating: 07_charges_distribution.png")
    
    # Prepare data for box plot
    retained_charges = df[df['churned'] == 0]['monthly_charges']
    churned_charges = df[df['churned'] == 1]['monthly_charges']
    
    # Create box plot
    fig, ax = plt.subplots(figsize=(12, 8))
    box_data = [retained_charges, churned_charges]
    bp = ax.boxplot(box_data, labels=['Retained', 'Churned'], 
                    patch_artist=True, widths=0.6)
    
    # Color the boxes
    for patch, color in zip(bp['boxes'], [colors['success'], colors['danger']]):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    # Styling
    ax.set_title('Monthly Charges Distribution', fontsize=16, fontweight='bold', pad=20)
    ax.text(0.5, -0.1, 'Comparison by churn status', 
            ha='center', transform=ax.transAxes, fontsize=12, style='italic')
    ax.set_xlabel('Churn Status', fontsize=12)
    ax.set_ylabel('Monthly Charges ($)', fontsize=12)
    ax.grid(axis='y', alpha=0.3, linestyle='--', color='#EEEEEE')
    ax.set_axisbelow(True)
    
    # Save
    output_path = OUTPUT_DIR / '07_charges_distribution.png'
    plt.tight_layout()
    plt.savefig(output_path, dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"    [OK] Saved: {output_path.name}")


def create_support_calls_churn(df):
    """
    Chart 8: Support Calls vs Churn (Stacked bar chart)
    """
    print("  Creating: 08_support_calls_churn.png")
    
    # Group by num_support_calls and churned, count customers
    support_churn = df.groupby(['num_support_calls', 'churned']).size().unstack(fill_value=0)
    support_churn.columns = ['Retained', 'Churned']
    
    # Create stacked bar chart
    fig, ax = plt.subplots(figsize=(12, 8))
    x = range(len(support_churn))
    width = 0.6
    
    bars1 = ax.bar(x, support_churn['Retained'], width, 
                   label='Retained', color=colors['success'], alpha=0.8)
    bars2 = ax.bar(x, support_churn['Churned'], width, 
                   bottom=support_churn['Retained'], 
                   label='Churned', color=colors['danger'], alpha=0.8)
    
    # Styling
    ax.set_title('Support Calls Distribution by Churn Status', fontsize=16, fontweight='bold', pad=20)
    ax.text(0.5, -0.1, 'Customer support interaction patterns', 
            ha='center', transform=ax.transAxes, fontsize=12, style='italic')
    ax.set_xlabel('Number of Support Calls', fontsize=12)
    ax.set_ylabel('Customer Count', fontsize=12)
    ax.set_xticks(x)
    ax.set_xticklabels(support_churn.index, fontsize=11)
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(axis='y', alpha=0.3, linestyle='--', color='#EEEEEE')
    ax.set_axisbelow(True)
    
    # Save
    output_path = OUTPUT_DIR / '08_support_calls_churn.png'
    plt.tight_layout()
    plt.savefig(output_path, dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"    [OK] Saved: {output_path.name}")


def create_dashboard(df):
    """
    Chart 9: Comprehensive Dashboard (2x2 subplot grid)
    """
    print("  Creating: 09_churn_dashboard.png")
    
    # Create 2x2 subplot grid
    fig = plt.figure(figsize=(16, 12))
    gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)
    
    # Subplot 1: Churn by Contract
    ax1 = fig.add_subplot(gs[0, 0])
    contract_churn = df.groupby('contract_type')['churned'].agg(['mean', 'count'])
    contract_churn['churn_rate'] = contract_churn['mean'] * 100
    order = ['Month-to-month', 'One year', 'Two year']
    contract_churn = contract_churn.reindex(order)
    bar_colors = [colors['danger'], colors['warning'], colors['success']]
    bars = ax1.bar(range(len(contract_churn)), contract_churn['churn_rate'], 
                   color=bar_colors)
    for i, (bar, rate) in enumerate(zip(bars, contract_churn['churn_rate'])):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{rate:.1f}%', ha='center', va='bottom', fontsize=10)
    ax1.set_title('Churn by Contract Type', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Contract Type', fontsize=11)
    ax1.set_ylabel('Churn Rate (%)', fontsize=11)
    ax1.set_xticks(range(len(contract_churn)))
    ax1.set_xticklabels(contract_churn.index, fontsize=10, rotation=15)
    ax1.grid(axis='y', alpha=0.3)
    
    # Subplot 2: Churn by Tenure
    ax2 = fig.add_subplot(gs[0, 1])
    df['tenure_group'] = pd.cut(df['tenure_months'], bins=[0, 12, 24, 36, 72],
                                labels=['0-12', '13-24', '25-36', '37-72'])
    tenure_churn = df.groupby('tenure_group')['churned'].agg(['mean', 'count'])
    tenure_churn['churn_rate'] = tenure_churn['mean'] * 100
    ax2.plot(range(len(tenure_churn)), tenure_churn['churn_rate'],
             marker='o', markersize=10, linewidth=2, color=colors['primary'])
    for i, rate in enumerate(tenure_churn['churn_rate']):
        ax2.text(i, rate + 1, f'{rate:.1f}%', ha='center', va='bottom', fontsize=10)
    ax2.set_title('Churn by Tenure', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Tenure Group (months)', fontsize=11)
    ax2.set_ylabel('Churn Rate (%)', fontsize=11)
    ax2.set_xticks(range(len(tenure_churn)))
    ax2.set_xticklabels(tenure_churn.index, fontsize=10)
    ax2.grid(axis='y', alpha=0.3)
    
    # Subplot 3: Churn by Products
    ax3 = fig.add_subplot(gs[1, 0])
    products_churn = df.groupby('num_products')['churned'].agg(['mean', 'count'])
    products_churn['churn_rate'] = products_churn['mean'] * 100
    products_churn = products_churn.sort_index()
    bars = ax3.bar(products_churn.index, products_churn['churn_rate'], 
                   color=colors['secondary'])
    for bar, rate in zip(bars, products_churn['churn_rate']):
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height,
                f'{rate:.1f}%', ha='center', va='bottom', fontsize=10)
    ax3.set_title('Churn by Product Count', fontsize=14, fontweight='bold')
    ax3.set_xlabel('Number of Products', fontsize=11)
    ax3.set_ylabel('Churn Rate (%)', fontsize=11)
    ax3.grid(axis='y', alpha=0.3)
    
    # Subplot 4: Key metrics table
    ax4 = fig.add_subplot(gs[1, 1])
    ax4.axis('off')
    total_customers = len(df)
    churned_count = len(df[df['churned'] == 1])
    retained_count = len(df[df['churned'] == 0])
    churn_rate = (churned_count / total_customers) * 100
    
    metrics_text = f"""
    Key Metrics
    
    Total Customers: {total_customers:,}
    Churned: {churned_count:,} ({churn_rate:.1f}%)
    Retained: {retained_count:,} ({100-churn_rate:.1f}%)
    
    Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    """
    ax4.text(0.5, 0.5, metrics_text, ha='center', va='center',
             fontsize=12, family='monospace',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    # Main title
    fig.suptitle('Customer Churn Analysis Dashboard', fontsize=18, fontweight='bold', y=0.98)
    
    # Save
    output_path = OUTPUT_DIR / '09_churn_dashboard.png'
    plt.savefig(output_path, dpi=DPI, bbox_inches='tight')
    plt.close()
    print(f"    [OK] Saved: {output_path.name}")

# ============================================================================
# MAIN EXECUTION FUNCTION
# ============================================================================

def main():
    """
    Main execution function.
    """
    print("=" * 70)
    print(" CUSTOMER CHURN VISUALIZATION TASK")
    print("=" * 70)
    
    # Load data
    print("\n[Step 1/2] Loading data...")
    try:
        df = load_data()
    except Exception as e:
        print(f"  Error loading data: {e}")
        sys.exit(1)
    
    # Create all charts
    print("\n[Step 2/2] Creating visualizations...")
    try:
        create_customer_distribution(df)
        create_churn_by_contract(df)
        create_churn_by_payment(df)
        create_churn_by_tenure(df)
        create_churn_by_products(df)
        create_age_distribution(df)
        create_charges_distribution(df)
        create_support_calls_churn(df)
        create_dashboard(df)
    except Exception as e:
        print(f"  Error creating visualizations: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    # Summary
    print("\n" + "=" * 70)
    print("All 9 visualizations created successfully!")
    print(f"Generated 9 chart files in {OUTPUT_DIR}")
    print("=" * 70)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nTask interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\nFatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
