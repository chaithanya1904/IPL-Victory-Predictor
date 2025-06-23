# 🏏 IPL Victory Predictor

A machine learning web app that predicts the **likely winner of an IPL (Indian Premier League) match** based on match conditions and current score.

---

## 🌐 Live Demo

👉 [Click here to try the IPL Victory Predictor](https://ipl-victory-predictor.onrender.com)

> ⚠️ **Note:** The app may take up to **50 seconds to load** initially due to Render server cold-start latency (free tier).

---

## 🚀 Features

✅ Predicts IPL match outcome using:
- Batting & bowling teams  
- Venue & target score  
- Current score, overs, and wickets

✅ Computes:
- Required Run Rate  
- Current Run Rate  
- Balls remaining  
- Wickets left

✅ Real-time prediction result

---

## 🧠 Machine Learning Details

- **Algorithms Used**:
  - 🟢 Random Forest Classifier
  - 🔵 Logistic Regression (for comparison)

- **Data Processing**:
  - Converted categorical inputs into numerical vectors (One-Hot Encoding)

- **Accuracy**:
  - Achieved higher accuracy with **Random Forest** after tuning

---

## 🛠️ Tech Stack

| Layer       | Technologies Used                         |
|-------------|-------------------------------------------|
| Frontend    | HTML, CSS (Flask Templates)               |
| Backend     | Python, Flask                             |
| ML & Data   | scikit-learn, pandas, numpy               |
| Deployment  | Render                                     |

