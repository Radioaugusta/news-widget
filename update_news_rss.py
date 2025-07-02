import feedparser
import json

# 🌍 Flux RSS BBC World
rss_url = "https://feeds.bbci.co.uk/news/world/rss.xml"

# 🛰️ Lecture du flux
print(f"⏳ Lecture du flux RSS : {rss_url}")
feed = feedparser.parse(rss_url)
print(f"🛰️ Flux BBC → {len(feed.entries)} articles détectés")

# 📰 Initialisation de la liste
titres = []

# 🔍 Extraction et logs article par article
for i, entry in enumerate(feed.entries[:10]):
    titre = entry.get("title")
    lien = entry.get("link")

    print(f"\n🔹 Article {i+1}:")
    print(f"  - title: {titre}")
    print(f"  - link: {lien}")

    if titre and lien:
        titres.append({
            "title": titre,
            "link": lien
        })
    else:
        print(f"⚠️ Article {i+1} ignoré (donnée manquante)")

# 📋 Affichage complet de la liste avant écriture
print(f"\n📚 Contenu total à écrire :")
print(json.dumps(titres, ensure_ascii=False, indent=2))

# 💾 Écriture du fichier JSON
if titres:
    try:
        with open("titres.json", "w", encoding="utf-8") as f:
            json.dump(titres, f, ensure_ascii=False, indent=2)
        print(f"\n✅ {len(titres)} titres enregistrés dans 'titres.json'")
    except Exception as e:
        print(f"❌ Erreur lors de l’écriture du fichier : {e}")
else:
    print("\n⚠️ Aucun titre récupéré. Le fichier n’a pas été modifié.")
