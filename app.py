pip install joblib
import pandas as pd
import joblib
import streamlit as st

# Title of the app
st.title('Enter Soil Test Results')

# Input fields for pH, Potassium, and Sodium
pH = st.number_input("Enter pH value", min_value=0.0, max_value=14.0, step=0.1)
Potassium = st.number_input("Enter Potassium value", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
Sodium = st.number_input("Enter Sodium value", min_value=0.0, max_value=100.0, value=0.0, step=0.1)


# Load the trained model
model = joblib.load('crop_suggestion_model.pkl')

def predict_crops(ph, sodium, potassium):
    # Prepare features for prediction
    X_new = pd.DataFrame({'ph': [ph], 'sodium': [sodium], 'potassium': [potassium]})
    
    # Make predictions
    predictions = model.predict(X_new)
    
    # Return the predicted crops
    return predictions
 
crops = predict_crops(pH, Sodium, Potassium)
# Display the entered values
if st.button("Submit", type="primary"):
  st.write(f"Crop: {crops[0]}")
