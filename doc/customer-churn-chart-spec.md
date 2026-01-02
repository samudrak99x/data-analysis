# Customer Churn Analysis - BI Visualization Specification

**Dataset**: customer_churn.csv  
**Analysis Type**: Business Intelligence & Visualization  
**Domain**: Customer Retention Analytics  
**Created**: 2026-01-02  
**Architect**: @data-architect  

---

## 📊 Dataset Schema Overview

**Rows**: 1,000 customer records  
**Columns**: 10 fields  
**Grain**: One row per customer  

### Field Inventory

| Field | Type | Description | Sample Values | Unique Values |
|-------|------|-------------|---------------|---------------|
| customer_id | Numeric | Customer identifier | 1, 2, 3 | 100 |
| age | Numeric | Customer age in years | 52, 42, 54 | 41 |
| tenure_months | Numeric | Months as customer | 4, 2, 24 | 41 |
| monthly_charges | Numeric | Monthly bill amount | 55.72, 42.44, 74.58 | 91 |
| total_charges | Numeric | Cumulative charges | 222.89, 84.87, 1789.81 | 98 |
| num_products | Numeric | Number of products subscribed | 1, 2, 3 | 5 (1-5) |
| num_support_calls | Numeric | Support calls made | 0, 1, 2 | 6 (0-5) |
| contract_type | Categorical | Contract duration | Month-to-month, One year, Two year | 3 |
| payment_method | Categorical | Payment type | Electronic, Credit card, Bank transfer, Mailed check | 4 |
| churned | Binary | Churn status (0=Active, 1=Churned) | 0, 1 | 2 |

### Data Dictionary

**Target Variable**: `churned` (0 = Active: 794 customers, 1 = Churned: 206 customers)  
**Churn Rate**: ~20.6% (206 out of 1,000 customers)

**Categorical Distributions**:
- **Contract Type**: Month-to-month (507), One year (300), Two year (193)
- **Payment Method**: Credit card (263), Mailed check (259), Electronic (255), Bank transfer (223)
- **Products**: 1 product (399), 2 products (272), 3 products (197), 4 products (96), 5 products (36)
- **Support Calls**: 0 calls (359), 1 call (400), 2 calls (179), 3 calls (54), 4 calls (6), 5 calls (2)

---

## 🎯 Visual Business Questions

1. **Q1**: What is the overall churn rate breakdown?
2. **Q2**: How does churn vary by contract type?
3. **Q3**: Which payment methods have the highest churn rates?
4. **Q4**: What is the relationship between customer tenure and churn?
5. **Q5**: How does the number of products affect churn rates?
6. **Q6**: How do support calls correlate with churn?
7. **Q7**: What is the distribution of customer age?
8. **Q8**: How do monthly charges compare between churned and active customers?
9. **Q9**: What is the distribution of customer tenure?
10. **Q10**: How are customers distributed across contract types and payment methods?

---

## 📈 Chart Specifications (10 Charts)

### Chart 1: Churn Rate Overview (Pie Chart)
**Business Question**: Q1 - Overall churn breakdown  
**Chart Type**: Pie Chart  
**Data Source**: `churned` column  
**Visual Elements**:
- **Values**: Count of churned (1) vs active (0) customers
- **Labels**: "Active Customers (79.4%)", "Churned Customers (20.6%)"
- **Colors**: 
  - Active: `#2ecc71` (green)
  - Churned: `#e74c3c` (red)
- **Title**: "Customer Churn Rate Distribution"
- **Additional**: Display percentages, explode churned slice slightly
**Insight**: Shows proportion of customers lost vs retained

---

### Chart 2: Churn by Contract Type (Grouped Bar Chart)
**Business Question**: Q2 - Contract type impact on churn  
**Chart Type**: Grouped Bar Chart  
**Data Source**: `contract_type` + `churned`  
**Visual Elements**:
- **X-axis**: Contract type (Month-to-month, One year, Two year)
- **Y-axis**: Count of customers
- **Groups**: Active (green) vs Churned (red)
- **Colors**: Active `#2ecc71`, Churned `#e74c3c`
- **Title**: "Customer Churn by Contract Type"
- **Labels**: X-label="Contract Type", Y-label="Number of Customers"
**Insight**: Reveals which contract types have highest retention

---

### Chart 3: Churn Rate by Payment Method (Stacked Bar Chart)
**Business Question**: Q3 - Payment method influence on churn  
**Chart Type**: Stacked Bar Chart (100% normalized)  
**Data Source**: `payment_method` + `churned`  
**Visual Elements**:
- **X-axis**: Payment method (Electronic, Credit card, Bank transfer, Mailed check)
- **Y-axis**: Percentage (0-100%)
- **Stacks**: Active (bottom, green) vs Churned (top, red)
- **Colors**: Active `#2ecc71`, Churned `#e74c3c`
- **Title**: "Churn Rate by Payment Method (%)"
- **Labels**: X-label="Payment Method", Y-label="Percentage (%)"
**Insight**: Identifies payment methods with highest churn risk

---

### Chart 4: Tenure vs Churn (Box Plot)
**Business Question**: Q4 - Tenure relationship with churn  
**Chart Type**: Box Plot  
**Data Source**: `tenure_months` grouped by `churned`  
**Visual Elements**:
- **X-axis**: Churn status (Active, Churned)
- **Y-axis**: Tenure (months)
- **Boxes**: Active (green), Churned (red)
- **Colors**: Active `#2ecc71`, Churned `#e74c3c`
- **Title**: "Customer Tenure Distribution by Churn Status"
- **Labels**: X-label="Customer Status", Y-label="Tenure (Months)"
**Insight**: Shows whether newer customers churn more

---

### Chart 5: Churn by Number of Products (Grouped Bar Chart)
**Business Question**: Q5 - Product count impact on churn  
**Chart Type**: Grouped Bar Chart  
**Data Source**: `num_products` + `churned`  
**Visual Elements**:
- **X-axis**: Number of products (1, 2, 3, 4, 5)
- **Y-axis**: Count of customers
- **Groups**: Active (green) vs Churned (red)
- **Colors**: Active `#2ecc71`, Churned `#e74c3c`
- **Title**: "Customer Churn by Number of Products"
- **Labels**: X-label="Number of Products", Y-label="Number of Customers"
**Insight**: Reveals if multi-product customers have better retention

---

### Chart 6: Churn by Support Calls (Grouped Bar Chart)
**Business Question**: Q6 - Support call correlation with churn  
**Chart Type**: Grouped Bar Chart  
**Data Source**: `num_support_calls` + `churned`  
**Visual Elements**:
- **X-axis**: Number of support calls (0, 1, 2, 3, 4, 5)
- **Y-axis**: Count of customers
- **Groups**: Active (green) vs Churned (red)
- **Colors**: Active `#2ecc71`, Churned `#e74c3c`
- **Title**: "Customer Churn by Number of Support Calls"
- **Labels**: X-label="Number of Support Calls", Y-label="Number of Customers"
**Insight**: Indicates if support issues predict churn

---

### Chart 7: Age Distribution (Histogram)
**Business Question**: Q7 - Customer age demographics  
**Chart Type**: Histogram  
**Data Source**: `age` column  
**Visual Elements**:
- **X-axis**: Age bins (5-year intervals)
- **Y-axis**: Frequency (count)
- **Bars**: Blue `#3498db`
- **Title**: "Customer Age Distribution"
- **Labels**: X-label="Age (Years)", Y-label="Number of Customers"
- **Additional**: Add KDE curve overlay
**Insight**: Shows age demographics of customer base

---

### Chart 8: Monthly Charges by Churn Status (Violin Plot)
**Business Question**: Q8 - Pricing impact on churn  
**Chart Type**: Violin Plot  
**Data Source**: `monthly_charges` grouped by `churned`  
**Visual Elements**:
- **X-axis**: Churn status (Active, Churned)
- **Y-axis**: Monthly charges ($)
- **Violins**: Active (green), Churned (red)
- **Colors**: Active `#2ecc71`, Churned `#e74c3c`
- **Title**: "Monthly Charges Distribution by Churn Status"
- **Labels**: X-label="Customer Status", Y-label="Monthly Charges ($)"
- **Additional**: Show median line
**Insight**: Identifies if high charges drive churn

---

### Chart 9: Tenure Distribution (Histogram)
**Business Question**: Q9 - Customer lifecycle stages  
**Chart Type**: Histogram  
**Data Source**: `tenure_months` column  
**Visual Elements**:
- **X-axis**: Tenure bins (6-month intervals)
- **Y-axis**: Frequency (count)
- **Bars**: Orange `#f39c12`
- **Title**: "Customer Tenure Distribution"
- **Labels**: X-label="Tenure (Months)", Y-label="Number of Customers"
- **Additional**: Add KDE curve overlay
**Insight**: Reveals customer lifecycle distribution

---

### Chart 10: Contract Type by Payment Method (Heatmap)
**Business Question**: Q10 - Contract-payment combinations  
**Chart Type**: Heatmap  
**Data Source**: Cross-tabulation of `contract_type` + `payment_method`  
**Visual Elements**:
- **X-axis**: Payment method
- **Y-axis**: Contract type
- **Cells**: Count of customers (color intensity)
- **Colormap**: Blues (light to dark)
- **Title**: "Customer Distribution: Contract Type vs Payment Method"
- **Labels**: X-label="Payment Method", Y-label="Contract Type"
- **Additional**: Annotate cells with counts
**Insight**: Identifies popular contract-payment combinations

---

## 🛠️ Task-Based Implementation Plan

### TASK 1: Setup & Configuration
**Subtask 1.1**: Import required libraries
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
```

**Subtask 1.2**: Define configuration constants
```python
OUTPUT_DIR = Path('./outputs')
DPI = 300
COLORS = {
    'active': '#2ecc71',
    'churned': '#e74c3c',
    'primary': '#3498db',
    'secondary': '#f39c12'
}
```

**Subtask 1.3**: Create output directory
```python
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
```

---

### TASK 2: Data Loading & Preparation
**Subtask 2.1**: Create data loading function
```python
def load_data(file_path):
    df = pd.read_csv(file_path)
    # Convert numeric fields
    numeric_cols = ['age', 'tenure_months', 'monthly_charges', 
                   'total_charges', 'num_products', 'num_support_calls', 'churned']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df
```

**Subtask 2.2**: Load dataset
```python
df = load_data('data/customer_churn.csv')
```

---

### TASK 3: Chart Generation Functions (10 Functions)

**Subtask 3.1**: Chart 1 - Churn Rate Pie Chart
```python
def create_churn_pie(df):
    # Count churn values
    churn_counts = df['churned'].value_counts()
    # Create pie chart with green/red colors
    # Save as '01_churn_rate_overview.png'
```

**Subtask 3.2**: Chart 2 - Churn by Contract Type
```python
def create_churn_by_contract(df):
    # Group by contract_type and churned
    # Create grouped bar chart
    # Save as '02_churn_by_contract_type.png'
```

**Subtask 3.3**: Chart 3 - Churn by Payment Method (Stacked %)
```python
def create_churn_by_payment(df):
    # Cross-tab payment_method and churned
    # Normalize to percentages
    # Create 100% stacked bar chart
    # Save as '03_churn_by_payment_method.png'
```

**Subtask 3.4**: Chart 4 - Tenure Box Plot
```python
def create_tenure_boxplot(df):
    # Box plot of tenure_months grouped by churned
    # Save as '04_tenure_vs_churn_boxplot.png'
```

**Subtask 3.5**: Chart 5 - Churn by Products
```python
def create_churn_by_products(df):
    # Group by num_products and churned
    # Create grouped bar chart
    # Save as '05_churn_by_num_products.png'
```

**Subtask 3.6**: Chart 6 - Churn by Support Calls
```python
def create_churn_by_support(df):
    # Group by num_support_calls and churned
    # Create grouped bar chart
    # Save as '06_churn_by_support_calls.png'
```

**Subtask 3.7**: Chart 7 - Age Histogram
```python
def create_age_histogram(df):
    # Histogram of age with KDE overlay
    # Save as '07_age_distribution.png'
```

**Subtask 3.8**: Chart 8 - Monthly Charges Violin Plot
```python
def create_charges_violin(df):
    # Violin plot of monthly_charges by churned
    # Save as '08_monthly_charges_violin.png'
```

**Subtask 3.9**: Chart 9 - Tenure Histogram
```python
def create_tenure_histogram(df):
    # Histogram of tenure_months with KDE overlay
    # Save as '09_tenure_distribution.png'
```

**Subtask 3.10**: Chart 10 - Contract-Payment Heatmap
```python
def create_contract_payment_heatmap(df):
    # Cross-tab contract_type and payment_method
    # Create heatmap with counts
    # Save as '10_contract_payment_heatmap.png'
```

---

### TASK 4: Main Execution Function
**Subtask 4.1**: Create main orchestration function
```python
def main():
    print("Loading customer churn data...")
    df = load_data('data/customer_churn.csv')
    
    print("Generating Chart 1: Churn Rate Overview...")
    create_churn_pie(df)
    
    print("Generating Chart 2: Churn by Contract Type...")
    create_churn_by_contract(df)
    
    # ... call all 10 chart functions
    
    print(f"\n✅ All 10 charts generated successfully in {OUTPUT_DIR}")
```

**Subtask 4.2**: Add entry point
```python
if __name__ == '__main__':
    main()
```

---

### TASK 5: Quality Assurance
**Subtask 5.1**: Verify all 10 PNG files generated
**Subtask 5.2**: Check file naming convention (01_, 02_, etc.)
**Subtask 5.3**: Verify high resolution (300 DPI)
**Subtask 5.4**: Confirm proper colors (green for active, red for churned)

---

## 📦 Expected Outputs

### Files Generated
1. `01_churn_rate_overview.png` - Pie chart showing 79.4% active, 20.6% churned
2. `02_churn_by_contract_type.png` - Grouped bars by contract duration
3. `03_churn_by_payment_method.png` - Stacked % bars by payment type
4. `04_tenure_vs_churn_boxplot.png` - Box plot comparing tenure distributions
5. `05_churn_by_num_products.png` - Grouped bars by product count
6. `06_churn_by_support_calls.png` - Grouped bars by support call frequency
7. `07_age_distribution.png` - Histogram with KDE of customer ages
8. `08_monthly_charges_violin.png` - Violin plot comparing charges
9. `09_tenure_distribution.png` - Histogram with KDE of tenure
10. `10_contract_payment_heatmap.png` - Heatmap of contract-payment combinations

### Implementation Requirements
- **Total Charts**: 10 PNG files
- **File Format**: High-resolution PNG (300 DPI)
- **Output Location**: `./outputs/` directory
- **Color Scheme**: Consistent use of green (active), red (churned), blue/orange (distributions)
- **Code Structure**: Single `task.py` file (~400-500 lines)
- **Dependencies**: pandas, matplotlib, seaborn (in `requirements.txt`)

---

## 🎨 Visual Design Guidelines

### Color Palette
- **Active/Retained**: `#2ecc71` (Green)
- **Churned/At-Risk**: `#e74c3c` (Red)
- **Neutral/Primary**: `#3498db` (Blue)
- **Secondary**: `#f39c12` (Orange)

### Typography & Styling
- **Title Font Size**: 14pt, bold
- **Axis Labels**: 12pt, regular
- **Legend**: 10pt, positioned best fit
- **Grid**: Light gray, subtle
- **Figure Size**: 10x6 inches (standard)

### Best Practices
- All charts have descriptive titles
- Axes always labeled with units
- Consistent color usage (green=good, red=churn)
- High DPI for presentation quality
- Sequential file naming for easy ordering

---

## 📊 Implementation Notes for @data-dev

### Code Generation Instructions
1. Follow the task-based plan exactly (Task 1 → 2 → 3 → 4 → 5)
2. Implement all 10 chart functions as specified
3. Use the defined color scheme consistently
4. Save files with sequential numbering (01_, 02_, etc.)
5. Set figure DPI to 300 for high quality
6. Close figures after saving to free memory
7. Add logging for each chart generation step

### Validation Checklist
- [ ] All 10 chart functions implemented
- [ ] Correct chart types used (pie, bar, box, violin, histogram, heatmap)
- [ ] Colors match specification (green/red for churn)
- [ ] All files saved to `./outputs/` directory
- [ ] High resolution (300 DPI) PNG format
- [ ] Descriptive file names with numbering
- [ ] Code validated (no syntax errors, no smart quotes)
- [ ] requirements.txt includes pandas, matplotlib, seaborn

---

## ✅ Success Criteria

### Specification Complete
- ✅ 10 visual business questions identified
- ✅ 10 chart specifications defined (type, axes, colors, labels)
- ✅ Task-based implementation plan created (5 tasks)
- ✅ Data dictionary documented
- ✅ Color scheme defined
- ✅ Output structure specified

### Ready for Implementation
This specification provides all information needed for @data-dev to implement `task.py` without ambiguity. The task-based structure ensures systematic implementation and quality assurance.

---

**Next Step**: Pass this specification to @data-dev for code implementation using the *implement-with-git command.
