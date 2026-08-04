# Import
import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("model/XGBoost_model.pkl")

# Header
with st.container(border=True):
    st.title("**🛒 Walmart Weekly Sales Prediction**")

st.subheader("Prediction Dashboard")
st.caption("Estimate Walmart's weekly sales using historical store, seasonal, and economic data.")

# Sidebar
with st.sidebar:
    st.title("⚙️ Input Parameters")
    st.caption("Enter the required information below.")
    st.divider()

    store = st.number_input("Store Number")
    temperature = st.slider("Temperature", 0.0, 100.0, 50.0)
    holiday = st.selectbox("Holiday", [0, 1])
    week = st.slider("Week", 1, 52, 1)
    year = st.selectbox("Year", [2010, 2011, 2012])
    fuel_price = st.number_input("Fuel Price")
    cpi = st.number_input("Consumer Price Index (CPI)", value=220)
    unemployment = st.number_input("Unemployment Rate", value=7)

    st.divider()
    predict = st.button("🔮 Predict Weekly Sales")

# Input Dataframe
input_data = pd.DataFrame({
    "Year": [year],
    "Week": [week],
    "Store": [store],
    "Holiday_Flag": [holiday],
    "Temperature": [temperature],
    "Fuel_Price": [fuel_price],
    "CPI": [cpi],
    "Unemployment": [unemployment]
})

#page
with st.container(border=True):

    st.subheader("Model Information")

    st.markdown("""
    - **Algorithm:** XGBoost Regressor
    - **Hyperparameter Tuning:** RandomizedSearchCV
    - **Cross Validation:** 5-Fold
    - **Evaluation Metric:** R²
    """)

# Model Performance
st.subheader("Model Performance")
c1,c2,c3 = st.columns(3)
c1.metric("R² Score","0.9781")
c2.metric("MAE","50,799")
c3.metric("RMSE","84,008")

# Input summary
with st.expander("📋 Input Summary"):
    st.dataframe(input_data,use_container_width=True)

# Predict
if predict:
    prediction = model.predict(input_data)
    st.success("Prediction Successful!")
    with st.container(border=True):
        st.metric(label="Predicted Weekly Sales: ",value=f"{prediction[0]:,.2f}")