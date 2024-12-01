import streamlit as st
import joblib
import numpy as np
import pandas as pd

model = joblib.load('house_price_prediction.pkl')

st.markdown("""
    <style>
        .title {
            font-size: 36px;
            color: #003366;
            font-weight: bold;
            text-align: center;
        }
        .sidebar-header {
            font-size: 20px;
            font-weight: bold;
            color: #003366;
        }
        .prediction-result {
            font-size: 24px;
            font-weight: bold;
            color: #FF6347;
        }
        .input-box {
            margin-bottom: 20px;
        }
        body {
            background-image: url('https://www.w3schools.com/w3images/forestbridge.jpg');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: white;
        }
        .sidebar .sidebar-content {
            background-color: rgba(0, 0, 0, 0.7);
        }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="title">House Price Prediction</div>', unsafe_allow_html=True)

st.sidebar.markdown('<div class="sidebar-header">Enter Property Details</div>', unsafe_allow_html=True)

def user_input_features():
    longitude = st.sidebar.number_input('Longitude', value=0.0, step=0.001, format="%.3f")
    latitude = st.sidebar.number_input('Latitude', value=0.0, step=0.001, format="%.3f")
    housing_median_age = st.sidebar.slider('Housing Median Age', min_value=0, max_value=52, value=20)
    total_rooms = st.sidebar.slider('Total Rooms', min_value=0, max_value=10000, value=500)
    total_bedrooms = st.sidebar.slider('Total Bedrooms', min_value=0, max_value=2000, value=300)
    population = st.sidebar.slider('Population', min_value=0, max_value=20000, value=1500)
    households = st.sidebar.slider('Households', min_value=0, max_value=5000, value=700)
    median_income = st.sidebar.number_input('Median Income', value=0.0, step=0.01)
    ocean_proximity = st.sidebar.selectbox('Ocean Proximity', options=['<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR OCEAN', 'NEAR BAY'])

    data = {
        'longitude': longitude,
        'latitude': latitude,
        'housing_median_age': housing_median_age,
        'total_rooms': total_rooms,
        'total_bedrooms': total_bedrooms,
        'population': population,
        'households': households,
        'median_income': median_income,
        'ocean_proximity': ocean_proximity
    }

    features = pd.DataFrame(data, index=[0])
    return features

user_input = user_input_features()

st.write("### Input Data")
st.write(user_input)

prediction = model.predict(user_input)

predicted_value = round(np.exp(prediction[0]), 2)

st.markdown(f"<div class='prediction-result'>Predicted Median House Value: ${predicted_value:,.2f}</div>", unsafe_allow_html=True)
