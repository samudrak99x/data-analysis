# Customer Churn Visualization Specification

**Generated:** January 2, 2026  
**Data Source:** `../data/customer_churn.csv`  
**Output Directory:** `../outputs/`

---

## 1. Dataset Schema Brief

### Dataset Structure
- **Type:** Tabular (CSV)
- **Total Records:** 1,000 rows
- **Total Columns:** 10 fields
- **Data Quality:** 100% complete (no missing values)
- **File Size:** 73.8 KB
- **Encoding:** ASCII
- **Delimiter:** Comma

### Field Catalog

| Field Name | Type | Format | Unique Values | Business Meaning |
|------------|------|--------|---------------|------------------|
| `customer_id` | String | Numeric ID | 100 | Unique customer identifier |
| `age` | Numeric | Integer | 41 | Customer age in years (18-80) |
| `tenure_months` | Numeric | Integer | 41 | Customer relationship duration (0-72 months) |
| `monthly_charges` | Numeric | Decimal | 91 | Monthly service charges ($20-$150) |
| `total_charges` | Numeric | Decimal | 98 | Cumulative lifetime charges ($0-$10,800) |
| `num_products` | Numeric | Integer | 5 | Number of products/services (1-5) |
| `num_support_calls` | Numeric | Integer | 5 | Support interactions count (0-5) |
| `contract_type` | Categorical | String | 3 | Service contract duration |
| `payment_method` | Categorical | String | 4 | Payment mechanism |
| `churned` | Binary | Integer | 2 | Churn status (0=Retained, 1=Churned) |

### Categorical Field Values

**contract_type:**
- Month-to-month (507 customers)
- One year (300 customers)
- Two year (193 customers)

**payment_method:**
- Credit card (263 customers)
- Mailed check (259 customers)
- Electronic (255 customers)
- Bank transfer (223 customers)

**churned:**
- 0 = Retained (794 customers)
- 1 = Churned (206 customers)

---

## 2. Visual Business Questions

Based on the schema, here are 8 visual questions that can be answered with charts:

1. **What is the overall churn vs retention distribution?**
   - Visual: Pie chart showing retained vs churned split

2. **How does churn rate vary by contract type?**
   - Visual: Bar chart comparing churn rates across contract types

3. **Which payment methods correlate with higher churn?**
   - Visual: Horizontal bar chart sorted by churn rate

4. **How does customer tenure affect churn probability?**
   - Visual: Line chart showing churn rate by tenure groups

5. **What is the relationship between number of products and churn?**
   - Visual: Column chart showing churn rate by product count

6. **How does age distribution differ between churned and retained customers?**
   - Visual: Overlapping histogram comparing age distributions

7. **What is the distribution of monthly charges for churned vs retained?**
   - Visual: Box plot comparing charge distributions

8. **How do support call patterns relate to churn?**
   - Visual: Stacked bar chart showing support calls by churn status

---

## 3. Chart Specifications (9 Charts)

### Chart 1: Customer Churn Overview
**File:** `01_customer_distribution.png`  
**Type:** Pie chart  
**Purpose:** Show overall churn vs retention split

**Specifications:**
- **Data:** Group by `churned` field (0 vs 1)
- **Labels:** "Retained" and "Churned" with percentages
- **Colors:** Green (#6BCF7F) for Retained, Red (#FF6B6B) for Churned
- **Explode:** Churned segment by 0.1
- **Title:** "Customer Churn Overview"
- **Subtitle:** "1,000 Total Customers"
- **Size:** 1000x1000 pixels
- **DPI:** 300

---

### Chart 2: Churn Rate by Contract Type
**File:** `02_churn_by_contract.png`  
**Type:** Vertical bar chart  
**Purpose:** Show dramatic difference in churn rates across contract types

**Specifications:**
- **X-axis:** Contract type (Month-to-month, One year, Two year)
- **Y-axis:** Churn rate (percentage)
- **Data:** Group by `contract_type`, calculate mean of `churned`
- **Colors:** Red (#FF6B6B) for Month-to-month, Yellow (#FFD93D) for One year, Green (#6BCF7F) for Two year
- **Labels:** Percentage labels on top of bars, customer count below x-axis
- **Title:** "Churn Rate by Contract Type"
- **Subtitle:** "Month-to-month contracts show higher churn"
- **Grid:** Light gray dashed grid (#EEEEEE)
- **Size:** 1200x800 pixels
- **DPI:** 300

---

### Chart 3: Churn Rate by Payment Method
**File:** `03_churn_by_payment.png`  
**Type:** Horizontal bar chart  
**Purpose:** Compare churn rates across payment methods

**Specifications:**
- **Y-axis:** Payment method (sorted by churn rate descending)
- **X-axis:** Churn rate (percentage)
- **Data:** Group by `payment_method`, calculate mean of `churned`
- **Colors:** Gradient from red to green based on churn rate
- **Labels:** Percentage labels at end of each bar
- **Title:** "Churn Rate by Payment Method"
- **Subtitle:** "Manual payment methods show higher churn"
- **Size:** 1200x800 pixels
- **DPI:** 300

---

### Chart 4: Churn Rate by Tenure Group
**File:** `04_churn_by_tenure.png`  
**Type:** Line chart with markers  
**Purpose:** Show how churn decreases with tenure

**Specifications:**
- **X-axis:** Tenure groups (0-12, 13-24, 25-36, 37-72 months)
- **Y-axis:** Churn rate (percentage)
- **Data:** Create tenure bins using `pd.cut()` on `tenure_months`, then group and calculate mean of `churned`
- **Bins:** `[0, 12, 24, 36, 72]` with labels `['0-12', '13-24', '25-36', '37-72']`
- **Line Color:** Blue (#4A90E2) with circular markers
- **Labels:** Percentage labels above each point
- **Highlight:** Emphasize 0-12 months group (critical period) with different marker style
- **Title:** "Churn Rate by Customer Tenure"
- **Subtitle:** "First year is critical period"
- **Size:** 1200x800 pixels
- **DPI:** 300

---

### Chart 5: Churn Rate by Number of Products
**File:** `05_churn_by_products.png`  
**Type:** Column chart  
**Purpose:** Show relationship between product diversification and churn

**Specifications:**
- **X-axis:** Number of products (1, 2, 3, 4, 5)
- **Y-axis:** Churn rate (percentage)
- **Data:** Group by `num_products`, calculate mean of `churned`
- **Color:** Purple (#9B59B6)
- **Labels:** Percentage labels on bars, customer count below x-axis
- **Title:** "Churn Rate by Product Count"
- **Subtitle:** "3-4 products show lowest churn"
- **Size:** 1200x800 pixels
- **DPI:** 300

---

### Chart 6: Age Distribution Comparison
**File:** `06_age_distribution.png`  
**Type:** Overlapping histogram  
**Purpose:** Compare age distributions between churned and retained

**Specifications:**
- **X-axis:** Age (bins: 18-30, 31-40, 41-50, 51-60, 61-70, 71-80)
- **Y-axis:** Customer count
- **Data:** Filter by `churned` (0 vs 1), create histogram of `age`
- **Bins:** `[18, 30, 40, 50, 60, 70, 80]`
- **Colors:** Red (#FF6B6B) for Churned (alpha=0.7), Green (#6BCF7F) for Retained (alpha=0.7)
- **Legend:** Show both groups with labels
- **Title:** "Age Distribution: Churned vs Retained"
- **Subtitle:** "Comparison of customer age patterns"
- **Size:** 1200x800 pixels
- **DPI:** 300

---

### Chart 7: Monthly Charges Distribution
**File:** `07_charges_distribution.png`  
**Type:** Box plot  
**Purpose:** Compare monthly charges between churned and retained

**Specifications:**
- **X-axis:** Churn status (Retained, Churned)
- **Y-axis:** Monthly charges ($)
- **Data:** Group by `churned`, plot `monthly_charges` as box plot
- **Colors:** Green (#6BCF7F) for Retained, Red (#FF6B6B) for Churned
- **Title:** "Monthly Charges Distribution"
- **Subtitle:** "Comparison by churn status"
- **Size:** 1200x800 pixels
- **DPI:** 300

---

### Chart 8: Support Calls vs Churn
**File:** `08_support_calls_churn.png`  
**Type:** Stacked bar chart  
**Purpose:** Show support call patterns by churn status

**Specifications:**
- **X-axis:** Number of support calls (0, 1, 2, 3, 4, 5)
- **Y-axis:** Customer count
- **Data:** Group by `num_support_calls` and `churned`, count customers
- **Colors:** Stacked bars with Green (#6BCF7F) for Retained, Red (#FF6B6B) for Churned
- **Title:** "Support Calls Distribution by Churn Status"
- **Subtitle:** "Customer support interaction patterns"
- **Size:** 1200x800 pixels
- **DPI:** 300

---

### Chart 9: Comprehensive Dashboard
**File:** `09_churn_dashboard.png`  
**Type:** 2x2 subplot grid  
**Purpose:** Comprehensive view of all key metrics

**Subplots:**
1. **Top-left:** Churn by Contract (bar chart from Chart 2)
2. **Top-right:** Churn by Tenure (line chart from Chart 4)
3. **Bottom-left:** Churn by Products (column chart from Chart 5)
4. **Bottom-right:** Key metrics table (text summary with counts)

**Dashboard Specifications:**
- **Figure Size:** 16x12 inches
- **Main Title:** "Customer Churn Analysis Dashboard"
- **Date Stamp:** Footer with generation date
- **Color Scheme:** Consistent across all subplots
- **DPI:** 300

---

## 4. Task-Based Implementation Plan

### TASK 1: Setup & Configuration
**Subtask 1.1:** Import required libraries
- `pandas` for data manipulation
- `matplotlib.pyplot` for charting
- `seaborn` for enhanced styling
- `numpy` for numerical operations
- `pathlib.Path` for file paths

**Subtask 1.2:** Define constants
- `INPUT_FILE = '../data/customer_churn.csv'`
- `OUTPUT_DIR = '../outputs/'`
- `DPI = 300`
- Color palette dictionary:
  ```python
  colors = {
      'danger': '#FF6B6B',      # Red for high churn
      'warning': '#FFD93D',     # Yellow for medium
      'success': '#6BCF7F',     # Green for low churn
      'primary': '#4A90E2',     # Blue for neutral
      'secondary': '#9B59B6'    # Purple for accent
  }
  ```

**Subtask 1.3:** Create output directory
- Check if `OUTPUT_DIR` exists
- Create directory if it doesn't exist using `Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)`

---

### TASK 2: Data Loading Function
**Subtask 2.1:** Create `load_data()` function
- Input: None (uses constant `INPUT_FILE`)
- Read CSV file using `pd.read_csv(INPUT_FILE)`
- Convert string columns to numeric: `age`, `tenure_months`, `monthly_charges`, `total_charges`, `num_products`, `num_support_calls`, `churned`
- Use `pd.to_numeric()` with `errors='coerce'`
- Return DataFrame

---

### TASK 3: Chart Generation Functions

**TASK 3.1:** Implement `create_customer_distribution(df)`
- Group by `churned` field, count customers
- Create pie chart with explode effect (churned segment: 0.1)
- Apply colors (green for retained, red for churned)
- Add title, subtitle, labels with percentages
- Save as `01_customer_distribution.png` with 300 DPI
- Close figure using `plt.close()`

**TASK 3.2:** Implement `create_churn_by_contract(df)`
- Group by `contract_type`, calculate mean of `churned` (this gives churn rate)
- Create vertical bar chart
- Apply color scheme (red for Month-to-month, yellow for One year, green for Two year)
- Add percentage labels on top of bars
- Add customer count labels below x-axis
- Add grid (light gray, dashed)
- Save as `02_churn_by_contract.png` with 300 DPI
- Close figure

**TASK 3.3:** Implement `create_churn_by_payment(df)`
- Group by `payment_method`, calculate mean of `churned`
- Sort by churn rate descending
- Create horizontal bar chart
- Apply color gradient from red to green based on churn rate
- Add percentage labels at end of each bar
- Save as `03_churn_by_payment.png` with 300 DPI
- Close figure

**TASK 3.4:** Implement `create_churn_by_tenure(df)`
- Create tenure bins: `pd.cut(df['tenure_months'], bins=[0, 12, 24, 36, 72], labels=['0-12', '13-24', '25-36', '37-72'])`
- Group by tenure bins, calculate mean of `churned`
- Create line chart with circular markers
- Use blue color (#4A90E2)
- Highlight 0-12 months group with different marker style (larger, different color)
- Add percentage labels above each point
- Save as `04_churn_by_tenure.png` with 300 DPI
- Close figure

**TASK 3.5:** Implement `create_churn_by_products(df)`
- Group by `num_products`, calculate mean of `churned`
- Create column chart
- Apply purple color (#9B59B6)
- Add percentage labels on bars
- Add customer count labels below x-axis
- Save as `05_churn_by_products.png` with 300 DPI
- Close figure

**TASK 3.6:** Implement `create_age_distribution(df)`
- Create age bins: `pd.cut(df['age'], bins=[18, 30, 40, 50, 60, 70, 80])`
- Filter by `churned` (0 and 1 separately)
- Create overlapping histograms with transparency (alpha=0.7)
- Apply colors (red for churned, green for retained)
- Add legend with labels
- Save as `06_age_distribution.png` with 300 DPI
- Close figure

**TASK 3.7:** Implement `create_charges_distribution(df)`
- Group by `churned`, extract `monthly_charges` values
- Create box plot for each group
- Apply colors (green for retained, red for churned)
- Add title and labels
- Save as `07_charges_distribution.png` with 300 DPI
- Close figure

**TASK 3.8:** Implement `create_support_calls_churn(df)`
- Group by `num_support_calls` and `churned`, count customers
- Create stacked bar chart
- Apply colors (green for retained, red for churned)
- Add title and labels
- Save as `08_support_calls_churn.png` with 300 DPI
- Close figure

**TASK 3.9:** Implement `create_dashboard(df)`
- Create 2x2 subplot grid (figure size 16x12 inches)
- Subplot 1 (top-left): Call `create_churn_by_contract()` logic inline
- Subplot 2 (top-right): Call `create_churn_by_tenure()` logic inline
- Subplot 3 (bottom-left): Call `create_churn_by_products()` logic inline
- Subplot 4 (bottom-right): Create text table with key metrics (total customers, churned count, retained count)
- Add main title "Customer Churn Analysis Dashboard"
- Add date stamp in footer
- Save as `09_churn_dashboard.png` with 300 DPI
- Close figure

---

### TASK 4: Main Execution Function
**Subtask 4.1:** Create `main()` function
- Load data using `load_data()`
- Call all 9 chart functions in sequence (3.1 through 3.9)
- Print completion message: "All 9 visualizations created successfully!"
- Print file count: "Generated 9 chart files in ../outputs/"

**Subtask 4.2:** Add entry point
- `if __name__ == '__main__': main()`

---

### TASK 5: Quality Assurance
**Subtask 5.1:** Verify all charts use 300 DPI
**Subtask 5.2:** Verify consistent color palette across charts
**Subtask 5.3:** Verify all 9 output files are created
**Subtask 5.4:** Test execution time (should be < 1 minute)

---

## 5. APPENDIX: Data Dictionary

### Field Specifications

| Field | Type | Format | Range/Values | Business Meaning | Usage in Charts |
|-------|------|--------|--------------|------------------|-----------------|
| `customer_id` | String | Numeric ID | 1-100 | Unique identifier | Not used in charts |
| `age` | Numeric | Integer | 18-80 | Customer age | Chart 6 (distribution) |
| `tenure_months` | Numeric | Integer | 0-72 | Relationship duration | Chart 4 (tenure groups) |
| `monthly_charges` | Numeric | Decimal | $20-$150 | Monthly fee | Chart 7 (distribution) |
| `total_charges` | Numeric | Decimal | $0-$10,800 | Lifetime value | Not used in charts |
| `num_products` | Numeric | Integer | 1-5 | Product count | Chart 5 (churn by products) |
| `num_support_calls` | Numeric | Integer | 0-5 | Support interactions | Chart 8 (support calls) |
| `contract_type` | Categorical | String | Month-to-month, One year, Two year | Contract duration | Chart 2 (churn by contract) |
| `payment_method` | Categorical | String | Credit card, Mailed check, Electronic, Bank transfer | Payment type | Chart 3 (churn by payment) |
| `churned` | Binary | Integer | 0 (Retained), 1 (Churned) | Churn status | All charts (target variable) |

---

## Technical Requirements

### Python Libraries
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path
```

### Style Guidelines
- **Font:** Arial or Helvetica
- **Title font size:** 16pt (bold)
- **Subtitle font size:** 12pt (italic)
- **Label font size:** 10pt
- **Grid:** Light gray (#EEEEEE), dashed
- **Figure DPI:** 300 for high quality
- **Background:** White
- **Save format:** PNG with tight layout

### Color Palette
```python
colors = {
    'danger': '#FF6B6B',      # Red for high churn
    'warning': '#FFD93D',     # Yellow for medium
    'success': '#6BCF7F',     # Green for low churn
    'primary': '#4A90E2',     # Blue for neutral
    'secondary': '#9B59B6'    # Purple for accent
}
```

---

## Success Criteria

The visualization task is complete when:
1. ✅ All 9 chart files are generated in `../outputs/`
2. ✅ Charts match the specifications above
3. ✅ All percentages are calculated correctly
4. ✅ Color scheme is consistently applied
5. ✅ Charts are high resolution (300 DPI)
6. ✅ Script runs without errors

---

**Specification Version:** 1.0  
**Last Updated:** January 2, 2026  
**Status:** Ready for implementation
