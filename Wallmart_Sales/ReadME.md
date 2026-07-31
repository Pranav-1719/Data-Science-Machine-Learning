# Walmart Sales Prediction using Linear Regression

A Machine Learning project focused on predicting Walmart weekly sales using historical sales and economic indicators. This project follows an end-to-end machine learning workflow, beginning with Exploratory Data Analysis (EDA) and progressing toward model development, evaluation, and deployment-ready practices.

---

## Project Status

**Current Progress:** Exploratory Data Analysis (EDA) Completed

Upcoming Stages:
- Data Preprocessing
- Feature Scaling
- Train-Test Split
- Linear Regression Model
- Cross Validation
- Model Evaluation
- Model Comparison
- Tableau Dashboard
- Model Serialization

---

## Dataset

**Dataset:** Walmart Sales Dataset

Features:

- Store
- Holiday_Flag
- Temperature
- Fuel_Price
- CPI
- Unemployment
- Date
- Weekly_Sales (Target Variable)

Date has been transformed into:

- Year
- Month
- Week
- Quarter

The cleaned dataset is also exported for Tableau dashboard development.

---

## Project Structure

```
Walmart_Sales/
│
├── Images/
│   ├── histogram_weekly_sales.png
│   ├── boxplot_weekly_sales.png
│   ├── temperature_vs_sales.png
│   ├── fuel_price_vs_sales.png
│   ├── cpi_vs_sales.png
│   ├── unemployment_vs_sales.png
│   ├── holiday_vs_sales.png
│   ├── monthly_sales_trend.png
│   ├── store_wise_sales.png
│   └── correlation_heatmap.png
│
├── linear_regression.ipynb
│
├── Walmart_Sales_Cleaned.csv
│
└── README.md
```

---

## Exploratory Data Analysis

The following analyses were performed:

### Data Cleaning

- Duplicate record inspection
- Feature selection
- Date conversion
- Feature engineering
- Creation of cleaned dataset for Tableau

---

### Feature Engineering

Extracted from Date:

- Year
- Month
- Week
- Quarter

---

### Visualizations

- Distribution of Weekly Sales
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

## Key Insights

- Weekly sales contain several outliers.
- Store number has the strongest linear relationship with sales among the available features.
- Holiday weeks exhibit slightly higher average sales.
- Month, Week, and Quarter are highly correlated, indicating multicollinearity among time-based features.
- Economic indicators (Fuel Price, CPI, and Unemployment) show weak linear correlations with weekly sales.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- KaggleHub
- Jupyter Notebook

---

## Next Steps

- Data Preprocessing
- Feature Scaling
- Train-Test Split
- Linear Regression
- Cross Validation
- Performance Metrics
- Residual Analysis
- Feature Importance
- Model Comparison
- Tableau Dashboard
- Save Trained Model

---

## Author

**Pranav Sankpal**

Computer Science Engineering Student

Government College of Engineering, Kolhapur

LinkedIn: *(Add your LinkedIn URL)*

GitHub: *(Add your GitHub URL)*
