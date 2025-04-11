import asyncio
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Step 1: Scraping
from scraper.reddit_scraper import scrape_reddit_posts
from scraper.google_news_scraper import scrape_google_news

# Step 2: Sentiment Analysis
from analysis.sentiment_analyzer import main as run_sentiment_analysis

# Step 3: Sentiment Summary
from analysis.sentiment_summary import main as generate_summary

# Step 4: Telegram + Discord
from bot.telegram_bot import send_telegram_message
from bot.discord_bot import bot, DISCORD_BOT_TOKEN

def run_scrapers():
    print("Running Reddit scraper...")
    scrape_reddit_posts(limit_per_keyword=10)

    print("\nRunning Google News scraper...")
    scrape_google_news(pages_per_keyword=1)

async def run_all_async():
    print("\nSending signals to Telegram...")
    await send_telegram_message()

    print("\nSending signals to Discord...")
    await bot.start(DISCORD_BOT_TOKEN)

def run_all():
    run_scrapers()

    print("\nRunning FinBERT sentiment analysis...")
    run_sentiment_analysis()

    print("\nGenerating sentiment summary...")
    generate_summary()

    # Now handle async part cleanly
    asyncio.run(run_all_async())

if __name__ == "__main__":
    run_all()
