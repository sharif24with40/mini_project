import requests
from twilio.rest import Client
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

# Twilio and API credentials (replace with your actual values)
VIRTUAL_TWILIO_NUMBER = "your virtual twilio number"
VERIFIED_NUMBER = "your own phone number verified with Twilio"

# Stock and Company info
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

# API endpoints and keys
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "YOUR OWN API KEY FROM ALPHAVANTAGE"
NEWS_API_KEY = "YOUR OWN API KEY FROM NEWSAPI"
TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"

# Threshold for triggering news (in percentage)
THRESHOLD = 5

# Fetch stock data from Alpha Vantage API
def get_stock_data():
    try:
        stock_params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": STOCK_NAME,
            "apikey": STOCK_API_KEY,
        }
        response = requests.get(STOCK_ENDPOINT, params=stock_params)
        response.raise_for_status()
        data = response.json()["Time Series (Daily)"]
        return [value for (key, value) in data.items()]
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching stock data: {e}")
        return None
    except KeyError:
        logging.error("Unexpected data format received from Alpha Vantage.")
        return None

# Fetch news related to the company from NewsAPI
def get_news():
    try:
        news_params = {
            "apiKey": NEWS_API_KEY,
            "qInTitle": COMPANY_NAME,
            "language": "en",
            "sortBy": "publishedAt",
        }
        news_response = requests.get(NEWS_ENDPOINT, params=news_params)
        news_response.raise_for_status()
        return news_response.json()["articles"][:3]
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching news data: {e}")
        return None
    except KeyError:
        logging.error("Unexpected data format received from NewsAPI.")
        return None

# Send SMS via Twilio
def send_message(formatted_articles):
    try:
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        for article in formatted_articles:
            message = client.messages.create(
                body=article,
                from_=VIRTUAL_TWILIO_NUMBER,
                to=VERIFIED_NUMBER
            )
            logging.info(f"Message sent: {message.sid}")
    except Exception as e:
        logging.error(f"Error sending message via Twilio: {e}")

def main():
    # Get stock data
    stock_data = get_stock_data()
    if not stock_data:
        return
    
    # Extract yesterday's and day-before-yesterday's closing prices
    yesterday_data = stock_data[0]
    day_before_yesterday_data = stock_data[1]
    
    try:
        yesterday_closing_price = float(yesterday_data["4. close"])
        day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])
    except (KeyError, ValueError):
        logging.error("Error processing stock data.")
        return
    
    # Calculate the price difference and direction (up or down)
    difference = yesterday_closing_price - day_before_yesterday_closing_price
    up_down = "🔺" if difference > 0 else "🔻"
    
    # Calculate percentage difference
    diff_percent = round((difference / yesterday_closing_price) * 100, 2)
    
    # If change exceeds threshold, fetch news and send messages
    if abs(diff_percent) >= THRESHOLD:
        articles = get_news()
        if not articles:
            return
        
        # Format articles for SMS
        formatted_articles = [
            f"{STOCK_NAME}: {up_down}{diff_percent}%\n"
            f"Headline: {article['title']}\n"
            f"Brief: {article['description']}\n"
            f"Published on: {article.get('publishedAt', 'N/A')} by {article.get('author', 'Unknown')}"
            for article in articles
        ]
        
        # Send formatted articles via SMS
        send_message(formatted_articles)
    else:
        logging.info(f"No significant stock change detected. Change: {diff_percent}%")

if __name__ == "__main__":
    main()
