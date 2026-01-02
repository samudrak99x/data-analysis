# Customer Churn - BI Chart Specification

**Dataset:** `customer_churn.csv`  
**Created:** January 2, 2026  
**Specification Type:** Chart-Only Visualization Plan  
**Role:** BI Visualization Architect (Specification Only - No Code, No Statistics)

---

## 📋 DATASET SCHEMA BRIEF

**File Information:**
- Format: CSV (ASCII, comma-delimited)
- Size: 73.8 KB
- Records: 1,000 customers
- Fields: 10 columns
- Data Quality: ✅ No missing values

**Column Structure:**

| Field | Type | Unique | Description |
|-------|------|--------|-------------|
| customer_id | Numeric | 100 | Customer identifier |
| age | Numeric | 41 | Customer age |
| tenure_months | Numeric | 41 | Months with company |
| monthly_charges | Numeric | 91 | Monthly bill amount |
| total_charges | Numeric | 98 | Lifetime charges |
| num_products | Numeric | 5 | Products owned (1-5) |
| num_support_calls | Numeric | 5 | Support interactions (0-4+) |
| contract_type | Categorical | 3 | Month-to-month, One year, Two year |
| payment_method | Categorical | 4 | Credit card, Mailed check, Electronic, Bank transfer |
| churned | Binary | 2 | 0=Retained, 1=Churned |

**Key Categorical Distributions:**
- **Contract Types:** Month-to-month (507), One year (300), Two year (193)
- **Payment Methods:** Credit card (263), Mailed check (259), Electronic (255), Bank transfer (223)
- **Churn Status:** Retained (794), Churned (206)

---

## 🎯 VISUAL BUSINESS QUESTIONS

The following questions can be answered through visual chart analysis:

1. **What is the overall churn rate distribution?**  
   → Visual: Pie/Donut chart showing retained vs churned proportions

2. **Which contract types have highest churn rates?**  
   → Visual: Bar chart comparing churn rates across contract types

3. **How does support call frequency correlate with churn?**  
   → Visual: Bar chart showing churn rate by number of support calls

4. **Which payment methods show different churn patterns?**  
   → Visual: Grouped bar chart of churn by payment method

5. **How does product ownership affect retention?**  
   → Visual: Bar chart of churn rate by number of products

6. **What's the relationship between tenure and churn?**  
   → Visual: Histogram/distribution showing tenure patterns for churned vs retained

7. **How does age distribution differ between churned and retained customers?**  
   → Visual: Side-by-side histogram or box plot

8. **What are the monthly charge patterns for churned vs retained?**  
   → Visual: Box plot or violin plot comparison

9. **How do multiple factors combine to show risk patterns?**  
   → Visual: Stacked bar showing contract type + product count interaction

10. **What's the demographic overview of our customer base?**  
    → Visual: Multi-panel dashboard showing age, tenure, charges distributions

---

## 📊 CHART SPECIFICATIONS

### CHART 1: Overall Churn Distribution
**Chart Type:** Pie Chart  
**Purpose:** Show proportion of churned vs retained customers  
**Data Required:**
- Count of churned=0 (Retained)
- Count of churned=1 (Churned)
- Calculate percentages

**Visual Specifications:**
- Colors: Green (#2ecc71) for Retained, Red (#e74c3c) for Churned
- Labels: Show both count and percentage
- Title: "Customer Churn Distribution"
- Legend: Bottom position
- Size: 600x400px

**Output:** `churn_distribution_pie.png`

---

### CHART 2: Churn Rate by Contract Type
**Chart Type:** Bar Chart  
**Purpose:** Compare churn rates across different contract types  
**Data Required:**
- Group by contract_type
- For each group: count total customers, count churned customers
- Calculate churn rate percentage for each contract type

**Visual Specifications:**
- X-axis: Contract types (Month-to-month, One year, Two year)
- Y-axis: Churn Rate (%)
- Bar Colors: Red gradient based on churn rate intensity
- Add value labels on top of each bar
- Title: "Churn Rate by Contract Type"
- Y-axis range: 0-100%
- Size: 800x500px

**Output:** `churn_by_contract.png`

---

### CHART 3: Churn Rate by Support Calls
**Chart Type:** Bar Chart  
**Purpose:** Identify correlation between support calls and churn  
**Data Required:**
- Group by num_support_calls (0, 1, 2, 3, 4+)
- For each group: count total, count churned
- Calculate churn rate percentage

**Visual Specifications:**
- X-axis: Number of Support Calls
- Y-axis: Churn Rate (%)
- Bar Colors: Color intensity increases with call count (yellow to red gradient)
- Add value labels on bars
- Title: "Churn Rate by Number of Support Calls"
- Highlight 3+ calls as high risk zone
- Size: 800x500px

**Output:** `churn_by_support_calls.png`

---

### CHART 4: Churn Rate by Payment Method
**Chart Type:** Grouped Bar Chart  
**Purpose:** Compare churn patterns across payment methods  
**Data Required:**
- Group by payment_method
- For each method: count total, count churned, count retained
- Calculate churn rate percentage

**Visual Specifications:**
- X-axis: Payment Methods
- Y-axis: Customer Count
- Two bars per method: Churned (red) and Retained (green)
- Title: "Customer Status by Payment Method"
- Legend: Top right
- Size: 900x500px

**Output:** `churn_by_payment.png`

---

### CHART 5: Churn Rate by Number of Products
**Chart Type:** Bar Chart  
**Purpose:** Show how product ownership affects retention  
**Data Required:**
- Group by num_products (1, 2, 3, 4, 5)
- For each group: count total, count churned
- Calculate churn rate percentage

**Visual Specifications:**
- X-axis: Number of Products
- Y-axis: Churn Rate (%)
- Bar Colors: Green gradient (lower churn = darker green)
- Add value labels on bars
- Title: "Churn Rate by Product Portfolio Size"
- Size: 800x500px

**Output:** `churn_by_products.png`

---

### CHART 6: Tenure Distribution Comparison
**Chart Type:** Overlapping Histogram  
**Purpose:** Compare tenure patterns between churned and retained customers  
**Data Required:**
- Tenure values for churned=0
- Tenure values for churned=1
- Bin size: 5 months

**Visual Specifications:**
- X-axis: Tenure (months)
- Y-axis: Customer Count
- Two overlapping histograms: Retained (blue, alpha=0.6), Churned (red, alpha=0.6)
- Title: "Tenure Distribution: Churned vs Retained Customers"
- Legend: Top right
- Size: 900x500px

**Output:** `tenure_distribution.png`

---

### CHART 7: Age Distribution Comparison
**Chart Type:** Box Plot (Side-by-Side)  
**Purpose:** Show age patterns for churned vs retained customers  
**Data Required:**
- Age values for churned=0
- Age values for churned=1

**Visual Specifications:**
- X-axis: Customer Status (Retained, Churned)
- Y-axis: Age
- Box Colors: Green for Retained, Red for Churned
- Show median line, quartiles, and outliers
- Title: "Age Distribution: Churned vs Retained"
- Size: 700x500px

**Output:** `age_boxplot.png`

---

### CHART 8: Monthly Charges Distribution
**Chart Type:** Violin Plot  
**Purpose:** Compare monthly charge patterns  
**Data Required:**
- Monthly_charges values for churned=0
- Monthly_charges values for churned=1

**Visual Specifications:**
- X-axis: Customer Status
- Y-axis: Monthly Charges ($)
- Colors: Green for Retained, Red for Churned
- Show median line
- Title: "Monthly Charges Distribution: Churned vs Retained"
- Size: 700x500px

**Output:** `charges_violin.png`

---

### CHART 9: Contract Type + Product Count Heatmap
**Chart Type:** Stacked Bar Chart  
**Purpose:** Show interaction between contract type and product count  
**Data Required:**
- Group by contract_type and num_products
- Count customers in each combination
- Separate by churn status

**Visual Specifications:**
- X-axis: Contract Type
- Y-axis: Customer Count
- Stacks: Different colors for each product count (1-5)
- Title: "Customer Segmentation: Contract Type × Product Count"
- Legend: Right side
- Size: 900x600px

**Output:** `contract_product_stack.png`

---

### CHART 10: Dashboard Overview (Multi-Panel)
**Chart Type:** 2×2 Grid of Small Charts  
**Purpose:** Executive summary dashboard  
**Charts Included:**
1. Top-left: Churn pie chart
2. Top-right: Contract type churn rates
3. Bottom-left: Support calls churn rates
4. Bottom-right: Product count churn rates

**Visual Specifications:**
- Overall size: 1200x900px
- Each subplot: 500x400px
- Consistent color scheme across all panels
- Main title: "Customer Churn Analysis Dashboard"
- Tight layout for clean presentation

**Output:** `dashboard_overview.png`

---

## 🛠️ TASK-BASED IMPLEMENTATION PLAN (task.py Blueprint)

This is a step-by-step blueprint for the developer to implement ALL charts.

### TASK 1: Setup & Configuration
**Purpose:** Initialize environment and define constants

**Subtasks:**
- Task 1.1: Import required libraries (pandas, matplotlib, seaborn, numpy)
- Task 1.2: Define color palette constants (CHURN_RED, RETAIN_GREEN, etc.)
- Task 1.3: Define output directory path (`outputs/`)
- Task 1.4: Set matplotlib style and defaults (figure size, font sizes)
- Task 1.5: Create output directory if it doesn't exist

**Expected Code Structure:**
```python
# Task 1: Imports & Configuration
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

# Color scheme
CHURN_RED = '#e74c3c'
RETAIN_GREEN = '#2ecc71'
...

# Output configuration
OUTPUT_DIR = Path('outputs')
OUTPUT_DIR.mkdir(exist_ok=True)
```

---

### TASK 2: Data Loading & Validation
**Purpose:** Load dataset and verify structure

**Subtasks:**
- Task 2.1: Create `load_data()` function
- Task 2.2: Read CSV file into DataFrame
- Task 2.3: Verify expected columns exist
- Task 2.4: Check for missing values
- Task 2.5: Convert data types if needed (ensure numeric columns are numeric)
- Task 2.6: Print data summary (shape, columns, sample)
- Task 2.7: Return validated DataFrame

**Expected Function Signature:**
```python
def load_data(filepath: str) -> pd.DataFrame:
    """Load and validate customer churn dataset"""
    # Implementation here
    return df
```

---

### TASK 3: Chart Generation Functions
**Purpose:** Create individual chart generation functions

#### Task 3.1: Overall Churn Distribution (Pie Chart)
**Function:** `create_churn_pie_chart(df)`
- Calculate churn counts
- Create pie chart with specified colors
- Add percentage labels
- Save to `outputs/churn_distribution_pie.png`

#### Task 3.2: Churn by Contract Type (Bar Chart)
**Function:** `create_contract_churn_chart(df)`
- Group by contract_type
- Calculate churn rate for each group
- Create bar chart with red gradient
- Add value labels on bars
- Save to `outputs/churn_by_contract.png`

#### Task 3.3: Churn by Support Calls (Bar Chart)
**Function:** `create_support_calls_chart(df)`
- Group by num_support_calls
- Calculate churn rates
- Create bar chart with yellow-to-red gradient
- Highlight high-risk zone (3+ calls)
- Save to `outputs/churn_by_support_calls.png`

#### Task 3.4: Churn by Payment Method (Grouped Bar)
**Function:** `create_payment_method_chart(df)`
- Group by payment_method and churned
- Count customers in each group
- Create grouped bar chart (churned vs retained)
- Save to `outputs/churn_by_payment.png`

#### Task 3.5: Churn by Products (Bar Chart)
**Function:** `create_products_chart(df)`
- Group by num_products
- Calculate churn rates
- Create bar chart with green gradient
- Save to `outputs/churn_by_products.png`

#### Task 3.6: Tenure Distribution (Histogram)
**Function:** `create_tenure_histogram(df)`
- Separate tenure data by churn status
- Create overlapping histograms
- Use semi-transparent colors
- Save to `outputs/tenure_distribution.png`

#### Task 3.7: Age Distribution (Box Plot)
**Function:** `create_age_boxplot(df)`
- Prepare age data for churned and retained
- Create side-by-side box plots
- Use specified colors
- Save to `outputs/age_boxplot.png`

#### Task 3.8: Monthly Charges (Violin Plot)
**Function:** `create_charges_violin(df)`
- Prepare monthly_charges by churn status
- Create violin plot comparison
- Save to `outputs/charges_violin.png`

#### Task 3.9: Contract × Product Interaction (Stacked Bar)
**Function:** `create_contract_product_stack(df)`
- Group by contract_type and num_products
- Count combinations
- Create stacked bar chart
- Save to `outputs/contract_product_stack.png`

#### Task 3.10: Dashboard Overview (Multi-Panel)
**Function:** `create_dashboard(df)`
- Create 2×2 subplot grid
- Call mini versions of charts 1, 2, 3, 5
- Arrange in grid layout
- Save to `outputs/dashboard_overview.png`

**Expected Structure for Each Function:**
```python
def create_churn_pie_chart(df: pd.DataFrame) -> str:
    """Generate overall churn distribution pie chart"""
    # Data preparation
    # Chart creation
    # Styling
    # Save file
    return output_path
```

---

### TASK 4: Main Execution Function
**Purpose:** Orchestrate all chart generation

**Subtasks:**
- Task 4.1: Create `main()` function
- Task 4.2: Print execution start message
- Task 4.3: Call `load_data()` function
- Task 4.4: Call each chart function sequentially (Task 3.1 through 3.10)
- Task 4.5: Track which charts were successfully created
- Task 4.6: Print summary of generated charts
- Task 4.7: Handle any errors gracefully (try/except blocks)

**Expected Structure:**
```python
def main():
    """Main execution function"""
    print("Starting Customer Churn Chart Generation...")
    
    # Load data
    df = load_data('data/customer_churn.csv')
    
    # Generate all charts
    charts_created = []
    
    try:
        charts_created.append(create_churn_pie_chart(df))
        charts_created.append(create_contract_churn_chart(df))
        # ... call all chart functions
    except Exception as e:
        print(f"Error: {e}")
    
    print(f"✓ Generated {len(charts_created)} charts")
    
if __name__ == "__main__":
    main()
```

---

### TASK 5: Quality Assurance & Documentation
**Purpose:** Ensure code quality and maintainability

**Subtasks:**
- Task 5.1: Add docstrings to all functions
- Task 5.2: Add inline comments for complex logic
- Task 5.3: Verify all charts are saved to correct paths
- Task 5.4: Test with actual dataset
- Task 5.5: Verify output file naming matches specification
- Task 5.6: Check color consistency across all charts
- Task 5.7: Ensure all titles and labels are correctly formatted

**Implementation Notes:**
- Each function should have a docstring explaining purpose, parameters, and return value
- Complex calculations should have explanatory comments
- Use consistent naming conventions
- Handle edge cases (empty groups, division by zero)

---

## 📊 EXPECTED OUTPUTS

When the developer implements this specification, the following files should be generated:

```
outputs/
├── churn_distribution_pie.png         # Chart 1
├── churn_by_contract.png              # Chart 2
├── churn_by_support_calls.png         # Chart 3
├── churn_by_payment.png               # Chart 4
├── churn_by_products.png              # Chart 5
├── tenure_distribution.png            # Chart 6
├── age_boxplot.png                    # Chart 7
├── charges_violin.png                 # Chart 8
├── contract_product_stack.png         # Chart 9
└── dashboard_overview.png             # Chart 10
```

**Total Charts:** 10 visualization files

---

## 🎨 VISUAL DESIGN GUIDELINES

### Color Palette
- **Churn (Negative):** #e74c3c (Red)
- **Retained (Positive):** #2ecc71 (Green)
- **Neutral/Info:** #3498db (Blue)
- **Warning:** #f39c12 (Orange)
- **Gradients:** Use color intensity to show severity/magnitude

### Typography
- **Chart Titles:** 14pt, Bold
- **Axis Labels:** 11pt, Regular
- **Value Labels:** 9pt, Regular
- **Legend:** 10pt, Regular

### Layout
- Consistent figure sizes per chart type
- White background with light gray grid
- Clear axis labels with units
- Legends placed to not obscure data
- Adequate spacing between elements

---

## 🚫 ARCHITECT ROLE BOUNDARIES

**This specification provides:**
- ✅ Business questions to answer
- ✅ Chart types and visual specifications
- ✅ Data grouping and aggregation requirements
- ✅ Color schemes and styling guidelines
- ✅ Task-based implementation blueprint
- ✅ Expected output structure

**This specification does NOT include:**
- ❌ Actual Python code implementation
- ❌ Statistical calculations or analysis
- ❌ Machine learning or predictive modeling
- ❌ Data cleaning or transformation code
- ❌ Feature engineering
- ❌ Missing value handling

**Next Step:** Hand this specification to `@data-dev` agent to implement the code in `task.py`

---

## 📚 APPENDIX: DATA DICTIONARY

### Customer Identification
**customer_id**
- Type: Numeric (Integer)
- Description: Unique customer identifier
- Range: 1-100 (appears to be customer segment IDs, with multiple records per ID)
- Unique Values: 100
- Business Use: Customer tracking and grouping

---

### Demographic Fields

**age**
- Type: Numeric (Integer)
- Description: Customer age in years
- Range: 18-80 years (based on unique count of 41)
- Unique Values: 41
- Business Use: Age-based segmentation, demographic analysis
- Notes: Representative of adult customer base

**tenure_months**
- Type: Numeric (Integer)
- Description: Number of months customer has been with company
- Range: 1-40+ months (based on unique count of 41)
- Unique Values: 41
- Business Use: Loyalty analysis, retention patterns
- Notes: Critical field for churn prediction - longer tenure typically indicates loyalty

---

### Financial Fields

**monthly_charges**
- Type: Numeric (Float)
- Description: Current monthly billing amount in dollars
- Range: Approximately $25-$120 (inferred from sample values)
- Unique Values: 91 distinct price points
- Business Use: Revenue analysis, pricing tier identification
- Format: Decimal values with high precision
- Notes: Continuous variable, useful for revenue segmentation

**total_charges**
- Type: Numeric (Float)
- Description: Cumulative total amount customer has paid to date
- Range: Wide range from $50 to $4000+ (inferred)
- Unique Values: 98 distinct values
- Business Use: Customer lifetime value calculation, spending pattern analysis
- Formula: Approximately `monthly_charges × tenure_months` (may vary due to price changes)
- Notes: Indicator of customer value and engagement

---

### Product & Service Usage

**num_products**
- Type: Numeric (Integer)
- Description: Count of products/services customer has subscribed to
- Range: 1-5 products
- Unique Values: 5 (1, 2, 3, 4, 5)
- Business Use: Cross-sell effectiveness, product bundle analysis
- Distribution: Varies (see categorical interpretation)
- Notes: Higher product count may indicate higher engagement and lower churn risk

**num_support_calls**
- Type: Numeric (Integer)
- Description: Number of customer support interactions
- Range: 0-4+ calls
- Unique Values: 5 levels (0, 1, 2, 3, 4+)
- Business Use: Service quality indicator, churn risk signal
- Warning Sign: High support call counts (3-4+) may indicate dissatisfaction
- Notes: Critical field for identifying at-risk customers

---

### Contract & Payment Fields

**contract_type**
- Type: Categorical (String)
- Description: Type of contract customer has signed
- Categories: 
  - "Month-to-month" (507 customers, 50.7%)
  - "One year" (300 customers, 30.0%)
  - "Two year" (193 customers, 19.3%)
- Unique Values: 3
- Business Use: Commitment level analysis, contract optimization
- Business Impact: Critical churn predictor - month-to-month contracts typically have higher churn
- Notes: Imbalanced distribution with majority on flexible contracts

**payment_method**
- Type: Categorical (String)
- Description: How customer pays their bill
- Categories:
  - "Credit card" (263 customers, 26.3%)
  - "Mailed check" (259 customers, 25.9%)
  - "Electronic" (255 customers, 25.5%)
  - "Bank transfer" (223 customers, 22.3%)
- Unique Values: 4
- Business Use: Payment processing analysis, friction point identification
- Distribution: Relatively balanced across all methods
- Notes: Payment method may correlate with customer demographics and tech-savviness

---

### Target Variable

**churned**
- Type: Binary (Integer)
- Description: Whether customer has churned (left the service)
- Values:
  - 0 = Retained/Active (794 customers, 79.4%)
  - 1 = Churned/Inactive (206 customers, 20.6%)
- Unique Values: 2
- Business Use: Target variable for churn prediction, retention analysis
- Class Balance: Imbalanced (approximately 4:1 ratio)
- Notes: This is the outcome variable that all other fields help predict

---

### Data Quality Summary
- **Missing Values:** 0 across all fields ✅
- **Total Records:** 1,000 customer records
- **Total Fields:** 10 columns
- **Data Integrity:** High quality, ready for analysis
- **Encoding:** ASCII (simple, no special characters)

---

### Business Context Notes

**Churn Rate:** 20.6% overall churn rate indicates moderate customer turnover

**Key Relationships to Explore:**
- Contract type → Churn (likely strong relationship)
- Support calls → Churn (high call counts = risk signal)
- Tenure → Churn (longer tenure = more stable)
- Product count → Churn (more products = more "stickiness")

**Segmentation Opportunities:**
- High-value customers (high total_charges, multiple products, long tenure)
- At-risk customers (month-to-month, high support calls, short tenure)
- Stable customers (long contracts, low support calls, multiple products)

---

**END OF SPECIFICATION**

This document provides complete visual specification for chart development.  
Implementation → `@data-dev` agent  
Execution → `@run-agent`