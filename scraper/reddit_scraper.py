import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import praw
import os
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT, HUMAN_KEYWORDS

OUTPUT_FILE = os.path.join("scraper", "reddit_posts.txt")

def scrape_reddit_posts(limit_per_keyword=10, max_length=250):
    try:
        reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            user_agent=REDDIT_USER_AGENT
        )

        subreddit = reddit.subreddit("stocks+investing+IndianStockMarket")
        posts_set = set()
        seen_post_ids = set()

        for i, keyword in enumerate(HUMAN_KEYWORDS):
            print(f"{i+1}/{len(HUMAN_KEYWORDS)}] Searching Reddit for: {keyword}")
            try:
                for post in subreddit.search(keyword, sort="new", limit=limit_per_keyword):
                    if post.id in seen_post_ids:
                        continue

                    title = post.title.strip().replace("\n", " ")
                    body = (post.selftext or "").strip().replace("\n", " ")
                    combined = f"{title} {body}".strip()

                    # Basic filter for junk/empty posts
                    if len(combined) < 20:
                        continue

                    trimmed_text = combined[:max_length]
                    formatted_post = f"{trimmed_text}, #{keyword.upper().replace(' ', '')}"
                    posts_set.add(formatted_post)
                    seen_post_ids.add(post.id)

            except Exception as e:
                print(f"Error for keyword '{keyword}': {e}")

        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            for line in posts_set:
                f.write(line + "\n")

        print(f"Scraped {len(posts_set)} cleaned Reddit posts to {OUTPUT_FILE}")

    except Exception as e:
        print(f"Reddit Scraper Error] {e}")


if __name__ == "__main__":
    scrape_reddit_posts()
