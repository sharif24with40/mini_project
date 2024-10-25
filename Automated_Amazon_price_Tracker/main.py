import os
import requests
import smtplib
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get SMTP server details and email credentials from environment variables
SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Amazon product URL
url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

# Request headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Accept-Language": "en-US"
}

# Send GET request to the product page
response = requests.get(url, headers=headers)

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(response.content, "lxml")

# Extract the product price
price = soup.find(class_="a-offscreen").get_text()
price_as_float = float(price.split("$")[1])  # Convert price to float

# Extract the product title
title = soup.find(id="productTitle").get_text().strip()

# Target price for the alert
BUY_PRICE = 100

# Send email alert if price is below target
if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!\n{url}"
    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_ADDRESS,
            to_addrs=EMAIL_ADDRESS,  # Change this if you want to send to another email
            msg=f"Subject:Amazon Price Alert!\n\n{message}".encode("utf-8")
        )
        print("Email sent successfully!")
