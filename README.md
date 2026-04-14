# 🏠 Future Property Price Prediction & Investment Advisor

## 📌 Overview

This project is an end-to-end Machine Learning system designed to **predict future real estate prices (5-year horizon)** and assist users in evaluating whether a property is a **good investment**.

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

## 🗂️ Project Structure

```
├── Datasets/
│   └── Future_Price.csv
├── notebooks/
│   └── price_prediction.ipynb
├── plots/
│   ├── actual_vs_predicted/
│   └── residuals/
├── models/
├── src/
│   ├── preprocessing.py
│   ├── pipelines.py
│   └── utils.py
├── .env
├── requirements.txt
└── README.md
```

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

## 🎯 Use Case

* Property investment analysis
* Price forecasting
* Real estate decision support systems
* Integration into web apps (e.g., Streamlit / FlutterFlow)

---

## 💡 Future Improvements

* Add deep learning models
* Deploy as API (FastAPI / Flask)
* Integrate with frontend (Streamlit / Web App)
* Real-time data ingestion
* Feature importance dashboard

---

## 🤝 Contributing

Feel free to fork the repo and submit pull requests.

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Acknowledgements

* Scikit-learn
* XGBoost
* MLflow
* DagsHub

---

## 📬 Contact

For queries or collaboration:

* GitHub: your-username
* Email: [your-email@example.com](mailto:your-email@example.com)
