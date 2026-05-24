import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

@st.cache_resource
def train_model():
    df = pd.read_csv('student_dataset.csv')
    X = df[['Study_Hours', 'Attendance_Pct', 'Sleep_Hours']]
    y = df['Score']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    r2  = r2_score(y_test, model.predict(X_test))
    mae = mean_absolute_error(y_test, model.predict(X_test))
    return model, round(r2, 3), round(mae, 2)

model, r2, mae = train_model()

st.title("🎓 Student Score Predictor")

st.sidebar.header("📊 Model Info")
st.sidebar.metric("R² Score", r2)
st.sidebar.metric("MAE", mae)
st.sidebar.caption("Trained on 1500 student records using Linear Regression")

st.subheader("Enter Student Details")

study  = st.number_input("📖 Study Hours per Day  (e.g. 5.0)",  min_value=0.0, max_value=15.0, value=None, placeholder="Enter hours like 5.0")
attend = st.number_input("🏫 Attendance % (e.g. 75.0)",         min_value=0.0, max_value=100.0, value=None, placeholder="Enter percentage like 75.0")
sleep  = st.number_input("😴 Sleep Hours per Day  (e.g. 7.0)",  min_value=0.0, max_value=12.0, value=None, placeholder="Enter hours like 7.0")

if st.button("Predict Score", use_container_width=True):
    if study is None or attend is None or sleep is None:
        st.warning("⚠️ Please fill in all three fields before predicting.")
    else:
        pred = float(np.clip(model.predict([[study, attend, sleep]])[0], 0, 100))
        st.success(f"🎯 Predicted Score: **{pred:.1f} / 100**")
        if pred >= 80:
            st.info("🟢 High Performance")
        elif pred >= 55:
            st.info("🟡 Medium Performance")
        else:
            st.info("🔴 Needs Improvement")
