# 🏠 Real Estate Investment Advisor: Predicting Property Profitability & Future Value

## 📌 Overview

The project aims to reduce uncertainty in real estate decisions by combining data analysis, predictive modeling, and investment guidance into a single intelligent tool for buyers and investors.

Use Case

* ✅ Empower real estate investors with intelligent tools to assess long-term returns.
* ✅ Support buyers in choosing high-return properties in developing areas.
* ✅ Help real estate companies automate investment analysis for listings.
* ✅ Improve customer trust in real estate platforms with data-backed predictions.

---

## 🚀 Key Features

* Dashboard 📊 – Interactive dashboard with filters and visualizations to explore property trends, pricing patterns, and investment insights.
* Future Price Predictor 🔮 – Predicts future property prices using ML models with confidence intervals based on user-input features.
* Investment Advisor 🧠 – Recommends whether a property is a good investment using ensemble ML model predictions from user inputs.


---

## 📊 Dataset

The dataset contains real estate features such as:

* Location: State, City, Locality
* Property Details: BHK, Size, Floor, Total Floors
* Pricing: Price, Price per SqFt
* Amenities: Parking, Security, etc.
* Target: `Future_Price_5Y` and `Investment`

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

### For Price Prediction
### Linear Models

* Linear Regression
* Ridge Regression (with GridSearchCV)
* Lasso Regression (with GridSearchCV)

### Tree-Based Models

* Decision Tree Regressor
* Random Forest Regressor
* XGBoost Regressor

### For Investment Advisor

* Decision Tree Classifier
* Random Forest Regressor
* XGBoost Classifier
---

## 📉 Model Evaluation

### Price Predictor
Models are evaluated using:

* R² Score
* MAE (Mean Absolute Error)
* RMSE (Root Mean Squared Error)

Visualizations:

* Actual vs Predicted plots
* Residual plots

### For Investment Advisor
* Classification Report
* AUC Score

Visualization:
* AUC-ROC Curve

---

## 🧪 Experiment Tracking

Integrated with:

* **MLflow**
* **DagsHub**

Tracks:

* Datasets
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

### For Price Prediction
An ensemble approach is used:

* Multiple production models generate predictions
* Final prediction = mean of all models
* Confidence derived from:

  * Standard deviation of predictions

### For Investment Advisor
* Multiple production models generate predictions
* Final Prediction = Most common outcome of all the models

### Output:

* Predicted price
* Prediction range (uncertainty interval)
* Confidence score
* Good Investment / Not Good Investment

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
