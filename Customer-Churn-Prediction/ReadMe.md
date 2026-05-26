````markdown
# Customer Churn Prediction and Behavior Analysis

An end-to-end customer churn analytics project focused on data collection, exploratory data analysis (EDA), preprocessing, feature engineering, and machine learning-ready dataset preparation using Python.

---

# Project Overview

Customer churn is one of the most critical business problems in customer-centric industries. This project focuses on analyzing customer demographics, transaction behavior, customer service interactions, and platform usage patterns to identify potential indicators of churn.

The project currently includes:

- Data collection from multiple Excel sheets
- Data preprocessing and cleaning
- Exploratory Data Analysis (EDA)
- Feature engineering
- Dataset integration
- Correlation analysis
- Standardization and encoding

Machine learning model development and predictive analysis will be added in later stages.

---

# Dataset Source

Dataset provided through The Forage virtual internship program.

```python
url = "https://cdn.theforage.com/vinternships/companyassets/Zbnc2o4ok6kD2NEXx/2kCX23cgKgCumeEam/1721851467492/Customer_Churn_Data_Large.xlsx"

excel = pd.ExcelFile(url)
````

---

# Datasets Used

The Excel workbook contains multiple datasets related to customer behavior.

## DF1 — Customer Demographics

Includes:

* CustomerID
* Age
* Gender
* MaritalStatus
* IncomeLevel

---

## DF2 — Transaction History

Includes:

* Transaction data
* Amount spent
* Product categories
* Purchase activity

---

## DF3 — Customer Service Interactions

Includes:

* Complaints
* Feedback
* Inquiry interactions
* Resolution status

---

## DF4 — Service Usage Data

Includes:

* Login frequency
* Last login date
* Platform/service usage

---

## DF5 — Churn Labels

Includes:

* Customer churn status
* Binary target variable

---

# Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SciPy
* Statsmodels
* Scikit-learn

---

# Data Preprocessing

The preprocessing pipeline currently includes:

## Data Cleaning

* Missing value analysis
* Duplicate value detection
* Datatype inspection

## Encoding

* Label encoding
* One-hot encoding for categorical variables

## Standardization

* Numerical feature scaling using `StandardScaler`

## Feature Engineering

* Total transaction spending
* Transaction counts
* Average customer spending
* Interaction counts
* Complaint counts
* Unresolved issue counts

## Dataset Integration

All datasets were merged using:

* `CustomerID`

to create a customer-level analytical dataset.

---

# Exploratory Data Analysis (EDA)

EDA currently includes:

* Statistical summaries
* Distribution analysis
* Correlation analysis
* Customer behavior analysis
* Transaction behavior analysis
* Service interaction analysis
* Churn-related feature exploration

---

# Current Project Status

Completed:

* Data collection
* Data preprocessing
* Dataset merging
* Feature engineering
* Exploratory Data Analysis (EDA)

Upcoming:

* Machine learning model building
* Churn prediction
* Model evaluation
* Feature importance analysis
* Business insights generation

---

# Repository Structure

```text
Customer-Churn-Prediction-and-Behavior-Analysis/
│
├── data/
├── notebooks/
├── images/
├── cleaned_dataset/
├── README.md
└── churn_analysis.ipynb
```

---

# Key Objectives

* Understand customer churn behavior
* Engineer useful behavioral features
* Prepare machine learning-ready datasets
* Identify important churn indicators
* Build predictive churn models

---

# Author

Pranav

```
```
