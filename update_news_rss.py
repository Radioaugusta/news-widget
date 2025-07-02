import feedparser
import json

# 🌍 Flux RSS BBC World
rss_url = "https://feeds.bbci.co.uk/news/world/rss.xml"

# 🛰️ Lecture du flux
feed = feedparser.parse(rss_url)
print(f"🛰️ Flux BBC → {len(feed.entries)} articles détectés")

# 🔍 Log détaillé : structure des articles
for i, entry in enumerate(feed.entries[:5]):
    print(f"\n🔹 Article {i+1} brut :")
    for key in entry:
        try:
            print(f"{key}: {entry[key]}")
        except:
            print(f"{key}: [Valeur non affichable]")

# 📰 Extraction des titres
titres = []
for entry in feed.entries[:10]:
    if "title" in entry and "link" in entry:
        titres.append({
            "title": entry.title,
            "link": entry.link
        })

# 💾 Écriture conditionnelle
if titres:
    with open("titres.json", "w", encoding="utf-8") as f:
        json.dump(titres, f, ensure_ascii=False, indent=2)
    print(f"\n✅ {len(titres)} titres enregistrés dans 'titres.json'")
else:
    print("\n⚠️ Aucun titre récupéré. Le fichier n’a pas été modifié.")

