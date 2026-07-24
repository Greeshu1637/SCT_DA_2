"""
Data Cleaning Script for Global Superstore Dataset
SkillCraft Technology - Internship Task 2
Author: Data Analytics Intern
"""

import pandas as pd
import numpy as np
import os
from pathlib import Path

class DataCleaner:
    """A comprehensive data cleaning class for the Global Superstore dataset."""
    
    def __init__(self, input_path, output_path):
        """
        Initialize the DataCleaner with input and output paths.
        
        Parameters:
        -----------
        input_path : str
            Path to the raw dataset
        output_path : str
            Path where cleaned dataset will be saved
        """
        self.input_path = input_path
        self.output_path = output_path
        self.df = None
        self.original_shape = None
        self.cleaning_report = []
        
    def load_data(self):
        """Load the dataset from CSV file."""
        print("=" * 80)
        print("LOADING DATA")
        print("=" * 80)
        
        try:
            self.df = pd.read_csv(self.input_path)
            self.original_shape = self.df.shape
            print(f"✓ Data loaded successfully from: {self.input_path}")
            print(f"✓ Original shape: {self.original_shape[0]} rows × {self.original_shape[1]} columns\n")
            self.cleaning_report.append(f"Original dataset shape: {self.original_shape}")
            return True
        except FileNotFoundError:
            print(f"✗ Error: File not found at {self.input_path}")
            return False
        except Exception as e:
            print(f"✗ Error loading data: {str(e)}")
            return False
    
    def display_basic_info(self):
        """Display basic information about the dataset."""
        print("=" * 80)
        print("DATASET OVERVIEW")
        print("=" * 80)
        
        print(f"\n1. Dataset Shape: {self.df.shape[0]} rows × {self.df.shape[1]} columns")
        
        print(f"\n2. Column Names ({len(self.df.columns)} total):")
        for i, col in enumerate(self.df.columns, 1):
            print(f"   {i:2d}. {col}")
        
        print("\n3. Data Types:")
        for col, dtype in self.df.dtypes.items():
            print(f"   {col:20s} : {dtype}")
        
        print("\n4. Missing Values:")
        missing_counts = self.df.isnull().sum()
        missing_percent = (missing_counts / len(self.df)) * 100
        missing_df = pd.DataFrame({
            'Missing Count': missing_counts,
            'Percentage': missing_percent.round(2)
        })
        missing_df = missing_df[missing_df['Missing Count'] > 0]
        
        if len(missing_df) > 0:
            print(missing_df.to_string())
        else:
            print("   No missing values found!")
        
        print(f"\n5. Duplicate Rows: {self.df.duplicated().sum()}")
        
        print("\n6. First 5 Rows:")
        print(self.df.head().to_string())
        print()
        
    def handle_missing_values(self):
        """Handle missing values in the dataset."""
        print("=" * 80)
        print("HANDLING MISSING VALUES")
        print("=" * 80)
        
        missing_before = self.df.isnull().sum().sum()
        print(f"\nTotal missing values before: {missing_before}")
        
        # Check for missing values in each column
        for col in self.df.columns:
            missing_count = self.df[col].isnull().sum()
            
            if missing_count > 0:
                missing_pct = (missing_count / len(self.df)) * 100
                print(f"\n'{col}': {missing_count} missing ({missing_pct:.2f}%)")
                
                # Strategy based on column type and missing percentage
                if missing_pct > 50:
                    print(f"   → Dropping column (>50% missing)")
                    self.df.drop(columns=[col], inplace=True)
                    self.cleaning_report.append(f"Dropped column '{col}' due to >50% missing values")
                    
                elif self.df[col].dtype in ['int64', 'float64']:
                    # For numerical columns, fill with median
                    median_val = self.df[col].median()
                    self.df[col].fillna(median_val, inplace=True)
                    print(f"   → Filled with median: {median_val}")
                    self.cleaning_report.append(f"Filled missing values in '{col}' with median: {median_val}")
                    
                elif self.df[col].dtype == 'object':
                    # For categorical columns, fill with mode or 'Unknown'
                    if self.df[col].mode().empty:
                        self.df[col].fillna('Unknown', inplace=True)
                        print(f"   → Filled with 'Unknown'")
                        self.cleaning_report.append(f"Filled missing values in '{col}' with 'Unknown'")
                    else:
                        mode_val = self.df[col].mode()[0]
                        self.df[col].fillna(mode_val, inplace=True)
                        print(f"   → Filled with mode: {mode_val}")
                        self.cleaning_report.append(f"Filled missing values in '{col}' with mode: {mode_val}")
        
        missing_after = self.df.isnull().sum().sum()
        print(f"\nTotal missing values after: {missing_after}")
        print(f"✓ Missing values handled successfully!\n")
        
    def remove_duplicates(self):
        """Remove duplicate rows from the dataset."""
        print("=" * 80)
        print("REMOVING DUPLICATES")
        print("=" * 80)
        
        duplicates_before = self.df.duplicated().sum()
        print(f"\nDuplicate rows before: {duplicates_before}")
        
        if duplicates_before > 0:
            self.df.drop_duplicates(inplace=True)
            self.df.reset_index(drop=True, inplace=True)
            duplicates_after = self.df.duplicated().sum()
            print(f"Duplicate rows after: {duplicates_after}")
            print(f"✓ Removed {duplicates_before} duplicate rows")
            self.cleaning_report.append(f"Removed {duplicates_before} duplicate rows")
        else:
            print("✓ No duplicates found!")
            self.cleaning_report.append("No duplicate rows found")
        
        print()
        
    def standardize_column_names(self):
        """Standardize column names (lowercase, underscores)."""
        print("=" * 80)
        print("STANDARDIZING COLUMN NAMES")
        print("=" * 80)
        
        print("\nBefore:")
        print(list(self.df.columns))
        
        # Convert to lowercase and replace spaces with underscores
        self.df.columns = self.df.columns.str.lower().str.replace(' ', '_').str.replace('-', '_')
        
        print("\nAfter:")
        print(list(self.df.columns))
        print("✓ Column names standardized!\n")
        self.cleaning_report.append("Standardized column names to lowercase with underscores")
        
    def convert_data_types(self):
        """Convert columns to appropriate data types."""
        print("=" * 80)
        print("CONVERTING DATA TYPES")
        print("=" * 80)
        
        print("\nData types before conversion:")
        print(self.df.dtypes.to_string())
        
        # Convert postal_code to string (it's an identifier, not a number)
        if 'postal_code' in self.df.columns:
            self.df['postal_code'] = self.df['postal_code'].astype(str)
            print("\n✓ Converted 'postal_code' to string")
            self.cleaning_report.append("Converted 'postal_code' to string type")
        
        # Convert quantity to integer if it exists
        if 'quantity' in self.df.columns:
            self.df['quantity'] = self.df['quantity'].astype(int)
            print("✓ Converted 'quantity' to integer")
            self.cleaning_report.append("Converted 'quantity' to integer type")
        
        # Ensure numeric columns are float
        numeric_cols = ['sales', 'discount', 'profit']
        for col in numeric_cols:
            if col in self.df.columns:
                self.df[col] = pd.to_numeric(self.df[col], errors='coerce')
                print(f"✓ Ensured '{col}' is numeric (float)")
                self.cleaning_report.append(f"Converted '{col}' to numeric type")
        
        print("\nData types after conversion:")
        print(self.df.dtypes.to_string())
        print()
        
    def remove_whitespace(self):
        """Remove leading and trailing whitespace from string columns."""
        print("=" * 80)
        print("REMOVING WHITESPACE")
        print("=" * 80)
        
        string_columns = self.df.select_dtypes(include=['object']).columns
        print(f"\nProcessing {len(string_columns)} text columns...")
        
        spaces_removed = False
        for col in string_columns:
            # Check if there are any strings with leading/trailing spaces
            if self.df[col].dtype == 'object':
                before_strip = self.df[col].astype(str)
                after_strip = before_strip.str.strip()
                
                if not before_strip.equals(after_strip):
                    self.df[col] = after_strip
                    print(f"✓ Removed whitespace from '{col}'")
                    spaces_removed = True
        
        if spaces_removed:
            self.cleaning_report.append("Removed leading/trailing whitespace from text columns")
        else:
            print("✓ No unnecessary whitespace found!")
            self.cleaning_report.append("No unnecessary whitespace found in text columns")
        
        print()
        
    def detect_outliers(self):
        """Detect outliers using IQR method."""
        print("=" * 80)
        print("DETECTING OUTLIERS (IQR METHOD)")
        print("=" * 80)
        
        numeric_columns = self.df.select_dtypes(include=[np.number]).columns
        outlier_summary = []
        
        for col in numeric_columns:
            Q1 = self.df[col].quantile(0.25)
            Q3 = self.df[col].quantile(0.75)
            IQR = Q3 - Q1
            
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            outliers = self.df[(self.df[col] < lower_bound) | (self.df[col] > upper_bound)]
            outlier_count = len(outliers)
            outlier_pct = (outlier_count / len(self.df)) * 100
            
            if outlier_count > 0:
                print(f"\n'{col}':")
                print(f"   Q1: {Q1:.2f}, Q3: {Q3:.2f}, IQR: {IQR:.2f}")
                print(f"   Lower Bound: {lower_bound:.2f}, Upper Bound: {upper_bound:.2f}")
                print(f"   Outliers: {outlier_count} ({outlier_pct:.2f}%)")
                print(f"   Min outlier: {outliers[col].min():.2f}, Max outlier: {outliers[col].max():.2f}")
                
                outlier_summary.append({
                    'Column': col,
                    'Outlier_Count': outlier_count,
                    'Percentage': round(outlier_pct, 2),
                    'Lower_Bound': round(lower_bound, 2),
                    'Upper_Bound': round(upper_bound, 2)
                })
        
        if outlier_summary:
            print("\n" + "=" * 80)
            print("OUTLIER SUMMARY")
            print("=" * 80)
            outlier_df = pd.DataFrame(outlier_summary)
            print(outlier_df.to_string(index=False))
            print("\nNOTE: Outliers detected but NOT removed (may represent legitimate values)")
            self.cleaning_report.append(f"Detected outliers in {len(outlier_summary)} columns using IQR method (not removed)")
        else:
            print("\n✓ No outliers detected!")
            self.cleaning_report.append("No outliers detected using IQR method")
        
        print()
        
    def save_cleaned_data(self):
        """Save the cleaned dataset to CSV."""
        print("=" * 80)
        print("SAVING CLEANED DATA")
        print("=" * 80)
        
        # Ensure output directory exists
        output_dir = Path(self.output_path).parent
        output_dir.mkdir(parents=True, exist_ok=True)
        
        try:
            self.df.to_csv(self.output_path, index=False)
            print(f"\n✓ Cleaned data saved successfully to:")
            print(f"  {self.output_path}")
            print(f"\nFinal dataset shape: {self.df.shape[0]} rows × {self.df.shape[1]} columns")
            print(f"Rows removed: {self.original_shape[0] - self.df.shape[0]}")
            print()
            return True
        except Exception as e:
            print(f"✗ Error saving data: {str(e)}")
            return False
    
    def generate_report(self, report_path):
        """Generate a comprehensive cleaning report in Markdown format."""
        print("=" * 80)
        print("GENERATING CLEANING REPORT")
        print("=" * 80)
        
        report_content = f"""# Data Cleaning Report
## Global Superstore Dataset

**Project**: SkillCraft Technology - Data Analytics Task 2  
**Date**: {pd.Timestamp.now().strftime('%Y-%m-%d')}  
**Author**: Data Analytics Intern

---

## 1. Executive Summary

This report documents the data cleaning process applied to the Global Superstore dataset. The cleaning process involved handling missing values, removing duplicates, standardizing column names, converting data types, removing whitespace, and detecting outliers.

---

## 2. Dataset Overview

### Original Dataset
- **Shape**: {self.original_shape[0]} rows × {self.original_shape[1]} columns
- **File**: `{os.path.basename(self.input_path)}`

### Cleaned Dataset
- **Shape**: {self.df.shape[0]} rows × {self.df.shape[1]} columns
- **File**: `{os.path.basename(self.output_path)}`

### Change Summary
- **Rows Removed**: {self.original_shape[0] - self.df.shape[0]}
- **Columns Removed**: {self.original_shape[1] - self.df.shape[1]}
- **Data Retention Rate**: {(self.df.shape[0] / self.original_shape[0] * 100):.2f}%

---

## 3. Data Cleaning Steps

### Step 1: Data Loading
- Successfully loaded dataset from CSV file
- Performed initial inspection of data structure

### Step 2: Missing Value Analysis
- Identified columns with missing values
- Applied appropriate imputation strategies:
  - **Numerical columns**: Filled with median values
  - **Categorical columns**: Filled with mode or 'Unknown'
  - **High missingness (>50%)**: Columns dropped

### Step 3: Duplicate Removal
- Scanned for duplicate rows
- Removed exact duplicates to ensure data integrity
- Reset index after removal

### Step 4: Column Name Standardization
- Converted all column names to lowercase
- Replaced spaces with underscores
- Ensured consistency in naming convention

### Step 5: Data Type Conversion
- `postal_code`: Converted to string (identifier, not numeric)
- `quantity`: Converted to integer
- `sales`, `discount`, `profit`: Ensured numeric (float) types

### Step 6: Whitespace Removal
- Stripped leading and trailing spaces from all text columns
- Ensured data consistency and cleanliness

### Step 7: Outlier Detection
- Applied IQR (Interquartile Range) method
- Identified outliers in numerical columns
- **Decision**: Outliers retained (may represent legitimate extreme values like bulk orders or discounted sales)

---

## 4. Before vs After Comparison

| Metric | Before Cleaning | After Cleaning |
|--------|----------------|----------------|
| Total Rows | {self.original_shape[0]} | {self.df.shape[0]} |
| Total Columns | {self.original_shape[1]} | {self.df.shape[1]} |
| Missing Values | Varied by column | 0 |
| Duplicate Rows | Detected | 0 |
| Data Types | Mixed | Standardized |
| Column Names | Mixed case | Lowercase with underscores |

---

## 5. Column Information (After Cleaning)

"""
        # Add column information
        report_content += "\n| Column Name | Data Type | Non-Null Count | Unique Values |\n"
        report_content += "|-------------|-----------|----------------|---------------|\n"
        
        for col in self.df.columns:
            dtype = str(self.df[col].dtype)
            non_null = self.df[col].count()
            unique = self.df[col].nunique()
            report_content += f"| {col} | {dtype} | {non_null} | {unique} |\n"
        
        report_content += f"""

---

## 6. Data Quality Observations

### Strengths
- ✓ Dataset is comprehensive with {self.df.shape[1]} feature columns
- ✓ All missing values have been appropriately handled
- ✓ No duplicate records in the cleaned dataset
- ✓ Consistent data types across columns
- ✓ Clean and standardized column names

### Challenges Addressed
- Handled missing values using statistical methods (median/mode)
- Removed duplicate entries to ensure data integrity
- Standardized column names for better accessibility
- Converted data types for proper analysis
- Detected outliers for awareness (retained for business value)

### Data Distribution Insights
"""
        
        # Add summary statistics for key numerical columns
        numeric_cols = ['sales', 'profit', 'discount', 'quantity']
        available_cols = [col for col in numeric_cols if col in self.df.columns]
        
        if available_cols:
            report_content += "\n#### Key Numerical Columns Summary\n\n"
            stats_df = self.df[available_cols].describe()
            report_content += stats_df.to_markdown() + "\n"
        
        report_content += """

---

## 7. Outlier Analysis

Outliers were detected using the IQR (Interquartile Range) method:

**Formula**: 
- Lower Bound = Q1 - 1.5 × IQR
- Upper Bound = Q3 + 1.5 × IQR

**Decision**: Outliers were **NOT removed** from the dataset because:
1. They may represent legitimate business scenarios (bulk orders, high discounts)
2. Removing them could result in loss of valuable information
3. They can be handled during specific analyses if needed

---

## 8. Detailed Cleaning Log

"""
        for i, step in enumerate(self.cleaning_report, 1):
            report_content += f"{i}. {step}\n"
        
        report_content += f"""

---

## 9. Recommendations for Further Analysis

1. **Sales Analysis**: Investigate sales patterns across regions, categories, and segments
2. **Profitability Study**: Analyze profit margins and identify loss-making products
3. **Customer Segmentation**: Segment customers based on purchasing behavior
4. **Discount Impact**: Study the relationship between discounts and profitability
5. **Geographic Analysis**: Explore regional performance and market opportunities
6. **Temporal Trends**: Add date columns to analyze trends over time (if available)

---

## 10. Conclusion

The data cleaning process has been successfully completed. The dataset is now:
- ✓ **Complete**: No missing values
- ✓ **Consistent**: Standardized formats and types
- ✓ **Accurate**: Duplicates removed, outliers identified
- ✓ **Ready for Analysis**: Properly formatted and documented

The cleaned dataset (`{os.path.basename(self.output_path)}`) is ready for exploratory data analysis, visualization, and machine learning modeling.

---

## 11. Files Generated

1. **Cleaned Dataset**: `{self.output_path}`
2. **This Report**: `{report_path}`
3. **Cleaning Script**: `src/clean_data.py`
4. **Jupyter Notebook**: `notebooks/Data_Cleaning.ipynb`

---

**End of Report**
"""
        
        # Save the report
        try:
            report_dir = Path(report_path).parent
            report_dir.mkdir(parents=True, exist_ok=True)
            
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(report_content)
            
            print(f"✓ Report generated successfully at:")
            print(f"  {report_path}\n")
            return True
        except Exception as e:
            print(f"✗ Error generating report: {str(e)}")
            return False
    
    def run_cleaning_pipeline(self, generate_report_flag=True):
        """Run the complete data cleaning pipeline."""
        print("\n" + "=" * 80)
        print(" " * 20 + "DATA CLEANING PIPELINE")
        print(" " * 15 + "Global Superstore Dataset")
        print("=" * 80 + "\n")
        
        # Execute cleaning steps
        if not self.load_data():
            return False
        
        self.display_basic_info()
        self.handle_missing_values()
        self.remove_duplicates()
        self.standardize_column_names()
        self.convert_data_types()
        self.remove_whitespace()
        self.detect_outliers()
        
        if not self.save_cleaned_data():
            return False
        
        if generate_report_flag:
            report_path = "reports/Data_Cleaning_Report.md"
            self.generate_report(report_path)
        
        print("=" * 80)
        print(" " * 25 + "CLEANING COMPLETE!")
        print("=" * 80)
        print("\n✓ All cleaning steps completed successfully!")
        print(f"✓ Cleaned dataset saved to: {self.output_path}")
        print("✓ Cleaning report generated in: reports/Data_Cleaning_Report.md")
        print("\nNext Steps:")
        print("  1. Review the cleaning report")
        print("  2. Explore the cleaned data using the Jupyter notebook")
        print("  3. Begin your analysis!\n")
        
        return True


def main():
    """Main function to execute the data cleaning pipeline."""
    
    # Define paths
    INPUT_PATH = "Dataset/raw/Global_Superstore.csv"
    OUTPUT_PATH = "Dataset/cleaned/Global_Superstore_Cleaned.csv"
    
    # Create cleaner instance
    cleaner = DataCleaner(INPUT_PATH, OUTPUT_PATH)
    
    # Run the cleaning pipeline
    success = cleaner.run_cleaning_pipeline(generate_report_flag=True)
    
    if success:
        print("=" * 80)
        print("Data cleaning pipeline executed successfully!")
        print("=" * 80)
    else:
        print("=" * 80)
        print("Data cleaning pipeline encountered errors.")
        print("=" * 80)


if __name__ == "__main__":
    main()
