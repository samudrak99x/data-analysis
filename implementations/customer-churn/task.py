"""
Customer Churn Visualization Analysis

This script generates 10 comprehensive visualizations to analyze customer churn patterns
based on demographics, service usage, contract types, and financial metrics.

Dataset: customer_churn.csv (1,000 customers, 10 fields)
Output: 10 PNG charts showing churn analysis from multiple angles

Author: DataJames (BI & Visualization Developer)
Date: 2026-01-02
"""

# ============================================================================
# SECTION 1: IMPORTS & CONFIGURATION
# ============================================================================

from pathlib import Path
import sys

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================================
# SECTION 2: CONSTANTS & CONFIGURATION
# ============================================================================

# Color scheme constants
CHURN_RED = '#e74c3c'
RETAIN_GREEN = '#2ecc71'
NEUTRAL_BLUE = '#3498db'
WARNING_ORANGE = '#f39c12'
NEUTRAL_GRAY = '#95a5a6'

# Color gradients
YELLOW_TO_RED = ['#f1c40f', '#e67e22', '#f39c12', '#e74c3c', '#c0392b']

# Output configuration
OUTPUT_DIR = Path('outputs')
OUTPUT_DIR.mkdir(exist_ok=True)

# Visualization defaults
DEFAULT_DPI = 100
DEFAULT_FIGSIZE = (10, 6)
SMALL_FIGSIZE = (8, 5)
LARGE_FIGSIZE = (14, 10)

# Matplotlib style configuration
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

print("=" * 70)
print(" CUSTOMER CHURN VISUALIZATION ANALYSIS")
print("=" * 70)
print()

# ============================================================================
# SECTION 3: DATA LOADING & VALIDATION
# ============================================================================

def load_data(filepath: str) -> pd.DataFrame:
    """
    Load and validate customer churn dataset.
    
    Args:
        filepath: Path to the CSV file
        
    Returns:
        Validated pandas DataFrame with proper data types
        
    Raises:
        FileNotFoundError: If the dataset file doesn't exist
        ValueError: If required columns are missing
    """
    print("[Task 2] Loading and validating data...")
    
    # Check file exists
    data_path = Path(filepath)
    if not data_path.exists():
        raise FileNotFoundError(f"Data file not found: {filepath}")
    
    # Load CSV
    try:
        df = pd.read_csv(data_path)
    except Exception as e:
        raise ValueError(f"Error reading CSV file: {e}")
    
    # Validate non-empty
    if df.empty:
        raise ValueError("Dataset contains no rows")
    
    # Define expected columns
    expected_columns = [
        'customer_id', 'age', 'tenure_months', 'monthly_charges',
        'total_charges', 'num_products', 'num_support_calls',
        'contract_type', 'payment_method', 'churned'
    ]
    
    # Check for missing columns
    missing_cols = set(expected_columns) - set(df.columns)
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")
    
    # Data type conversions
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df['tenure_months'] = pd.to_numeric(df['tenure_months'], errors='coerce')
    df['monthly_charges'] = pd.to_numeric(df['monthly_charges'], errors='coerce')
    df['total_charges'] = pd.to_numeric(df['total_charges'], errors='coerce')
    df['num_products'] = pd.to_numeric(df['num_products'], errors='coerce')
    df['num_support_calls'] = pd.to_numeric(df['num_support_calls'], errors='coerce')
    df['churned'] = pd.to_numeric(df['churned'], errors='coerce')
    
    # Print summary
    print(f"  ✓ Loaded {len(df):,} rows × {len(df.columns)} columns")
    print(f"  ✓ Churn Rate: {df['churned'].mean()*100:.1f}%")
    print()
    
    return df

# ============================================================================
# SECTION 4: VISUALIZATION FUNCTIONS
# ============================================================================

def create_churn_pie(df: pd.DataFrame) -> None:
    """Create pie chart showing overall churn distribution."""
    print("  Creating: 01_churn_distribution_pie.png")
    
    # Data preparation
    churn_counts = df['churned'].value_counts().sort_index()
    labels = ['Retained', 'Churned']
    colors = [RETAIN_GREEN, CHURN_RED]
    
    # Create figure
    fig, ax = plt.subplots(figsize=SMALL_FIGSIZE)
    
    # Create pie chart
    ax.pie(
        churn_counts.values,
        labels=labels,
        colors=colors,
        autopct='%1.1f%%',
        startangle=90
    )
    
    # Styling
    ax.set_title('Customer Churn Distribution', fontsize=14, fontweight='bold')
    
    # Save
    output_path = OUTPUT_DIR / '01_churn_distribution_pie.png'
    plt.tight_layout()
    plt.savefig(output_path, dpi=DEFAULT_DPI, bbox_inches='tight')
    plt.close()
    
    print(f"    [OK] Saved: {output_path.name}")


def create_churn_by_contract(df: pd.DataFrame) -> None:
    """Create bar chart showing churn rate by contract type."""
    print("  Creating: 02_churn_by_contract.png")
    
    # Data preparation
    contract_churn = df.groupby('contract_type').agg({
        'churned': ['sum', 'count']
    })
    contract_churn.columns = ['churned', 'total']
    contract_churn['churn_rate'] = (contract_churn['churned'] / contract_churn['total']) * 100
    contract_churn = contract_churn.sort_values('churn_rate', ascending=False)
    
    # Create figure
    fig, ax = plt.subplots(figsize=DEFAULT_FIGSIZE)
    
    # Create bar chart
    bars = ax.bar(
        range(len(contract_churn)),
        contract_churn['churn_rate'],
        color=[CHURN_RED, '#ff6b6b', '#ff8787']
    )
    
    # Add value labels
    for i, (bar, value) in enumerate(zip(bars, contract_churn['churn_rate'])):
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width()/2., height,
            f'{height:.1f}%',
            ha='center', va='bottom', fontsize=10
        )
    
    # Styling
    ax.set_title('Churn Rate by Contract Type', fontsize=14, fontweight='bold')
    ax.set_xlabel('Contract Type', fontsize=11)
    ax.set_ylabel('Churn Rate (%)', fontsize=11)
    ax.set_xticks(range(len(contract_churn)))
    ax.set_xticklabels(contract_churn.index, rotation=15)
    ax.set_ylim(0, 100)
    plt.grid(axis='y', alpha=0.3)
    
    # Save
    output_path = OUTPUT_DIR / '02_churn_by_contract.png'
    plt.tight_layout()
    plt.savefig(output_path, dpi=DEFAULT_DPI, bbox_inches='tight')
    plt.close()
    
    print(f"    [OK] Saved: {output_path.name}")


def create_churn_by_support(df: pd.DataFrame) -> None:
    """Create bar chart showing churn rate by support calls."""
    print("  Creating: 03_churn_by_support_calls.png")
    
    # Data preparation
    support_churn = df.groupby('num_support_calls').agg({
        'churned': ['sum', 'count']
    })
    support_churn.columns = ['churned', 'total']
    support_churn['churn_rate'] = (support_churn['churned'] / support_churn['total']) * 100
    
    # Create figure
    fig, ax = plt.subplots(figsize=DEFAULT_FIGSIZE)
    
    # Create bar chart with gradient colors
    colors = YELLOW_TO_RED[:len(support_churn)]
    bars = ax.bar(
        support_churn.index,
        support_churn['churn_rate'],
        color=colors
    )
    
    # Add value labels
    for i, (bar, value) in enumerate(zip(bars, support_churn['churn_rate'])):
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width()/2., height,
            f'{height:.1f}%',
            ha='center', va='bottom', fontsize=10
        )
    
    # Styling
    ax.set_title('Churn Rate by Number of Support Calls', fontsize=14, fontweight='bold')
    ax.set_xlabel('Number of Support Calls', fontsize=11)
    ax.set_ylabel('Churn Rate (%)', fontsize=11)
    ax.set_ylim(0, max(support_churn['churn_rate']) * 1.2)
    plt.grid(axis='y', alpha=0.3)
    
    # Save
    output_path = OUTPUT_DIR / '03_churn_by_support_calls.png'
    plt.tight_layout()
    plt.savefig(output_path, dpi=DEFAULT_DPI, bbox_inches='tight')
    plt.close()
    
    print(f"    [OK] Saved: {output_path.name}")


def create_churn_by_payment(df: pd.DataFrame) -> None:
    """Create grouped bar chart of churn by payment method."""
    print("  Creating: 04_churn_by_payment.png")
    
    # Data preparation
    payment_churn = df.groupby(['payment_method', 'churned']).size().unstack(fill_value=0)
    payment_churn.columns = ['Retained', 'Churned']
    
    # Create figure
    fig, ax = plt.subplots(figsize=DEFAULT_FIGSIZE)
    
    # Create stacked bar chart
    x = np.arange(len(payment_churn))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, payment_churn['Retained'], width, 
                   label='Retained', color=RETAIN_GREEN)
    bars2 = ax.bar(x + width/2, payment_churn['Churned'], width,
                   label='Churned', color=CHURN_RED)
    
    # Styling
    ax.set_title('Customer Status by Payment Method', fontsize=14, fontweight='bold')
    ax.set_xlabel('Payment Method', fontsize=11)
    ax.set_ylabel('Customer Count', fontsize=11)
    ax.set_xticks(x)
    ax.set_xticklabels(payment_churn.index, rotation=15)
    ax.legend(loc='upper right')
    plt.grid(axis='y', alpha=0.3)
    
    # Save
    output_path = OUTPUT_DIR / '04_churn_by_payment.png'
    plt.tight_layout()
    plt.savefig(output_path, dpi=DEFAULT_DPI, bbox_inches='tight')
    plt.close()
    
    print(f"    [OK] Saved: {output_path.name}")


def create_churn_by_products(df: pd.DataFrame) -> None:
    """Create bar chart showing churn rate by product count."""
    print("  Creating: 05_churn_by_products.png")
    
    # Data preparation
    products_churn = df.groupby('num_products').agg({
        'churned': ['sum', 'count']
    })
    products_churn.columns = ['churned', 'total']
    products_churn['churn_rate'] = (products_churn['churned'] / products_churn['total']) * 100
    
    # Create figure
    fig, ax = plt.subplots(figsize=DEFAULT_FIGSIZE)
    
    # Color intensity based on churn rate (reverse: lower churn = darker green)
    max_rate = products_churn['churn_rate'].max()
    colors = []
    for rate in products_churn['churn_rate']:
        intensity = 1 - (rate / max_rate) * 0.5  # 0.5 to 1.0 range
        colors.append((0.18 * intensity, 0.8 * intensity, 0.44 * intensity))
    
    # Create bar chart
    bars = ax.bar(
        products_churn.index,
        products_churn['churn_rate'],
        color=colors
    )
    
    # Add value labels
    for i, (bar, value) in enumerate(zip(bars, products_churn['churn_rate'])):
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width()/2., height,
            f'{height:.1f}%',
            ha='center', va='bottom', fontsize=10
        )
    
    # Styling
    ax.set_title('Churn Rate by Product Portfolio Size', fontsize=14, fontweight='bold')
    ax.set_xlabel('Number of Products', fontsize=11)
    ax.set_ylabel('Churn Rate (%)', fontsize=11)
    ax.set_ylim(0, max(products_churn['churn_rate']) * 1.2)
    plt.grid(axis='y', alpha=0.3)
    
    # Save
    output_path = OUTPUT_DIR / '05_churn_by_products.png'
    plt.tight_layout()
    plt.savefig(output_path, dpi=DEFAULT_DPI, bbox_inches='tight')
    plt.close()
    
    print(f"    [OK] Saved: {output_path.name}")


def create_tenure_histogram(df: pd.DataFrame) -> None:
    """Create histogram showing tenure distribution by churn status."""
    print("  Creating: 06_tenure_distribution.png")
    
    # Data preparation
    tenure_retained = df[df['churned'] == 0]['tenure_months']
    tenure_churned = df[df['churned'] == 1]['tenure_months']
    
    # Create figure
    fig, ax = plt.subplots(figsize=DEFAULT_FIGSIZE)
    
    # Create overlapping histograms
    ax.hist(tenure_retained, bins=12, alpha=0.6, color=NEUTRAL_BLUE, 
            label='Retained', edgecolor='black')
    ax.hist(tenure_churned, bins=12, alpha=0.6, color=CHURN_RED,
            label='Churned', edgecolor='black')
    
    # Styling
    ax.set_title('Tenure Distribution: Churned vs Retained Customers', 
                 fontsize=14, fontweight='bold')
    ax.set_xlabel('Tenure (months)', fontsize=11)
    ax.set_ylabel('Customer Count', fontsize=11)
    ax.legend(loc='upper right')
    plt.grid(axis='y', alpha=0.3)
    
    # Save
    output_path = OUTPUT_DIR / '06_tenure_distribution.png'
    plt.tight_layout()
    plt.savefig(output_path, dpi=DEFAULT_DPI, bbox_inches='tight')
    plt.close()
    
    print(f"    [OK] Saved: {output_path.name}")


def create_age_boxplot(df: pd.DataFrame) -> None:
    """Create box plot comparing age distributions."""
    print("  Creating: 07_age_boxplot.png")
    
    # Data preparation
    age_data = [df[df['churned'] == 0]['age'], df[df['churned'] == 1]['age']]
    labels = ['Retained', 'Churned']
    colors = [RETAIN_GREEN, CHURN_RED]
    
    # Create figure
    fig, ax = plt.subplots(figsize=DEFAULT_FIGSIZE)
    
    # Create box plot
    bp = ax.boxplot(age_data, labels=labels, patch_artist=True)
    
    # Color the boxes
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    # Styling
    ax.set_title('Age Distribution: Churned vs Retained', 
                 fontsize=14, fontweight='bold')
    ax.set_xlabel('Customer Status', fontsize=11)
    ax.set_ylabel('Age', fontsize=11)
    plt.grid(axis='y', alpha=0.3)
    
    # Save
    output_path = OUTPUT_DIR / '07_age_boxplot.png'
    plt.tight_layout()
    plt.savefig(output_path, dpi=DEFAULT_DPI, bbox_inches='tight')
    plt.close()
    
    print(f"    [OK] Saved: {output_path.name}")


def create_charges_violin(df: pd.DataFrame) -> None:
    """Create violin plot of monthly charges distribution."""
    print("  Creating: 08_charges_violin.png")
    
    # Data preparation
    df_plot = df.copy()
    df_plot['Status'] = df_plot['churned'].map({0: 'Retained', 1: 'Churned'})
    
    # Create figure
    fig, ax = plt.subplots(figsize=DEFAULT_FIGSIZE)
    
    # Create violin plot
    parts = ax.violinplot(
        [df[df['churned'] == 0]['monthly_charges'],
         df[df['churned'] == 1]['monthly_charges']],
        positions=[0, 1],
        showmeans=True,
        showmedians=True
    )
    
    # Color the violins
    for i, pc in enumerate(parts['bodies']):
        color = RETAIN_GREEN if i == 0 else CHURN_RED
        pc.set_facecolor(color)
        pc.set_alpha(0.5)
    
    # Styling
    ax.set_title('Monthly Charges Distribution: Churned vs Retained',
                 fontsize=14, fontweight='bold')
    ax.set_xlabel('Customer Status', fontsize=11)
    ax.set_ylabel('Monthly Charges ($)', fontsize=11)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['Retained', 'Churned'])
    plt.grid(axis='y', alpha=0.3)
    
    # Save
    output_path = OUTPUT_DIR / '08_charges_violin.png'
    plt.tight_layout()
    plt.savefig(output_path, dpi=DEFAULT_DPI, bbox_inches='tight')
    plt.close()
    
    print(f"    [OK] Saved: {output_path.name}")


def create_contract_product_stack(df: pd.DataFrame) -> None:
    """Create stacked bar showing contract type × product count."""
    print("  Creating: 09_contract_product_stack.png")
    
    # Data preparation
    contract_product = df.groupby(['contract_type', 'num_products']).size().unstack(fill_value=0)
    
    # Create figure
    fig, ax = plt.subplots(figsize=DEFAULT_FIGSIZE)
    
    # Create stacked bar chart
    contract_product.plot(kind='bar', stacked=True, ax=ax, 
                          colormap='Set3', edgecolor='black', linewidth=0.5)
    
    # Styling
    ax.set_title('Customer Segmentation: Contract Type × Product Count',
                 fontsize=14, fontweight='bold')
    ax.set_xlabel('Contract Type', fontsize=11)
    ax.set_ylabel('Customer Count', fontsize=11)
    ax.legend(title='Products', loc='upper right', ncol=1)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=15)
    plt.grid(axis='y', alpha=0.3)
    
    # Save
    output_path = OUTPUT_DIR / '09_contract_product_stack.png'
    plt.tight_layout()
    plt.savefig(output_path, dpi=DEFAULT_DPI, bbox_inches='tight')
    plt.close()
    
    print(f"    [OK] Saved: {output_path.name}")


def create_dashboard(df: pd.DataFrame) -> None:
    """Create multi-panel dashboard with key metrics."""
    print("  Creating: 10_dashboard_overview.png")
    
    # Create figure with subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=LARGE_FIGSIZE)
    
    fig.suptitle('Customer Churn Analysis Dashboard', 
                 fontsize=16, fontweight='bold')
    
    # Panel 1: Overall Churn (pie)
    churn_counts = df['churned'].value_counts().sort_index()
    ax1.pie(churn_counts, labels=['Retained', 'Churned'], 
            colors=[RETAIN_GREEN, CHURN_RED],
            autopct='%1.1f%%', startangle=90)
    ax1.set_title('Overall Churn Distribution', fontsize=12)
    
    # Panel 2: Churn by Contract (bar)
    contract_churn = df.groupby('contract_type').agg({'churned': ['sum', 'count']})
    contract_churn.columns = ['churned', 'total']
    contract_churn['churn_rate'] = (contract_churn['churned'] / contract_churn['total']) * 100
    contract_churn = contract_churn.sort_values('churn_rate', ascending=False)
    bars2 = ax2.bar(range(len(contract_churn)), contract_churn['churn_rate'],
                    color=[CHURN_RED, '#ff6b6b', '#ff8787'])
    ax2.set_xticks(range(len(contract_churn)))
    ax2.set_xticklabels(contract_churn.index, rotation=15, fontsize=9)
    ax2.set_title('Churn Rate by Contract', fontsize=12)
    ax2.set_ylabel('Churn Rate (%)', fontsize=10)
    ax2.grid(axis='y', alpha=0.3)
    
    # Panel 3: Support Calls (bar)
    support_churn = df.groupby('num_support_calls').agg({'churned': ['sum', 'count']})
    support_churn.columns = ['churned', 'total']
    support_churn['churn_rate'] = (support_churn['churned'] / support_churn['total']) * 100
    colors = YELLOW_TO_RED[:len(support_churn)]
    ax3.bar(support_churn.index, support_churn['churn_rate'], color=colors)
    ax3.set_title('Support Calls Impact', fontsize=12)
    ax3.set_xlabel('Support Calls', fontsize=10)
    ax3.set_ylabel('Churn Rate (%)', fontsize=10)
    ax3.grid(axis='y', alpha=0.3)
    
    # Panel 4: Age Distribution (box)
    age_data = [df[df['churned'] == 0]['age'], df[df['churned'] == 1]['age']]
    bp = ax4.boxplot(age_data, labels=['Retained', 'Churned'], patch_artist=True)
    for i, (patch, color) in enumerate(zip(bp['boxes'], [RETAIN_GREEN, CHURN_RED])):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    ax4.set_title('Age: Churned vs Retained', fontsize=12)
    ax4.set_ylabel('Age', fontsize=10)
    ax4.grid(axis='y', alpha=0.3)
    
    # Save
    output_path = OUTPUT_DIR / '10_dashboard_overview.png'
    plt.tight_layout()
    plt.savefig(output_path, dpi=DEFAULT_DPI, bbox_inches='tight')
    plt.close()
    
    print(f"    [OK] Saved: {output_path.name}")


# ============================================================================
# SECTION 5: MAIN EXECUTION
# ============================================================================

def main():
    """Main execution function."""
    
    # Load data
    df = load_data('data/customer_churn.csv')
    
    # Generate all visualizations
    print("[Task 3] Creating visualizations...")
    create_churn_pie(df)
    create_churn_by_contract(df)
    create_churn_by_support(df)
    create_churn_by_payment(df)
    create_churn_by_products(df)
    create_tenure_histogram(df)
    create_age_boxplot(df)
    create_charges_violin(df)
    create_contract_product_stack(df)
    create_dashboard(df)
    
    # Print summary
    print()
    print("=" * 70)
    print(" TASK COMPLETED SUCCESSFULLY")
    print("=" * 70)
    output_files = list(OUTPUT_DIR.glob('*.png'))
    print(f"  Created {len(output_files)} visualization(s):")
    for f in sorted(output_files):
        size_kb = f.stat().st_size / 1024
        print(f"    - {f.name} ({size_kb:.1f} KB)")
    print()


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
