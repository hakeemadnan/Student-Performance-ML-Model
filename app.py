import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# --- Train model on startup ---
@st.cache_resource
def train_model():
    df = pd.read_csv('student_dataset.csv')
    X = df[['Study_Hours', 'Attendance_Pct', 'Sleep_Hours']]
    y = df['Score']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

model = train_model()

# --- UI ---
st.title("🎓 Student Score Predictor")
st.write("Enter student details to predict their exam score.")

study  = st.slider("Study Hours per Day",  1.0, 10.0, 5.0, 0.5)
attend = st.slider("Attendance %",        40.0, 100.0, 75.0, 1.0)
sleep  = st.slider("Sleep Hours per Day",  4.0,  9.0,  7.0, 0.5)

if st.button("Predict Score"):
    pred = model.predict([[study, attend, sleep]])[0]
    st.success(f"Predicted Score: **{pred:.1f} / 100**")