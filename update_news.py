import requests
import json
import os

API_KEY = os.getenv("GNEWS_API_KEY")
from datetime import date

today = date.today().isoformat()
from datetime import date

today = date.today().isoformat()
API_KEY = os.getenv("GNEWS_API_KEY")
URL = f"https://gnews.io/api/v4/search?q=politique OR économie OR culture&lang=fr&from={today}&max=4&token={API_KEY}"


response = requests.get(URL)
data = response.json()

headlines = []

for article in data.get("articles", []):
    item = {
        "en": article.get("title", "")[:90],
        "fr": article.get("title", "")[:90],
        "link": article.get("url", "#")
    }
    headlines.append(item)

with open("titres.json", "w", encoding="utf-8") as f:
    json.dump(headlines, f, indent=2, ensure_ascii=False)
