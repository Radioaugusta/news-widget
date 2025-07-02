# 🧭 News Widget pour Radio Augusta

Ce dépôt contient le widget d’affichage des titres d’actualité, générés depuis un flux RSS BBC World.

## 🐍 Contenu du projet

- `titres.py` : script Python qui récupère les 10 derniers titres du flux RSS BBC et génère un fichier `titres.json`
- `titres.json` : fichier JSON contenant les titres et liens des articles
- Intégration HTML + JavaScript prévue pour afficher ces titres dans un diaporama ou une liste sur le site de Radio Augusta

## 🛠️ Utilisation

```bash
pip install feedparser
python titres.py
