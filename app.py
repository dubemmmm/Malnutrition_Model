import streamlit as st
import joblib
import pandas as pd
pipeline = joblib.load('pipeline.pkl')
st.title('Malnutrition Prediction')
median_year = st.number_input(f'MEDIAN YEAR (Min: {int(min_values["MEDIAN YEAR"])}, Max: {int(max_values["MEDIAN YEAR"])})', 
                                  min_value=int(min_values['MEDIAN YEAR']), max_value=int(max_values['MEDIAN YEAR']), value=int(min_values['MEDIAN YEAR']))
    
sample_size = st.number_input(f'SAMPLE SIZE (Min: {float(min_values["SAMPLE SIZE"])}, Max: {float(max_values["SAMPLE SIZE"])})', 
                                  min_value=0.0, max_value=15.0, value=0.0)
    
severe_wasting = st.number_input(f'SEVERE WASTING (Min: {float(min_values["SEVERE WASTING"])}, Max: {float(max_values["SEVERE WASTING"])})', 
                                     min_value=0.0, max_value=5.0, value=0.0)
    
wasting = st.number_input(f'WASTING (Min: {float(min_values["WASTING"])}, Max: {float(max_values["WASTING"])})', 
                              min_value=0.0, max_value=5.0, value=0.0)
    
overweight = st.number_input(f'OVERWEIGHT (Min: {float(min_values["OVERWEIGHT"])}, Max: {float(max_values["OVERWEIGHT"])})', 
                                 min_value=0.0, max_value=5.0, value=0.0)
    
stunting = st.number_input(f'STUNTING (Min: {float(min_values["STUNTING"])}, Max: {float(max_values["STUNTING"])})', 
                               min_value=0.0, max_value=5.0, value=0.0)
    
underweight = st.number_input(f'UNDERWEIGHT (Min: {float(min_values["UNDERWEIGHT"])}, Max: {float(max_values["UNDERWEIGHT"])})', 
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


