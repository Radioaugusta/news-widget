import requests
import json
import os
import random
from datetime import date

# Mot-clé aléatoire
keywords = ["politique", "économie", "culture", "technologie", "Afrique", "justice", "société", "international"]
chosen = random.choice(keywords)

# Date du jour
today = date.today().isoformat()

# Récupération de la clé depuis les secrets GitHub
API_KEY = os.getenv("NEWSAPI_KEY")

# Requête à NewsAPI
URL = f"https://newsapi.org/v2/everything?q={chosen}&language=fr&from={today}&pageSize=8&apiKey={API_KEY}"

# Requête HTTP
response = requests.get(URL)
data = response.json()

# Affichage dans les logs
print("Mot-clé choisi :", chosen)
print("Nombre d'articles :", len(data.get("articles", [])))
print("Réponse brute :")
print(json.dumps(data, indent=2, ensure_ascii=False))

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

# Sauvegarde du fichier JSON
with open("titres.json", "w", encoding="utf-8") as f:
    json.dump(headlines, f, indent=2, ensure_ascii=False)
