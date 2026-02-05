# 🚀 KfW Förderrechner - Quick Setup

## Schritt 1: Git Repository initialisieren

Öffnen Sie PowerShell/Terminal in diesem Ordner und führen Sie aus:

```bash
git init
git add .
git commit -m "🎉 Initial commit - KfW Förderrechner mit Auto-Update"
```

## Schritt 2: GitHub Repository erstellen

1. Gehen Sie zu: https://github.com/new
2. Repository Name: `kfw-foerderrechner` (oder einen anderen Namen)
3. **Wichtig**: Repository sollte **Public** sein (für GitHub Actions kostenlos)
4. Klicken Sie auf **Create repository**

## Schritt 3: Code auf GitHub pushen

Kopieren Sie die Befehle von GitHub (werden nach dem Erstellen angezeigt):

```bash
git remote add origin https://github.com/IHR-USERNAME/kfw-foerderrechner.git
git branch -M main
git push -u origin main
```

## Schritt 4: Fertig! 🎉

Die automatischen Updates starten ab jetzt:
- ✅ Täglich um 6:00 Uhr
- ✅ Oder manuell über GitHub Actions

## Optional: GitHub Pages aktivieren (Kostenlose Website)

1. Gehen Sie zu Ihrem Repository auf GitHub
2. **Settings** → **Pages**
3. **Source**: Branch `main` → Ordner `/` (root)
4. **Save**

Nach 1-2 Minuten ist Ihre Website live unter:
```
https://IHR-USERNAME.github.io/kfw-foerderrechner/
```

## Erste Schritte nach dem Setup

### Scraper manuell testen:
```bash
pip install -r requirements.txt
python scraper.py
```

### Lokalen Webserver starten (optional):
```bash
# Python 3
python -m http.server 8000

# Dann öffnen: http://localhost:8000
```

## GitHub Actions prüfen

1. Gehen Sie zu Ihrem Repository
2. Klicken Sie auf **Actions** (oben)
3. Sie sehen den Workflow **"Update KfW Zinssätze"**
4. Klicken Sie auf **Run workflow** um ihn sofort zu testen

## Troubleshooting

**"Permission denied" beim Push:**
```bash
# Authentifizierung mit GitHub CLI
gh auth login

# Oder verwenden Sie ein Personal Access Token
```

**Actions laufen nicht:**
- Repository muss **Public** sein ODER
- Sie benötigen GitHub Pro für private Repos mit Actions

**Scraper findet keine Zinsen:**
- Das ist normal am Anfang
- Die aktuellen Werte in `zinssaetze.json` bleiben erhalten
- Scraper verbessert sich mit der Zeit

## Nächste Schritte

1. ✅ Repository auf GitHub erstellen
2. ✅ Code pushen
3. ✅ Ersten Workflow-Run triggern
4. 🎉 Entspannen - alles läuft automatisch!

---

**Fragen?** Prüfen Sie die vollständige [README.md](README.md) für Details.
