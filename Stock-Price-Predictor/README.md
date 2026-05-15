# 📈 Stock Price Predictor

A Machine Learning-based stock price forecasting system that predicts stock closing prices using historical market data and multiple regression models.

The project uses Yahoo Finance data, performs preprocessing and feature engineering, and applies Linear Regression, Random Forest Regression, and Ensemble Learning techniques to improve prediction accuracy and robustness.

---

# 🚀 Features

- Real-time stock market data collection using Yahoo Finance
- Data preprocessing and cleaning
- Feature scaling using StandardScaler
- Linear Regression model implementation
- Random Forest Regression model
- Ensemble Learning for improved prediction accuracy
- Train/Test dataset splitting
- Stock price prediction and forecasting
- Model evaluation using MAE, RMSE, and R² Score
- Actual vs Predicted visualization
- Smoothed prediction error analysis
- Time-series plotting and trend visualization

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn
- Yahoo Finance API (`yfinance`)

---

# 📂 Project Structure

```bash
Stock-Price-Predictor/
│
├── Stock_Price_Predictor.ipynb
├── requirements.txt
└── README.md
```

---

# 📊 Workflow

```text
Stock Data Collection
        ↓
Data Preprocessing
        ↓
Feature Engineering
        ↓
Feature Scaling
        ↓
Train/Test Split
        ↓
Linear Regression Model
        ↓
Random Forest Model
        ↓
Ensemble Learning
        ↓
Prediction
        ↓
Model Evaluation
        ↓
Visualization
```

---

# 📈 Models Used

This project currently uses:

- Linear Regression
- Random Forest Regressor
- Ensemble Learning Techniques

The models predict stock closing prices using features such as:

- Open Price
- High Price
- Low Price
- Trading Volume

---

# 📉 Model Performance

- Improved Linear Regression accuracy
- Ensemble-based prediction improvement
- Mean Absolute Error (MAE) ≈ 3
- Better robustness against market fluctuations

---

# 📊 Visualizations

The project includes:

- Scatter plots
- Actual vs Predicted stock price graphs
- Smoothed prediction error graphs
- Time-series visualizations
- Regression performance analysis

---

# ▶️ How to Run

## Clone Repository

```bash
git clone https://github.com/Pranav-1719/Data-Science-Machine-Learning.git
```

## Install Required Libraries

```bash
pip install pandas numpy scipy seaborn matplotlib scikit-learn statsmodels yfinance jupyter
```

OR

```bash
pip install -r requirements.txt
```

## Run the Notebook

Open:

```bash
Stock_Price_Predictor.ipynb
```

and run all cells.

---

# 📌 Dataset Source

Stock market data is collected using:

- Yahoo Finance API (`yfinance`)

---

# 🎯 Purpose of the Project

This project was built to:

- Learn Machine Learning workflows
- Explore financial data analysis
- Understand regression and ensemble learning
- Improve stock price forecasting accuracy
- Practice data visualization and model evaluation
- Build practical machine learning projects for real-world applications

---

# 🔮 Future Improvements

- Sentiment Analysis using financial news and social media
- Deep Learning models (LSTM/GRU)
- Streamlit Web Application
- Real-time stock prediction dashboard
- Hyperparameter tuning and optimization
- Multi-stock forecasting system
