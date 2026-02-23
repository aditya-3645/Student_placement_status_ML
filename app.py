import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load saved model and preprocessor
model = pickle.load(open("placement_model.pkl", "rb"))
preprocessor = pickle.load(open("preprocessor.pkl", "rb"))

st.set_page_config(page_title="Placement Prediction App")

st.title("🎓 Student Placement Prediction System")
st.write("Enter student details to predict placement status.")

# ---- INPUT FIELDS ----

gender = st.selectbox("Gender", ["Male", "Female"])
degree = st.selectbox("Degree", ["B.Tech", "B.Sc", "B.Com", "BBA"])
branch = st.selectbox("Branch", ["CSE", "IT", "ECE", "Mechanical", "Civil"])
cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0)
internships = st.number_input("Internships", min_value=0)
projects = st.number_input("Projects", min_value=0)
coding_skills = st.slider("Coding Skills (1-10)", 1, 10)
communication_skills = st.slider("Communication Skills (1-10)", 1, 10)
aptitude_score = st.number_input("Aptitude Test Score", min_value=0)
soft_skills = st.slider("Soft Skills Rating (1-10)", 1, 10)
certifications = st.number_input("Certifications", min_value=0)
backlogs = st.number_input("Backlogs", min_value=0)
age = st.number_input("Age", min_value=16, max_value=40)

# ---- PREDICTION BUTTON ----

if st.button("Predict Placement"):

    # Convert gender
    gender = 1 if gender == "Female" else 0

    # Create dataframe
    input_data = pd.DataFrame({
        "Age": [age],
        "Gender": [gender],
        "Degree": [degree],
        "Branch": [branch],
        "CGPA": [cgpa],
        "Internships": [internships],
        "Projects": [projects],
        "Coding_Skills": [coding_skills],
        "Communication_Skills": [communication_skills],
        "Aptitude_Test_Score": [aptitude_score],
        "Soft_Skills_Rating": [soft_skills],
        "Certifications": [certifications],
        "Backlogs": [backlogs]
    })

    # Preprocess
    input_encoded = preprocessor.transform(input_data)

    # Predict
    prediction = model.predict(input_encoded)[0]
    probability = model.predict_proba(input_encoded)[0][1]

    # Output
    if prediction == 1:
        st.success(f"✅ Student is Likely to be Placed")
    else:
        st.error(f"❌ Student is Likely NOT to be Placed")

    st.write(f"📊 Placement Probability: {round(probability*100,2)}%")