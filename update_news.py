import requests
import json
import os

# 🔐 Clé API depuis GitHub Secrets
API_KEY = os.getenv("API_KEY")

# 🌍 Source des actualités (tu peux mettre "us", "gb", etc. si tu veux du contenu anglophone)
URL = "https://newsapi.org/v2/top-headlines"
params = {
    "country": "fr",  # Modifie ici si tu veux changer de pays
    "pageSize": 5,
    "apiKey": API_KEY
}

# 🚀 Requête vers l'API
response = requests.get(URL, params=params)

if response.status_code != 200:
    print(f"❌ Erreur API : {response.status_code} - {response.text}")
    exit(1)

# 📰 Extraction des titres
data = response.json()
articles = data.get("articles", [])
titres = [article["title"] for article in articles if article.get("title")]

# 🔎 Log des titres
if titres:
    print(f"✅ {len(titres)} titres récupérés :")
    for titre in titres:
        print("•", titre)
    # 💾 Écriture du fichier JSON
    with open("titres.json", "w", encoding="utf-8") as f:
        json.dump(titres, f, ensure_ascii=False, indent=2)
    print("📁 Fichier 'titres.json' mis à jour avec succès.")
else:
    print("⚠️ Aucun titre trouvé. Le fichier n'a pas été modifié.")
