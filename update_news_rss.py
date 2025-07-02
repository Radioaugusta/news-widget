import feedparser
import json

# 🌍 Flux RSS Sky News uniquement
rss_url = "https://feeds.skynews.com/feeds/rss/world.xml"

# 📥 Récupération des titres
feed = feedparser.parse(rss_url)
print(f"🔍 Sky News → {len(feed.entries)} articles trouvés")

titres = []
for entry in feed.entries[:10]:  # Tu peux ajuster le nombre ici
    titres.append({
        "title": entry.title,
        "link": entry.link
    })

# 💾 Écriture du fichier JSON si des titres sont présents
if titres:
    with open("titres.json", "w", encoding="utf-8") as f:
        json.dump(titres, f, ensure_ascii=False, indent=2)
    print(f"✅ {len(titres)} titres enregistrés dans 'titres.json'")
else:
    print("⚠️ Aucun titre récupéré. Le fichier n’a pas été modifié.")
