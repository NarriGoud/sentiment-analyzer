import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load sentiment summary
SUMMARY_PATH = os.path.join("analysis", "sentiment_summary.csv")
RESULTS_PATH = os.path.join("analysis", "sentiment_results.csv")

st.set_page_config(page_title="Stock Sentiment Dashboard", layout="centered")
st.title("Stock Sentiment Dashboard")
st.caption("Powered by FinBERT · Reddit & Google News Sentiment")

# Load data
summary = pd.read_csv(SUMMARY_PATH)
results = pd.read_csv(RESULTS_PATH)

# Summary section
st.header("Sentiment Summary by Source")

# Bar chart
fig, ax = plt.subplots(figsize=(8, 4))
summary.set_index("source")[["positive", "neutral", "negative"]].plot(
    kind="bar", stacked=True, ax=ax, colormap="viridis"
)
plt.ylabel("Number of Posts")
plt.title("Sentiment Distribution")
st.pyplot(fig)

# Signals table
st.subheader("Trading Signals")
st.dataframe(summary[["source", "positive_percent", "signal"]].set_index("source"))

# Detailed sentiment view
st.header("Detailed Sentiment Posts")
