import feedparser
import json

rss_url = "https://feeds.bbci.co.uk/news/world/rss.xml"

feed = feedparser.parse(rss_url)
print(f"🔍 BBC → {len(feed.entries)} articles trouvés")

titres = []
for entry in feed.entries[:10]:  # Tu peux ajuster le nombre ici
    titres.append({
        "title": entry.title,
        "link": entry.link
    })

if titres:
    with open("titres.json", "w", encoding="utf-8") as f:
        json.dump(titres, f, ensure_ascii=False, indent=2)
    print(f"✅ {len(titres)} titres enregistrés dans 'titres.json'")
else:
    print("⚠️ Aucun titre récupéré. Le fichier n’a pas été modifié.")
