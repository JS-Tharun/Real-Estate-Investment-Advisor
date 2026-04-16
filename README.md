# 🏠 Real Estate Investment Advisor: Predicting Property Profitability & Future Value

## 📌 Overview

This project is designed as an end-to-end real estate decision-support platform that helps users move from exploration → prediction → decision-making:

It combines:

* Advanced feature engineering
* Multiple regression models
* Experiment tracking (MLflow + DagsHub)
* Ensemble-based confidence scoring

---

## 🚀 Key Features

* 📊 Predicts **Future Property Price (5 Years)**
* 🧠 Uses multiple ML models (Linear + Tree-based)
* ⚙️ Robust preprocessing pipelines
* 📉 Model evaluation with visual diagnostics
* 🧪 Experiment tracking using MLflow + DagsHub
* 📦 Model versioning & production readiness
* 📈 Confidence score using ensemble variance

---

## 📊 Dataset

The dataset contains real estate features such as:

* Location: State, City, Locality
* Property Details: BHK, Size, Floor, Total Floors
* Pricing: Price, Price per SqFt
* Amenities: Parking, Security, etc.
* Target: `Future_Price_5Y`

---

## 🧹 Data Preprocessing

* Invalid data filtering (e.g., Floor > Total Floors)
* Binary encoding (Yes/No → 1/0)
* Feature grouping:

  * Numerical
  * Categorical
  * Binary
  * Ordinal
  * Location-based

---

## ⚙️ Feature Engineering

* 📍 **City + Locality combination**
* 🎯 **Target Encoding (with smoothing)** for location features
* 🔄 ColumnTransformer pipelines for:

  * Scaling (StandardScaler)
  * Encoding (OneHot / Ordinal)
  * Custom transformers

---

## 🤖 Models Used

### Linear Models

* Linear Regression
* Ridge Regression (with GridSearchCV)
* Lasso Regression (with GridSearchCV)

### Tree-Based Models

* Decision Tree Regressor
* Random Forest Regressor
* XGBoost Regressor

---

## 📉 Model Evaluation

Models are evaluated using:

* R² Score
* MAE (Mean Absolute Error)
* RMSE (Root Mean Squared Error)

Visualizations:

* Actual vs Predicted plots
* Residual plots

---

## 🧪 Experiment Tracking

Integrated with:

* **MLflow**
* **DagsHub**

Tracks:

* Parameters
* Metrics
* Models
* Plots

---

## 📦 Model Lifecycle

* Model registration (MLflow)
* Versioning
* Promotion to production (Champion model)
* Model loading for inference

---

## 📈 Confidence Scoring (Advanced)

An ensemble approach is used:

* Multiple production models generate predictions
* Final prediction = mean of all models
* Confidence derived from:

  * Standard deviation of predictions

### Output:

* Predicted price
* Prediction range (uncertainty interval)
* Confidence score

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* XGBoost
* MLflow
* DagsHub
* Matplotlib / Seaborn

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/JS-Tharun/Real-Estate-Investment-Advisor.git
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set environment variables

Create a `.env` file:

```
MLFLOW_TRACKING_URI=your_uri
MLFLOW_EXPERIMENT_NAME=your_experiment
```

### 4. Run notebook

```bash
jupyter notebook
```

---

## 🤝 Contributing

Feel free to fork the repo and submit pull requests.

---

## 📬 Contact

For queries or collaboration:

* GitHub: your-username
* Email: [tharunjs06@gmail.com](mailto:tharunjs06@gmail.com)
