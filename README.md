
# Stock Sentiment Analyzer Bot

A complete end-to-end sentiment analysis pipeline for stock market signals. This system scrapes data from Reddit and Google News, analyzes it using FinBERT, generates a trading sentiment summary, and delivers Buy/Hold/Sell alerts to Telegram & Discord.

---

## Features

- Scrape stock-related news from **Reddit** & **Google News**
- Perform **Sentiment Analysis** with `FinBERT`
- Generate **sentiment summary reports** & confidence scores
- Push signals to **Telegram** & **Discord bots**
- Visualize everything with a **Streamlit Dashboard**
- Easy to plug into a trading bot decision engine

## Project Structure

index+trading_bot/
├── analysis/
│   ├── sentiment_analyzer.py
│   ├── sentiment_results.csv
│   ├── sentiment_summary.csv
│   ├── sentiment_summary.py
│   ├── sentiment_summary_chart.png
│   └── stock_mapping.json
│
├── bot/
│   ├── discord_bot.py
│   └── telegram_bot.py
│
├── dashboard/
│   └── streamlit_dashboard.py
|
├── scraper/
│   ├── google_news_scraper.py
│   ├── reddit_scraper.py
│   ├── google_news.txt
│   └── reddit_posts.txt
│
├── config.py
├── main.py
└── requirements.txt

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/index+trading_bot.git
cd index+trading_bot
```

### 2. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 3. Configure Your API Keys in `config.py`

```python
# Reddit
REDDIT_CLIENT_ID = "your_reddit_client_id"
REDDIT_CLIENT_SECRET = "your_reddit_client_secret"
REDDIT_USER_AGENT = "your_app_name"

# Telegram
TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"
TELEGRAM_CHAT_ID = "your_telegram_chat_id"

# Discord
DISCORD_BOT_TOKEN = "your_discord_bot_token"
DISCORD_CHANNEL_ID = "your_discord_channel_id"

# Keywords
HUMAN_KEYWORDS = ["reliance", "infosys", "hdfc bank", ...]
```

## Run the Full Pipeline

```bash
python main.py
```

What happens:
1. Scrapes posts from Reddit and Google News
2. Analyzes sentiment using FinBERT
3. Generates a CSV + chart of Buy/Hold/Sell confidence
4. Sends top signals to Telegram and Discord

---

## Messaging Bots

### Telegram & Discord
After analysis, your bots will automatically send:
- Top 5 Bullish Stocks
- Top 5 Bearish Stocks
- With sentiment scores above 90% confidence

---

## Launch Streamlit Dashboard

```bash
streamlit run dashboard/streamlit_dashboard.py
```

Visualize:
- Sentiment by stock & source
- Price trends & predictions (optional)
- Individual post-level analysis

---

## Sample Output - `sentiment_results.csv`

| headline                    | stock   | sentiment | confidence | source | length |
|-----------------------------|---------|-----------|------------|--------|--------|
| Infosys beats Q4 earnings   | INFY    | positive  | 0.93       | reddit | 144    |
| HDFC Bank market reaction   | HDFCBANK| neutral   | 0.84       | google | 121    |

---

## Dependencies (in `requirements.txt`)

- `transformers`
- `torch`
- `pandas`, `numpy`
- `matplotlib`, `seaborn`
- `streamlit`
- `PRAW`, `GoogleNews`
- `discord.py`, `python-telegram-bot`
- `sklearn`, `tqdm`

---

## Future Plans

- [ ] Fine-tune FinBERT on Indian stock news
- [ ] Add Nifty/Sensex integration
- [ ] Real-time sentiment monitoring (demon mode)
- [ ] Live trading integration

---

## Author

**Chintakuntla Narendra Sai**
*AI/ML + Cybersecurity Enthusiast*  
 Parul University |  Cybersecurity Intern
 • [GitHub](https://github.com/NarriGoud)

---