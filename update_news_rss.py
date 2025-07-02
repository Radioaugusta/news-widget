import feedparser
import json

rss_url = "https://feeds.bbci.co.uk/news/world/rss.xml"

# 🔍 Analyse du flux RSS
feed = feedparser.parse(rss_url)
print(f"🛰️ Flux BBC → {len(feed.entries)} articles détectés")

# 📰 Extraction des titres
titres = []
for entry in feed.entries[:10]:
    print(f"📌 Titre : {entry.title}")
    titres.append({
        "title": entry.title,
        "link": entry.link
    })

# 💾 Écriture du fichier JSON
if titres:
    with open("titres.json", "w", encoding="utf-8") as f:
        json.dump(titres, f, ensure_ascii=False, indent=2)
    print(f"✅ {len(titres)} titres enregistrés dans 'titres.json'")
else:
    print("⚠️ Aucun titre récupéré. Le fichier n’a pas été modifié.")
