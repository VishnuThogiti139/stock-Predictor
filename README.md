# stock-Predictor

# 📊 AI-Powered Stock Market Insight App

This project is a modular **stock analysis web app** built with **Streamlit**. It uses **Gemini AI** (Google Generative AI) and **Yahoo Finance** to:

- 📈 Fetch 5+ years of historical and live stock data  
- 🧠 Predict future stock prices using Gemini AI  
- 🔁 Recommend Buy/Sell/Hold actions using AI reasoning  
- 🧭 Identify the stock’s sector and suggest peer companies  

---

## 🚀 Features

### ✅ Interactive Dashboard
- Built with **Streamlit** for a clean and responsive UI.
- User inputs a stock symbol (e.g., AAPL, TSLA) and selects the number of years (1–10) to visualize historical data.

### 📈 Stock Price Visualization
- Historical prices fetched using yfinance (Yahoo Finance).
- Interactive chart showing closing prices for the selected period.

### 🔮 AI Price Prediction
- Uses **Gemini 2.0 Flash model** to predict the next day's stock price.
- Data passed as tabular input via AI prompts.

### 🧠 AI-Driven Buy/Sell/Hold Suggestions
- Gemini evaluates 30-day price trends.
- Outputs human-like investment suggestions with reasoning.

### 👥 Peer Company Suggestions
- Gemini AI analyzes the company name and suggests 3–5 top peers in the same sector.

---
