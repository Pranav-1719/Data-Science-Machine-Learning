# Customer Churn Prediction and Behavior Analysis

An end-to-end machine learning project focused on customer churn analysis, behavioral analytics, feature engineering, exploratory data analysis (EDA), predictive modeling, and business insights using Python and Scikit-learn.

---

# Project Overview

Customer churn is one of the most critical business challenges in customer-centric industries. Retaining existing customers is often significantly more cost-effective than acquiring new ones, making churn prediction an essential component of business strategy.

This project analyzes customer demographics, transaction history, customer service interactions, and service usage behavior to identify churn drivers and develop a machine learning model capable of predicting customer attrition.

The project covers the complete data science workflow, from data preprocessing and exploratory analysis to machine learning implementation and business interpretation.

### Project Workflow

* Data Collection
* Data Cleaning and Preprocessing
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Customer-Level Aggregation
* Correlation Analysis
* Feature Scaling and Encoding
* Machine Learning Modeling
* Model Evaluation
* Feature Importance Analysis
* Business Interpretation
* Churn Prediction Insights

---

# Dataset Source

Dataset provided through The Forage Virtual Internship Program.

```python
url = "https://cdn.theforage.com/vinternships/companyassets/Zbnc2o4ok6kD2NEXx/2kCX23cgKgCumeEam/1721851467492/Customer_Churn_Data_Large.xlsx"
```

---

# Datasets Used

The project utilizes multiple datasets contained within a single Excel workbook.

## DF1 — Customer Demographics

Includes:

* CustomerID
* Age
* Gender
* MaritalStatus
* IncomeLevel

Purpose:

Analyze demographic characteristics and their relationship with customer churn.

---

## DF2 — Transaction History

Includes:

* Purchase transactions
* Amount spent
* Product categories
* Transaction frequency

Purpose:

Evaluate spending behavior and purchasing patterns.

---

## DF3 — Customer Service Interactions

Includes:

* Customer complaints
* Feedback records
* Interaction types
* Resolution status

Purpose:

Assess customer satisfaction and service-related churn indicators.

---

## DF4 — Service Usage Data

Includes:

* Login frequency
* Platform activity
* Usage patterns

Purpose:

Measure customer engagement and product adoption.

---

## DF5 — Churn Labels

Includes:

* Customer churn status

Purpose:

Provide the target variable for machine learning classification.

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

The preprocessing pipeline transformed raw customer data into a structured machine learning-ready dataset.

## Data Cleaning

Performed:

* Missing value analysis
* Duplicate detection
* Datatype validation
* Consistency checks

Results:

* Minimal missing values
* No significant data quality issues
* Clean analytical dataset generated

---

## Encoding

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

## Feature Scaling

Standardization was performed using:

```python
from sklearn.preprocessing import StandardScaler
```

Scaled Features:

* Age
* AmountSpent
* LoginFrequency
* TotalSpent
* AvgSpent
* TransactionCount
* InteractionCount
* ComplaintCount
* UnresolvedCount

---

# Feature Engineering

Several behavioral indicators were created to improve model performance.

## Transaction Features

Generated:

* TotalSpent
* TransactionCount
* AvgSpent

Purpose:

Capture customer purchasing behavior and spending habits.

---

## Customer Interaction Features

Generated:

* InteractionCount
* ComplaintCount
* UnresolvedCount

Purpose:

Measure customer engagement with support services and dissatisfaction levels.

---

## Customer-Level Aggregation

All datasets were merged using:

```python
"CustomerID"
```

The final dataset combines:

* Demographic information
* Transaction history
* Customer service interactions
* Platform engagement metrics
* Churn labels

---

# Exploratory Data Analysis (EDA)

EDA was conducted to understand customer behavior and identify factors associated with churn.

Analysis included:

* Descriptive statistics
* Churn distribution analysis
* Spending behavior analysis
* Login frequency analysis
* Complaint trend analysis
* Correlation heatmaps
* Feature relationship analysis
* Distribution visualizations

---

# Key EDA Findings

## Churn Distribution

The dataset exhibits a moderate class imbalance, with the majority of customers remaining active and a smaller segment identified as churned.

---

## Login Frequency Analysis

Customers with lower login frequency demonstrated significantly higher churn rates.

This indicates customer engagement is a critical retention factor.

---

## Spending Behavior Analysis

Customers with lower spending activity and fewer transactions were more likely to churn.

Consistent purchasing behavior correlated with improved customer retention.

---

## Complaint Analysis

Customers with multiple complaints and unresolved issues displayed substantially higher churn probabilities.

Customer support quality emerged as a major business driver.

---

## Correlation Analysis

Behavioral variables demonstrated stronger relationships with churn than demographic features.

Key observations:

* Negative correlation between LoginFrequency and churn.
* Positive correlation between ComplaintCount and churn.
* Positive relationship between customer activity and retention.

---

# Machine Learning Implementation

## Random Forest Classifier

A Random Forest Classifier was developed to predict customer churn.

### Libraries Used

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
```

### Modeling Workflow

1. Train-Test Split
2. Feature Scaling
3. Model Training
4. Prediction Generation
5. Model Evaluation
6. Feature Importance Analysis

### Objectives

* Predict customer churn probability
* Identify major churn drivers
* Generate actionable business insights
* Support customer retention strategies

---

# Model Evaluation

The Random Forest model was evaluated using multiple classification metrics.

## Evaluation Metrics

* Accuracy Score
* Precision Score
* Recall Score
* F1-Score
* ROC-AUC Score
* Confusion Matrix

The model demonstrated strong predictive performance in identifying customers at risk of churn.

---

## Classification Report

The classification report provided a detailed assessment of model performance across both churn and non-churn classes.

Metrics analyzed:

* Precision
* Recall
* F1 Score
* Support

---

## Confusion Matrix Analysis

The confusion matrix was used to evaluate:

* True Positives
* True Negatives
* False Positives
* False Negatives

This analysis helps quantify the business impact of incorrect churn predictions.

---

# Feature Importance Analysis

Feature importance scores from the Random Forest model were used to identify the strongest contributors to churn prediction.

Most influential factors included:

* Login Frequency
* Complaint Count
* Unresolved Issues
* Transaction Count
* Total Spending

The analysis confirms that customer behavior is more predictive of churn than demographic attributes.

---

# Business Interpretation

The project generated several actionable business insights.

### Customer Engagement

Customers with declining login frequency exhibited significantly higher churn risk.

Recommendation:

* Implement engagement campaigns.
* Introduce personalized notifications.
* Improve customer onboarding experiences.

---

### Customer Support Quality

Unresolved complaints emerged as one of the strongest churn indicators.

Recommendation:

* Reduce complaint resolution time.
* Improve support responsiveness.
* Monitor customer satisfaction metrics.

---

### Spending Behavior

Customers with declining transaction activity often displayed elevated churn risk.

Recommendation:

* Deploy targeted retention offers.
* Introduce loyalty programs.
* Increase personalized product recommendations.

---

# Key Insights

Major churn indicators identified include:

* Low Login Frequency
* High Complaint Count
* High Unresolved Complaint Rate
* Low Transaction Activity
* Reduced Customer Engagement

Additional observations:

* Behavioral metrics outperform demographic variables in predictive power.
* Customer experience significantly influences retention.
* Early behavioral signals can be used to proactively identify at-risk customers.

---

# Conclusion

This project successfully developed a complete customer churn prediction pipeline using real-world customer data.

Beginning with raw multi-source datasets, the project progressed through preprocessing, feature engineering, exploratory analysis, machine learning implementation, and business interpretation.

The Random Forest model effectively identified customers likely to churn and highlighted the most influential behavioral drivers behind customer attrition.

The findings demonstrate that customer engagement, transaction behavior, and support experiences play a significantly greater role in churn prediction than demographic attributes.

These insights can help organizations improve retention strategies, reduce revenue loss, and make data-driven customer management decisions.

---

# Project Status

## Completed

✔ Data Collection

✔ Data Cleaning

✔ Data Preprocessing

✔ Feature Engineering

✔ Dataset Integration

✔ Customer-Level Aggregation

✔ Exploratory Data Analysis (EDA)

✔ Correlation Analysis

✔ Data Visualization

✔ Random Forest Model Development

✔ Model Evaluation

✔ Feature Importance Analysis

✔ Business Interpretation

✔ Churn Prediction Analysis

✔ Final Conclusions and Recommendations

---

# Future Improvements

* Hyperparameter Optimization
* Cross-Validation
* XGBoost Implementation
* LightGBM Comparison
* Customer Segmentation
* Interactive Dashboards
* Real-Time Churn Prediction
* Flask/FastAPI Deployment
* Cloud-Based Model Hosting

---

# Repository Structure

```text
Customer-Churn-Prediction/
│
├── Customer Churn Prediction and Behavior Analysis.ipynb
└── README.md
```

---

# Author

**Pranav Sankpal**

Engineering Student | Data Science & Machine Learning Enthusiast

