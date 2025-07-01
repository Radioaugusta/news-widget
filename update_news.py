import requests
import json
import os

# 1. Clé API récupérée depuis les variables d'environnement (via GitHub Secrets)
API_KEY = os.getenv("API_KEY")

# 2. URL de l'API (exemple avec NewsAPI.org)
URL = "https://newsapi.org/v2/top-headlines"
params = {
    "country": "fr",
    "pageSize": 5,
    "apiKey": API_KEY
}

# 3. Requête HTTP
response = requests.get(URL, params=params)

if response.status_code != 200:
    print(f"❌ Erreur API : {response.status_code} - {response.text}")
    exit(1)

# 4. Extraction des titres
data = response.json()
articles = data.get("articles", [])
titres = [article["title"] for article in articles if "title" in article]

print(f"✅ {len(titres)} titres récupérés :")
for titre in titres:
    print("•", titre)

# 5. Écriture dans titres.json
with open("titres.json", "w", encoding="utf-8") as f:
    json.dump(titres, f, ensure_ascii=False, indent=2)

print("💾 Fichier 'titres.json' mis à jour avec succès.")
