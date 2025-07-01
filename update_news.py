import requests
import json
import os
import random
from datetime import date

# Mot-clé aléatoire pour varier chaque jour
keywords = ["politique", "économie", "culture", "technologie", "Afrique", "élections", "justice", "société"]
chosen = random.choice(keywords)

# Date du jour
today = date.today().isoformat()

# Clé API
API_KEY = os.getenv("GNEWS_API_KEY")

# Requête à l'API GNews
URL = f"https://gnews.io/api/v4/search?q={chosen}&lang=fr&from={today}&max=4&token={API_KEY}"

# Requête HTTP
response = requests.get(URL)
data = response.json()

# Traitement des titres
headlines = []

for article in data.get("articles", []):
    item = {
        "en": article.get("title", "")[:90],
        "fr": article.get("title", "")[:90],
        "link": article.get("url", "#"),
        "date": article.get("publishedAt", "")[:10]
    }
    headlines.append(item)

# Sauvegarde dans le fichier JSON
with open("titres.json", "w", encoding="utf-8") as f:
    json.dump(headlines, f, indent=2, ensure_ascii=False)
