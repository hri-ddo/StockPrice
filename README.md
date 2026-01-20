
# Stock Price Prediction Pipeline 📈

This repository contains the solution for the Final Exam Machine Learning project. The project focuses on building a complete Machine Learning pipeline to predict stock prices based on historical data and competitor performance.

## 🚀 Project Overview

The goal of this project is to predict the value of **`Stock_1`** using a Random Forest Regression model. The solution covers the entire ML lifecycle, from data loading and cleaning to hyperparameter tuning and model deployment via a web interface.

### Key Features
* **Data Preprocessing:** Handling outliers, date conversion, and feature engineering (creating `Competitor_Mean`).
* **Pipeline:** Integrated `StandardScaler` and `RandomForestRegressor` into a Scikit-Learn pipeline.
* **Hyperparameter Tuning:** Optimized model performance using `GridSearchCV`.
* **Evaluation:** Achieved high accuracy with an **R² score of ~0.96**.
* **Deployment:** Interactive web interface built with **Gradio** and deployed on **Hugging Face Spaces**.

## 📊 Dataset

* **Source:** `stock_data.csv` (Provided in exam instructions).
* **Target Variable:** `Stock_1`
* **Features:** Date-derived features (Day, Month, DayOfWeek) and competitor stock prices (`Stock_2` through `Stock_5`).

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Gradio, Joblib
* **Environment:** Google Colab

## 📂 Repository Structure

```
├── stock_data.csv        # The dataset used for training
├── stock_prediction.ipynb # The Jupyter Notebook containing the full code
├── stock_model.pkl       # The trained model (saved artifact)
├── requirements.txt      # List of dependencies
└── README.md             # Project documentation
```

## 📈 Model Performance

The Random Forest Regressor was selected as the final model after extensive hyperparameter tuning. It was evaluated on a held-out test set (20% of the data), achieving state-of-the-art results for this dataset.

| Metric | Score | Description |
| :--- | :--- | :--- |
| **R² Score** | **0.9614** | The model explains **96.14%** of the variance in the stock price, indicating a very strong fit. |
| **MAE** | **1.0209** | On average, predictions deviate from the actual price by only **$1.02**. |
| **MSE** | **1.8556** | The low mean squared error confirms the model is robust with few significant outliers. |

These metrics demonstrate that the model captures the underlying market trends effectively and is highly reliable for forecasting daily stock values.

## 📝 Usage

To run this project on your local machine, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/hri-ddo/StockPrice.git
cd StockPrice
```
### 2. Install Dependencies
Ensure you have Python installed. Then, install the required libraries using pip:
```bash
pip install -r requirements.txt
```
### 3. Launch the Web App
```bash
python app.py
```
The app will launch in your browser at http://127.0.0.1:7860.
