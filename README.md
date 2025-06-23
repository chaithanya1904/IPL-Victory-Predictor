# 🏏 IPL Victory Predictor

A Machine Learning-based web application that predicts the probable winner of an IPL (Indian Premier League) match based on team, venue, and match conditions.

## 🔗 Live Demo

👉 [IPL Victory Predictor on Render](https://ipl-victory-predictor.onrender.com)

> ⚠️ **Note:** The application may take up to **50 seconds to respond** initially due to server cold-start latency on Render's free tier.

---

## 🚀 Features

- Predicts match winners using input such as:
  - Batting and bowling team
  - Venue
  - Target score
  - Current score and overs
- Calculates:
  - Run rate
  - Required run rate
  - Balls left and wickets remaining
- Provides real-time prediction results

---

## 🧠 Machine Learning

- **Algorithms Used**:
  - Random Forest Classifier
  - Logistic Regression (for comparison)
- **Vectorization**:
  - Categorical inputs are transformed using one-hot encoding
- **Accuracy**:
  - Random Forest delivered the best accuracy on test data

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS (integrated with Flask templates)
- **Backend**: Python, Flask
- **ML Libraries**: scikit-learn, pandas, numpy
- **Deployment**: Render

---

