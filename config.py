from dotenv import load_dotenv
import os

load_dotenv()

# Telegram Bot
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

# FinBERT Model
FINBERT_MODEL = "ProsusAI/finbert"

# Discord Bot
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
DISCORD_CHANNEL_ID = os.getenv('DISCORD_CHANNEL_ID')

# Reddit API
REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
REDDIT_CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
REDDIT_USER_AGENT = os.getenv('REDDIT_USER_AGENT')

KEYWORDS = [
    "RELIANCE", "HDFCBANK", "ICICIBANK", "INFY", "TCS", "SBIN", "ITC", "LT",
    "WIPRO", "ASIANPAINT", "BAJFINANCE", "AXISBANK", "SUNPHARMA", "HCLTECH",
    "NESTLEIND", "KOTAKBANK"
]

# For scraping more naturally written content from news/Reddit etc.
HUMAN_KEYWORDS = [
    "reliance", "hdfc bank", "icici bank", "infosys", "tcs", "hul", "itc",
    "kotak bank", "l&t", "larsen", "axis bank", "sbi", "bharti airtel",
    "asian paints", "bajaj finance", "hcl", "maruti", "titan", "nestle",
    "wipro", "sun pharma", "tata motors", "ultratech", "mahindra", "powergrid",
    "tech mahindra", "tata steel", "bajaj finserv", "jsw steel", "dr reddy", "cipla",
    "grasim", "ntpc", "bajaj auto", "hdfc life", "divis labs", "hindalco", "adani enterprises",
    "coal india", "sbi life", "bpcl", "eicher motors", "apollo hospitals", "hero motocorp",
    "britannia", "ongc", "tata consumer", "indusind bank", "upl", "adani ports",
    "nestle", "hdfc", "lt", "sun pharma", "titan", "tata motors", "maruti suzuki",
    "ultratech cement", "tech mahindra", "jsw", "indusind", "bajaj", "power grid", "bajaj auto",
    "nifty", "nifty50", "sensex", "sensex30", "banknifty", "bank nifty", "nifty next 50", "nifty 500", "midcap", "smallcap"
]

