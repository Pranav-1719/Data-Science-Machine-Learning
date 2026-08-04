# Import
import streamlit as st

# Page
st.title("Walmart Weekly Sales Prediction")
st.header("Project Overview")
st.subheader("Predict Weekly Sales")
st.write("This application predicts Walmart weekly sales using an XGBoost model.")

# inputs
store = st.number_input("Store Number")
temperature = st.slider("Temperature",0.0,100.0,50.0)
holiday = st.selectbox("Holiday",[0,1])
