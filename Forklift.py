import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from telegram import Bot
import schedule
import time

# Telegram Bot settings
bot_token = "6537804902:AAFNHcQnJnwZChvNupmRxWL24ok4OSM_xF4"
chat_id = "6163180261"

# Meta AI API settings
api_token = "meta-bot-token-prod-abcdefghijk"
api_endpoint = "https://api.meta.ai/bot/v2/information"

# Set up Telegram Bot
bot = Bot(token=bot_token)


# Define a function to query Meta AI API
def query_api(query):
    headers = {"Authorization": f"Bearer {api_token}"}
    params = {"query": query, "format": "json"}
    response = requests.get(api_endpoint, headers=headers, params=params)
    return response.json()


# Define a function to process API data
def process_api_data(data):
    return data["result"]


# Define a function to send Telegram notification
def send_notification(message):
    bot.send_message(chat_id=chat_id, text=message, parse_mode="Markdown")


# Define a function to run tasks
def run_tasks():
    # Query Meta AI API
    query = "forklift machines"
    api_data = query_api(query)
    processed_api_data = process_api_data(api_data)

    # Send Telegram notification
    message = "*New Data Available!* " + processed_api_data
    send_notification(message)


# Schedule tasks to run every hour
schedule.every(1).hours.do(run_tasks)

while True:
    schedule.run_pending()
    time.sleep(1)
