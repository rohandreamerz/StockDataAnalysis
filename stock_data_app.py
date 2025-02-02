from flask import Flask, request, jsonify
import yfinance as yf
import pandas as pd
import openai
from chat_gpt import gpt_analyze_data


app = Flask(__name__)

@app.route('/')
def home():
    return "Flask App is Running!"

# Company Information Endpoint
@app.route('/company_info/<symbol>', methods=['GET'])
def get_company_info(symbol):
    try:
        stock = yf.Ticker(symbol)
        info = stock.info
        company_data = {
            "name": info.get("longName"),
            "summary": info.get("longBusinessSummary"),
            "industry": info.get("industry"),
            "sector": info.get("sector"),
            "key_officers": info.get("companyOfficers", [])
        }
        return jsonify(company_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
# Stock Market Data Endpoint
@app.route('/market_data/<symbol>', methods=['GET'])
def get_market_data(symbol):
    try:
        stock = yf.Ticker(symbol)
        market_data = {
            "market_state": stock.history(period='1d').reset_index(drop=True).to_dict(),
            "current_price": stock.info.get("currentPrice"),
            "price_change": stock.info.get("regularMarketChange"),
            "percent_change": stock.info.get("regularMarketChangePercent"),
        }
        return jsonify(market_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
# Historical Market Data Endpoint
@app.route('/historical_data', methods=['POST'])
def get_historical_data():
    try:
        data = request.json
        symbol = data.get("symbol")
        start_date = data.get("start_date")
        end_date = data.get("end_date")
        
        stock = yf.Ticker(symbol)
        hist_data = stock.history(start=start_date, end=end_date)
        hist_data.reset_index(inplace=True)
        result = hist_data.to_dict(orient="records")
        
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    

    
# Analytical Insights Endpoint
@app.route('/analytical_insights', methods=['POST'])
def get_analytical_insights():
    try:
        data = request.json
        symbol = data.get("symbol")
        start_date = data.get("start_date")
        end_date = data.get("end_date")
        api_key = data.get("api_key")
        
        stock = yf.Ticker(symbol)
        hist_data = stock.history(start=start_date, end=end_date)
        
        hist_data=hist_data.reset_index()
        hist_data['Date']=hist_data['Date'].dt.strftime("%Y-%m-%d")
        hist_data_dict=hist_data.to_dict(orient='records') 
        
        trend = "upward" if hist_data["Close"].iloc[-1] > hist_data["Close"].iloc[0] else "downward"
        
        insights = {
            "start_price": hist_data["Close"].iloc[0],
            "end_price": hist_data["Close"].iloc[-1],
            "trend": trend,
            "max_price": hist_data["High"].max(),
            "min_price": hist_data["Low"].min()
        }
        
        analysis=gpt_analyze_data(symbol,hist_data_dict,insights,api_key)
        
        return jsonify(analysis)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400
        
if __name__ == '__main__':
    app.run(debug=True)