import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from GoogleNews import GoogleNews
import os
from config import HUMAN_KEYWORDS

OUTPUT_FILE = os.path.join("scraper", "google_news.txt")

def scrape_google_news(pages_per_keyword=1, max_length=250):
    try:
        googlenews = GoogleNews(lang='en')
        posts_set = set()

        for i, keyword in enumerate(HUMAN_KEYWORDS):
            print(f"[{i+1}/{len(HUMAN_KEYWORDS)}] Searching Google News for: {keyword}")
            try:
                googlenews.clear()
                googlenews.search(keyword)

                for page in range(pages_per_keyword):
                    googlenews.get_page(page)
                    results = googlenews.results()

                    for entry in results:
                        title = entry.get("title", "").strip()
                        desc = entry.get("desc", "").strip()
                        combined = f"{title} {desc}".strip().replace("\n", " ")

                        if len(combined) < 20:
                            continue

                        trimmed = combined[:max_length]
                        formatted_post = f"{trimmed}, #{keyword.upper().replace(' ', '')}"
                        posts_set.add(formatted_post)
            except Exception as e:
                print(f"Error for keyword '{keyword}': {e}")

        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            for line in posts_set:
                f.write(line + "\n")

        print(f"Scraped {len(posts_set)} Google News articles to {OUTPUT_FILE}")

    except Exception as e:
        print(f"Google News Scraper Error] {e}")


if __name__ == "__main__":
    scrape_google_news()
