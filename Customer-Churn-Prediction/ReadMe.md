Here is an updated professional README version that includes your Random Forest model implementation and current ML progress.

# Customer Churn Prediction and Behavior Analysis

An end-to-end machine learning project focused on customer churn analysis, behavioral analytics, feature engineering, exploratory data analysis (EDA), and predictive modeling using Python and Scikit-learn.

---

# Project Overview

Customer churn is one of the most critical business challenges in customer-centric industries. This project analyzes customer demographics, transaction history, service interactions, and platform engagement behavior to identify key churn indicators and build predictive machine learning models.

The project includes:

* Data collection from multiple Excel sheets
* Data preprocessing and cleaning
* Exploratory Data Analysis (EDA)
* Feature engineering
* Customer-level dataset aggregation
* Correlation analysis
* Feature scaling and encoding
* Machine learning model development
* Random Forest model implementation
* Churn prediction analysis

The project successfully transforms raw multi-source customer data into a machine learning-ready analytical pipeline capable of identifying customer churn patterns and predicting future churn probability.

---

# Dataset Source

Dataset provided through The Forage virtual internship program.

```python
url = "https://cdn.theforage.com/vinternships/companyassets/Zbnc2o4ok6kD2NEXx/2kCX23cgKgCumeEam/1721851467492/Customer_Churn_Data_Large.xlsx"
```

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

Purpose:
Analyze demographic attributes influencing churn behavior.

---

## DF2 — Transaction History

Includes:

* Transaction activity
* Amount spent
* Product categories
* Purchase frequency

Purpose:
Analyze customer spending patterns and purchasing behavior.

---

## DF3 — Customer Service Interactions

Includes:

* Complaints
* Customer feedback
* Interaction types
* Resolution status

Purpose:
Understand customer satisfaction and service-related churn indicators.

---

## DF4 — Service Usage Data

Includes:

* Login frequency
* Last login date
* Platform/service usage

Purpose:
Measure customer engagement and activity.

---

## DF5 — Churn Labels

Includes:

* Customer churn status
* Binary target variable

Purpose:
Provide the target variable for machine learning prediction.

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
* Jupyter Notebook

---

# Data Preprocessing

The preprocessing pipeline ensured clean, structured, and machine learning-ready data.

## Data Cleaning

Performed:

* Missing value analysis
* Duplicate record detection
* Datatype validation
* Data consistency checks

Results:

* No major missing value issues detected
* Minimal duplicate records
* Clean structured dataset prepared for analysis

---

## Encoding

Categorical features were converted into numerical format using:

### Label Encoding

Applied to:

* Gender
* IncomeLevel

### One-Hot Encoding

Applied to:

* MaritalStatus
* ProductCategory
* InteractionType
* ResolutionStatus
* ServiceUsage

---

## Standardization

Numerical variables were standardized using:

```python
StandardScaler()
```

Standardized features included:

* AmountSpent
* LoginFrequency
* Age
* TotalSpent
* AvgSpent
* TransactionCount
* InteractionCount
* ComplaintCount
* UnresolvedCount

---

# Feature Engineering

Several behavioral features were engineered to improve predictive capability.

## Transaction Features

Generated:

* TotalSpent
* TransactionCount
* AvgSpent

These summarize customer purchasing behavior and spending patterns.

---

## Customer Interaction Features

Generated:

* InteractionCount
* ComplaintCount
* UnresolvedCount

These capture customer dissatisfaction and support engagement.

---

## Customer-Level Aggregation

All datasets were merged using:

```python
CustomerID
```

The final dataset combines:

* demographic information
* transaction behavior
* service interaction history
* platform engagement
* churn status

---

# Exploratory Data Analysis (EDA)

EDA was conducted to identify trends, behavioral patterns, and relationships associated with customer churn.

The analysis included:

* Statistical summaries
* Churn distribution analysis
* Spending behavior analysis
* Login activity analysis
* Complaint analysis
* Correlation heatmaps
* Feature relationship analysis

---

# Key EDA Findings

## Churn Distribution

The dataset contains a moderate class imbalance where most customers remain active while a smaller percentage churn.

---

## Login Frequency Analysis

Customers with lower login frequency demonstrated a significantly higher probability of churn.

This indicates customer engagement is strongly associated with retention.

---

## Spending Behavior Analysis

Customers with lower spending activity and fewer transactions were more likely to churn.

Higher purchasing frequency generally correlated with stronger retention.

---

## Complaint and Resolution Analysis

Customers with higher complaint counts and unresolved issues showed increased churn probability.

This suggests customer support quality plays a major role in retention.

---

## Correlation Analysis

Behavioral features demonstrated stronger correlation with churn than demographic variables.

Important observations:

* Negative relationship between LoginFrequency and churn
* Positive relationship between complaint-related variables and churn
* Moderate positive relationship between transaction activity and customer retention

---

# Machine Learning Implementation

## Random Forest Model

A Random Forest Classifier was implemented for customer churn prediction.

### Model Workflow

* Train-test split
* Feature scaling
* Model training
* Prediction generation
* Model evaluation

### Libraries Used

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
```

### Objectives

* Predict customer churn probability
* Identify important churn-driving features
* Improve customer retention strategy insights

---

# Current Project Status

## Completed

* Data collection
* Data preprocessing
* Data cleaning
* Feature engineering
* Dataset merging
* Customer-level aggregation
* Exploratory Data Analysis (EDA)
* Correlation analysis
* Machine learning-ready dataset preparation
* Random Forest model implementation
* Initial churn prediction modeling

---

## Upcoming

* Hyperparameter tuning
* Feature importance visualization
* Cross-validation
* Advanced model comparison
* XGBoost implementation
* Model optimization
* Business recommendation system
* Deployment pipeline

---

# Repository Structure

```text id="m6pw1t"
Customer-Churn-Prediction/
│
├── Customer Churn Prediction and Behavior Analysis.ipynb
├── model.csv
└── README.md
```


---

# Key Objectives

* Understand customer churn behavior
* Analyze engagement patterns
* Engineer predictive behavioral features
* Identify major churn indicators
* Build machine learning churn prediction models
* Improve retention strategy insights

---

# Key Insights

The analysis identified several major churn indicators:

* Lower login frequency strongly increased churn probability
* Unresolved complaints significantly impacted customer retention
* Lower transaction activity correlated with customer attrition
* Behavioral features were more predictive than demographic variables
* Customer engagement metrics played a critical role in churn prediction

---

# Future Improvements

Future development stages may include:

* Advanced ensemble models
* Feature importance dashboards
* Customer segmentation
* Real-time churn prediction
* Interactive analytics dashboards
* Deployment using Flask or FastAPI
* Cloud deployment and monitoring

---

# Author

Pranav Sankpal

Engineering Student | Machine Learning & Data Science Enthusiast
