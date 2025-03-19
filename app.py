import streamlit as st
import pickle
import json
import numpy as np

# Load model
with open("banglore_home_prices_model.pickle", 'rb') as file:
    model = pickle.load(file)

# Load feature columns
with open("columns.json", 'r') as file:
    data_columns = json.load(file)["data_columns"]

# Streamlit UI
st.title("🏠 Bangalore Home Price Predictor")
st.markdown("Enter the details below to predict the home price:")

# User Inputs
total_sqft = st.number_input("Total Square Feet", min_value=100.0, max_value=10000.0, value=1000.0)
bath = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=2)
bhk = st.number_input("Number of BHK", min_value=1, max_value=10, value=3)

# Location Dropdown
location = st.selectbox("Location", data_columns[3:])

# Prediction Function
def predict_price(total_sqft, bath, bhk, location):
    input_data = np.zeros(len(data_columns))
    input_data[0] = total_sqft
    input_data[1] = bath
    input_data[2] = bhk

    if location in data_columns:
        loc_index = data_columns.index(location)
        input_data[loc_index] = 1

    prediction = model.predict([input_data])[0]
    return round(prediction, 2)

# Prediction Button
if st.button("Predict Price"):
    predicted_price = predict_price(total_sqft, bath, bhk, location)
    st.success(f"Estimated Price: ₹{predicted_price} Lakhs")
