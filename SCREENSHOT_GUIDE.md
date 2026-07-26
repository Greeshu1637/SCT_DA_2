# Screenshot Guide - SCT_DA_2
## What to Capture for Your Documentation

I've generated all the outputs for you! Here's what you should screenshot:

---

## 📸 **Screenshot 1: Terminal Output - Data Cleaning Process**

**What to capture**: The complete output from running the cleaning script

**How to get it**:
```bash
python run_notebook_with_outputs.py
```

**What it shows**:
- ✅ All 13 cleaning steps with detailed output
- Dataset shape before and after
- Column names standardization
- Data type conversions
- Outlier detection results
- Before/After comparison table

**Save as**: `screenshots/cleaning_output.png`

---

## 📸 **Screenshot 2: Outlier Visualization (Box Plots)**

**What to capture**: Box plots showing outliers in numerical columns

**Already generated**: `screenshots/outlier_boxplots.png`

**What it shows**:
- 4 box plots (sales, quantity, discount, profit)
- Visual representation of outliers
- Distribution patterns

**Note**: ✅ This is already saved automatically!

---

## 📸 **Screenshot 3: Dataset Preview - Before**

**What to capture**: First few rows of the original dataset

**How to get it**:
```python
import pandas as pd
df = pd.read_csv('Dataset/raw/Global_Superstore.csv')
print(df.head())
print(f"\nShape: {df.shape}")
print(f"Duplicates: {df.duplicated().sum()}")
```

**What it shows**:
- Original column names (Mixed case, spaces)
- Original data types
- Presence of duplicates

**Save as**: `screenshots/dataset_before.png`

---

## 📸 **Screenshot 4: Dataset Preview - After**

**What to capture**: First few rows of cleaned dataset

**How to get it**:
```python
import pandas as pd
df = pd.read_csv('Dataset/cleaned/Global_Superstore_Cleaned.csv')
print(df.head(10))
print(f"\nShape: {df.shape}")
print(f"Missing values: {df.isnull().sum().sum()}")
print(f"Duplicates: {df.duplicated().sum()}")
```

**What it shows**:
- Standardized column names (lowercase, underscores)
- Clean data
- No duplicates, no missing values

**Save as**: `screenshots/dataset_after.png`

---

## 📸 **Screenshot 5: Data Cleaning Report**

**What to capture**: The generated Markdown report

**Where to find it**: `reports/Data_Cleaning_Report.md`

**What to show**:
- Open in a Markdown viewer or VS Code
- Scroll through sections
- Capture key sections:
  - Executive Summary
  - Before vs After table
  - Column Information table
  - Outlier Summary

**Save as**: `screenshots/cleaning_report.png`

---

## 📸 **Screenshot 6: Project Structure**

**What to capture**: File explorer showing complete project structure

**How to capture**:
1. Open File Explorer
2. Navigate to `SCT_DA_2` folder
3. Expand all folders
4. Take screenshot showing:
   - Dataset/raw/ and cleaned/
   - notebooks/
   - src/
   - reports/
   - All root files

**Save as**: `screenshots/project_structure.png`

---

## 📸 **Screenshot 7: Before vs After Comparison**

**What to capture**: Key metrics comparison

**Already shown in terminal output**, but you can create a nice table:

```
| Metric          | Before  | After |
|-----------------|---------|-------|
| Rows            | 9,993   | 9,976 |
| Columns         | 13      | 13    |
| Missing Values  | 0       | 0     |
| Duplicates      | 17      | 0     |
```

**Save as**: `screenshots/before_after_comparison.png`

---

## 🎨 **Optional Screenshots** (Bonus)

### 8. Code Screenshot
- Open `src/clean_data.py` in VS Code
- Show the DataCleaner class
- **Save as**: `screenshots/code_structure.png`

### 9. README File
- Open `README.md` in VS Code or GitHub
- Show professional documentation
- **Save as**: `screenshots/readme.png`

### 10. Requirements File
- Show `requirements.txt` content
- **Save as**: `screenshots/requirements.png`

---

## 📋 **Quick Capture Checklist**

- [ ] Terminal output (cleaning process)
- [ ] Box plots (already generated!)
- [ ] Dataset before cleaning
- [ ] Dataset after cleaning
- [ ] Cleaning report
- [ ] Project structure
- [ ] Before/after comparison
- [ ] Code structure (optional)
- [ ] README (optional)

---

## 💡 **Pro Tips for Great Screenshots**

1. **Resolution**: Use at least 1920x1080
2. **Zoom**: Make sure text is readable
3. **Crop**: Remove unnecessary parts
4. **Highlight**: Use arrows or boxes to emphasize key points
5. **Organize**: Name files clearly
6. **Context**: Include headers/titles in screenshots

---

## 🚀 **Quick Commands**

Run these in order to generate all outputs:

```bash
# 1. Generate all outputs
python run_notebook_with_outputs.py

# 2. View cleaned data
python -c "import pandas as pd; df=pd.read_csv('Dataset/cleaned/Global_Superstore_Cleaned.csv'); print(df.head()); print(f'\nShape: {df.shape}')"

# 3. Check the box plot
# Already saved to: screenshots/outlier_boxplots.png
```

---

## 📦 **What You Already Have**

✅ **Generated automatically**:
- `screenshots/outlier_boxplots.png` - Box plot visualization

✅ **Ready to view**:
- `reports/Data_Cleaning_Report.md` - Complete report
- `Dataset/cleaned/Global_Superstore_Cleaned.csv` - Cleaned data
- All source code and documentation

---

## 🎯 **Screenshot Priority**

**Must Have** (for portfolio/submission):
1. Terminal cleaning output
2. Box plots (already saved!)
3. Project structure
4. Before/after data preview

**Nice to Have** (adds professionalism):
5. Cleaning report
6. Code structure
7. README preview

---

**All outputs are ready! Just capture the screenshots using the methods above.** 📸✨
