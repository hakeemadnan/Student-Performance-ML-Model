# 🎓 Student Score Predictor — ML Project

A machine learning web app that predicts student exam scores based on study habits and lifestyle factors, built with **Python**, **Scikit-learn**, and **Streamlit**.

---

## 🔗 Live Demo

👉  https://studentscorepredicto.streamlit.app/

---

## 📌 Project Overview

This project aims to predict a student's exam score using three simple but powerful factors:

- 📖 **Study Hours per Day**
- 🏫 **Attendance Percentage**
- 😴 **Sleep Hours per Day**

The goal is to help identify students who may need academic support before exams.

---

## 📁 Project Structure

```
📦 student-score-predictor/
├── app.py                  # Streamlit web app
├── student_dataset.csv     # Dataset (1500 student records)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 📊 Dataset

- **Source:** Synthetically generated using NumPy
- **Size:** 1500 rows × 4 columns
- **Target Variable:** `Score` (0–100)

| Feature | Description | Range |
|---|---|---|
| `Study_Hours` | Hours studied per day | 1 – 11 |
| `Attendance_Pct` | Class attendance percentage | 0 – 100% |
| `Sleep_Hours` | Hours of sleep per day | 2 – 10 |
| `Score` | Exam score *(target)* | 20 – 100 |

---

## 🤖 Model

| Detail | Value |
|---|---|
| Algorithm | Linear Regression |
| Train/Test Split | 80% / 20% |
| R² Score | **0.957** |
| MAE | **2.33** |

**R² = 0.957** means the model explains 95.7% of the variation in student scores.  
**MAE = 2.33** means predictions are off by only ~2.3 marks on average.

---

## 🚀 Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/yourusername/student-score-predictor.git
cd student-score-predictor
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Pandas** — data handling
- **NumPy** — numerical operations
- **Scikit-learn** — ML model
- **Streamlit** — web app deployment
- **Matplotlib / Seaborn** — data visualization (notebook)

---

## 📈 Key Insights

- Study hours is the **strongest predictor** of exam score
- Students with attendance above **75%** consistently score higher
- Adequate sleep (7–8 hrs) positively impacts performance
- Students scoring below **55** are flagged as needing academic support

---

## 👨‍💻 Author

Made by **Adnan Mushtaq**  
