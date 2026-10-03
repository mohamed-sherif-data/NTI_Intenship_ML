import streamlit as st
import pandas as pd
import xgboost as xgb
import pickle

# Load the model
model = xgb.XGBClassifier()
model.load_model("personality_model.json")
# Load preprocessing pipeline
with open("model_scaler.pkl", "rb") as f:
    preprocess = pickle.load(f)

scaler = preprocess["scaler"]
numeric_cols = preprocess["numeric_cols"]
binary_cols = preprocess["binary_cols"]
feature_order = preprocess["feature_order"]

binary_map = {'Yes': 1, 'No': 0}

# Streamlit UI
st.title("Personality Predictor")
st.write("Fill in the details to find out if you're an Introvert or Extrovert!")

# User Inputs
user_inputs = {}

for col in feature_order:
    if col in binary_cols:
        user_inputs[col] = st.selectbox(f"{col.replace('_', ' ')}", options=["Yes", "No"])
    else:
        user_inputs[col] = st.number_input(f"{col.replace('_', ' ')}", min_value=0.0, step=1.0)

if st.button("Predict"):
    # Convert inputs to DataFrame
    df = pd.DataFrame([user_inputs], columns=feature_order)

    # Map binary columns
    for col in binary_cols:
        df[col] = df[col].map(binary_map)

    # Scale numeric columns
    df[numeric_cols] = scaler.transform(df[numeric_cols])

    # Make prediction
    prediction = model.predict(df)[0]

    if prediction == 1:
        st.success("🎉 You are an **Extrovert**!")
    else:
        st.info("😊 You are an **Introvert**!")