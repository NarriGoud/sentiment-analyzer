import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pandas as pd
import csv
from datetime import datetime
import asyncio
from telegram import Bot
from telegram.constants import ParseMode
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

SIGNAL_CSV = "analysis/sentiment_results.csv"
TOP_N = 5

def save_sentiments_to_csv(filename, results):
    fieldnames = ['date', 'stock', 'sentiment_score', 'sentiment_label', 'source', 'snippet']
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        # Write header only if file is empty
        f.seek(0)
        if not f.read(1):
            writer.writeheader()

        for item in results:
            writer.writerow({
                'date': datetime.utcnow().date(),
                'stock': item['stock'],
                'sentiment_score': item['score'],
                'sentiment_label': item['label'],
                'source': item['source'],
                'snippet': item['text']
            })

def get_top_sentiment(df, sentiment_type, top_n):
    df = df[
        (df['sentiment'] == sentiment_type) &
        (df['confidence'] >= 0.90) &
        df['stock'].notnull()
    ]
    return df.sort_values(by='confidence', ascending=False).head(top_n)

def format_signals(df, icon):
    messages = []
    for _, row in df.iterrows():
        messages.append(
            f"{icon} *{row['stock']}* | `{row['source']}`\n"
            f"*{row['sentiment'].capitalize()}* ({round(row['confidence'], 3)})\n"
            f"_{row['headline']}_\n"
        )
    return "\n".join(messages)

async def send_telegram_message():
    try:
        df = pd.read_csv(SIGNAL_CSV)
    except FileNotFoundError:
        print("Sentiment results file not found.")
        return

    bullish_df = get_top_sentiment(df, "positive", TOP_N)
    bearish_df = get_top_sentiment(df, "negative", TOP_N)

    message_parts = []

    if not bullish_df.empty:
        message_parts.append("*Top 5 Bullish Stocks:*\n\n" + format_signals(bullish_df, "🟢"))

    if not bearish_df.empty:
        message_parts.append("*Top 5 Bearish Stocks:*\n\n" + format_signals(bearish_df, "🔴"))

    if message_parts:
        final_message = "\n\n".join(message_parts)
        bot = Bot(token=TELEGRAM_BOT_TOKEN)
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=final_message, parse_mode=ParseMode.MARKDOWN)
        print("Message sent to Telegram.")
        save_sentiments_to_csv("analysis/daily_sentiment_log.csv", bullish_df + bearish_df)
        print("Sentiment results saved to daily_sentiment_log.csv.")

    else:
        print("No high-confidence bullish or bearish signals found.")

if __name__ == "__main__":
    asyncio.run(send_telegram_message())
