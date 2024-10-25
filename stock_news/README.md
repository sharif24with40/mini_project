# Stock Price Alert and News Notification System

## Overview

This Python-based application monitors the stock price of a specific company (e.g., Tesla Inc.) and sends a text message with related news articles if the stock price changes significantly. The project uses the Alpha Vantage API to fetch stock data, the NewsAPI to fetch relevant news articles, and Twilio to send SMS notifications.

## Features

- **Stock Monitoring:** Fetches daily stock prices for a specified company.
- **Percentage Threshold:** Sends an alert if the stock price changes by more than a specified percentage (default: 5%).
- **News Fetching:** Retrieves the latest news articles related to the company if the threshold is met.
- **SMS Notifications:** Sends the news articles as SMS messages to a verified phone number using Twilio.

## Prerequisites

- **Python 3.x** installed on your machine.
- **Twilio account** with a verified phone number.
- **Alpha Vantage API Key** for fetching stock data.
- **NewsAPI Key** for fetching news articles.

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sharif24with40/project1.git
cd stock-news-alert
```

### 2.Install Dependencies

Install the requried Python libraries using pip:

```bash
pip install requests twilio
```

### 3.Configure the Script

Open `main.py` and replace the placeholders with your actual API keys and credentials:

- VIRTUAL_TWILIO_NUMBER: Your Twilio virtual phone number.
- VERIFIED_NUMBER: Your verified phone number.
- STOCK_NAME: The stock ticker symbol (e.g., "TSLA" for Tesla).
- COMPANY_NAME: The name of the company (e.g., "Tesla Inc").
- STOCK_API_KEY: Your Alpha Vantage API key.
- NEWS_API_KEY: Your NewsAPI key.
- TWILIO_SID: Your Twilio Account SID.
- TWILIO_AUTH_TOKEN: Your Twilio Auth Token.

### 4. Set the Threshold

The script checks the percentage change in the stock price. By default, the threshold is set to 5%. You can change this by modifying the `THRESHOLD` variable in the script.

### 5. Run the Script

Run the script using:

```bash
python main.py
```

## Logging

The script uses logging to display information and errors. You can view the logs in the console for detailed insights.

## Troubleshooting

-API Errors: Ensure that your API keys are correct and that your accounts are active.
-SMS Issues: Verify that your Twilio account is set up correctly and that you are using valid phone numbers.

## Development Status

Note: This project is currently in development. While it is functional, there may be ongoing updates and improvements. Please check back for the latest features and fixes.

## Credits

- **Alpha Vantage:** Provides the stock data API used in this project. [Alpha Vantage API](https://www.alphavantage.co/)
- **NewsAPI:** Powers the news article fetching. [NewsAPI](https://newsapi.org/)
- **Twilio:** Powers the SMS notifications. [Twilio](https://www.twilio.com/)
- **Python:** The programming language used for the development of this application. [Python](https://www.python.org/)
- **Requests:** A Python library used for making HTTP requests. [Requests Library](https://requests.readthedocs.io/)

Developed and maintained by [S. Sharif.](https://github.com/sharif24with6)
