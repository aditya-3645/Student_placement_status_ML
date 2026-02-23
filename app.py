import streamlit as st
import pickle
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# ---------------- LOAD MODEL ----------------
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.set_page_config(page_title="Smart Placement Dashboard", layout="wide")

# ---------------- PREMIUM CSS ----------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.main {
    background-color: #0e1117;
}
h1, h2, h3 {
    color: white;
}
.stButton>button {
    background: linear-gradient(90deg,#00c6ff,#0072ff);
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}
.stButton>button:hover {
    background: linear-gradient(90deg,#0072ff,#00c6ff);
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🎓 AI Powered Placement Analytics Dashboard")
st.write("Smart prediction system with performance insights")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("📌 Basic Info")
    age = st.number_input("Age", 18, 30)
    gender = st.selectbox("Gender", ["Male", "Female"])
    degree = st.selectbox("Degree", ["B.Tech", "BCA", "MCA", "B.Sc"])
    branch = st.selectbox("Branch", ["CSE", "ECE", "ME", "Civil", "IT", "EEE"])

with col2:
    st.subheader("📊 Skills & Academics")
    cgpa = st.number_input("CGPA", 0.0, 10.0, step=0.1)
    internships = st.number_input("Internships", 0, 10)
    projects = st.number_input("Projects", 0, 20)
    coding_skills = st.slider("Coding Skills", 0, 10)
    communication = st.slider("Communication Skills", 0, 10)
    aptitude = st.slider("Aptitude Score", 0, 100)
    soft_skills = st.slider("Soft Skills", 0, 10)
    certifications = st.number_input("Certifications", 0, 20)
    backlogs = st.number_input("Backlogs", 0, 20)

# ---------------- PREDICT ----------------
if st.button("🚀 Analyze Placement Probability"):

    input_data = np.array([[projects, cgpa, certifications, coding_skills,
                            aptitude, communication, internships, backlogs]])

    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    st.divider()

    # ---------------- GAUGE CHART ----------------
    st.subheader("🎯 Placement Probability Gauge")

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=probability * 100,
        title={'text': "Placement Probability (%)"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "#00c6ff"},
            'steps': [
                {'range': [0, 40], 'color': "#ff4b4b"},
                {'range': [40, 70], 'color': "#ffa500"},
                {'range': [70, 100], 'color': "#00ff99"},
            ],
        }
    ))

    st.plotly_chart(fig, use_container_width=True)

    # ---------------- RESULT TEXT ----------------
    if prediction == 1:
        st.success("✅ High Chances of Placement")
    else:
        st.error("❌ Low Placement Probability")

    # ---------------- PERSONALIZED FEEDBACK ----------------
    st.subheader("📈 Personalized Suggestions")

    suggestions = []

    if cgpa < 7:
        suggestions.append("Improve CGPA above 7.5.")
    if projects < 3:
        suggestions.append("Build more real-world projects.")
    if coding_skills < 6:
        suggestions.append("Practice DSA daily.")
    if internships < 1:
        suggestions.append("Get internship experience.")
    if aptitude < 60:
        suggestions.append("Improve aptitude preparation.")
    if communication < 6:
        suggestions.append("Work on interview communication.")
    if certifications < 2:
        suggestions.append("Add technical certifications.")
    if backlogs > 0:
        suggestions.append("Clear backlogs immediately.")
    if soft_skills < 6:
        suggestions.append("Improve soft skills & teamwork.")

    if suggestions:
        for s in suggestions:
            st.write("•", s)
    else:
        st.success("🔥 Excellent Profile! Keep it up.")