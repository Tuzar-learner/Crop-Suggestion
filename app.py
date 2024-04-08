import pandas as pd
import streamlit as st

# Title of the app
st.title('Enter Soil Test Results')

# Input fields for pH, Potassium, and Sodium
pH = st.number_input("Enter pH value", min_value=0.0, max_value=14.0, step=0.1)
Potassium = st.number_input("Enter Potassium value", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
Sodium = st.number_input("Enter Sodium value", min_value=0.0, max_value=100.0, value=0.0, step=0.1)


from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv('crop_data.csv')

# Prepare features and labels
X = data[['ph', 'sodium', 'potassium']]
y = data['crop']

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train decision tree classifier
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

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
