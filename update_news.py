import requests
import json
import random
from datetime import date

# Mots-clés aléatoires
keywords = ["politique", "économie", "culture", "technologie", "Afrique", "justice", "société", "international"]
chosen = random.choice(keywords)

# Date du jour
today = date.today().isoformat()

# Requête à GNews (langue française, max 8 articles)
URL = f"https://gnews.io/api/v4/search?q={chosen}&lang=fr&max=8&apikey=8f3e1d1f3c4c4e1f3c4c4e1f3c4c4e1f"  # Clé publique de test

# Requête HTTP
response = requests.get(URL)
data = response.json()

# Logs pour le workflow
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
        "date": today  # 💡 Date d'exécution du script
    }
    headlines.append(item)

# Sauvegarde du fichier JSON
with open("titres.json", "w", encoding="utf-8") as f:
    json.dump(headlines, f, indent=2, ensure_ascii=False)
