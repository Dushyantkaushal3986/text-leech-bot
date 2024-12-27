import os

API_ID    = os.environ.get("22203196", "")
API_HASH  = os.environ.get("d46cc0f7be2029768555fd5933e79f3e", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
