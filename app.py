import streamlit as st
import joblib
pipeline = joblib.load('pipeline.pkl')
def main():
  st.title('Malnutrition Prediction')
  median_year = st.number_input("MEDIAN YEAR", min_value=1900, max_value=2100, value=2022)
  sample_size = st.slider('SAMPLE SIZE', min_value=0, max_value=15, value=0)
  severe_wasting = st.slider('SEVERE WASTING', min_value=0, max_value=5, min_values['SEVERE WASTING'])
  wasting = st.slider('WASTING', min_value=0, max_value=5, min_values['WASTING'])
  overweight = st.slider('OVERWEIGHT', min_value=0, max_value=5, min_values['OVERWEIGHT'])
  stunting = st.slider('STUNTING', min_value=0, max_value=5, min_values['STUNTING'])
  underweight = st.slider('UNDERWEIGHT', min_value=0, max_value=5, min_values['UNDERWEIGHT'])
  country = st.selectbox("COUNTRY", options=["Afghanistan", "Bangladesh", "Cambodia"])
  input_data = {
        'MEDIAN YEAR': [median_year],
        'SAMPLE SIZE': [sample_size],
        'SEVERE WASTING': [severe_wasting],
        'WASTING': [wasting],
        'OVERWEIGHT': [overweight],
        'STUNTING': [stunting],
        'UNDERWEIGHT': [underweight],
        'country': [country]
    }
  input_df = pd.DataFrame(input_data)
  if st.button("Predict"):
        predictions = pipeline.predict(input_df)
        st.write(f"The prediction is: {'Malnourished' if predictions[0] == 1 else 'Not Malnourished'}")

if __name__ == "__main__":
    main()
