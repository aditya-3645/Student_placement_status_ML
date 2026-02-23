# 📊 Student’s Placement Record Analysis

## 📌 Project Overview
The **Student’s Placement Record Analysis** project is a Data Science–based exploratory study aimed at identifying the key factors that influence campus placement outcomes. By analyzing academic, technical, and skill-based attributes of students, the project provides actionable insights into what truly matters for securing placements.

Through detailed exploratory data analysis, the project seeks to uncover hidden patterns, trends, and relationships within the dataset that differentiate placed students from non-placed students. By quantifying the relative importance of each feature, the study helps in understanding which aspects of a student’s profile contribute most strongly to employability.

Ultimately, the objective is to provide meaningful, actionable insights that can guide students in prioritizing skill development and academic improvement throughout their educational journey. In addition, the project aims to support educational institutions and training programs by offering data-backed evidence that can be used to design more effective placement preparation strategies and career guidance initiatives.

---

## 🎯 Objective
- To analyze how factors such as **CGPA, internships, projects, coding skills, aptitude, communication skills, certifications, and backlogs** impact placement outcomes.
- To help students understand and prioritize the most important areas for improving employability.

---

## 🧠 Hypothesis
A student’s **academic performance, technical skills, internships, aptitude test performance, and soft skills** significantly influence their campus placement status.

---

## 📂 Dataset Description
- **Total Records:** ~4500 students  
- **Target Variable:** `Placement_Status` (Placed / Not Placed)
- **No missing values or duplicate records**, ensuring high data quality.

### Key Features:
- **Academic:** CGPA, Backlogs  
- **Technical:** Coding Skills, Projects, Internships  
- **Skill-Based:** Communication Skills, Aptitude Test Score, Soft Skills Rating  
- **Profile-Based:** Gender, Degree, Branch  
- **Additional:** Certifications  

---

## 🔍 Exploratory Data Analysis (EDA)
EDA was performed using **Matplotlib, Seaborn, and Plotly** to visualize patterns and relationships.

### 🔑 Major Insights:
- Students with **CGPA above 7.5** have a higher placement probability.
- **More than one internship** significantly boosts placement chances.
- Students with **4 or more projects** are more likely to get placed.
- **Coding skills above 6/10** are critical for placement.
- **Communication skills above 5/10** positively impact outcomes.
- **Aptitude scores above 80%** strongly correlate with placements.
- **Soft skills rating** shows minimal impact on placement.
- At least **2 certifications** improve employability.
- Students with **zero backlogs** are far more likely to be placed.
- Civil Engineering students show comparatively **lower placement rates**.
- The dataset shows **class imbalance** between placed and non-placed students.

---

## ⚙️ Data Preprocessing
- Removed irrelevant column: `Student_ID`
- Encoded categorical variables:
  - Gender and Placement Status using label encoding
  - Degree and Branch using one-hot encoding
- Prepared a clean and structured dataset ready for machine learning models.

---

## 📊 Model Performance Summary

We trained a **Logistic Regression** model for a **binary classification** problem.  
The dataset has a **mild class imbalance** (approximately **63% vs 34%**), so no resampling techniques were applied. Instead, appropriate evaluation metrics were used to assess model performance.

---

## 🔹 Evaluation Metrics

The model was evaluated on the test dataset using **Precision, Recall, F1-Score, and Accuracy**.

| Class | Precision | Recall | F1-Score | Support |
|------|-----------|--------|----------|---------|
| 0 | 0.88 | 0.88 | 0.88 | 5738 |
| 1 | 0.79 | 0.79 | 0.79 | 3262 |

- **Overall Accuracy:** 85%  
- **Macro Average F1-Score:** 0.84  
- **Weighted Average F1-Score:** 0.85  

---

## 🔹 Interpretation

- The model performs **consistently well across both classes**
- The **minority class (1)** is handled effectively with a recall of **79%**
- No significant bias toward the majority class is observed
- Balanced precision and recall indicate a **stable and reliable classifier**

---

## 🔹 Conclusion

The Logistic Regression model demonstrates **strong baseline performance** without requiring data balancing techniques.  
With a clean preprocessing pipeline and balanced evaluation metrics, the model is well-suited for further optimization and comparison with more advanced models.

---

## 🚀 Future Scope
- Implement machine learning models for placement prediction
- Address class imbalance using SMOTE
- Perform feature importance analysis
- Build a placement prediction dashboard
- Deploy the model as a student career guidance tool

---

## 👤 Contributor
**Aditya Dhumal**


# Placement Prediction Insights – Logistic Regression Suitability

## 1️⃣ Strong Positive Predictors (Feature ↑ → Placement ↑)

| Feature | Correlation | Interpretation |
|---------|------------|----------------|
| Projects | 0.50 | More projects strongly increase placement chances |
| CGPA | 0.49 | Higher CGPA positively influences placement |
| Certifications | 0.47 | More certifications → higher chance |
| Coding_Skills | 0.44 | Better coding skills → higher chance |
| Aptitude_Test_Score | 0.39 | Higher aptitude → better placement odds |
| Communication_Skills | 0.33 | Good communication helps placement |
| Internships | 0.31 | More internships → better placement probability |

✅ **These features are strong linear predictors, ideal for Logistic Regression.**

---

## 2️⃣ Strong Negative Predictor (Feature ↑ → Placement ↓)

| Feature | Correlation | Interpretation |
|---------|------------|----------------|
| Backlogs | -0.49 | More backlogs reduce placement probability |

✅ **Logistic Regression can naturally capture this negative effect.**

---

## 3️⃣ Weak or Negligible Correlation Features

| Feature | Correlation | Notes |
|---------|------------|-------|
| Branch_Civil | -0.08 | Very weak linear effect |
| Branch_ME | -0.04 | Very weak linear effect |
| Branch_ECE | -0.001 | Negligible effect |
| Branch_IT | 0.06 | Very weak effect |
| Branch_CSE | 0.06 | Very weak effect |
| Degree_B.Tech | -0.005 | Negligible effect |
| Degree_BCA | -0.003 | Negligible effect |
| Degree_B.Sc | 0.003 | Negligible effect |
| Degree_MCA | 0.006 | Negligible effect |
| Gender | -0.002 | No effect |
| Age | 0.003 | No effect |
| Soft_Skills_Rating | -0.003 | No effect |

⚠️ **These features have very weak linear correlation with Placement_Status.**  
May not improve Logistic Regression performance unless used with **interactions or transformations**.

---

## 4️⃣ Insights About Logistic Regression

- Logistic Regression is **suitable for this dataset**.  
- Models the **log-odds of Placement_Status** as a linear combination of features.  
- **Strongly correlated features** will drive predictions.  
- **Weakly correlated features** can be dropped to simplify the model.  
- LR provides **probabilities**, allowing ranking of students by placement chance.

---

## 5️⃣ Recommended Features for Logistic Regression

```text
Projects, CGPA, Certifications, Coding_Skills, Aptitude_Test_Score,
Communication_Skills, Internships, Backlogs
