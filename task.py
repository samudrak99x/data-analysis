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
