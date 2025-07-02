import feedparser
import json

# 🌍 Flux RSS BBC World
rss_url = "https://feeds.bbci.co.uk/news/world/rss.xml"

# 🛰️ Lecture du flux
feed = feedparser.parse(rss_url)
print(f"🛰️ Flux BBC → {len(feed.entries)} articles détectés")

# 📰 Extraction des 10 premiers titres
titres = []
for i, entry in enumerate(feed.entries[:10]):
    titre = entry.get("title")
    lien = entry.get("link")
    print(f"📌 {i+1}. {titre} → {lien}")

    # Vérifie que titre et lien existent
    if titre and lien:
        titres.append({
            "title": titre,
            "link": lien
        })

# 💾 Sauvegarde dans titres.json
if titres:
    with open("titres.json", "w", encoding="utf-8") as f:
        json.dump(titres, f, ensure_ascii=False, indent=2)
    print(f"\n✅ {len(titres)} titres enregistrés dans 'titres.json'")
else:
    print("\n⚠️ Aucun titre récupéré. Le fichier n’a pas été modifié.")
