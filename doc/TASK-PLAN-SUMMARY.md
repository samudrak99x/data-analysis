# Task-Based Implementation Plan - Quick Reference

**Project:** Customer Churn Visualization  
**Developer Reference:** Task list for implementing `task.py`  
**Full Specification:** See `customer-churn-chart-spec.md`

---

## 📋 TASK CHECKLIST

### ✅ TASK 1: Setup & Configuration
- [ ] Task 1.1: Import libraries (pandas, matplotlib, seaborn, numpy)
- [ ] Task 1.2: Define color constants (CHURN_RED, RETAIN_GREEN, etc.)
- [ ] Task 1.3: Define output directory path
- [ ] Task 1.4: Set matplotlib defaults (style, sizes)
- [ ] Task 1.5: Create output directory

**Estimated Time:** 5 minutes

---

### ✅ TASK 2: Data Loading & Validation
- [ ] Task 2.1: Create `load_data()` function
- [ ] Task 2.2: Read CSV into DataFrame
- [ ] Task 2.3: Verify column structure
- [ ] Task 2.4: Check for missing values
- [ ] Task 2.5: Convert data types
- [ ] Task 2.6: Print data summary
- [ ] Task 2.7: Return validated DataFrame

**Estimated Time:** 10 minutes

---

### ✅ TASK 3: Chart Generation Functions (10 Charts)

#### Chart Functions to Implement:

- [ ] **Task 3.1:** `create_churn_pie_chart(df)` → `churn_distribution_pie.png`
- [ ] **Task 3.2:** `create_contract_churn_chart(df)` → `churn_by_contract.png`
- [ ] **Task 3.3:** `create_support_calls_chart(df)` → `churn_by_support_calls.png`
- [ ] **Task 3.4:** `create_payment_method_chart(df)` → `churn_by_payment.png`
- [ ] **Task 3.5:** `create_products_chart(df)` → `churn_by_products.png`
- [ ] **Task 3.6:** `create_tenure_histogram(df)` → `tenure_distribution.png`
- [ ] **Task 3.7:** `create_age_boxplot(df)` → `age_boxplot.png`
- [ ] **Task 3.8:** `create_charges_violin(df)` → `charges_violin.png`
- [ ] **Task 3.9:** `create_contract_product_stack(df)` → `contract_product_stack.png`
- [ ] **Task 3.10:** `create_dashboard(df)` → `dashboard_overview.png`

**Estimated Time:** 60-90 minutes (6-9 min per chart)

---

### ✅ TASK 4: Main Execution Function
- [ ] Task 4.1: Create `main()` function
- [ ] Task 4.2: Print start message
- [ ] Task 4.3: Call `load_data()`
- [ ] Task 4.4: Call all chart functions (3.1-3.10)
- [ ] Task 4.5: Track successful chart creation
- [ ] Task 4.6: Print summary
- [ ] Task 4.7: Add error handling

**Estimated Time:** 15 minutes

---

### ✅ TASK 5: Quality Assurance & Documentation
- [ ] Task 5.1: Add docstrings to all functions
- [ ] Task 5.2: Add inline comments
- [ ] Task 5.3: Verify output paths
- [ ] Task 5.4: Test with dataset
- [ ] Task 5.5: Verify file naming
- [ ] Task 5.6: Check color consistency
- [ ] Task 5.7: Ensure proper formatting

**Estimated Time:** 20 minutes

---

## 🎯 IMPLEMENTATION ORDER

**Recommended sequence:**

1. **Setup First** (Task 1) - Get environment ready
2. **Data Loading** (Task 2) - Ensure data is accessible
3. **Simple Charts First** (Tasks 3.1, 3.2, 3.3) - Build confidence with basic charts
4. **Complex Charts Next** (Tasks 3.4-3.9) - Grouped, stacked, distributions
5. **Dashboard Last** (Task 3.10) - Combine multiple charts
6. **Main Function** (Task 4) - Wire everything together
7. **Polish** (Task 5) - Documentation and testing

---

## 📦 EXPECTED OUTPUTS

```
outputs/
├── churn_distribution_pie.png         # Task 3.1 ✓
├── churn_by_contract.png              # Task 3.2 ✓
├── churn_by_support_calls.png         # Task 3.3 ✓
├── churn_by_payment.png               # Task 3.4 ✓
├── churn_by_products.png              # Task 3.5 ✓
├── tenure_distribution.png            # Task 3.6 ✓
├── age_boxplot.png                    # Task 3.7 ✓
├── charges_violin.png                 # Task 3.8 ✓
├── contract_product_stack.png         # Task 3.9 ✓
└── dashboard_overview.png             # Task 3.10 ✓
```

**Total:** 10 chart files

---

## 🎨 QUICK REFERENCE: Color Scheme

```python
CHURN_RED = '#e74c3c'      # For churned customers
RETAIN_GREEN = '#2ecc71'   # For retained customers
NEUTRAL_BLUE = '#3498db'   # For neutral info
WARNING_ORANGE = '#f39c12' # For warnings/attention
```

---

## ⏱️ TOTAL ESTIMATED TIME

- Task 1: 5 min
- Task 2: 10 min
- Task 3: 60-90 min (10 charts)
- Task 4: 15 min
- Task 5: 20 min

**Total: 110-140 minutes (2-2.5 hours)**

---

## 🚀 NEXT STEPS FOR DEVELOPER

1. Review full specification: `customer-churn-chart-spec.md`
2. Set up development environment
3. Follow tasks sequentially
4. Test each function as you build it
5. Run final execution to generate all charts

**Command to run after implementation:**
```bash
python task.py
```

---

**Status:** ✅ Specification Complete  
**Ready For:** `@data-dev` implementation  
**Execute With:** `@run-agent`