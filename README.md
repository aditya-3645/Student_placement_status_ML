# 🚀 PlaceSense AI – Smart Student Placement Prediction System  


## **Aditya Dhumal**  
Individual Contributor  

---

## 📌 Project Overview  

**PlaceSense AI** is a machine learning–based prediction system that analyzes student academic performance, technical skills, soft skills, and experience to determine the likelihood of placement.

This project demonstrates a **complete end-to-end Data Science workflow** including:

- Exploratory Data Analysis  
- Feature Engineering  
- Machine Learning Modeling  
- Model Evaluation  
- Streamlit Deployment  

The system helps institutions and students understand **what truly drives placement success**.

---

## 🎯 Problem Statement  

Student placement outcomes depend on multiple academic and skill-based factors.  
Institutions often lack a data-driven method to:

- Identify placement-ready students  
- Understand skill gaps  
- Improve placement success rates  

This project uses machine learning to solve this problem.

---

## 📂 Dataset Description  

The dataset contains **45,000 student records** with **15 features**.

### 🔹 Feature Groups  

#### 👤 Student Profile
- Age  
- Gender  
- Degree  
- Branch  

#### 🎓 Academic Performance
- CGPA  
- Backlogs  

#### 💼 Experience Indicators
- Internships  
- Projects  
- Certifications  

#### 🧠 Skill Ratings
- Coding Skills  
- Communication Skills  
- Soft Skills Rating  
- Aptitude Test Score  

#### 🎯 Target Variable
- `Placement_Status` → Placed / Not Placed  

---

## 🔬 Project Workflow  

### 1️⃣ Exploratory Data Analysis (EDA)
- Analyzed placement distribution  
- Studied effect of CGPA on placement  
- Evaluated importance of internships/projects  
- Observed role of communication & aptitude scores  

---

### 2️⃣ Data Preprocessing  

- Removed non-useful columns (`Student_ID`)  
- Encoded categorical variables  
- Converted target to binary classification  
- Prepared model-ready dataset  

---

### 3️⃣ Feature Engineering  

- One-Hot Encoding for Degree & Branch  
- Binary Encoding for Gender & Target  
- Combined academic, skill, and experience features  

---

### 4️⃣ Model Building  

A classification model was trained to predict student placement probability.

Baseline model used:
- Logistic Regression  

This model provides interpretability and strong baseline performance.

---

## 📊 Model Performance  

### 🔹 Accuracy
**86.64%**

### 🔹 Classification Report

| Class | Precision | Recall | F1-Score |
|------|-----------|--------|---------|
| Not Placed (0) | 0.89 | 0.90 | 0.90 |
| Placed (1) | 0.82 | 0.81 | 0.81 |

**Overall Accuracy:** 0.87  
**Macro Avg F1:** 0.85  
**Weighted Avg F1:** 0.87  

---

### 🔹 Confusion Matrix  

[ [5169 569]<br>
[ 633 2629] ]


This shows the model performs strongly in identifying both placed and non-placed students.

---

## 💡 Key Insights  

- Internships and projects significantly increase placement probability  
- Coding skills and aptitude scores are strong predictors  
- Soft skills and communication have noticeable influence  
- Academic performance alone is not sufficient for placement  

---

## 🖥️ Deployment  

The model is deployed using **Streamlit**, allowing users to:

- Enter student details  
- Get instant placement prediction  
- Understand placement readiness  

This makes the project usable in real-world academic environments.

---

## 🛠️ Tech Stack  

- Python  
- Pandas & NumPy  
- Scikit-learn  
- Matplotlib & Seaborn  
- Streamlit  

---

## 🚀 Future Improvements  

- Try advanced models (Random Forest, XGBoost)  
- Hyperparameter tuning  
- Feature importance visualization  
- Placement recommendation system  
- Cloud deployment  

---

## 🎯 Conclusion  

This project demonstrates how machine learning can be used to predict student placement outcomes and identify key success factors.

It showcases a **complete production-style data science pipeline**, making it a strong portfolio project for roles in:

- Data Science  
- Machine Learning  
- Analytics  

---

⭐ If you found this project useful, consider starring the repository!