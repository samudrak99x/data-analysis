#!/usr/bin/env python3
"""
Customer Churn Visualization - Complete Implementation

Generates 10 professional charts for customer churn analysis based on
specification from customer-churn-chart-spec.md.

Charts Generated:
1. Overall Churn Distribution (Pie Chart)
2. Churn Rate by Contract Type (Bar Chart)
3. Churn Rate by Support Calls (Bar Chart with gradient)
4. Customer Status by Payment Method (Grouped Bar Chart)
5. Churn Rate by Product Count (Bar Chart)
6. Tenure Distribution Comparison (Histogram)
7. Age Distribution Comparison (Box Plot)
8. Monthly Charges Distribution (Violin Plot)
9. Contract × Product Interaction (Stacked Bar Chart)
10. Executive Dashboard (2×2 Multi-Panel)

Usage:
    python task.py

Requirements:
    - pandas
    - matplotlib
    - seaborn
    - numpy

Author: DataJames (@data-dev)
Date: January 2, 2026
Version: 1.0
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
CHURN_RED = '#e74c3c'      # For churned customers
RETAIN_GREEN = '#2ecc71'   # For retained customers
NEUTRAL_BLUE = '#3498db'   # For neutral/info
WARNING_ORANGE = '#f39c12' # For warnings

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
    
    Performs comprehensive validation including:
    - Column existence verification
    - Missing value detection
    - Data type conversion
    - Basic data quality checks
    
    Args:
        filepath (str): Path to CSV file containing customer churn data
        
    Returns:
        pd.DataFrame: Validated and type-converted customer churn DataFrame
        
    Raises:
        FileNotFoundError: If the specified file doesn't exist
        ValueError: If required columns are missing from the dataset
    """
    # Task 2.2: Read CSV file
    df = pd.read_csv(filepath)
    
    # Task 2.3: Verify expected columns exist
    required_cols = [
        'customer_id', 'age', 'tenure_months', 'monthly_charges',
        'total_charges', 'num_products', 'num_support_calls',
        'contract_type', 'payment_method', 'churned'
    ]
    
    missing_cols = set(required_cols) - set(df.columns)
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")
    
    # Task 2.4: Check for missing values
    null_counts = df[required_cols].isnull().sum()
    if null_counts.any():
        print(f"Warning: Found missing values:\n{null_counts[null_counts > 0]}")
    
    # Task 2.5: Convert data types for proper analysis
    df['churned'] = df['churned'].astype(int)
    df['num_products'] = df['num_products'].astype(int)
    df['num_support_calls'] = df['num_support_calls'].astype(int)
    df['age'] = df['age'].astype(int)
    df['tenure_months'] = df['tenure_months'].astype(int)
    
    # Task 2.6: Print data summary
    print(f"\n[OK] Task 2: Data loaded successfully")
    print(f"  - Shape: {df.shape[0]} rows x {df.shape[1]} columns")
    print(f"  - Churn Rate: {df['churned'].mean()*100:.1f}%")
    print(f"  - Tenure Range: {df['tenure_months'].min()}-{df['tenure_months'].max()} months")
    
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
    
    Shows the proportion of retained vs churned customers with
    percentage labels and color coding.
    
    Args:
        df (pd.DataFrame): Customer churn DataFrame
        
    Returns:
        str: Path to saved chart file
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
    
    # Save with sequential numbering
    output_path = OUTPUT_DIR / '01_churn_distribution_pie.png'
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()  # Free memory
    
    print(f"  [OK] Saved: {output_path}")
    return str(output_path)


# Task 3.2: Churn by Contract Type (Bar Chart)
def create_contract_churn_chart(df: pd.DataFrame) -> str:
    """
    Generate churn rate by contract type bar chart.
    
    Compares churn rates across different contract types with
    red gradient coloring based on churn intensity.
    
    Args:
        df (pd.DataFrame): Customer churn DataFrame
        
    Returns:
        str: Path to saved chart file
    """
    # Calculate churn rates by contract type
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
        color=[CHURN_RED, '#e67e73', '#f1948a']  # Red gradient
    )
    
    # Add value labels on bars
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
    
    Shows correlation between support call frequency and churn,
    with yellow-to-red gradient and high-risk zone highlighting.
    
    Args:
        df (pd.DataFrame): Customer churn DataFrame
        
    Returns:
        str: Path to saved chart file
    """
    # Calculate churn rates by support calls
    support_churn = df.groupby('num_support_calls').agg({
        'churned': ['sum', 'count']
    })
    support_churn.columns = ['churned', 'total']
    support_churn['churn_rate'] = (support_churn['churned'] / support_churn['total']) * 100
    
    # Create bar chart with yellow-to-red gradient
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
    
    Compares retained vs churned customers across different
    payment methods using side-by-side bars.
    
    Args:
        df (pd.DataFrame): Customer churn DataFrame
        
    Returns:
        str: Path to saved chart file
    """
    # Calculate counts by payment method and churn status
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
    
    Shows how product ownership affects retention using
    green gradient (lower churn = darker green).
    
    Args:
        df (pd.DataFrame): Customer churn DataFrame
        
    Returns:
        str: Path to saved chart file
    """
    # Calculate churn rates by product count
    products_churn = df.groupby('num_products').agg({
        'churned': ['sum', 'count']
    })
    products_churn.columns = ['churned', 'total']
    products_churn['churn_rate'] = (products_churn['churned'] / products_churn['total']) * 100
    
    # Create bar chart with green gradient
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


# Task 3.6: Tenure Distribution (Histogram)
def create_tenure_histogram(df: pd.DataFrame) -> str:
    """
    Generate tenure distribution comparison histogram.
    
    Overlapping histograms showing tenure patterns for
    churned vs retained customers.
    
    Args:
        df (pd.DataFrame): Customer churn DataFrame
        
    Returns:
        str: Path to saved chart file
    """
    # Separate data by churn status
    retained = df[df['churned'] == 0]['tenure_months']
    churned = df[df['churned'] == 1]['tenure_months']
    
    # Create overlapping histograms
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.hist(retained, bins=8, alpha=0.6, label='Retained', color=NEUTRAL_BLUE, edgecolor='black')
    ax.hist(churned, bins=8, alpha=0.6, label='Churned', color=CHURN_RED, edgecolor='black')
    
    # Styling
    ax.set_xlabel('Tenure (months)')
    ax.set_ylabel('Customer Count')
    ax.set_title('Tenure Distribution: Churned vs Retained Customers')
    ax.legend(loc='upper right')
    ax.grid(axis='y', alpha=0.3)
    
    # Save
    output_path = OUTPUT_DIR / '06_tenure_distribution.png'
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    
    print(f"  [OK] Saved: {output_path}")
    return str(output_path)


# Task 3.7: Age Distribution (Box Plot)
def create_age_boxplot(df: pd.DataFrame) -> str:
    """
    Generate age distribution box plot comparison.
    
    Side-by-side box plots showing age patterns with
    median lines, quartiles, and outliers.
    
    Args:
        df (pd.DataFrame): Customer churn DataFrame
        
    Returns:
        str: Path to saved chart file
    """
    # Prepare data
    df_plot = df.copy()
    df_plot['Status'] = df_plot['churned'].map({0: 'Retained', 1: 'Churned'})
    
    # Create box plot
    fig, ax = plt.subplots(figsize=(7, 5))
    bp = ax.boxplot(
        [df[df['churned'] == 0]['age'], df[df['churned'] == 1]['age']],
        labels=['Retained', 'Churned'],
        patch_artist=True,
        medianprops=dict(color='black', linewidth=2)
    )
    
    # Color boxes
    bp['boxes'][0].set_facecolor(RETAIN_GREEN)
    bp['boxes'][1].set_facecolor(CHURN_RED)
    
    # Styling
    ax.set_xlabel('Customer Status')
    ax.set_ylabel('Age')
    ax.set_title('Age Distribution: Churned vs Retained')
    ax.grid(axis='y', alpha=0.3)
    
    # Save
    output_path = OUTPUT_DIR / '07_age_boxplot.png'
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    
    print(f"  [OK] Saved: {output_path}")
    return str(output_path)


# Task 3.8: Monthly Charges (Violin Plot)
def create_charges_violin(df: pd.DataFrame) -> str:
    """
    Generate monthly charges violin plot comparison.
    
    Violin plots showing distribution density of monthly
    charges with median lines.
    
    Args:
        df (pd.DataFrame): Customer churn DataFrame
        
    Returns:
        str: Path to saved chart file
    """
    # Prepare data
    df_plot = df.copy()
    df_plot['Status'] = df_plot['churned'].map({0: 'Retained', 1: 'Churned'})
    
    # Create violin plot
    fig, ax = plt.subplots(figsize=(7, 5))
    parts = ax.violinplot(
        [df[df['churned'] == 0]['monthly_charges'], df[df['churned'] == 1]['monthly_charges']],
        positions=[0, 1],
        showmeans=True,
        showmedians=True
    )
    
    # Color violins
    parts['bodies'][0].set_facecolor(RETAIN_GREEN)
    parts['bodies'][0].set_alpha(0.7)
    parts['bodies'][1].set_facecolor(CHURN_RED)
    parts['bodies'][1].set_alpha(0.7)
    
    # Styling
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['Retained', 'Churned'])
    ax.set_xlabel('Customer Status')
    ax.set_ylabel('Monthly Charges ($)')
    ax.set_title('Monthly Charges Distribution: Churned vs Retained')
    ax.grid(axis='y', alpha=0.3)
    
    # Save
    output_path = OUTPUT_DIR / '08_charges_violin.png'
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    
    print(f"  [OK] Saved: {output_path}")
    return str(output_path)


# Task 3.9: Contract × Product Interaction (Stacked Bar)
def create_contract_product_stack(df: pd.DataFrame) -> str:
    """
    Generate contract type × product count stacked bar chart.
    
    Shows interaction between contract type and product count
    using stacked bars with viridis colormap.
    
    Args:
        df (pd.DataFrame): Customer churn DataFrame
        
    Returns:
        str: Path to saved chart file
    """
    # Calculate counts by contract type and product count
    contract_product = df.groupby(['contract_type', 'num_products']).size().unstack(fill_value=0)
    
    # Create stacked bar chart
    fig, ax = plt.subplots(figsize=(9, 6))
    contract_product.plot(kind='bar', stacked=True, ax=ax, 
                         colormap='viridis', edgecolor='black', linewidth=0.5)
    
    # Styling
    ax.set_xlabel('Contract Type')
    ax.set_ylabel('Customer Count')
    ax.set_title('Customer Segmentation: Contract Type × Product Count')
    ax.set_xticklabels(contract_product.index, rotation=15, ha='right')
    ax.legend(title='Products', bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.grid(axis='y', alpha=0.3)
    
    # Save
    output_path = OUTPUT_DIR / '09_contract_product_stack.png'
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    
    print(f"  [OK] Saved: {output_path}")
    return str(output_path)


# Task 3.10: Dashboard Overview (Multi-Panel)
def create_dashboard(df: pd.DataFrame) -> str:
    """
    Generate executive dashboard with 2×2 grid of charts.
    
    Combines key visualizations into a single dashboard:
    - Churn pie chart
    - Contract type churn rates
    - Support calls churn rates
    - Product count churn rates
    
    Args:
        df (pd.DataFrame): Customer churn DataFrame
        
    Returns:
        str: Path to saved chart file
    """
    # Create 2×2 subplot grid
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 9))
    fig.suptitle('Customer Churn Analysis Dashboard', fontsize=16, fontweight='bold')
    
    # Top-left: Churn pie chart
    churn_counts = df['churned'].value_counts().sort_index()
    ax1.pie(churn_counts, labels=['Retained', 'Churned'], 
            colors=[RETAIN_GREEN, CHURN_RED], autopct='%1.1f%%', startangle=90)
    ax1.set_title('Overall Churn Distribution')
    
    # Top-right: Contract type churn rates
    contract_churn = df.groupby('contract_type').agg({'churned': ['sum', 'count']})
    contract_churn.columns = ['churned', 'total']
    contract_churn['rate'] = (contract_churn['churned'] / contract_churn['total']) * 100
    contract_churn = contract_churn.sort_values('rate', ascending=False)
    ax2.bar(range(len(contract_churn)), contract_churn['rate'], color=CHURN_RED)
    ax2.set_xticks(range(len(contract_churn)))
    ax2.set_xticklabels(contract_churn.index, rotation=15, ha='right')
    ax2.set_ylabel('Churn Rate (%)')
    ax2.set_title('Churn by Contract Type')
    ax2.grid(axis='y', alpha=0.3)
    
    # Bottom-left: Support calls churn rates
    support_churn = df.groupby('num_support_calls').agg({'churned': ['sum', 'count']})
    support_churn.columns = ['churned', 'total']
    support_churn['rate'] = (support_churn['churned'] / support_churn['total']) * 100
    colors_grad = ['#f39c12', '#e67e22', '#d35400', '#c0392b', '#a93226']
    ax3.bar(support_churn.index, support_churn['rate'], color=colors_grad[:len(support_churn)])
    ax3.set_xlabel('Support Calls')
    ax3.set_ylabel('Churn Rate (%)')
    ax3.set_title('Churn by Support Calls')
    ax3.grid(axis='y', alpha=0.3)
    
    # Bottom-right: Product count churn rates
    products_churn = df.groupby('num_products').agg({'churned': ['sum', 'count']})
    products_churn.columns = ['churned', 'total']
    products_churn['rate'] = (products_churn['churned'] / products_churn['total']) * 100
    colors_green = ['#27ae60', '#2ecc71', '#52be80', '#7dcea0', '#a9dfbf']
    ax4.bar(products_churn.index, products_churn['rate'], color=colors_green[:len(products_churn)])
    ax4.set_xlabel('Number of Products')
    ax4.set_ylabel('Churn Rate (%)')
    ax4.set_title('Churn by Product Count')
    ax4.grid(axis='y', alpha=0.3)
    
    # Save
    output_path = OUTPUT_DIR / '10_dashboard_overview.png'
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    
    print(f"  [OK] Saved: {output_path}")
    return str(output_path)


print("[OK] Task 3: All 10 chart generation functions complete")


# ============================================================================
# TASK 4: MAIN EXECUTION FUNCTION
# ============================================================================

def main():
    """
    Main execution function - orchestrates all chart generation.
    
    Coordinates the complete workflow:
    1. Loads and validates data
    2. Generates all 10 charts sequentially
    3. Tracks success/failure for each chart
    4. Provides comprehensive summary
    
    Returns:
        int: Number of charts successfully created (0-10)
    """
    # Task 4.2: Print start message
    print("\n" + "="*70)
    print("Customer Churn Chart Generation")
    print("="*70)
    print(f"Output Directory: {OUTPUT_DIR}")
    print(f"Data Source: {DATA_PATH}")
    print("="*70 + "\n")
    
    try:
        # Task 4.3: Load data
        df = load_data(DATA_PATH)
        
        # Task 4.4: Generate all charts
        print("\n[TASK 3] Generating Charts...\n")
        charts_created = []
        
        # Task 4.5: Track successful chart creation
        chart_functions = [
            ("Chart 1: Churn Distribution Pie", create_churn_pie_chart),
            ("Chart 2: Churn by Contract Type", create_contract_churn_chart),
            ("Chart 3: Churn by Support Calls", create_support_calls_chart),
            ("Chart 4: Churn by Payment Method", create_payment_method_chart),
            ("Chart 5: Churn by Products", create_products_chart),
            ("Chart 6: Tenure Distribution", create_tenure_histogram),
            ("Chart 7: Age Box Plot", create_age_boxplot),
            ("Chart 8: Monthly Charges Violin", create_charges_violin),
            ("Chart 9: Contract × Product Stack", create_contract_product_stack),
            ("Chart 10: Dashboard Overview", create_dashboard),
        ]
        
        # Generate each chart with individual error handling
        for name, func in chart_functions:
            try:
                print(f"\nGenerating {name}...")
                path = func(df)
                charts_created.append(path)
            except Exception as e:
                print(f"  [ERROR] Failed to create {name}: {e}")
        
        # Task 4.6: Print summary
        print("\n" + "="*70)
        print(f"[OK] Task 4: Chart Generation Complete!")
        print(f"  - Charts Created: {len(charts_created)}/10")
        print(f"  - Output Location: {OUTPUT_DIR.absolute()}")
        print(f"  - All charts saved with 300 DPI quality")
        print("="*70 + "\n")
        
        return len(charts_created)
        
    except Exception as e:
        # Task 4.7: Error handling
        print(f"\n[ERROR] Chart generation failed: {e}")
        import traceback
        traceback.print_exc()
        return 0


print("[OK] Task 4: Main execution function defined")


# ============================================================================
# TASK 5: QUALITY ASSURANCE & ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    """
    Entry point for script execution.
    
    Executes main function and returns appropriate exit code:
    - 0: Success (all 10 charts created)
    - 1: Failure (less than 10 charts created)
    """
    # Execute main function
    num_charts = main()
    
    # Exit with appropriate code for automation
    exit(0 if num_charts == 10 else 1)


print("[OK] Task 5: Quality assurance complete")
print("[OK] All tasks complete - ready for execution!")
