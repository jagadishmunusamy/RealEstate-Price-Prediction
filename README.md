# 🏠 Real Estate Price Prediction (Streamlit Application)

## 📌 Project Overview

This **Real Estate Price Prediction** project is a web application built using **Streamlit**. It allows users to predict the price of real estate properties in Bangalore based on various features such as location, square footage, number of bathrooms, and number of BHKs.

## 🚀 Features

* User-friendly interface for price prediction.
* Real-time price prediction using a pre-trained machine learning model.
* Predicts prices based on:

  * Total Square Feet
  * Number of Bathrooms
  * Number of BHKs
  * Location
* Supports over 300 locations in Bangalore.

## 💡 Technologies Used

* **Frontend:** Streamlit (Python)
* **Machine Learning:** Scikit-learn (Linear Regression Model)
* **Model:** Pre-trained model (banglore\_home\_prices\_model.pickle)
* **Data:** JSON file for locations (columns.json)

## ⚡ Project Structure

* `app.py`: Main Streamlit application file.
* `banglore_home_prices_model.pickle`: Trained model for price prediction.
* `columns.json`: List of locations/features used in the model.
* `requirements.txt`: Required dependencies.

## 💡 How to Run the Project

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/Real-Estate-Price-Prediction.git
   cd Real-Estate-Price-Prediction
   ```
2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Application:**

   ```bash
   streamlit run app.py
   ```

## 📚 Usage

* Enter the total square feet, number of bathrooms, and number of BHKs.
* Select the location from the dropdown list.
* Click the **Predict Price** button.
* View the estimated price of the property in lakhs.

## ⚡ How It Works

* The application uses a pre-trained regression model to predict property prices.
* Location is one-hot encoded, and the model uses the input values to make predictions.
