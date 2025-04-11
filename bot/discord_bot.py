import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
import asyncio
from discord import Intents
from discord.ext import commands
from config import DISCORD_BOT_TOKEN, DISCORD_CHANNEL_ID

# Config
SIGNAL_CSV = "analysis/sentiment_results.csv"
TOP_N = 5

intents = Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

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
            f"{icon} **{row['stock']}** | `{row['source']}`\n"
            f"**{row['sentiment'].capitalize()}** ({round(row['confidence'], 3)})\n"
            f"*{row['headline']}*\n"
        )
    return "\n".join(messages)

@bot.event
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    df = pd.read_csv(SIGNAL_CSV)
    bullish_df = get_top_sentiment(df, "positive", TOP_N)
    bearish_df = get_top_sentiment(df, "negative", TOP_N)

    channel = bot.get_channel(int(DISCORD_CHANNEL_ID))
    if not channel:
        print("Channel not found.")
        await bot.close()
        return

    # Send Bullish Message
    if not bullish_df.empty:
        bullish_message = "**🟢 Top 5 Bullish Stocks:**\n\n" + format_signals(bullish_df, "🟢")
        if len(bullish_message) > 2000:
            await channel.send(bullish_message[:2000])  # Truncate if needed
        else:
            await channel.send(bullish_message)

    # Send Bearish Message
    if not bearish_df.empty:
        bearish_message = "**🔴 Top 5 Bearish Stocks:**\n\n" + format_signals(bearish_df, "🔴")
        if len(bearish_message) > 2000:
            await channel.send(bearish_message[:2000])  # Truncate if needed
        else:
            await channel.send(bearish_message)

    print("Messages sent to Discord.")
    await bot.close()

if __name__ == "__main__":
    asyncio.run(bot.start(DISCORD_BOT_TOKEN))
