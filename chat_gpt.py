import requests
from openai import OpenAI

# Construct a detailed prompt for GPT
def gpt_analyze_data(symbol,hist_data_dict,insights,api_key):
    
    client = OpenAI(api_key=api_key)
    
    prompt = f"""
    Analyze the following stock market data for {symbol}:
    - Start Price: {insights['start_price']}
    - End Price: {insights['end_price']}
    - Trend: {insights['trend']}
    - Highest Price: {insights['max_price']}
    - Lowest Price: {insights['min_price']}
    
    Daily Prices: {hist_data_dict}

    Provide an expert analysis including:
    1. Interpretation of the trend.
    2. Market behavior insights.
    3. Possible reasons for fluctuations.
    4. Future predictions based on the data.
    """

    # Send request to OpenAI API
    gpt_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "You are a financial market analyst."},
                  {"role": "user", "content": prompt}]
    )

    # Print AI-generated analysis
    analysis = gpt_response.choices[0].message.content
    return ("\n💡 OpenAI Stock Analysis:\n", analysis)