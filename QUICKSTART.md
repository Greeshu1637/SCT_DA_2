# Quick Start Guide
## SCT_DA_2 - Data Cleaning Project

This guide will get you up and running in 5 minutes!

---

## ⚡ 3-Step Setup

### Step 1: Install Dependencies (1 minute)

Open your terminal in the project directory and run:

```bash
pip install -r requirements.txt
```

**Expected Output**: All packages installed successfully ✅

### Step 2: Run the Cleaning Script (2 minutes)

```bash
python src/clean_data.py
```

**What happens:**
- Loads the raw dataset (9,993 rows)
- Performs 7 cleaning operations
- Saves cleaned dataset (9,976 rows)
- Generates comprehensive report
- Shows detailed progress in terminal

**Expected Output:**
```
================================================================================
                    DATA CLEANING PIPELINE
               Global Superstore Dataset
================================================================================

✓ Data loaded successfully
✓ Missing values handled
✓ Duplicates removed (17 rows)
✓ Column names standardized
✓ Data types converted
✓ Whitespace removed
✓ Outliers detected
✓ Cleaned data saved
✓ Report generated

CLEANING COMPLETE!
```

### Step 3: Explore with Jupyter (2 minutes)

```bash
jupyter notebook notebooks/Data_Cleaning.ipynb
```

**What you'll see:**
- Interactive data cleaning walkthrough
- Visualizations and charts
- Step-by-step explanations
- Before/after comparisons

---

## 📂 What Gets Generated?

After running the script, you'll have:

1. **Cleaned Dataset**
   - Location: `Dataset/cleaned/Global_Superstore_Cleaned.csv`
   - Size: 9,976 rows × 13 columns
   - Quality: 0 missing values, 0 duplicates

2. **Cleaning Report**
   - Location: `reports/Data_Cleaning_Report.md`
   - Content: Full analysis, statistics, recommendations


---

## 🎯 Verify Everything Works

Run this quick test:

```bash
python -c "import pandas as pd; df = pd.read_csv('Dataset/cleaned/Global_Superstore_Cleaned.csv'); print(f'✅ Dataset loaded: {df.shape[0]} rows × {df.shape[1]} columns'); print(f'✅ Missing values: {df.isnull().sum().sum()}'); print(f'✅ Duplicates: {df.duplicated().sum()}')"
```

**Expected Output:**
```
✅ Dataset loaded: 9976 rows × 13 columns
✅ Missing values: 0
✅ Duplicates: 0
```

---

## 📊 What's in the Dataset?

### Columns (After Cleaning)
```
1.  ship_mode      → Shipping method (4 types)
2.  segment        → Customer segment (3 types)
3.  country        → Country (United States)
4.  city           → City name (531 unique)
5.  state          → US State (49 states)
6.  postal_code    → ZIP code (631 unique)
7.  region         → Region (4 regions)
8.  category       → Product category (3 types)
9.  sub_category   → Product subcategory (17 types)
10. sales          → Sales amount ($)
11. quantity       → Items ordered
12. discount       → Discount applied (0-80%)
13. profit         → Profit/Loss ($)
```

### Sample Data
```
ship_mode    | segment  | city        | sales   | profit
-------------|----------|-------------|---------|--------
Second Class | Consumer | Henderson   | 261.96  | 41.91
Second Class | Consumer | Henderson   | 731.94  | 219.58
Standard     | Consumer | Los Angeles | 957.58  | -383.03
```

---

## 🚀 Common Tasks

### View the Cleaned Data
```python
import pandas as pd
df = pd.read_csv('Dataset/cleaned/Global_Superstore_Cleaned.csv')
print(df.head())
```

### Check Data Quality
```python
print(f"Shape: {df.shape}")
print(f"Missing: {df.isnull().sum().sum()}")
print(f"Duplicates: {df.duplicated().sum()}")
```

### Basic Analysis
```python
print(df.describe())
print(df['category'].value_counts())
print(df['region'].value_counts())
```

---

## 🔧 Troubleshooting

### Issue: ModuleNotFoundError
**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: File Not Found
**Solution:** Make sure you're in the project root directory
```bash
cd SCT_DA_2
python src/clean_data.py
```

### Issue: Jupyter won't start
**Solution:**
```bash
pip install jupyter notebook
jupyter notebook
```

---

## 📖 Next Steps

1. ✅ Run the cleaning script
2. ✅ Review the generated report
3. ✅ Explore the Jupyter notebook
4. 📸 Capture screenshots for documentation
5. 🌐 Push to GitHub
6. 📊 Start your analysis!

---

## 🎓 Learning Path

### Beginner
- Run the script and observe output
- Read the cleaning report
- Explore the Jupyter notebook

### Intermediate
- Modify cleaning parameters
- Add your own cleaning steps
- Customize the visualizations

### Advanced
- Extend the DataCleaner class
- Add automated testing
- Create a data quality dashboard

---

## 📞 Need Help?

### Documentation
- 📄 `README.md` - Full project documentation
- 📊 `reports/Data_Cleaning_Report.md` - Cleaning analysis
- 📋 `PROJECT_SUMMARY.md` - Complete overview

### Code
- 🐍 `src/clean_data.py` - Main cleaning script
- 📓 `notebooks/Data_Cleaning.ipynb` - Interactive guide

---

## ✨ Pro Tips

1. **Always run from project root**: `cd SCT_DA_2`
2. **Check Python version**: `python --version` (need 3.8+)
3. **Use virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Mac/Linux
   ```

4. **Save terminal output**: Run `python src/clean_data.py > output.txt`
5. **Take screenshots**: Useful for portfolio and documentation

---

## 🎉 Success Indicators

You're all set when you see:

- ✅ Script runs without errors
- ✅ Cleaned CSV file created
- ✅ Report generated
- ✅ Jupyter notebook opens
- ✅ All tests pass

---

**Time to complete**: ~5 minutes  
**Difficulty**: Beginner-friendly  
**Prerequisites**: Python 3.8+, pip

---

**Happy Data Cleaning! 🧹📊✨**
