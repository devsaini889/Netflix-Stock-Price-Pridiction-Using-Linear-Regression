import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit UI
st.title("📈 Netflix Stock Price Prediction")

# Sidebar for user input
st.sidebar.header("Enter Stock Details")

open_price = st.sidebar.number_input("Open Price ($)", min_value=0.0, format="%.2f")
high_price = st.sidebar.number_input("High Price ($)", min_value=0.0, format="%.2f")
low_price = st.sidebar.number_input("Low Price ($)", min_value=0.0, format="%.2f")
volume = st.sidebar.number_input("Volume", min_value=0, step=1000)
adj_close = st.sidebar.number_input("Adj Close Price ($)", min_value=0.0, format="%.2f")  # ADD THIS FEATURE

# Prediction
if st.sidebar.button("Predict"):
    input_data = np.array([[open_price, high_price, low_price, volume, adj_close]])  # ADDING THE MISSING FEATURE
    prediction = model.predict(input_data)
    st.success(f"Predicted Closing Price: **${prediction[0]:.2f}**")

# Dataset Display
st.subheader("📊 Netflix Stock Dataset Sample")
df = pd.read_csv("Netflix_Stock_Price.csv")
st.dataframe(df.head(10))
