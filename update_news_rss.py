import feedparser
import json

# 🌍 Flux RSS anglophones
rss_feeds = [
    "https://feeds.bbci.co.uk/news/world/rss.xml",
    "https://feeds.skynews.com/feeds/rss/world.xml"
]

# 📥 Récupération des titres
titres = []

for url in rss_feeds:
    feed = feedparser.parse(url)
    for entry in feed.entries[:5]:  # Limite à 5 titres par source
        titres.append({
            "title": entry.title,
            "link": entry.link
        })

# 🧪 Vérification et écriture
if titres:
    with open("titres.json", "w", encoding="utf-8") as f:
        json.dump(titres, f, ensure_ascii=False, indent=2)
    print(f"✅ {len(titres)} titres enregistrés dans 'titres.json'")
else:
    print("⚠️ Aucun titre récupéré. Le fichier n'a pas été modifié.")
