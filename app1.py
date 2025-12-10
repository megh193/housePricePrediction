import streamlit as st
import numpy as np
import joblib

model = joblib.load('model1.pkl')

st.title("House Price Prediction")

st.divider()

st.write("Enter the details of the house to predict its price:")

st.divider()

bedrooms = st.number_input("Number of Bedrooms", min_value=1, value=1)
bathrooms = st.number_input("Number of Bathrooms", min_value=0, value=1)
livingarea = st.number_input("Square Footage of Living Area", min_value=0, value=2000)
condition = st.number_input("Condition of the House", min_value=0, value=3)
noofschools = st.number_input("Number of Schools Nearby", min_value=0, value=0)

st.divider()

X = [[bedrooms, bathrooms, livingarea, condition, noofschools]]

predictbutton = st.button("Predict Price")

if predictbutton:
    st.balloons()

    X_array = np.array(X)
    prediction = model.predict(X_array)

    st.write(f"🏠 The predicted price of the house is:  {prediction[0]:,.2f}")

else:
    st.write("Please click the **Predict Price** button after entering details.")



# Command to run : streamlit run g:/housePricePrediction/app1.py