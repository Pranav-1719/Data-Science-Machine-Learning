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
- Customer-level aggregation
- Standardization and encoding

The project successfully identifies important behavioral factors influencing customer churn and prepares a machine learning-ready analytical dataset for future predictive modeling.

---

# Dataset Source

Dataset provided through The Forage virtual internship program.

```python
url = "https://cdn.theforage.com/vinternships/companyassets/Zbnc2o4ok6kD2NEXx/2kCX23cgKgCumeEam/1721851467492/Customer_Churn_Data_Large.xlsx"

excel = pd.ExcelFile(url)
```

---

# Datasets Used

The Excel workbook contains multiple datasets related to customer behavior.

## DF1 — Customer Demographics

Includes:

- CustomerID
- Age
- Gender
- MaritalStatus
- IncomeLevel

Purpose:
Analyze demographic patterns and customer attributes that may influence churn behavior.

---

## DF2 — Transaction History

Includes:

- Transaction data
- Amount spent
- Product categories
- Purchase activity

Purpose:
Analyze customer spending behavior, purchasing frequency, and financial engagement.

---

## DF3 — Customer Service Interactions

Includes:

- Complaints
- Feedback
- Inquiry interactions
- Resolution status

Purpose:
Understand customer satisfaction, complaints, and support-related churn indicators.

---

## DF4 — Service Usage Data

Includes:

- Login frequency
- Last login date
- Platform/service usage

Purpose:
Measure customer engagement and platform activity.

---

## DF5 — Churn Labels

Includes:

- Customer churn status
- Binary target variable

Purpose:
Serve as the target variable for churn analysis and future machine learning prediction.

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- Statsmodels
- Scikit-learn

---

# Data Preprocessing

The preprocessing pipeline included several stages to ensure high-quality analytical data.

## Data Cleaning

Performed:
- Missing value analysis
- Duplicate value detection
- Datatype inspection

Results:
- No significant missing value issues detected
- No major duplicate records identified

---

## Encoding

Categorical variables were transformed into numerical format using:

### Label Encoding
Used for:
- Gender
- IncomeLevel

### One-Hot Encoding
Used for:
- MaritalStatus
- ProductCategory
- InteractionType
- ResolutionStatus
- ServiceUsage

This conversion ensured compatibility with statistical analysis and future machine learning algorithms.

---

## Standardization

Numerical features were standardized using:

```python
StandardScaler()
```

Standardized variables included:
- AmountSpent
- LoginFrequency
- Age
- TotalSpent
- AvgSpent
- TransactionCount
- InteractionCount
- ComplaintCount
- UnresolvedCount

---

# Feature Engineering

To improve analytical quality, several behavioral features were engineered.

## Transaction Features

Generated:
- TotalSpent
- TransactionCount
- AvgSpent

These variables summarize customer purchasing behavior.

---

## Customer Interaction Features

Generated:
- InteractionCount
- ComplaintCount
- UnresolvedCount

These features capture customer dissatisfaction and support engagement.

---

## Customer-Level Aggregation

All datasets were merged using:

```python
CustomerID
```

This created a unified customer-level dataset combining:
- demographic information
- spending behavior
- customer support interactions
- service usage activity
- churn status

---

# Exploratory Data Analysis (EDA)

EDA was conducted to identify trends, behavioral patterns, and relationships associated with customer churn.

The analysis included:
- statistical summaries
- churn distribution analysis
- spending behavior analysis
- login activity analysis
- complaint analysis
- correlation analysis

---

## Key EDA Findings

### Churn Distribution

The dataset showed that most customers remained active while a smaller proportion churned, indicating moderate class imbalance.

---

### Login Frequency Analysis

Customers with lower login frequency demonstrated higher churn tendency, suggesting reduced customer engagement may contribute to customer attrition.

---

### Spending Behavior Analysis

Customers with lower spending activity and fewer transactions showed increased likelihood of churn.

Higher transaction activity generally indicated stronger customer retention.

---

### Complaint and Resolution Analysis

Customers with higher complaint counts and unresolved customer service issues demonstrated greater churn probability.

This suggests customer support quality strongly influences retention.

---

### Correlation Analysis

Behavioral features demonstrated stronger relationships with churn compared to demographic features.

Important observations included:
- negative relationship between LoginFrequency and churn
- positive relationship between complaint-related variables and churn
- moderate relationship between transaction activity and customer retention

---

# Current Project Status

## Completed

- Data collection
- Data preprocessing
- Data cleaning
- Feature engineering
- Dataset merging
- Customer-level aggregation
- Exploratory Data Analysis (EDA)
- Correlation analysis
- Machine learning-ready dataset preparation

---

## Upcoming

- Machine learning model development
- Churn prediction modeling
- Model evaluation
- Feature importance analysis
- Hyperparameter optimization
- Business recommendation system

---

# Repository Structure

```text
Customer-Churn-Prediction-and-Behavior-Analysis/
│
├── data/
├── notebooks/
├── images/
├── cleaned_dataset/
├── reports/
├── README.md
└── churn_analysis.ipynb
```

---

# Key Objectives

- Understand customer churn behavior
- Analyze customer engagement patterns
- Engineer meaningful behavioral features
- Identify important churn indicators
- Prepare machine learning-ready datasets
- Build predictive churn models

---

# Key Insights

The analysis identified several important churn indicators:

- Customers with lower login frequency were more likely to churn.
- Unresolved complaints significantly increased churn probability.
- Lower transaction activity correlated with customer attrition.
- Behavioral features were more informative than demographic variables.
- Customer engagement played a major role in retention.

---

# Future Improvements

Future stages of the project may include:

- Machine learning model training
- Feature importance analysis
- Predictive churn dashboards
- Customer segmentation
- Retention strategy recommendations
- Model deployment

---

# Author

Pranav