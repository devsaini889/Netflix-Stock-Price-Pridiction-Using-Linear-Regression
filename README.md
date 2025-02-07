# 📈 Stock Price Prediction using Linear Regression  

## 🔍 Overview  
This project aims to predict **Netflix (NFLX) stock prices** using a **Linear Regression model**.  
We use historical stock data, including **Open, High, Low, Close, Adjusted Close, and Volume**, to forecast future prices.  

---

## 📂 Dataset  
- **Data Source:** Historical stock data for Netflix (NFLX)  
- **Columns:** `Date`, `Open`, `High`, `Low`, `Close`, `Adj Close`, `Volume`  
- **Target Variable:** `Close` (Stock Closing Price)  

---

## ⚙️ Features Used  
✅ **Open** — Opening price of the stock  
✅ **High** — Highest price during the day  
✅ **Low** — Lowest price during the day  
✅ **Adj Close** — Adjusted closing price (accounts for stock splits & dividends)  
✅ **Volume** — Number of shares traded  

---

## 📌 Model Used  
- ✅ **Linear Regression**  
Simple linear regression to predict closing prices based on provided features.  

---

## 📊 Model Evaluation  
Evaluation metrics to assess model performance:  
✔ **R² Score (Coefficient of Determination)**  
✔ **Mean Squared Error (MSE)**  

---

## 🏗 Installation & Setup  
### 🔹 Clone the Repository  
```bash
git clone https://github.com/yourusername/stock-price-prediction.git
cd stock-price-prediction
```
🔹 Install Dependencies
```bash
pip install -r requirements.txt
```
🔹 Run the Streamlit App
```bash
streamlit run app.py
