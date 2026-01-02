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
print("[Task 1] Setup & Configuration: Complete")
print(f"  - Output directory: {OUTPUT_DIR}")
print(f"  - Default DPI: {DEFAULT_DPI}")
print(f"  - Matplotlib style configured")
print()
