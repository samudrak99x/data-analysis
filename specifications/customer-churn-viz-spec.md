# Customer Churn Data Visualization Specification

**Dataset**: `customer_churn.csv`  
**Analyst**: DataWinston (BI Visualization Architect)  
**Date**: 2026-01-02  
**Purpose**: Chart specifications for customer churn analysis dashboard

---

## 1. Dataset Schema Brief

### Dataset Overview
- **Type**: Tabular Customer Data
- **Records**: 1,000 customers
- **Columns**: 10 fields
- **One Row Represents**: A single customer with service details and churn status

### Column Structure

| Column Name | Data Type | Purpose | Sample Values |
|-------------|-----------|---------|---------------|
| `customer_id` | Integer | Unique identifier | 1, 2, 3 |
| `age` | Integer | Customer age (years) | 52, 42, 54 |
| `tenure_months` | Integer | Months with service | 4, 2, 24 |
| `monthly_charges` | Float | Monthly bill amount ($) | 55.72, 42.44, 74.58 |
| `total_charges` | Float | Lifetime revenue ($) | 222.89, 84.87, 1789.81 |
| `num_products` | Integer | Number of products subscribed | 1, 2, 3 (range: 1-5) |
| `num_support_calls` | Integer | Support call count | 0, 1, 2 (range: 0-5) |
| `contract_type` | String (Categorical) | Contract length | Month-to-month, One year, Two year |
| `payment_method` | String (Categorical) | Payment type | Electronic, Credit card, Bank transfer, Mailed check |
| `churned` | Integer (Binary) | Churn status | 0 (retained), 1 (churned) |

### Key Field Categories

**Target Variable**: `churned` (0 = Retained: 794 customers, 1 = Churned: 206 customers)

**Categorical Fields**:
- `contract_type`: 3 unique values (Month-to-month: 507, One year: 300, Two year: 193)
- `payment_method`: 4 unique values (Credit card: 263, Mailed check: 259, Electronic: 255, Bank transfer: 223)

**Numerical Fields**:
- **Demographics**: `age` (41 unique values)
- **Usage Metrics**: `tenure_months` (41 unique values), `num_products` (5 values), `num_support_calls` (6 values)
- **Financial**: `monthly_charges`, `total_charges`

---

## 2. Visual Business Questions

### Primary Business Questions (Answerable via Charts)

1. **What is the overall churn rate?**
   - Visual Answer: Pie chart showing retained vs churned proportions

2. **Which contract type has the highest churn risk?**
   - Visual Answer: Stacked bar chart of churn by contract type

3. **Does payment method affect churn rate?**
   - Visual Answer: Grouped bar chart of churn by payment method

4. **How does product count relate to churn?**
   - Visual Answer: Bar chart showing churn rate by number of products

5. **Do support calls correlate with churn?**
   - Visual Answer: Bar chart of average support calls for churned vs retained

6. **What is the age distribution of customers?**
   - Visual Answer: Histogram showing age distribution

7. **How does tenure vary across customers?**
   - Visual Answer: Histogram of tenure months

8. **Are there outliers in monthly charges?**
   - Visual Answer: Box plot of monthly charges

9. **What is the distribution of contract types?**
   - Visual Answer: Bar chart showing contract type frequency

10. **How are payment methods distributed?**
    - Visual Answer: Bar chart showing payment method frequency

---

## 3. Chart Specifications

### Chart 1: Overall Churn Rate (Pie Chart)
- **Type**: Pie Chart
- **Data Source**: `churned` column (value counts)
- **X/Y Axes**: N/A (pie chart)
- **Colors**:
  - Retained (0): Green `#2ecc71`
  - Churned (1): Red `#e74c3c`
- **Labels**: "Retained" (794), "Churned" (206)
- **Title**: "Customer Churn Overview"
- **Annotations**: Percentage labels on each slice (autopct='%1.1f%%')
- **Visual Insight**: Shows overall churn rate at a glance (~20.6%)
- **Output File**: `01_churn_pie.png`

---

### Chart 2: Churn by Contract Type (Grouped Bar Chart)
- **Type**: Grouped Bar Chart
- **Data Source**: Group by `contract_type`, count `churned` values (0 and 1)
- **X-Axis**: Contract types (Month-to-month, One year, Two year)
- **Y-Axis**: Customer count
- **Colors**:
  - Retained: Green `#2ecc71`
  - Churned: Red `#e74c3c`
- **Title**: "Churn Rate by Contract Type"
- **Annotations**: Value labels on bars
- **Grid**: Y-axis grid (alpha=0.3)
- **Visual Insight**: Identify which contract type has highest churn risk
- **Output File**: `02_churn_by_contract.png`

---

### Chart 3: Churn by Payment Method (Grouped Bar Chart)
- **Type**: Grouped Bar Chart
- **Data Source**: Group by `payment_method`, count `churned` values (0 and 1)
- **X-Axis**: Payment methods (Electronic, Credit card, Bank transfer, Mailed check)
- **Y-Axis**: Customer count
- **Colors**:
  - Retained: Green `#2ecc71`
  - Churned: Red `#e74c3c`
- **Title**: "Churn Rate by Payment Method"
- **Annotations**: Value labels on bars
- **Grid**: Y-axis grid (alpha=0.3)
- **Visual Insight**: Identify payment methods associated with higher churn
- **Output File**: `03_churn_by_payment.png`

---

### Chart 4: Churn by Number of Products (Bar Chart)
- **Type**: Bar Chart
- **Data Source**: Group by `num_products`, calculate churn rate (mean of `churned`)
- **X-Axis**: Number of products (1, 2, 3, 4, 5)
- **Y-Axis**: Churn rate (percentage)
- **Colors**: Gradient from Green to Red based on churn rate
- **Title**: "Churn Rate by Number of Products"
- **Annotations**: Percentage labels on bars
- **Grid**: Y-axis grid (alpha=0.3)
- **Visual Insight**: Show if more products reduce churn risk
- **Output File**: `04_churn_by_products.png`

---

### Chart 5: Support Calls vs Churn (Bar Chart)
- **Type**: Bar Chart
- **Data Source**: Group by `num_support_calls`, calculate churn rate (mean of `churned`)
- **X-Axis**: Number of support calls (0, 1, 2, 3, 4, 5)
- **Y-Axis**: Churn rate (percentage)
- **Colors**: Gradient from Green to Red based on churn rate
- **Title**: "Churn Rate by Number of Support Calls"
- **Annotations**: Percentage labels on bars
- **Grid**: Y-axis grid (alpha=0.3)
- **Visual Insight**: Identify if high support calls indicate churn risk
- **Output File**: `05_churn_by_support.png`

---

### Chart 6: Age Distribution (Histogram)
- **Type**: Histogram
- **Data Source**: `age` column
- **X-Axis**: Age (bins=20)
- **Y-Axis**: Frequency (count)
- **Colors**: Blue `#3498db`
- **Title**: "Customer Age Distribution"
- **Grid**: Y-axis grid (alpha=0.3)
- **Styling**: Alpha=0.7, black edges
- **Visual Insight**: Understand customer age demographics
- **Output File**: `06_age_histogram.png`

---

### Chart 7: Tenure Distribution (Histogram)
- **Type**: Histogram
- **Data Source**: `tenure_months` column
- **X-Axis**: Tenure months (bins=20)
- **Y-Axis**: Frequency (count)
- **Colors**: Blue `#3498db`
- **Title**: "Customer Tenure Distribution"
- **Grid**: Y-axis grid (alpha=0.3)
- **Styling**: Alpha=0.7, black edges
- **Visual Insight**: Understand how long customers typically stay
- **Output File**: `07_tenure_histogram.png`

---

### Chart 8: Monthly Charges Distribution (Box Plot)
- **Type**: Box Plot
- **Data Source**: `monthly_charges` column
- **X-Axis**: "Monthly Charges"
- **Y-Axis**: Dollar amount ($)
- **Colors**: Blue `#3498db`
- **Title**: "Monthly Charges Distribution"
- **Grid**: Y-axis grid (alpha=0.3)
- **Visual Insight**: Identify pricing outliers and median charges
- **Output File**: `08_charges_boxplot.png`

---

### Chart 9: Contract Type Distribution (Bar Chart)
- **Type**: Bar Chart
- **Data Source**: `contract_type` value counts
- **X-Axis**: Contract types
- **Y-Axis**: Customer count
- **Colors**: Blue `#3498db`
- **Title**: "Distribution of Contract Types"
- **Annotations**: Count labels on bars
- **Grid**: Y-axis grid (alpha=0.3)
- **Visual Insight**: Show which contract types are most popular
- **Output File**: `09_contract_distribution.png`

---

### Chart 10: Payment Method Distribution (Bar Chart)
- **Type**: Bar Chart
- **Data Source**: `payment_method` value counts
- **X-Axis**: Payment methods
- **Y-Axis**: Customer count
- **Colors**: Blue `#3498db`
- **Title**: "Distribution of Payment Methods"
- **Annotations**: Count labels on bars
- **Grid**: Y-axis grid (alpha=0.3)
- **Visual Insight**: Show which payment methods are most used
- **Output File**: `10_payment_distribution.png`

---

## 4. Task-Based Implementation Plan

### TASK 1: Setup & Configuration
**Subtask 1.1**: Import required libraries
- `from pathlib import Path`
- `import sys`
- `import pandas as pd`
- `import matplotlib.pyplot as plt`
- `import seaborn as sns`
- `import numpy as np`

**Subtask 1.2**: Define color constants
```python
CHURN_RED = '#e74c3c'
RETAIN_GREEN = '#2ecc71'
NEUTRAL_BLUE = '#3498db'
WARNING_ORANGE = '#f39c12'
NEUTRAL_GRAY = '#95a5a6'
```

**Subtask 1.3**: Configure matplotlib style and output directory
```python
plt.style.use('seaborn-v0_8-darkgrid')
OUTPUT_DIR = Path('outputs')
OUTPUT_DIR.mkdir(exist_ok=True)
DPI = 100
```

---

### TASK 2: Data Loading Function
**Subtask 2.1**: Create `load_data()` function with file validation

**Subtask 2.2**: Read CSV file and validate structure
- Check file exists
- Read CSV using pandas
- Validate required columns present

**Subtask 2.3**: Convert string columns to appropriate types
- Convert numeric strings to int/float
- Ensure `churned` is integer (0/1)

**Subtask 2.4**: Return validated DataFrame

**Implementation Pattern**:
```python
def load_data(filepath: str) -> pd.DataFrame:
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    
    df = pd.read_csv(path)
    
    # Type conversions
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df['tenure_months'] = pd.to_numeric(df['tenure_months'], errors='coerce')
    df['monthly_charges'] = pd.to_numeric(df['monthly_charges'], errors='coerce')
    df['total_charges'] = pd.to_numeric(df['total_charges'], errors='coerce')
    df['num_products'] = pd.to_numeric(df['num_products'], errors='coerce')
    df['num_support_calls'] = pd.to_numeric(df['num_support_calls'], errors='coerce')
    df['churned'] = pd.to_numeric(df['churned'], errors='coerce').astype(int)
    
    return df
```

---

### TASK 3: Chart Generation Functions

**TASK 3.1**: Implement `create_churn_pie(df)` - Overall Churn Rate Pie Chart
- Extract churn counts (value_counts)
- Create pie chart with green/red colors
- Add percentage labels
- Save as `01_churn_pie.png`

**TASK 3.2**: Implement `create_churn_by_contract(df)` - Churn by Contract Type
- Group by contract_type and churned
- Create grouped bar chart
- Add value labels on bars
- Save as `02_churn_by_contract.png`

**TASK 3.3**: Implement `create_churn_by_payment(df)` - Churn by Payment Method
- Group by payment_method and churned
- Create grouped bar chart
- Add value labels on bars
- Save as `03_churn_by_payment.png`

**TASK 3.4**: Implement `create_churn_by_products(df)` - Churn Rate by Products
- Group by num_products, calculate churn rate
- Create bar chart with gradient colors
- Add percentage labels
- Save as `04_churn_by_products.png`

**TASK 3.5**: Implement `create_churn_by_support(df)` - Churn Rate by Support Calls
- Group by num_support_calls, calculate churn rate
- Create bar chart with gradient colors
- Add percentage labels
- Save as `05_churn_by_support.png`

**TASK 3.6**: Implement `create_age_histogram(df)` - Age Distribution
- Create histogram of age (20 bins)
- Style with blue color, alpha 0.7
- Save as `06_age_histogram.png`

**TASK 3.7**: Implement `create_tenure_histogram(df)` - Tenure Distribution
- Create histogram of tenure_months (20 bins)
- Style with blue color, alpha 0.7
- Save as `07_tenure_histogram.png`

**TASK 3.8**: Implement `create_charges_boxplot(df)` - Monthly Charges Box Plot
- Create box plot of monthly_charges
- Show outliers
- Save as `08_charges_boxplot.png`

**TASK 3.9**: Implement `create_contract_distribution(df)` - Contract Type Distribution
- Get value counts of contract_type
- Create bar chart with count labels
- Save as `09_contract_distribution.png`

**TASK 3.10**: Implement `create_payment_distribution(df)` - Payment Method Distribution
- Get value counts of payment_method
- Create bar chart with count labels
- Save as `10_payment_distribution.png`

---

### TASK 4: Main Execution Function
**Subtask 4.1**: Create `main()` function

**Subtask 4.2**: Print execution header and load data
```python
print("=" * 50)
print("CUSTOMER CHURN VISUALIZATION TASK")
print("=" * 50)
print("\n[1/11] Loading data...")
df = load_data('data/customer_churn.csv')
print(f"  Loaded {len(df):,} rows × {len(df.columns)} columns")
```

**Subtask 4.3**: Call all chart functions in sequence
```python
print("\n[2/11] Creating Chart 1: Churn Pie...")
create_churn_pie(df)

print("[3/11] Creating Chart 2: Churn by Contract...")
create_churn_by_contract(df)

# ... (continue for all 10 charts)
```

**Subtask 4.4**: Print completion summary
```python
print("\n" + "=" * 50)
print("✅ COMPLETED: All 10 charts generated")
print("=" * 50)
print(f"Output location: {OUTPUT_DIR}")
```

**Subtask 4.5**: Add entry point
```python
if __name__ == '__main__':
    main()
```

---

### TASK 5: Quality Assurance
**Subtask 5.1**: Verify all charts use correct DPI (100)

**Subtask 5.2**: Verify consistent color palette across all charts

**Subtask 5.3**: Verify all 10 output PNG files created successfully

**Subtask 5.4**: Test execution time (target: < 10 seconds)

**Subtask 5.5**: Validate no errors or warnings during execution

---

## 5. APPENDIX: Data Dictionary

### Field Specifications

#### `customer_id`
- **Type**: Integer
- **Format**: Sequential numeric ID
- **Range**: 1 to 1000
- **Unique Count**: 1000 (100% unique)
- **Business Meaning**: Unique identifier for each customer record
- **Usage in Charts**: Not visualized (used as index/reference only)

#### `age`
- **Type**: Integer (Numerical - Continuous)
- **Format**: Years
- **Range**: 18 to 72 years
- **Unique Count**: 41 distinct ages
- **Sample Values**: 18, 19, 22, 23, 25, 26, 27, 29, 31, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44, 46, 47, 48, 49, 50, 52, 53, 54, 56, 57, 60, 66, 67, 68, 72
- **Business Meaning**: Customer's age at time of data collection
- **Usage in Charts**: Chart 6 (Age Distribution Histogram)

#### `tenure_months`
- **Type**: Integer (Numerical - Continuous)
- **Format**: Months
- **Range**: 0 to 72 months (0-6 years)
- **Unique Count**: 41 distinct tenure values
- **Sample Values**: 0, 1, 2, 4, 5, 6, 7, 9, 14, 16, 17, 18, 19, 24, 25, 27, 29, 30, 31, 32, 37, 38, 40, 48, 49, 54, 66, 72
- **Business Meaning**: Number of months customer has been with the service
- **Usage in Charts**: Chart 7 (Tenure Distribution Histogram)

#### `monthly_charges`
- **Type**: Float (Numerical - Continuous)
- **Format**: Dollar amount (USD)
- **Range**: $20.00 to $122.04
- **Sample Values**: $20.00, $32.29, $35.38, $38.26, $41.12, $42.44, $43.43, $45.50, $46.63, $50.51, $55.42, $55.72, $56.94, $58.25, $58.66, $61.06, $62.04, $65.56, $65.63, $67.31, $68.45, $69.40, $71.40, $71.99, $73.01, $73.61, $74.58, $78.26, $80.26, $85.14, $86.25, $91.85, $91.91, $93.59, $97.28, $105.21, $107.33, $113.37, $122.04
- **Business Meaning**: Amount customer pays per month for services
- **Usage in Charts**: Chart 8 (Monthly Charges Box Plot)

#### `total_charges`
- **Type**: Float (Numerical - Continuous)
- **Format**: Dollar amount (USD)
- **Range**: $0.00 to $5,554.96
- **Sample Values**: $0.00, $40.00, $60.20, $80.00, $84.87, $161.44, $222.89, $244.07, $277.62, $280.00, $303.05, $344.38, $349.53, $459.53, $480.00, $566.15, $603.73, $800.00, $831.21, $875.52, $1,007.95, $1,160.18, $1,241.23, $1,466.65, $1,492.06, $1,532.52, $1,562.53, $1,606.74, $1,662.85, $1,789.81, $1,956.46, $2,019.17, $2,070.48, $2,079.61, $2,282.03, $2,488.11, $2,625.57, $2,897.86, $3,051.19, $3,275.99, $3,411.73, $4,099.97, $4,492.52, $4,517.75, $5,044.29, $5,554.96
- **Business Meaning**: Total amount customer has paid over their lifetime
- **Usage in Charts**: Not directly visualized (derived metric)

#### `num_products`
- **Type**: Integer (Categorical - Ordinal)
- **Format**: Count (1-5)
- **Unique Values**: 5 distinct counts
- **Distribution**:
  - 1 product: 399 customers (39.9%)
  - 2 products: 272 customers (27.2%)
  - 3 products: 197 customers (19.7%)
  - 4 products: 96 customers (9.6%)
  - 5 products: 36 customers (3.6%)
- **Business Meaning**: Number of products/services customer subscribes to
- **Usage in Charts**: Chart 4 (Churn Rate by Number of Products)

#### `num_support_calls`
- **Type**: Integer (Categorical - Ordinal)
- **Format**: Count (0-5)
- **Unique Values**: 6 distinct counts
- **Distribution**:
  - 0 calls: 359 customers (35.9%)
  - 1 call: 400 customers (40.0%)
  - 2 calls: 179 customers (17.9%)
  - 3 calls: 54 customers (5.4%)
  - 4 calls: 6 customers (0.6%)
  - 5 calls: 2 customers (0.2%)
- **Business Meaning**: Number of times customer called support
- **Usage in Charts**: Chart 5 (Churn Rate by Number of Support Calls)

#### `contract_type`
- **Type**: String (Categorical - Nominal)
- **Format**: Contract length description
- **Unique Values**: 3 distinct types
- **Distribution**:
  - "Month-to-month": 507 customers (50.7%)
  - "One year": 300 customers (30.0%)
  - "Two year": 193 customers (19.3%)
- **Business Meaning**: Type of service contract customer has signed
- **Usage in Charts**: 
  - Chart 2 (Churn by Contract Type)
  - Chart 9 (Contract Type Distribution)

#### `payment_method`
- **Type**: String (Categorical - Nominal)
- **Format**: Payment method description
- **Unique Values**: 4 distinct types
- **Distribution**:
  - "Credit card": 263 customers (26.3%)
  - "Mailed check": 259 customers (25.9%)
  - "Electronic": 255 customers (25.5%)
  - "Bank transfer": 223 customers (22.3%)
- **Business Meaning**: How customer pays their monthly bill
- **Usage in Charts**: 
  - Chart 3 (Churn by Payment Method)
  - Chart 10 (Payment Method Distribution)

#### `churned`
- **Type**: Integer (Binary - Target Variable)
- **Format**: 0 or 1
- **Unique Values**: 2 (binary classification)
- **Distribution**:
  - 0 (Retained): 794 customers (79.4%)
  - 1 (Churned): 206 customers (20.6%)
- **Business Meaning**: Whether customer has churned (left the service)
- **Usage in Charts**: 
  - Chart 1 (Overall Churn Pie)
  - Chart 2 (Churn by Contract)
  - Chart 3 (Churn by Payment)
  - Chart 4 (Churn by Products)
  - Chart 5 (Churn by Support Calls)
- **Key Metric**: Churn Rate = 20.6%

---

## Implementation Notes

### For @data-dev Agent:
1. **Follow Task-Based Plan**: Implement tasks 1-5 sequentially
2. **Chart Functions**: Create one function per chart (10 functions total)
3. **Sequential File Naming**: Use 01_, 02_, ..., 10_ prefix for outputs
4. **Color Consistency**: Use defined color constants throughout
5. **Error Handling**: Add try-except blocks for file operations
6. **Progress Output**: Print status after each chart generation
7. **Data Validation**: Validate data types in load_data() function

### Expected Output:
- **File**: `task.py` (approximately 400-500 lines)
- **Dependencies**: `requirements.txt` (pandas, matplotlib, seaborn)
- **Execution Time**: < 10 seconds
- **Output Files**: 10 PNG files in `outputs/` directory

### Success Criteria:
- ✅ All 10 charts generated successfully
- ✅ No syntax errors or smart quotes
- ✅ Consistent styling across all visualizations
- ✅ Clear progress messages during execution
- ✅ All output files saved to `outputs/` directory

---

## Document Metadata

**Specification Version**: 1.0  
**Created By**: DataWinston (@data-architect)  
**Creation Date**: 2026-01-02  
**Target Implementation**: Python (pandas, matplotlib, seaborn)  
**Implementation Agent**: @data-dev  
**Execution Agent**: @run-agent  
**Total Charts**: 10  
**Total Tasks**: 5 (with 37 subtasks)
