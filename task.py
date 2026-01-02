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

def create_churn_pie_chart(df: pd.DataFrame) -> str:
    """
    TASK 3.1: Generate overall churn distribution pie chart.
    
    Args:
        df: Customer churn dataset
        
    Returns:
        str: Path to the saved chart
    """
    # Data preparation
    churn_counts = df['churned'].value_counts().sort_index()
    labels = ['Retained', 'Churned']
    colors = [RETAIN_GREEN, CHURN_RED]
    
    # Chart creation
    fig, ax = plt.subplots(figsize=(6, 4))
    wedges, texts, autotexts = ax.pie(
        churn_counts,
        labels=labels,
        colors=colors,
        autopct='%1.1f%%',
        startangle=90
    )
    
    # Styling
    ax.set_title('Customer Churn Distribution', fontsize=14, fontweight='bold')
    plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.1), ncol=2)
    
    # Save file
    output_path = OUTPUT_DIR / '01_churn_pie.png'
    plt.tight_layout()
    plt.savefig(output_path, dpi=100, bbox_inches='tight')
    plt.close()
    
    print(f"  [OK] Saved: {output_path.name}")
    return str(output_path)


def create_contract_churn_chart(df: pd.DataFrame) -> str:
    """
    TASK 3.2: Generate churn rate by contract type bar chart.
    
    Args:
        df: Customer churn dataset
        
    Returns:
        str: Path to the saved chart
    """
    # Data preparation - calculate churn rate by contract type
    contract_churn = df.groupby('contract_type').agg({
        'churned': ['sum', 'count']
    })
    contract_churn.columns = ['churned', 'total']
    contract_churn['churn_rate'] = (contract_churn['churned'] / contract_churn['total']) * 100
    contract_churn = contract_churn.sort_values('churn_rate', ascending=False)
    
    # Chart creation
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(
        contract_churn.index,
        contract_churn['churn_rate'],
        color=[CHURN_RED, '#ff6b6b', '#ff8787']
    )
    
    # Add value labels on bars
    for bar in bars:
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
    ax.set_ylim(0, 100)
    plt.xticks(rotation=15)
    plt.grid(axis='y', alpha=0.3)
    
    # Save file
    output_path = OUTPUT_DIR / '02_churn_by_contract.png'
    plt.tight_layout()
    plt.savefig(output_path, dpi=100, bbox_inches='tight')
    plt.close()
    
    print(f"  [OK] Saved: {output_path.name}")
    return str(output_path)


def create_support_calls_chart(df: pd.DataFrame) -> str:
    """
    TASK 3.3: Generate churn rate by support calls bar chart.
    
    Args:
        df: Customer churn dataset
        
    Returns:
        str: Path to the saved chart
    """
    # Data preparation
    support_churn = df.groupby('num_support_calls').agg({
        'churned': ['sum', 'count']
    })
    support_churn.columns = ['churned', 'total']
    support_churn['churn_rate'] = (support_churn['churned'] / support_churn['total']) * 100
    
    # Chart creation with gradient colors (yellow to red)
    colors = ['#f1c40f', '#e67e22', WARNING_ORANGE, '#e74c3c', CHURN_RED]
    
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(
        support_churn.index,
        support_churn['churn_rate'],
        color=colors[:len(support_churn)]
    )
    
    # Add value labels
    for bar in bars:
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
    
    # Save file
    output_path = OUTPUT_DIR / '05_churn_by_support.png'
    plt.tight_layout()
    plt.savefig(output_path, dpi=100, bbox_inches='tight')
    plt.close()
    
    print(f"  [OK] Saved: {output_path.name}")
    return str(output_path)


def create_payment_method_chart(df: pd.DataFrame) -> str:
    """
    TASK 3.4: Generate churn by payment method grouped bar chart.
    
    Args:
        df: Customer churn dataset
        
    Returns:
        str: Path to the saved chart
    """
    # Data preparation - count by payment method and churn status
    payment_churn = df.groupby(['payment_method', 'churned']).size().unstack(fill_value=0)
    payment_churn.columns = ['Retained', 'Churned']
    
    # Chart creation
    fig, ax = plt.subplots(figsize=(9, 5))
    x = np.arange(len(payment_churn.index))
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
    
    # Save file
    output_path = OUTPUT_DIR / '03_churn_by_payment.png'
    plt.tight_layout()
    plt.savefig(output_path, dpi=100, bbox_inches='tight')
    plt.close()
    
    print(f"  [OK] Saved: {output_path.name}")
    return str(output_path)


def create_products_chart(df: pd.DataFrame) -> str:
    """
    TASK 3.5: Generate churn rate by number of products bar chart.
    
    Args:
        df: Customer churn dataset
        
    Returns:
        str: Path to the saved chart
    """
    # Data preparation
    products_churn = df.groupby('num_products').agg({
        'churned': ['sum', 'count']
    })
    products_churn.columns = ['churned', 'total']
    products_churn['churn_rate'] = (products_churn['churned'] / products_churn['total']) * 100
    
    # Chart creation with green gradient (darker = lower churn)
    # Reverse color intensity - lower churn = darker green
    max_rate = products_churn['churn_rate'].max()
    colors = []
    for rate in products_churn['churn_rate']:
        intensity = 1 - (rate / max_rate) * 0.5  # 0.5 to 1.0 range
        colors.append((0.18 * intensity, 0.8 * intensity, 0.44 * intensity))
    
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(
        products_churn.index,
        products_churn['churn_rate'],
        color=colors
    )
    
    # Add value labels
    for bar in bars:
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
    
    # Save file
    output_path = OUTPUT_DIR / '04_churn_by_products.png'
    plt.tight_layout()
    plt.savefig(output_path, dpi=100, bbox_inches='tight')
    plt.close()
    
    print(f"  [OK] Saved: {output_path.name}")
    return str(output_path)


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
    print("  Generating Charts (Part 1: Charts 1-5)")
    print("="*60)
    
    # Generate charts 1-5
    try:
        charts_created.append(create_churn_pie_chart(df))
        charts_created.append(create_contract_churn_chart(df))
        charts_created.append(create_payment_method_chart(df))
        charts_created.append(create_products_chart(df))
        charts_created.append(create_support_calls_chart(df))
    except Exception as e:
        print(f"[ERROR] Chart generation failed: {e}")
        import traceback
        traceback.print_exc()
        return
    
    # Summary
    print(f"\n[OK] Generated {len(charts_created)} charts successfully")
    print(f"[OK] Output directory: {OUTPUT_DIR.absolute()}")
    print(f"\nNote: Charts 6-10 will be implemented in next commit")


if __name__ == "__main__":
    main()