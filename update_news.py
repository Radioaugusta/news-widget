import requests
import json
import random
import os
from datetime import date

# ✅ Clé API récupérée depuis la variable d'environnement GitHub Actions
api_key = os.environ.get("API_KEY")

if not api_key:
    raise ValueError("❌ Clé API manquante. Assurez-vous que le secret API_KEY est défini dans GitHub.")

# 🔀 Mots-clés aléatoires
keywords = ["politique", "économie", "culture", "technologie", "Afrique", "justice", "société", "international"]
chosen = random.choice(keywords)

# 📅 Date du jour
today = date.today().isoformat()

# 🔗 URL API GNews
URL = f"https://gnews.io/api/v4/search?q={chosen}&lang=fr&max=8&apikey={api_key}"

# 🔎 Requête HTTP
response = requests.get(URL)
data = response.json()

# 🧾 Logs pour GitHub Actions
print("📌 Mot-clé choisi :", chosen)
print("📰 Nombre d'articles récupérés :", len(data.get("articles", [])))

# 🧠 Traitement des titres
headlines = []

for article in data.get("articles", []):
    item = {
        "en": article.get("title", "")[:90],
        "fr": article.get("title", "")[:90],
        "link": article.get("url", "#"),
        "date": today
    }
    headlines.append(item)

# 💾 Sauvegarde dans titres.json
with open("titres.json", "w", encoding="utf-8") as f:
    json.dump(headlines, f, indent=2, ensure_ascii=False)

print("✅ Fichier titres.json mis à jour avec", len(headlines), "titres.")
