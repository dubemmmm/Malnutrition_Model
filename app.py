import streamlit as st
import joblib
import pandas as pd
pipeline = joblib.load('pipeline.pkl')
st.title('Malnutrition Prediction')
median_year = st.number_input("MEDIAN YEAR", min_value=1900, max_value=2100, value=2022)
    
sample_size = st.number_input(f'SAMPLE SIZE (Min: 0, Max: 15)', 
                                  min_value=0.0, max_value=15.0, value=0.0)
    
severe_wasting = st.number_input(f'SEVERE WASTING (Min: 0, Max: 5)', 
                                     min_value=0.0, max_value=5.0, value=0.0)
    
wasting = st.number_input(f'WASTING (Min: 0, Max: 5)', 
                              min_value=0.0, max_value=5.0, value=0.0)
    
overweight = st.number_input(f'OVERWEIGHT (Min: 0, Max: 5)', 
                                 min_value=0.0, max_value=5.0, value=0.0)
    
stunting = st.number_input(f'STUNTING (Min: 0, Max: 5)', 
                               min_value=0.0, max_value=5.0, value=0.0)
    
underweight = st.number_input(f'UNDERWEIGHT (Min: 0, Max: 5)', 
                                  min_value=0.0, max_value=5.0, value=0.0)
country = st.selectbox("COUNTRY", options=["Afghanistan", "Bangladesh", "Cambodia"])
input_data = {
        'MEDIAN YEAR': median_year,
    'SAMPLE SIZE': sample_size,
    'SEVERE WASTING': severe_wasting,
    'WASTING': wasting,
    'OVERWEIGHT': overweight,
    'STUNTING': stunting,
    'UNDERWEIGHT': underweight,
    'COUNTRY': [country]
    }
input_df = pd.DataFrame(input_data)
if st.button("Predict"):
  predictions = pipeline.predict(input_df)
  st.write(f"The prediction is: {'Malnourished' if predictions[0] == 1 else 'Not Malnourished'}")


