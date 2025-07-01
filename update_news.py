import requests
import json
import os
import random
from datetime import date

# Mots-clés aléatoires
keywords = ["politique", "économie", "culture", "technologie", "Afrique", "justice", "société", "international"]
chosen = random.choice(keywords)

# Date du jour
today = date.today().isoformat()

# Clé API NewsAPI
API_KEY = os.getenv("NEWSAPI_KEY")  # 💡 Mets ta clé API dans GitHub secrets

# Requête à NewsAPI
URL = f"https://newsapi.org/v2/everything?q={chosen}&language=fr&from={today}&pageSize=8&apiKey={API_KEY}"

# Requête HTTP
response = requests.get(URL)
data = response.json()

# Traitement des titres
headlines = []

for article in data.get("articles", []):
    item = {
        "en": article.get("title", "")[:90],  # Titre original
        "fr": article.get("title", "")[:90],  # Titre en français (même champ ici)
        "link": article.get("url", "#"),
        "date": article.get("publishedAt", "")[:10]  # ✅ Date au format AAAA-MM-JJ
    }
    headlines.append(item)

# Sauvegarde du fichier
with open("titres.json", "w", encoding="utf-8") as f:
    json.dump(headlines, f, indent=2, ensure_ascii=False)
