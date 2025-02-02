# 📈 Stock Market Data API with AI-Powered Analysis

This project is a **Flask-based Stock Market Data API** that fetches real-time and historical stock data using Yahoo Finance (`yfinance`) and performs **AI-driven analysis** using OpenAI's GPT models.

## 🚀 Features

- **Company Information Endpoint**: Retrieves company details like name, industry, and key officers.
- **Market Data Endpoint**: Fetches real-time market data (current price, price change, percentage change).
- **Historical Market Data Endpoint**: Provides stock price history for a specified date range.
- **AI-Powered Insights**: Uses OpenAI GPT to generate market trend analysis and predictions.

## 🛠️ Installation

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/yourusername/stock-market-api.git
cd stock-market-api
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```
Ensure you have the following dependencies:

- Flask
- yfinance
- pandas
- openai
-requests

### 3️⃣ Run the Flask App

```sh
python stock_data_app.py
```
The server will start on http://127.0.0.1:5000/.

## 🔗 API Endpoints
### 📌 1. Company Information
**URL:** /company_info/<symbol>
**Method:** GET
**Example Request:**
```sh
curl http://127.0.0.1:5000/company_info/AAPL
```
### 📌 2. Stock Market Data
**URL:** /market_data/<symbol>
**Method:** GET
**Example Request:**
```sh
curl http://127.0.0.1:5000/market_data/AAPL
```
### 📌 3. Historical Market Data
**URL:** /historical_data
**Method:** GET
**Example Request:**
```sh
curl -X POST http://127.0.0.1:5000/historical_data -H "Content-Type: application/json" -d '{
    "symbol": "AAPL",
    "start_date": "2023-01-01",
    "end_date": "2023-12-31"
}'
```
### 📌 4. AI-Powered Analytical Insights
**URL:** /analytical_insights
**Method:** GET
**Example Request:**
```sh
curl -X POST http://127.0.0.1:5000/analytical_insights -H "Content-Type: application/json" -d '{
    "symbol": "AAPL",
    "start_date": "2023-01-01",
    "end_date": "2023-12-31",
    "api_key": "your_openai_api_key"
}'
```
## 📀 How AI Analysis Works
The application sends stock data to OpenAI's **GPT-4o-mini** model for AI-powered insights.
It generates **market trend analysis, price predictions, and investment insights.**

## 🛠️ Customization
To use the **AI-powered insights**, replace `"your_openai_api_key"` in the request with your OpenAI API key.

## 🤝 Contributing
Pull requests are welcome! Feel free to fork and improve this project.

## 🐟 License
This project is licensed under the **MIT** License.

## 🚀 Happy Trading! 📊📈












