import streamlit as st
import joblib
import pandas as pd

# Load the saved pipeline
pipeline = joblib.load('pipeline.pkl')

# Set the title and description
st.title('🌟 Malnutrition Prediction App')
st.markdown("""
    Welcome to the Malnutrition Prediction App! Please enter the details below to predict if a child is malnourished. 
    Fill in all fields and click on **Predict**.
""")

# Organize layout with columns
col1, col2 = st.columns(2)

with col1:
    median_year = st.number_input("🗓️ MEDIAN YEAR", min_value=1900, max_value=2100, value=2022)
    sample_size = st.number_input("📏 SAMPLE SIZE (Min: 0, Max: 15)", min_value=0.0, max_value=15.0, value=0.0)
    severe_wasting = st.number_input("⚖️ SEVERE WASTING (Min: 0, Max: 5)", min_value=0.0, max_value=5.0, value=0.0)

with col2:
    wasting = st.number_input("📉 WASTING (Min: 0, Max: 5)", min_value=0.0, max_value=5.0, value=0.0)
    overweight = st.number_input("🏋️ OVERWEIGHT (Min: 0, Max: 5)", min_value=0.0, max_value=5.0, value=0.0)
    stunting = st.number_input("📏 STUNTING (Min: 0, Max: 5)", min_value=0.0, max_value=5.0, value=0.0)
    underweight = st.number_input("⚖️ UNDERWEIGHT (Min: 0, Max: 5)", min_value=0.0, max_value=5.0, value=0.0)

# Text input for country
country = st.text_input("🌍 COUNTRY").strip()

# Collecting the input data
input_data = {
    'MEDIAN YEAR': [median_year],
    'SAMPLE SIZE': [sample_size],
    'SEVERE WASTING': [severe_wasting],
    'WASTING': [wasting],
    'OVERWEIGHT': [overweight],
    'STUNTING': [stunting],
    'UNDERWEIGHT': [underweight],
    'COUNTRY': [country]
}

# Creating a DataFrame from the input data
input_df = pd.DataFrame(input_data)

# Predict button
if st.button("Predict"):
    predictions = pipeline.predict(input_df)
    result = 'Malnourished' if predictions[0] == 1 else 'Not Malnourished'
    st.markdown(f"### The prediction is: **{result}**")

# Add a footer
st.markdown("""
    ---
    *Developed by [Your Name](https://your-link.com)*
""")
