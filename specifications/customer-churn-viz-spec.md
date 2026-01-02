# Customer Churn BI Visualization Specification

**Created**: 2026-01-02  
**Analyst**: DataWinston (BI Visualization Architect)  
**Dataset**: customer_churn.csv (1,000 customers, 10 fields)  
**Analysis Type**: Descriptive BI Visualization (NO machine learning)  
**Focus**: Charts, dashboards, and statistics to understand churn patterns

---

## SECTION 1: DATASET SCHEMA BRIEF

### File Information
- **Type**: CSV
- **Size**: 73.8KB  
- **Encoding**: ASCII
- **Rows**: 1,000 customers
- **Columns**: 10 fields

### Row Grain
**One row = One customer** with their profile, service usage, and churn status

### Key Columns Analysis

#### ID Column
- `customer_id` (string) - 100 unique values, no nulls

#### Demographic
- `age` (string→numeric) - 41 unique values, range ~20-80 years

#### Service Metrics
- `tenure_months` (string→numeric) - Customer lifetime in months
- `monthly_charges` (string→numeric) - Current monthly bill amount
- `total_charges` (string→numeric) - Lifetime revenue from customer
- `num_products` (string→numeric) - Product portfolio size (1-5)
- `num_support_calls` (string→numeric) - Support interaction count (0-5)

#### Categorical Dimensions
- **contract_type** (3 values):
  - Month-to-month: 507 customers (50.7%)
  - One year: 300 customers (30.0%)
  - Two year: 193 customers (19.3%)

- **payment_method** (4 values):
  - Credit card: 263 customers
  - Mailed check: 259 customers
  - Electronic: 255 customers
  - Bank transfer: 223 customers

#### Target Variable
- **churned** (binary):
  - 0 (Retained): 794 customers (79.4%)
  - 1 (Churned): 206 customers (20.6%)

### Data Quality Notes
- **No missing values**: All fields have 100% coverage
- **Type conversions needed**: Numeric fields stored as strings
- **Data cleanliness**: No obvious anomalies from sample inspection

---

## SECTION 2: BUSINESS QUESTIONS IDENTIFICATION

### Visual Questions to Answer

1. **Q1**: What is our overall customer churn rate?
2. **Q2**: Which contract type has the highest churn rate?
3. **Q3**: How does churn vary by number of products owned?
4. **Q4**: What is the relationship between support calls and churn?
5. **Q5**: Which payment method has the best retention?
6. **Q6**: How does tenure relate to churn risk?
7. **Q7**: What is the age distribution of churned vs retained customers?
8. **Q8**: How do monthly charges differ between churners and non-churners?
9. **Q9**: What are the customer segments by contract type and product count?
10. **Q10**: How does total revenue vary by payment method and churn status?

---

## SECTION 3: VISUALIZATION SPECIFICATIONS

### Overview Charts

#### Chart 1: Overall Churn Rate (Pie Chart)
```yaml
visualization_name: "Overall Customer Churn Distribution"
chart_type: "Pie Chart"
purpose: "Show overall retention vs churn rate"
business_question: Q1

specification:
  data_preparation: "Count customers by churned status"
  segments:
    - label: "Retained Customers"
      value: "Count where churned=0"
      color: "#2ecc71"  # Green
    - label: "Churned Customers"
      value: "Count where churned=1"
      color: "#e74c3c"  # Red
  annotations: "Show percentages on pie slices"
  title: "Customer Churn Distribution"
  legend: "Bottom center, 2 columns"
  
output_file: "01_churn_pie.png"
business_insight: "Establishes baseline churn rate for comparison"
```

### Segmentation Analysis

#### Chart 2: Churn by Contract Type (Grouped Bar)
```yaml
visualization_name: "Churn Rate by Contract Type"
chart_type: "Grouped Bar Chart"
purpose: "Compare churn rates across contract types"
business_question: Q2

specification:
  data_preparation: "Group by contract_type, calculate churn rate"
  x_axis: "Contract Type (Month-to-month, One year, Two year)"
  y_axis: "Churn Rate (%)"
  bars:
    - metric: "Churn Rate"
      color: "#e74c3c"  # Red
  annotations: "Display percentage values on bars"
  sort_order: "Descending by churn rate"
  title: "Churn Rate by Contract Type"
  y_limit: "0-100%"
  grid: "Horizontal gridlines, alpha=0.3"
  
output_file: "02_churn_by_contract.png"
business_insight: "Identifies if flexible contracts have higher churn"
```

#### Chart 3: Churn by Payment Method (Stacked Bar)
```yaml
visualization_name: "Customer Status by Payment Method"
chart_type: "Stacked Bar Chart"
purpose: "Show retention patterns by payment type"
business_question: Q5

specification:
  data_preparation: "Group by payment_method and churned, count customers"
  x_axis: "Payment Method (4 categories)"
  y_axis: "Customer Count"
  stacks:
    - segment: "Retained"
      color: "#2ecc71"  # Green
    - segment: "Churned"
      color: "#e74c3c"  # Red
  annotations: "None"
  title: "Customer Status by Payment Method"
  legend: "Upper right"
  rotation: "15 degrees for x-labels"
  
output_file: "03_churn_by_payment.png"
business_insight: "Reveals if payment convenience affects retention"
```

#### Chart 4: Churn by Product Portfolio (Bar Chart)
```yaml
visualization_name: "Churn Rate by Number of Products"
chart_type: "Bar Chart"
purpose: "Analyze relationship between product count and churn"
business_question: Q3

specification:
  data_preparation: "Group by num_products, calculate churn rate"
  x_axis: "Number of Products (1-5)"
  y_axis: "Churn Rate (%)"
  colors: "Gradient from green (low churn) to red (high churn)"
  annotations: "Display percentage values on bars"
  title: "Churn Rate by Product Portfolio Size"
  y_limit: "Dynamic based on max rate + 20%"
  grid: "Horizontal gridlines, alpha=0.3"
  
output_file: "04_churn_by_products.png"
business_insight: "Shows if product diversification improves retention"
```

#### Chart 5: Churn by Support Calls (Bar Chart with Gradient)
```yaml
visualization_name: "Churn Rate by Number of Support Calls"
chart_type: "Bar Chart"
purpose: "Understand correlation between support needs and churn"
business_question: Q4

specification:
  data_preparation: "Group by num_support_calls, calculate churn rate"
  x_axis: "Number of Support Calls (0-5)"
  y_axis: "Churn Rate (%)"
  colors:
    - 0 calls: "#f1c40f"  # Yellow (low)
    - 1-2 calls: "#f39c12"  # Orange (medium)
    - 3-4 calls: "#e67e22"  # Dark orange (high)
    - 5 calls: "#e74c3c"  # Red (very high)
  annotations: "Display percentage values on bars"
  title: "Churn Rate by Number of Support Calls"
  y_limit: "Dynamic"
  grid: "Horizontal gridlines, alpha=0.3"
  
output_file: "05_churn_by_support.png"
business_insight: "High support calls may indicate dissatisfaction risk"
```

### Distribution Analysis

#### Chart 6: Age Distribution (Box Plot)
```yaml
visualization_name: "Age Distribution: Churned vs Retained"
chart_type: "Box Plot"
purpose: "Compare age distributions between segments"
business_question: Q7

specification:
  data_preparation: "Split age by churned status"
  x_axis: "Customer Status (Retained, Churned)"
  y_axis: "Age (years)"
  boxes:
    - group: "Retained"
      color: "#2ecc71"  # Green
    - group: "Churned"
      color: "#e74c3c"  # Red
  statistics: "Show median, quartiles, outliers"
  title: "Age Distribution: Churned vs Retained Customers"
  grid: "Horizontal gridlines, alpha=0.3"
  
output_file: "06_age_boxplot.png"
business_insight: "Identifies if certain age groups are more likely to churn"
```

#### Chart 7: Tenure Distribution (Histogram)
```yaml
visualization_name: "Tenure Distribution by Churn Status"
chart_type: "Overlapping Histograms"
purpose: "Analyze tenure patterns for churned vs retained"
business_question: Q6

specification:
  data_preparation: "Split tenure_months by churned status"
  x_axis: "Tenure (months)"
  y_axis: "Customer Count"
  histograms:
    - group: "Retained"
      color: "#3498db"  # Blue
      alpha: 0.6
    - group: "Churned"
      color: "#e74c3c"  # Red
      alpha: 0.6
  bins: 8
  title: "Tenure Distribution: Churned vs Retained Customers"
  legend: "Upper right"
  grid: "Horizontal gridlines, alpha=0.3"
  
output_file: "07_tenure_histogram.png"
business_insight: "Shows if early customers are more likely to churn"
```

#### Chart 8: Monthly Charges Distribution (Violin Plot)
```yaml
visualization_name: "Monthly Charges Distribution by Status"
chart_type: "Violin Plot"
purpose: "Compare pricing distributions between segments"
business_question: Q8

specification:
  data_preparation: "Split monthly_charges by churned status"
  x_axis: "Customer Status (Retained, Churned)"
  y_axis: "Monthly Charges ($)"
  violins:
    - group: "Retained"
      color: "#2ecc71"  # Green
      alpha: 0.5
    - group: "Churned"
      color: "#e74c3c"  # Red
      alpha: 0.5
  statistics: "Show median, quartiles"
  title: "Monthly Charges Distribution: Churned vs Retained"
  grid: "Horizontal gridlines, alpha=0.3"
  
output_file: "08_charges_violin.png"
business_insight: "Reveals if high pricing drives churn"
```

### Segmentation Charts

#### Chart 9: Contract Type × Product Count (Stacked Bar)
```yaml
visualization_name: "Customer Segmentation: Contract × Products"
chart_type: "Stacked Bar Chart"
purpose: "Show customer distribution across segments"
business_question: Q9

specification:
  data_preparation: "Group by contract_type and num_products"
  x_axis: "Contract Type"
  y_axis: "Customer Count"
  stacks: "One stack per product count (1-5)"
  colors: "Colormap 'Set3' (5 distinct colors)"
  title: "Customer Segmentation: Contract Type × Product Count"
  legend: "Upper right, title='Products'"
  rotation: "15 degrees for x-labels"
  grid: "Horizontal gridlines, alpha=0.3"
  
output_file: "09_contract_distribution.png"
business_insight: "Identifies largest customer segments"
```

#### Chart 10: Payment Method × Churn (Grouped Bar)
```yaml
visualization_name: "Revenue Distribution by Payment Method"
chart_type: "Grouped Bar Chart"
purpose: "Compare total revenue by payment method and status"
business_question: Q10

specification:
  data_preparation: "Group by payment_method and churned, sum total_charges"
  x_axis: "Payment Method"
  y_axis: "Total Revenue ($)"
  bars:
    - group: "Retained"
      color: "#2ecc71"  # Green
    - group: "Churned"
      color: "#e74c3c"  # Red
  title: "Total Revenue by Payment Method and Status"
  legend: "Upper right"
  rotation: "15 degrees for x-labels"
  grid: "Horizontal gridlines, alpha=0.3"
  
output_file: "10_payment_distribution.png"
business_insight: "Shows revenue at risk by payment method"
```

### Advanced Visualizations

#### Chart 11: Dashboard View (Subplot Grid 2×2)
```yaml
visualization_name: "Customer Churn Analysis Dashboard"
chart_type: "Multi-Panel Dashboard"
purpose: "Provide at-a-glance overview of key metrics"

specification:
  layout: "2 rows × 2 columns"
  figure_size: "(14, 10)"
  
  panel_1:
    position: "Top-left"
    chart: "Churn pie chart"
    title: "Overall Churn Distribution"
    
  panel_2:
    position: "Top-right"
    chart: "Churn by contract type (bar)"
    title: "Churn Rate by Contract"
    
  panel_3:
    position: "Bottom-left"
    chart: "Churn by support calls (bar)"
    title: "Support Calls Impact"
    
  panel_4:
    position: "Bottom-right"
    chart: "Age distribution (box plot)"
    title: "Age: Churned vs Retained"
  
  overall_title: "Customer Churn Analysis Dashboard"
  title_fontsize: 16
  
output_file: "11_dashboard.png"
business_insight: "Executive summary view of all key findings"
```

#### Chart 12: Correlation Heatmap
```yaml
visualization_name: "Feature Correlation Heatmap"
chart_type: "Heatmap"
purpose: "Show relationships between numeric variables"

specification:
  data_preparation: "Calculate correlation matrix for numeric fields"
  fields:
    - age
    - tenure_months
    - monthly_charges
    - total_charges
    - num_products
    - num_support_calls
    - churned
  colormap: "RdYlGn (red=negative, yellow=neutral, green=positive)"
  annotations: "Display correlation values in cells"
  title: "Feature Correlation Analysis"
  colorbar: "Show scale (-1 to 1)"
  
output_file: "12_correlation_heatmap.png"
business_insight: "Identifies which factors are most related to churn"
```

---

## SECTION 4: STATISTICS TO CALCULATE

### Overall Metrics
- Total customers: 1,000
- Churn rate: 20.6%
- Retention rate: 79.4%
- Average age: Calculate mean
- Average tenure: Calculate mean
- Average monthly charges: Calculate mean
- Average total charges: Calculate mean

### Segmentation Metrics

**By Contract Type:**
- Churn rate for each type
- Average revenue per customer by type
- Customer count by type

**By Payment Method:**
- Churn rate for each method
- Average revenue by method
- Customer distribution

**By Product Portfolio:**
- Churn rate by product count (1-5)
- Revenue concentration

**By Support Calls:**
- Churn rate by call count (0-5)
- Percentage of customers at each level

### Customer Profiles

**Churned Customers:**
- Average age
- Average tenure
- Average monthly charges
- Most common contract type
- Most common payment method
- Average support calls

**Retained Customers:**
- Same metrics as churned for comparison

### Revenue Analysis
- Total revenue at risk (sum of total_charges where churned=1)
- Revenue from retained customers
- Average customer lifetime value

### Correlation Analysis
- Correlation coefficients between all numeric fields
- Identify strongest predictors of churn

---

## SECTION 5: TASK-BASED IMPLEMENTATION PLAN

**Implementation Mode**: Single-file (task.py, ~500-600 lines)  
**Estimated Execution Time**: 1-2 minutes  
**Output**: 12 PNG charts + 1 statistics text file

### Task Structure

#### TASK 1: Setup & Configuration (Lines 1-30)

**Subtasks:**
1.1) Import libraries
   - pandas (data manipulation)
   - matplotlib.pyplot (visualization)
   - seaborn (statistical plots)
   - numpy (numerical operations)
   - pathlib.Path (file handling)

1.2) Define constants
   ```python
   INPUT_FILE = './data/customer_churn.csv'
   OUTPUT_DIR = Path('./outputs/')
   DPI = 100
   
   COLORS = {
       'retained': '#2ecc71',    # Green
       'churned': '#e74c3c',      # Red
       'neutral': '#3498db',      # Blue
       'warning': '#f39c12',      # Orange
       'accent': '#9b59b6'        # Purple
   }
   ```

1.3) Configure matplotlib style
   - Use 'seaborn-v0_8-darkgrid' style
   - Set default figure DPI

1.4) Create output directory
   - Use OUTPUT_DIR.mkdir(exist_ok=True)

#### TASK 2: Data Loading & Validation (Lines 31-55)

**Function**: `load_data() -> pd.DataFrame`

**Subtasks:**
2.1) Load CSV file
   - Use pd.read_csv(INPUT_FILE)

2.2) Convert data types
   - Convert string numeric fields to numeric:
     * age → numeric
     * tenure_months → numeric
     * monthly_charges → numeric
     * total_charges → numeric
     * num_products → numeric
     * num_support_calls → numeric
     * churned → numeric

2.3) Validate data
   - Check for null values
   - Verify expected shape (1000 rows × 10 columns)
   - Print data summary

2.4) Return DataFrame

#### TASK 3: Chart Generation Functions (Lines 56-450)

**Pattern for each chart function**:
```
Function: create_[chart_name](df: pd.DataFrame) -> None
   1. Prepare data (groupby, aggregations)
   2. Create figure with specified size
   3. Plot with exact specifications
   4. Style (title, labels, colors, grid)
   5. Save PNG at specified DPI
   6. Close figure
   7. Print confirmation
```

**Subtasks (one function per chart):**

3.1) create_churn_pie(df)
   - Pie chart of overall churn distribution
   - Output: 01_churn_pie.png

3.2) create_churn_by_contract(df)
   - Bar chart of churn rates by contract type
   - Output: 02_churn_by_contract.png

3.3) create_churn_by_payment(df)
   - Stacked bar of customers by payment method
   - Output: 03_churn_by_payment.png

3.4) create_churn_by_products(df)
   - Bar chart of churn rate by product count
   - Output: 04_churn_by_products.png

3.5) create_churn_by_support(df)
   - Bar chart of churn rate by support calls
   - Output: 05_churn_by_support.png

3.6) create_age_boxplot(df)
   - Box plot comparing age distributions
   - Output: 06_age_boxplot.png

3.7) create_tenure_histogram(df)
   - Overlapping histograms of tenure
   - Output: 07_tenure_histogram.png

3.8) create_charges_violin(df)
   - Violin plot of monthly charges
   - Output: 08_charges_violin.png

3.9) create_contract_distribution(df)
   - Stacked bar of contract × products
   - Output: 09_contract_distribution.png

3.10) create_payment_distribution(df)
   - Grouped bar of revenue by payment/status
   - Output: 10_payment_distribution.png

3.11) create_dashboard(df)
   - 2×2 subplot grid with key charts
   - Output: 11_dashboard.png

3.12) create_correlation_heatmap(df)
   - Correlation matrix heatmap
   - Output: 12_correlation_heatmap.png

#### TASK 4: Statistics Calculation (Lines 451-500)

**Function**: `calculate_statistics(df: pd.DataFrame) -> dict`

**Subtasks:**
4.1) Overall metrics
   - Total customers, churn rate, retention rate
   - Average age, tenure, charges

4.2) Segmentation analysis
   - Churn rates by contract, payment, products, support
   - Revenue summaries

4.3) Customer profiles
   - Churned vs retained comparisons

4.4) Correlation analysis
   - Correlation matrix for numeric fields

4.5) Return statistics dictionary

#### TASK 5: Save Statistics Report (Lines 501-540)

**Function**: `save_statistics_report(stats: dict) -> None`

**Subtasks:**
5.1) Format statistics as readable text
   - Section headers
   - Aligned values
   - Clear labels

5.2) Write to file
   - Output: summary_statistics.txt

5.3) Print confirmation

#### TASK 6: Main Execution (Lines 541-600)

**Function**: `main() -> None`

**Subtasks:**
6.1) Setup
   - Create output directory

6.2) Load data
   - Call load_data()
   - Print confirmation

6.3) Calculate statistics
   - Call calculate_statistics()

6.4) Generate all visualizations
   - Call each create_*() function in sequence
   - Print progress messages

6.5) Save statistics report
   - Call save_statistics_report()

6.6) Print completion summary
   - Total files created
   - Location of outputs
   - Execution time

6.7) Entry point
   ```python
   if __name__ == '__main__':
       main()
   ```

### Expected Outputs

```
./outputs/01_churn_pie.png
./outputs/02_churn_by_contract.png
./outputs/03_churn_by_payment.png
./outputs/04_churn_by_products.png
./outputs/05_churn_by_support.png
./outputs/06_age_boxplot.png
./outputs/07_tenure_histogram.png
./outputs/08_charges_violin.png
./outputs/09_contract_distribution.png
./outputs/10_payment_distribution.png
./outputs/11_dashboard.png
./outputs/12_correlation_heatmap.png
./outputs/summary_statistics.txt
```

### Quality Standards

- **Resolution**: All charts at 100 DPI
- **Colors**: Consistent use of COLORS dictionary
- **Titles**: Font size 14, bold
- **Labels**: Font size 11
- **Grid**: Subtle (alpha=0.3)
- **Layout**: tight_layout() before save
- **Professional**: Clean, publication-ready

### Error Handling

- File loading: Catch FileNotFoundError
- Data conversion: Catch ValueError
- Directory creation: Catch OSError
- Provide clear error messages

### Testing Checklist

- [ ] All 12 PNG files generated
- [ ] Statistics file created
- [ ] All images at correct DPI
- [ ] Colors match specification
- [ ] No errors during execution
- [ ] Execution time < 2 minutes
- [ ] Charts readable and professional
- [ ] File sizes reasonable (~50-150KB per chart)

---

## SECTION 6: BUSINESS INSIGHTS & QUESTIONS ANSWERED

This analysis answers the following business questions:

1. ✓ **Overall churn rate**: Establishes 20.6% baseline
2. ✓ **Contract impact**: Shows if flexible contracts drive churn
3. ✓ **Product diversification**: Reveals if more products = better retention
4. ✓ **Support correlation**: Identifies if high support calls indicate risk
5. ✓ **Payment method effect**: Shows if payment convenience matters
6. ✓ **Tenure patterns**: Reveals early vs late customer churn risk
7. ✓ **Age demographics**: Identifies age-related churn patterns
8. ✓ **Pricing impact**: Shows if high charges drive churn
9. ✓ **Customer segments**: Maps customer distribution
10. ✓ **Revenue at risk**: Quantifies revenue by segment and status

**Actionable Outcomes:**
- Identify high-risk customer segments
- Prioritize retention efforts
- Understand churn drivers
- Optimize pricing strategies
- Improve support processes
- Target marketing campaigns
- Develop retention programs

---

## APPENDIX: DATA DICTIONARY

### Field: customer_id
- **Data Type**: String
- **Storage Type**: VARCHAR(50)
- **Format**: Numeric string
- **Unit**: N/A (identifier)
- **Nullable**: No
- **Range**: 1-100 (unique identifiers)
- **Statistical Type**: Categorical (ID)

**Description**: Unique identifier for each customer in the dataset

**Statistical Summary**:
- Count: 1,000
- Unique: 100 (indicates multiple products/records per customer)
- Mean/Median: N/A (not meaningful for IDs)

**Business Rules**:
- Must be unique per row
- Required field for all records
- Used for linking to other systems

**Example Values**: "1", "2", "3", "4", "5"

**Data Quality**: No missing values, 100% coverage

**Usage Considerations**:
- Not used in analysis (identifier only)
- May be used for customer lookup
- Multiple rows per customer possible

---

### Field: age
- **Data Type**: Numeric (Integer)
- **Storage Type**: INT
- **Format**: Integer years
- **Unit**: Years
- **Nullable**: No
- **Range**: 18-80 years (estimated from 41 unique values)
- **Statistical Type**: Continuous

**Description**: Customer age in completed years at time of observation

**Statistical Summary**:
- Count: 1,000
- Unique: 41 distinct ages
- Distribution: Likely normal to slightly right-skewed
- Use in analysis: Segmentation, correlation with churn

**Value Distribution**: 
- Sample values: 52, 42, 54
- Spread across adult age range
- No children or extreme elderly

**Business Rules**:
- Must be ≥ 18 (service eligibility)
- Must be < 120 (data quality check)
- Validated at signup

**Data Quality**: No missing values, realistic range

**Usage Considerations**:
- Correlation with churn: Age groups may have different retention
- Segmentation: Create age bands (18-30, 31-50, 51+)
- Visualization: Box plots, histograms

**Transformation Recommendations**:
- Keep as continuous for correlation analysis
- Create age bands for segmentation:
  * Young: 18-35
  * Middle: 36-55
  * Senior: 56+

**Business Impact**: 
- Younger customers may have different churn patterns
- Pricing sensitivity may vary by age
- Product preferences differ across age groups

---

### Field: tenure_months
- **Data Type**: Numeric (Integer)
- **Storage Type**: INT
- **Format**: Integer months
- **Unit**: Months
- **Nullable**: No
- **Range**: 1-60 months (estimated)
- **Statistical Type**: Continuous

**Description**: Number of months customer has been with the service

**Statistical Summary**:
- Count: 1,000
- Unique: 41 distinct tenures
- Distribution: Likely right-skewed (more new customers)
- Key metric: Customer lifetime indicator

**Value Distribution**:
- Sample values: 4, 2, 24
- Range from new (1-3 months) to established (24+ months)

**Business Rules**:
- Must be ≥ 1 (at least one month)
- Increments monthly
- Used for customer cohort analysis

**Data Quality**: No missing values, logical progression

**Usage Considerations**:
- **Critical churn indicator**: Early tenure = high risk
- Segmentation: New (0-6), Growing (7-12), Established (13-24), Loyal (25+)
- Correlation with churn: Expected strong negative correlation

**Transformation Recommendations**:
- Create tenure bands for analysis
- Calculate tenure rate: tenure_months / age (customer maturity)
- Consider log transform if heavily skewed

**Business Impact**:
- Early customers (0-6 months) are highest churn risk
- Retention programs should target new customers
- Loyal customers (24+ months) are valuable to retain

---

### Field: monthly_charges
- **Data Type**: Numeric (Float)
- **Storage Type**: DECIMAL(10,2)
- **Format**: Currency with cents
- **Unit**: US Dollars ($)
- **Nullable**: No
- **Range**: $20-$120 (estimated from context)
- **Statistical Type**: Continuous

**Description**: Current monthly service charges in dollars

**Statistical Summary**:
- Count: 1,000
- Unique: 91 distinct values
- Distribution: Likely normal or bimodal
- Measure: Revenue per customer per month

**Value Distribution**:
- Sample values: $55.72, $42.44, $74.58
- Wide spread indicates varied service levels

**Business Rules**:
- Must be > $0
- Precision: 2 decimal places
- Updated monthly based on services
- Subject to promotions/discounts

**Data Quality**: No missing values, reasonable range

**Usage Considerations**:
- **Key churn driver**: High charges may drive churn
- Price sensitivity: Compare churned vs retained
- Revenue analysis: Total revenue = monthly_charges × tenure

**Transformation Recommendations**:
- Create price bands: Low ($0-40), Medium ($41-70), High ($71+)
- Calculate % of customer budget: monthly_charges / estimated_income
- Consider log transform if skewed

**Business Impact**:
- Customers paying >$70/month may be price-sensitive
- Churn correlation: High prices may increase churn
- Upsell opportunity: Low-price customers may upgrade

---

### Field: total_charges
- **Data Type**: Numeric (Float)
- **Storage Type**: DECIMAL(10,2)
- **Format**: Currency with cents
- **Unit**: US Dollars ($)
- **Nullable**: No
- **Range**: $50-$7,200 (estimated: monthly × tenure)
- **Statistical Type**: Continuous

**Description**: Total lifetime revenue from customer since signup

**Statistical Summary**:
- Count: 1,000
- Unique: 98 distinct values
- Distribution: Right-skewed (most customers are new)
- Measure: Customer lifetime value (CLV)

**Value Distribution**:
- Sample values: $222.89, $84.87, $1789.81
- High variance based on tenure and pricing

**Business Rules**:
- Should approximately equal: monthly_charges × tenure_months
- Accumulates monthly
- Includes all historical charges
- Does not include refunds

**Data Quality**: No missing values, logical relationship to other fields

**Usage Considerations**:
- **Revenue at risk**: Sum of total_charges where churned=1
- CLV analysis: Segment by value (low/medium/high)
- Profitability: High total_charges customers are valuable

**Transformation Recommendations**:
- Create value segments: Low (<$500), Medium ($500-$2000), High (>$2000)
- Calculate average revenue per month: total_charges / tenure_months
- Consider log transform for modeling

**Business Impact**:
- High-value customers (total_charges > $2000) should be prioritized for retention
- Revenue at risk = total_charges of churned customers
- Protect high CLV customers with proactive support

---

### Field: num_products
- **Data Type**: Numeric (Integer)
- **Storage Type**: INT
- **Format**: Count
- **Unit**: Count of products
- **Nullable**: No
- **Range**: 1-5 products
- **Statistical Type**: Discrete

**Description**: Number of distinct products/services customer has purchased

**Statistical Summary**:
- Count: 1,000
- Unique: 5 values (1,2,3,4,5)
- Distribution:
  * 1 product: 399 customers (39.9%)
  * 2 products: 272 customers (27.2%)
  * 3 products: 197 customers (19.7%)
  * 4 products: 96 customers (9.6%)
  * 5 products: 36 customers (3.6%)

**Value Distribution**:
- Most customers: 1-2 products (67%)
- Power users: 4-5 products (13%)
- Clear skew toward fewer products

**Business Rules**:
- Must be ≥ 1 (at least one product to be customer)
- Must be ≤ 5 (max product portfolio)
- Increments with each new product purchase

**Data Quality**: No missing values, valid range

**Usage Considerations**:
- **Cross-sell opportunity**: Most have 1-2 products, potential for more
- Churn correlation: Hypothesis - more products = better retention (ecosystem lock-in)
- Segmentation: Single-product vs multi-product customers

**Transformation Recommendations**:
- Create binary: single_product (1) vs multi_product (2+)
- Product diversity score: num_products / 5
- Interaction features: num_products × tenure_months

**Business Impact**:
- Multi-product customers likely have lower churn (ecosystem effect)
- Cross-sell campaigns should target single-product customers
- Product bundles may improve retention

---

### Field: num_support_calls
- **Data Type**: Numeric (Integer)
- **Storage Type**: INT
- **Format**: Count
- **Unit**: Number of calls
- **Nullable**: No
- **Range**: 0-5 calls
- **Statistical Type**: Discrete

**Description**: Number of support calls made by customer in observation period

**Statistical Summary**:
- Count: 1,000
- Unique: 6 values (0,1,2,3,4,5)
- Distribution:
  * 0 calls: 359 customers (35.9%)
  * 1 call: 400 customers (40.0%)
  * 2 calls: 179 customers (17.9%)
  * 3 calls: 54 customers (5.4%)
  * 4 calls: 6 customers (0.6%)
  * 5 calls: 2 customers (0.2%)

**Value Distribution**:
- Most customers: 0-1 calls (76%)
- High support: 3+ calls (6%)
- Clear skew toward low support needs

**Business Rules**:
- Counts all support interactions
- Resets annually (assumed)
- May include technical, billing, and general inquiries

**Data Quality**: No missing values, reasonable distribution

**Usage Considerations**:
- **Churn risk indicator**: High support calls may signal dissatisfaction
- Support quality metric: Effectiveness in resolving issues
- Customer satisfaction proxy: Few calls = happy customer OR poor support access

**Transformation Recommendations**:
- Create risk flags:
  * Low support: 0-1 calls (normal)
  * Medium support: 2-3 calls (attention needed)
  * High support: 4-5 calls (critical risk)
- Binary: has_support_issues (3+ calls)
- Interaction: support_calls × tenure (persistent issues)

**Business Impact**:
- Customers with 3+ support calls are high churn risk
- Early intervention needed for high-support customers
- Support effectiveness should be analyzed (resolution rates)
- May indicate product issues requiring fixes

---

### Field: contract_type
- **Data Type**: Categorical (String)
- **Storage Type**: VARCHAR(20)
- **Format**: Text label
- **Unit**: N/A (category)
- **Nullable**: No
- **Range**: 3 distinct values
- **Statistical Type**: Nominal (Categorical)

**Description**: Type of service contract customer has chosen

**Statistical Summary**:
- Count: 1,000
- Unique: 3 categories
- Distribution:
  * Month-to-month: 507 customers (50.7%)
  * One year: 300 customers (30.0%)
  * Two year: 193 customers (19.3%)

**Value Distribution**:
- Dominant: Month-to-month (flexible, no commitment)
- Moderate: One year (balance of flexibility and commitment)
- Low: Two year (highest commitment, likely lowest churn)

**Business Rules**:
- Must be one of three valid values
- Determines billing cycle and termination terms
- Cannot be null

**Data Quality**: No missing values, all valid categories

**Usage Considerations**:
- **Primary churn driver**: Flexible contracts likely have higher churn
- Segmentation: Key dimension for analysis
- Revenue predictability: Long contracts = stable revenue
- Churn hypothesis: Month-to-month > One year > Two year

**Transformation Recommendations**:
- One-hot encoding for ML: contract_month2month, contract_1year, contract_2year
- Ordinal encoding: 0=M2M, 1=1yr, 2=2yr (commitment level)
- Create commitment score: 0-1 scale based on contract length

**Business Impact**:
- Month-to-month customers are retention focus (highest churn risk)
- Incentivize contract upgrades: M2M → 1 year → 2 year
- Two-year contracts provide revenue stability
- Contract type is likely strongest single predictor of churn

---

### Field: payment_method
- **Data Type**: Categorical (String)
- **Storage Type**: VARCHAR(20)
- **Format**: Text label
- **Unit**: N/A (category)
- **Nullable**: No
- **Range**: 4 distinct values
- **Statistical Type**: Nominal (Categorical)

**Description**: Method customer uses to pay monthly bill

**Statistical Summary**:
- Count: 1,000
- Unique: 4 categories
- Distribution (fairly even):
  * Credit card: 263 customers (26.3%)
  * Mailed check: 259 customers (25.9%)
  * Electronic: 255 customers (25.5%)
  * Bank transfer: 223 customers (22.3%)

**Value Distribution**:
- Balanced distribution across all methods
- No dominant payment preference
- Mix of modern (electronic, card) and traditional (check, transfer)

**Business Rules**:
- Must be one of four valid values
- Determines billing frequency and processing
- Can be changed by customer

**Data Quality**: No missing values, all valid categories

**Usage Considerations**:
- Convenience hypothesis: Electronic/card may have lower churn (easy to pay)
- Payment friction: Mailed check may have higher churn (manual effort)
- Auto-pay correlation: Card/electronic likely auto-pay = better retention
- Churn analysis: Compare retention across methods

**Transformation Recommendations**:
- One-hot encoding: payment_card, payment_check, payment_electronic, payment_transfer
- Create auto_pay proxy: 1 if electronic/card, 0 if check/transfer
- Payment convenience score: 2=electronic/card, 1=bank, 0=check

**Business Impact**:
- Push customers toward electronic/auto-pay for better retention
- Manual payment methods (check) may have higher churn
- Payment convenience improves customer experience
- Analyze churn by payment method to validate hypothesis

---

### Field: churned
- **Data Type**: Binary (Integer)
- **Storage Type**: TINYINT or BIT
- **Format**: 0 or 1
- **Unit**: N/A (flag)
- **Nullable**: No
- **Range**: 0 (retained) or 1 (churned)
- **Statistical Type**: Binary (Target variable)

**Description**: Whether customer has canceled service (churned) or remains active (retained)

**Statistical Summary**:
- Count: 1,000
- Unique: 2 values
- Distribution:
  * 0 (Retained): 794 customers (79.4%)
  * 1 (Churned): 206 customers (20.6%)
- **Churn rate**: 20.6%
- **Retention rate**: 79.4%

**Value Distribution**:
- Balanced class distribution (not too imbalanced)
- Sufficient churned examples for analysis (206)
- Healthy retention rate (79.4%)

**Business Rules**:
- Binary only: 0 or 1
- Once churned (1), customer is no longer active
- Observation period: Determined by data collection timeframe

**Data Quality**: No missing values, valid binary values

**Usage Considerations**:
- **Target variable**: Primary metric for all analysis
- Segmentation: All visualizations split by churn status
- Success metric: Charts/statistics aim to understand drivers of churn
- Business goal: Reduce churn rate from 20.6% to target (e.g., 15%)

**Transformation Recommendations**:
- No transformation needed (already binary)
- Use as-is for all segmentation
- Create churn_rate calculations for categories:
  * churn_rate = (sum(churned=1) / count(*)) × 100%

**Business Impact**:
- **20.6% churn rate** indicates significant revenue leakage
- 206 churned customers = lost revenue opportunity
- Understanding drivers of churned=1 is primary analysis goal
- Retention improvements directly impact revenue and growth
- Reducing churn by 5% = ~50 customers saved = substantial revenue

**Revenue at Risk**:
- Total revenue from churned customers = sum(total_charges where churned=1)
- Monthly recurring revenue at risk = sum(monthly_charges where churned=1)
- Quantifies financial impact of churn

---

## SPECIFICATION COMPLETE

**Document Type**: BI Visualization Specification (NO machine learning)  
**Focus**: Charts, graphs, statistics to understand customer churn patterns  
**Next Step**: @data-dev agent implements task.py based on this specification  
**Execution**: Run task.py to generate 12 PNG charts + statistics report  
**Timeline**: 1-2 minutes execution time

**Key Deliverables**:
✓ Dataset schema understanding (structure inspection only)  
✓ 10 business questions identified  
✓ 12 chart specifications (precise implementation blueprints)  
✓ Task-based development plan (systematic implementation guide)  
✓ Complete data dictionary (all 10 fields documented)  

**Implementation Ready**: YES - Complete specifications for @data-dev to code
