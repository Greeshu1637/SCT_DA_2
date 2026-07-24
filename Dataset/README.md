# Dataset Information

## Overview

This folder contains the Global Superstore dataset in two versions:
- **raw/**: Original, unprocessed data
- **cleaned/**: Processed, analysis-ready data

---

## Raw Dataset

**File**: `raw/Global_Superstore.csv`

### Characteristics
- **Rows**: 9,993
- **Columns**: 13
- **Missing Values**: 0 (original dataset was clean)
- **Duplicates**: 17
- **Size**: ~1.5 MB

### Columns
1. Ship Mode (text)
2. Segment (text)
3. Country (text)
4. City (text)
5. State (text)
6. Postal Code (number)
7. Region (text)
8. Category (text)
9. Sub-Category (text)
10. Sales (decimal)
11. Quantity (integer)
12. Discount (decimal)
13. Profit (decimal)

---

## Cleaned Dataset

**File**: `cleaned/Global_Superstore_Cleaned.csv`

### Characteristics
- **Rows**: 9,976 (17 duplicates removed)
- **Columns**: 13
- **Missing Values**: 0
- **Duplicates**: 0
- **Size**: ~1.5 MB
- **Data Quality**: ✅ Production-ready

### Changes Applied
1. ✅ Removed 17 duplicate rows
2. ✅ Standardized column names (lowercase, underscores)
3. ✅ Converted postal_code to string type
4. ✅ Removed whitespace from text fields
5. ✅ Validated all data types
6. ✅ Detected outliers (retained for analysis)

### Columns (Standardized)
1. ship_mode (object)
2. segment (object)
3. country (object)
4. city (object)
5. state (object)
6. postal_code (object) ⚠️ Changed from int
7. region (object)
8. category (object)
9. sub_category (object)
10. sales (float64)
11. quantity (int64)
12. discount (float64)
13. profit (float64)

---

## Data Dictionary

### ship_mode
- **Type**: Categorical
- **Values**: First Class, Second Class, Standard Class, Same Day
- **Description**: Shipping method used for delivery

### segment
- **Type**: Categorical
- **Values**: Consumer, Corporate, Home Office
- **Description**: Customer segment classification

### country
- **Type**: Categorical
- **Values**: United States
- **Description**: Country of the customer (single country dataset)

### city
- **Type**: Categorical
- **Unique**: 531
- **Description**: City where order was placed/delivered

### state
- **Type**: Categorical
- **Unique**: 49
- **Description**: US state (all except Hawaii)

### postal_code
- **Type**: String (converted from integer)
- **Unique**: 631
- **Description**: US ZIP code (identifier, not numeric)

### region
- **Type**: Categorical
- **Values**: East, West, Central, South
- **Description**: Geographic region within US

### category
- **Type**: Categorical
- **Values**: Furniture, Office Supplies, Technology
- **Description**: Main product category

### sub_category
- **Type**: Categorical
- **Count**: 17 subcategories
- **Examples**: Chairs, Phones, Binders, Tables
- **Description**: Detailed product classification

### sales
- **Type**: Numerical (float)
- **Range**: $0.44 - $22,638.48
- **Unit**: USD
- **Description**: Total sales amount for the transaction

### quantity
- **Type**: Numerical (integer)
- **Range**: 1 - 14
- **Unit**: Items
- **Description**: Number of items ordered

### discount
- **Type**: Numerical (float)
- **Range**: 0.0 - 0.8 (0% - 80%)
- **Description**: Discount percentage applied to the order

### profit
- **Type**: Numerical (float)
- **Range**: -$6,599.98 to $8,399.98
- **Unit**: USD
- **Description**: Profit or loss on the transaction
- **Note**: Negative values indicate losses

---

## Data Quality Metrics

### Cleaned Dataset Quality

| Metric | Value | Status |
|--------|-------|--------|
| Completeness | 100% | ✅ |
| Uniqueness | 100% | ✅ |
| Consistency | 100% | ✅ |
| Accuracy | Validated | ✅ |
| Data Retention | 99.83% | ✅ |

### Outliers Detected (IQR Method)

| Column | Outliers | Percentage | Action |
|--------|----------|------------|--------|
| sales | 1,167 | 11.70% | Retained |
| quantity | 170 | 1.70% | Retained |
| discount | 855 | 8.57% | Retained |
| profit | 1,880 | 18.85% | Retained |

**Note**: Outliers were retained as they represent legitimate business scenarios (bulk orders, high discounts, significant losses/profits).

---

## Usage Guidelines

### Loading the Data

#### Python (Pandas)
```python
import pandas as pd

# Load cleaned data
df = pd.read_csv('Dataset/cleaned/Global_Superstore_Cleaned.csv')
```

#### R
```r
# Load cleaned data
df <- read.csv('Dataset/cleaned/Global_Superstore_Cleaned.csv')
```

### Recommended Analyses

1. **Sales Analysis**
   - Regional performance
   - Product category trends
   - Seasonal patterns (if dates available)

2. **Profitability Study**
   - Profit margins by category
   - Impact of discounts on profit
   - Loss-making transactions

3. **Customer Segmentation**
   - Behavior by segment (Consumer/Corporate/Home Office)
   - Segment-wise profitability
   - Shipping preferences

4. **Geographic Analysis**
   - State-level performance
   - Regional comparisons
   - City-wise sales distribution

---

## Data Source

- **Original Dataset**: Global Superstore
- **Domain**: Retail/E-commerce
- **Time Period**: Not specified in dataset
- **Geographic Scope**: United States only

---

## Data Cleaning Process

For detailed information about the cleaning process:
- See: `reports/Data_Cleaning_Report.md`
- Script: `src/clean_data.py`
- Notebook: `notebooks/Data_Cleaning.ipynb`

---

## Updates & Versioning

- **v1.0** (2024): Initial cleaned dataset
  - Removed 17 duplicates
  - Standardized column names
  - Converted data types
  - Validated data quality

---

## Contact & Support

For questions about the dataset:
- Review the cleaning report in `reports/`
- Check the Jupyter notebook for examples
- See `README.md` in project root

---

**Dataset Status**: ✅ Clean and Ready for Analysis
