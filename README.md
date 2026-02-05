# KfW Förderrechner 297/298 - VOLLAUTOMATISCH 🤖

## 🚀 Was ist neu?

Die Zinssätze werden jetzt **vollautomatisch täglich aktualisiert** - Sie müssen nichts mehr manuell machen!

## 📋 Übersicht

Dieser interaktive Rechner hilft Bauherren und Investoren, ihre Förderfähigkeit für die KfW-Programme 297/298 zu prüfen und die Zinsvorteile gegenüber marktüblichen Konditionen zu berechnen.

## 🎯 Verwendung

Öffnen Sie einfach die Datei **`index.html`** in einem modernen Webbrowser (Chrome, Firefox, Edge, Safari).

**Keine Installation oder Build-Tools erforderlich!**

## ⚙️ Automatisches Zinssatz-System

Die Zinssätze werden **täglich um 6:00 Uhr** automatisch von KfW und Interhyp abgerufen und aktualisiert. 

### So funktioniert das automatische System:

1. **Täglich um 6:00 Uhr** (MEZ): GitHub Actions startet automatisch
2. **Python-Scraper** liest KfW-Website und Interhyp
3. **Bei Änderungen**: `zinssaetze.json` wird automatisch aktualisiert
4. **Ihr Rechner**: Nutzt immer die neuesten Werte

### Technologie:
- **GitHub Actions** (kostenlos, kein Server nötig)
- **Python Web Scraping** (BeautifulSoup)
- **Automatische Git-Commits** bei Änderungen

## 📦 Setup (Einmalig für automatische Updates)

### 1. GitHub Repository erstellen

```bash
# Im Ordner kfw297298:
git init
git add .
git commit -m "Initial commit - KfW Förderrechner mit Auto-Update"
```

### 2. Auf GitHub pushen

1. Gehen Sie zu https://github.com/new
2. Erstellen Sie ein neues Repository (z.B. `kfw-foerderrechner`)
3. Pushen Sie den Code:

```bash
git remote add origin https://github.com/IHR-USERNAME/kfw-foerderrechner.git
git branch -M main
git push -u origin main
```

### 3. GitHub Pages aktivieren (optional - für Web-Hosting)

1. Repository → **Settings** → **Pages**
2. Source: **Deploy from a branch**
3. Branch: **main** → Ordner: **/ (root)**
4. **Save**

✅ **Fertig!** Ab jetzt aktualisieren sich die Zinsen täglich automatisch!

## 🔧 Manuelle Zinssatz-Anpassung (Fallback)

Falls Sie die Zinsen manuell überschreiben möchten:

1. Öffnen Sie `zinssaetze.json`
2. Ändern Sie die Werte
3. Speichern

Der automatische Scraper wird Ihre Werte beim nächsten Lauf wieder überschreiben.

## 🔧 Technische Details

- **Framework**: React 18 (via CDN)
- **Styling**: Tailwind CSS
- **Deployment**: Statische HTML-Datei (GitHub Pages, Netlify, oder lokal)
- **Auto-Update**: GitHub Actions + Python Web Scraping

## 🛠️ Lokales Testen des Scrapers

```bash
# Python Dependencies installieren
pip install -r requirements.txt

# Scraper manuell ausführen
python scraper.py
```

## 📊 Überwachung der automatischen Updates

**GitHub Actions Logs ansehen:**
1. Gehen Sie zu Ihrem Repository auf GitHub
2. Klicken Sie auf **Actions**
3. Sehen Sie alle Scraper-Läufe und Logs

**Manueller Trigger:**
1. Repository → **Actions**
2. **Update KfW Zinssätze** Workflow
3. **Run workflow** → **Run workflow**

## 🛡️ Fallback-System

**Was passiert bei Scraper-Fehlern?**
- ✅ Alte Werte werden beibehalten
- ✅ Rechner hat eingebaute Fallback-Werte
- ✅ Keine Ausfallzeiten

Sie können Werte auch jederzeit manuell in `zinssaetze.json` ändern.

## 📝 Hinweis

Die berechneten Werte sind Modellrechnungen und ersetzen keine verbindliche Bankauskunft. Die finale Förderfähigkeit muss durch einen zertifizierten Energie-Effizienz-Experten bestätigt werden.

## � Vorteile des automatischen Systems

| Vorher | Nachher |
|--------|---------|
| 📝 Manuelle Updates nötig | 🤖 Vollautomatisch |
| ⏰ Wöchentliche Arbeit | ✅ Null Aufwand |
| ❌ Veraltete Daten möglich | ✨ Immer aktuell |
| 💸 Server-Kosten | 🆓 Komplett kostenlos |

## 🆘 Problembehandlung

**Problem**: Rechner zeigt "Zinssätze verwenden Fallback-Werte"
- **Lösung**: `zinssaetze.json` fehlt oder ist fehlerhaft - Scraper einmal manuell laufen lassen

**Problem**: Automatische Updates funktionieren nicht
- **Lösung**: Prüfen Sie die GitHub Actions Logs, ggf. Repository-Permissions prüfen

**Problem**: Scraper findet keine Zinssätze
- **Lösung**: KfW hat möglicherweise Website geändert - manuell in JSON eintragen

## 📅 Update-Frequenz

- **Automatisch**: Täglich um 6:00 Uhr MEZ
- **Bei Bedarf**: Manueller Trigger über GitHub Actions
- **Fallback**: Manuelle Anpassung jederzeit möglich

## 📞 Support

Bei Fragen zur Förderung:
- KfW-Infocenter: 0800 539 9002
- Energie-Effizienz-Experten: https://www.energie-effizienz-experten.de/
