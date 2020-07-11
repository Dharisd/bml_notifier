import requests
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHANNEL = os.getenv("TELEGRAM_CHANNEL")

def send_text(transaction):
    tx = transaction
    text = f"New transaction of MVR {tx[0]} from {tx[1]}"
    message = requests.get(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={TELEGRAM_CHANNEL}&text={text}")
    return message

