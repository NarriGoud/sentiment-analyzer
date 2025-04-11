import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
        # Load the CSV
    input_csv = "analysis/sentiment_results.csv"
    output_csv = "analysis/sentiment_summary.csv"
    output_chart = "analysis/sentiment_summary_chart.png"

    df = pd.read_csv(input_csv)

    # Group by source and sentiment
    summary = df.groupby(['source', 'sentiment']).size().unstack(fill_value=0).reset_index()

    # Ensure all sentiment columns exist
    for col in ["positive", "neutral", "negative"]:
        if col not in summary.columns:
            summary[col] = 0

    # Calculate total & percentage
    summary["total"] = summary[["positive", "neutral", "negative"]].sum(axis=1)
    summary["positive_percent"] = round((summary["positive"] / summary["total"].replace(0, 1)) * 100, 1)

    # Generate trading signal
    def get_signal(row):
        if row["positive_percent"] > 60:
            return "Buy"
        elif row["positive_percent"] < 40:
            return "Sell"
        else:
            return "Hold"

    summary["signal"] = summary.apply(get_signal, axis=1)

    # Save updated summary CSV
    os.makedirs("analysis", exist_ok=True)
    summary.to_csv(output_csv, index=False)

    # Plot sentiment summary
    summary.set_index("source")[["positive", "neutral", "negative"]].plot(
        kind="bar", stacked=True, figsize=(8, 5), colormap="viridis"
    )
    plt.title("Sentiment Summary by Source")
    plt.xlabel("Source")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(output_chart)
    plt.close()

    print("Summary saved to", output_csv)
    print("Chart saved to", output_chart)
