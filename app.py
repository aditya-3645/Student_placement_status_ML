import streamlit as st
import pickle
import numpy as np
import plotly.graph_objects as go

# ---------------- LOAD MODEL ----------------
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.set_page_config(page_title="Smart Placement Dashboard", layout="wide")

# ---------------- PREMIUM CSS ----------------
st.markdown("""
<style>
body, .main {
    background-color: #0e1117;
    color: #ffffff;
    font-family: 'Segoe UI', sans-serif;
}
h1, h2, h3, h4 {
    color: #ffffff;
}

/* Input Boxes & Sliders */
.stTextInput>div>input, .stNumberInput>div>input, .stSelectbox>div>div>div>div {
    background-color: #1a1d27;
    color: white;
    border-radius: 8px;
    border: 1px solid #333;
    padding: 5px 10px;
}
.stSlider>div>div>div>div>div>div {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg,#00c6ff,#0072ff);
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
}
.stButton>button:hover {
    background: linear-gradient(90deg,#0072ff,#00c6ff);
    transform: scale(1.05);
}

/* Divider */
hr {
    border: 1px solid #444;
}

/* Suggestions bullets */
ul {
    color: #ffd700;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<h1 style='text-align:center;'>🎓 AI Powered Placement Analytics Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#bbbbbb;'>Smart prediction system with performance insights</p>", unsafe_allow_html=True)
st.divider()

# ---------------- FORM WITH TWO COLUMN ALIGNMENT ----------------
columns = st.columns(2)

with columns[0]:
    age = st.number_input("Age", 18, 30, key="age")
with columns[1]:
    cgpa = st.number_input("CGPA", 0.0, 10.0, step=0.1, key="cgpa")

with columns[0]:
    gender = st.selectbox("Gender", ["Male", "Female"], key="gender")
with columns[1]:
    internships = st.number_input("Internships", 0, 10, key="internships")

with columns[0]:
    degree = st.selectbox("Degree", ["B.Tech", "BCA", "MCA", "B.Sc"], key="degree")
with columns[1]:
    projects = st.number_input("Projects", 0, 20, key="projects")

with columns[0]:
    branch = st.selectbox("Branch", ["CSE", "ECE", "ME", "Civil", "IT", "EEE"], key="branch")
with columns[1]:
    coding_skills = st.slider("Coding Skills", 0, 10, key="coding")

with columns[0]:
    communication = st.slider("Communication Skills", 0, 10, key="comm")
with columns[1]:
    aptitude = st.slider("Aptitude Score", 0, 100, key="apt")

with columns[0]:
    soft_skills = st.slider("Soft Skills", 0, 10, key="soft")
with columns[1]:
    certifications = st.number_input("Certifications", 0, 20, key="certs")

with columns[0]:
    backlogs = st.number_input("Backlogs", 0, 20, key="backlogs")

st.divider()

# ---------------- PREDICT ----------------
if st.button("🚀 Analyze Placement Probability"):

    input_data = np.array([[projects, cgpa, certifications, coding_skills,
                            aptitude, communication, internships, backlogs]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    st.subheader("🎯 Placement Probability Gauge")
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=probability*100,
        title={'text': "Placement Probability (%)"},
        gauge={
            'axis': {'range':[0,100]},
            'bar': {'color':'#00ff99'},
            'steps': [
                {'range':[0,40], 'color':'#ff4b4b'},
                {'range':[40,70], 'color':'#ffa500'},
                {'range':[70,100], 'color':'#00ff99'}
            ],
        }
    ))
    st.plotly_chart(fig, use_container_width=True)

    # Personalized Suggestions
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
        st.markdown("<ul>" + "".join([f"<li>{s}</li>" for s in suggestions]) + "</ul>", unsafe_allow_html=True)
    else:
        st.success("🔥 Excellent Profile! Keep it up!")

    if prediction == 1:
        st.success("✅ High Chances of Placement")
    else:
        st.error("❌ Low Placement Probability")