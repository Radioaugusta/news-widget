import feedparser
import json
from datetime import datetime

# Flux RSS francophones
flux_urls = [
    "https://www.france24.com/fr/afrique/rss",
    "https://www.france24.com/fr/france/rss"
]

titres = []

for url in flux_urls:
    feed = feedparser.parse(url)
    for entry in feed.entries[:5]:  # 5 titres par flux
        titres.append({
            "title": entry.title,
            "link": entry.link
        })

# 💡 Ajout d'un timestamp pour forcer le commit
titres.insert(0, {
    "updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "title": "",
    "link": ""
})

# Sauvegarde dans titres_fr.json
with open("titres_fr.json", "w", encoding="utf-8") as f:
    json.dump(titres, f, ensure_ascii=False, indent=2)

print("✅ Fichier titres_fr.json mis à jour avec timestamp.")
