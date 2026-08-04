# 🛒 Walmart Weekly Sales Prediction using XGBoost

An end-to-end Machine Learning project focused on predicting Walmart's weekly sales using historical sales, seasonal trends, and economic indicators. The project follows an industry-standard machine learning workflow, beginning with data preprocessing and exploratory data analysis (EDA), followed by model development, hyperparameter tuning, evaluation, and deployment through a Streamlit web application.

---

## Project Status

**Current Progress:** Completed ✅

Project Includes:

- Data Cleaning
- Feature Engineering
- Exploratory Data Analysis (EDA)
- Feature Selection
- Train-Test Split
- Feature Scaling
- Model Training
- Cross Validation
- Hyperparameter Tuning
- Model Evaluation
- Feature Importance Analysis
- Residual Analysis
- Streamlit Web Application
- Model Serialization

---

## Dataset

**Dataset:** Walmart Weekly Sales Dataset

### Target Variable

- Weekly_Sales

### Features

- Store
- Holiday_Flag
- Temperature
- Fuel_Price
- CPI
- Unemployment
- Date

### Date Feature Engineering

The original **Date** column was transformed into:

- Year
- Month
- Week
- Quarter

The cleaned dataset was exported separately for Tableau dashboard development.

---

## Project Structure

```text
Walmart_Sales/
│
├── data/
│   ├── Walmart_Sales.csv
│   └── Walmart_Sales_Cleaned.csv
│
├── images/
│   ├── Actual_vs_Predicted.png
│   ├── CPI_vs_Weekly_Sales.png
│   ├── Feature_Importance.png
│   ├── Fuel_Price_vs_Weekly_Sales.png
│   ├── Heatmap.png
│   ├── Holiday_vs_Weekly_Sales.png
│   ├── Monthly_Sales_Trend.png
│   ├── Residual_plot.png
│   ├── Store_Wise_Sales.png
│   ├── Temperature_vs_Weekly_Sales.png
│   ├── Unemployment_vs_Weekly_Sales.png
│   ├── Weekly_sales_Boxplot.png
│   └── Weekly_sales_distribution.png
│
├── model/
│   ├── XGBoost_model.pkl
│   └── scaler.pkl
│
├── src/
│   ├── SS_1.png
│   ├── SS_2.png
│   ├── SS_3.png
│   └── SS_4.png
│
├── notebook/
│   └── Walmart_Sales_Prediction.ipynb
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Machine Learning Workflow

### 1. Data Preprocessing

- Removed duplicate records
- Converted Date to datetime format
- Feature Engineering
- Selected relevant features
- Exported cleaned dataset

---

### 2. Feature Engineering

Extracted from **Date**

- Year
- Month
- Week
- Quarter

---

### 3. Exploratory Data Analysis

Performed the following analyses:

- Weekly Sales Distribution
- Weekly Sales Boxplot
- Temperature vs Weekly Sales
- Fuel Price vs Weekly Sales
- CPI vs Weekly Sales
- Unemployment vs Weekly Sales
- Holiday vs Weekly Sales
- Monthly Sales Trend
- Store-wise Sales
- Correlation Heatmap

---

### 4. Model Development

Implemented multiple regression algorithms:

- Linear Regression
- Lasso Regression
- XGBoost Regressor

---

### 5. Cross Validation

Used **5-Fold K-Fold Cross Validation** to compare model performance.

Evaluation Metrics:

- R² Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

---

### 6. Hyperparameter Tuning

Optimized the XGBoost model using **RandomizedSearchCV**.

Best Parameters:

```python
{
    'subsample': 0.7,
    'n_estimators': 300,
    'max_depth': 5,
    'learning_rate': 0.1,
    'colsample_bytree': 1.0
}
```

---

### 7. Model Evaluation

| Metric | Score |
|---------|-------|
| R² Score | **0.9781** |
| MAE | **50,798.88** |
| RMSE | **84,007.97** |

Average Cross Validation R²:

**0.9763**

---

### 8. Model Interpretation

Generated:

- Feature Importance Plot
- Actual vs Predicted Plot
- Residual Plot

These visualizations help interpret model behavior and validate prediction quality.

---

## Key Insights

- XGBoost significantly outperformed Linear Regression and Lasso Regression.
- Store was the most influential feature affecting weekly sales.
- Holiday weeks generally exhibited higher average sales.
- Weekly sales contained several outliers.
- Temperature and economic indicators showed relatively weak linear relationships with weekly sales.
- The trained XGBoost model explained approximately **97.8%** of the variance in weekly sales.

---

## Streamlit Web Application

A fully interactive Streamlit application was developed to demonstrate the trained model.

### Features

- Interactive prediction dashboard
- Sidebar input controls
- Real-time weekly sales prediction
- Model information
- Performance metrics
- Feature importance visualization
- Residual analysis
- Correlation heatmap
- Dataset overview

---

## Application Preview

### Home Page

![Home](src/SS_1.png)


### Visualizations
![Dashboard](src/SS_2.png)



![Analysis](src/SS_3.png)


### About Model
![Visualizations](src/SS_4.png)

---

## Technologies Used

### Programming Language

- Python

### Data Analysis

- Pandas
- NumPy

### Visualization

- Matplotlib
- Seaborn

### Machine Learning

- Scikit-learn
- XGBoost

### Hyperparameter Tuning

- RandomizedSearchCV

### Deployment

- Streamlit

### Model Serialization

- Joblib

---

## Installation

Clone the repository

```bash
git clone https://github.com/Pranav-1719/Data-Science-Machine-Learning/tree/main/Wallmart_Sales
```

Navigate to the project directory

```bash
cd Walmart_Sales
```

Install the required packages

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

## Future Improvements

- Deploy on Streamlit Community Cloud
- Add SHAP Explainability
- Interactive Plotly Visualizations
- Batch Prediction using CSV Upload
- Docker Containerization
- CI/CD Pipeline

---

## Author

**Pranav Sankpal**

Computer Science Engineering Student

Government College of Engineering, Kolhapur

**GitHub:** *https://github.com/Pranav-1719*

**LinkedIn:** *https://www.linkedin.com/in/pranav-s-sankpal/*