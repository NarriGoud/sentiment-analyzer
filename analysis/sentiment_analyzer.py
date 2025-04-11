from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from torch.nn.functional import softmax
import pandas as pd
import os

# Load FinBERT
tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")

# Input Files
REDDIT_FILE = os.path.join("scraper", "reddit_posts.txt")
GOOGLE_FILE = os.path.join("scraper", "google_news.txt")

# Output CSV
OUTPUT_CSV = os.path.join("analysis", "sentiment_results.csv")

def load_data(file_path, source_name):
    data = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if "," not in line:
                continue
            try:
                text, tag = line.rsplit(",", 1)
                stock = tag.strip().replace("#", "")
                cleaned_text = text.strip()
                if len(cleaned_text) < 20:
                    continue
                data.append({
                    "text": cleaned_text,
                    "stock": stock,
                    "source": source_name,
                    "length": len(cleaned_text)
                })
            except Exception as e:
                print(f"Skipping line due to parse error: {line.strip()} | Error: {e}")
    return data

def analyze_sentiment(text):
    try:
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=256)
        with torch.no_grad():
            logits = model(**inputs).logits
            probs = softmax(logits, dim=1)
            sentiment_id = torch.argmax(probs).item()
            sentiment = ["negative", "neutral", "positive"][sentiment_id]
            confidence = round(probs[0][sentiment_id].item(), 3)
        return sentiment, confidence
    except Exception as e:
        print(f"Error analyzing text: {e}")
        return "unknown", 0.0

def main():
    all_data = []
    all_data += load_data(REDDIT_FILE, source_name="reddit")
    all_data += load_data(GOOGLE_FILE, source_name="google")

    print(f"Loaded {len(all_data)} posts for sentiment analysis.")

    results = []
    for i, item in enumerate(all_data):
        sentiment, confidence = analyze_sentiment(item["text"])
        results.append({
            "headline": item["text"],
            "stock": item["stock"],
            "sentiment": sentiment,
            "confidence": confidence,
            "source": item["source"],
            "length": item["length"]
        })

        if (i + 1) % 50 == 0:
            print(f"Analyzed {i+1}/{len(all_data)} posts...")

    df = pd.DataFrame(results)
    os.makedirs("analysis", exist_ok=True)
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"Saved sentiment results to {OUTPUT_CSV}")

if __name__ == "__main__":
    main()
