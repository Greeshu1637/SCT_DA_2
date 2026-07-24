# Data Cleaning and Preparation Project
## SkillCraft Technology - Data Analytics Internship Task 2

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.1.4-green)
![Status](https://img.shields.io/badge/Status-Complete-success)

---

## 📋 Project Overview

This project demonstrates professional data cleaning and preparation techniques using Python and Pandas. 
The goal is to transform raw, messy data into a clean, analysis-ready dataset following industry best practices.

**Dataset**: Global Superstore  
**Domain**: Retail Analytics  
**Objective**: Clean and prepare data for downstream analysis and machine learning



---

## 🎯 Objectives

1. Load and inspect the Global Superstore dataset
2. Identify and handle missing values
3. Remove duplicate records
4. Standardize column names and data types
5. Clean text data (remove whitespace)
6. Detect outliers using statistical methods
7. Export cleaned dataset for analysis
8. Document the entire process

---

## 📁 Project Structure

```
SCT_DA_2/
│
├── Dataset/
│   ├── raw/
│   │   └── Global_Superstore.csv          # Original dataset
│   └── cleaned/
│       └── Global_Superstore_Cleaned.csv  # Cleaned dataset
│
├── notebooks/
│   └── Data_Cleaning.ipynb                # Jupyter notebook with explanations
│
├── src/
│   └── clean_data.py                      # Python cleaning script
│
├── reports/
│   └── Data_Cleaning_Report.md            # Detailed cleaning report
│
├── screenshots/                           # Project screenshots
│
├── README.md                              # Project documentation
├── requirements.txt                       # Python dependencies
└── .gitignore                            # Git ignore rules
```

---

## 🔧 Technologies Used

- **Python 3.8+**: Core programming language
- **Pandas 2.1.4**: Data manipulation and analysis
- **NumPy 1.26.2**: Numerical computing
- **Jupyter Notebook**: Interactive development environment
- **Matplotlib & Seaborn**: Data visualization
- **Git**: Version control

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/SCT_DA_2.git
   cd SCT_DA_2
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

#### Option 1: Run the Python Script
```bash
python src/clean_data.py
```

#### Option 2: Use the Jupyter Notebook
```bash
jupyter notebook notebooks/Data_Cleaning.ipynb
```

---

## 📊 Data Cleaning Workflow

### 1. Data Loading
- Load CSV file using Pandas
- Display basic dataset information

### 2. Data Inspection
- Check shape (rows × columns)
- Identify column names and data types
- Count missing values
- Detect duplicate rows

### 3. Missing Value Handling
- Analyze missing value patterns
- Fill numerical columns with median
- Fill categorical columns with mode or 'Unknown'
- Drop columns with >50% missing data

### 4. Duplicate Removal
- Identify exact duplicate rows
- Remove duplicates and reset index

### 5. Column Standardization
- Convert column names to lowercase
- Replace spaces with underscores
- Ensure consistent naming convention

### 6. Data Type Conversion
- Convert postal codes to string
- Ensure quantity is integer
- Ensure sales, profit, discount are float

### 7. Whitespace Removal
- Strip leading/trailing spaces from text columns
- Ensure clean text data

### 8. Outlier Detection
- Apply IQR (Interquartile Range) method
- Identify outliers in numerical columns
- Report outliers (keep them for business value)

### 9. Export and Documentation
- Save cleaned dataset to CSV
- Generate comprehensive cleaning report

---

## 📈 Key Insights


- **Dataset Size**: ~10,000 rows with 13 columns
- **Missing Values**: Handled using statistical imputation
- **Duplicates**: Removed to ensure data integrity
- **Outliers**: Detected but retained (legitimate business cases)
- **Data Quality**: Improved from raw to analysis-ready state

---

## 📸 Screenshots

### Data Cleaning Process
![Cleaning Output](screenshots/cleaning_output.png)

### Before vs After Comparison
![Before After](screenshots/before_after_comparison.png)

### Cleaned Dataset Preview
![Clean Data](screenshots/cleaned_data_preview.png)

*Note: Add screenshots by running the script and capturing outputs*

---

## 📝 Reports

A detailed cleaning report is automatically generated at:
```
reports/Data_Cleaning_Report.md
```

This report includes:
- Executive summary
- Cleaning steps performed
- Before/after statistics
- Data quality observations
- Recommendations for analysis

---

## 🔍 Future Improvements

- [ ] Add date/time parsing if temporal columns exist
- [ ] Implement advanced outlier handling techniques
- [ ] Create data quality dashboard
- [ ] Add automated data validation tests
- [ ] Integrate data profiling libraries (pandas-profiling)
- [ ] Add unit tests for cleaning functions
- [ ] Create interactive visualizations
- [ ] Implement data versioning

---

## 👤 Author

**Data Analytics Intern**  
SkillCraft Technology Internship Program  
Task 2: Data Cleaning and Preparation

---

## 📄 License

This project is created for educational purposes as part of the SkillCraft Technology internship program.

---

## 🙏 Acknowledgments

- SkillCraft Technology for the internship opportunity
- Global Superstore dataset for real-world data practice
- Python and Pandas communities for excellent documentation

---

## 📞 Contact

For questions or feedback, please reach out through:
- GitHub Issues
- Email: [your-email@example.com]
- LinkedIn: [Your LinkedIn Profile]

---

**Last Updated**: 2024  
**Version**: 1.0.0

---

### Quick Start Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run cleaning script
python src/clean_data.py

# Launch Jupyter notebook
jupyter notebook notebooks/Data_Cleaning.ipynb
```

---

**Happy Data Cleaning! 🧹📊**
