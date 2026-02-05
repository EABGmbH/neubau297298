#!/usr/bin/env python3
"""
KfW Zinssatz-Scraper
Liest automatisch die aktuellen Zinssätze von der KfW-Website und Interhyp
und aktualisiert die zinssaetze.json Datei.
"""

import requests
from bs4 import BeautifulSoup
import json
import re
from datetime import datetime
import sys

class ZinsScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
    def scrape_kfw_zinsen(self):
        """Versucht KfW-Zinssätze zu scrapen"""
        urls_to_try = [
            'https://www.kfw.de/inlandsfoerderung/Privatpersonen/Neubau/Foerderprodukte/Klimafreundlicher-Neubau-Wohngeb%C3%A4ude-(297-298)/',
            'https://www.kfw.de/inlandsfoerderung/Privatpersonen/Neubau/',
        ]
        
        for url in urls_to_try:
            try:
                print(f"Versuche KfW-Website: {url}")
                response = self.session.get(url, timeout=10, verify=True)
                
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    
                    # Suche nach Zinssätzen (verschiedene Muster)
                    text = soup.get_text()
                    
                    # Muster für Zinssätze: "2,45 %" oder "2.45%"
                    zins_pattern = r'(\d{1,2}[,\.]\d{2})\s*%'
                    matches = re.findall(zins_pattern, text)
                    
                    if matches:
                        print(f"✓ Gefundene Zinssätze auf KfW: {matches[:5]}")
                        # Konvertiere zu float
                        zinsen = [float(z.replace(',', '.')) for z in matches[:3]]
                        
                        return {
                            'eh40_kfn': min(zinsen) if zinsen else None,
                            'eh55_befristet': min(zinsen) if len(zinsen) > 1 else None
                        }
                        
            except Exception as e:
                print(f"✗ Fehler bei {url}: {e}")
                continue
                
        return None
    
    def scrape_interhyp_zinsen(self):
        """Versucht Marktzinsen von Interhyp zu scrapen"""
        try:
            url = 'https://www.interhyp.de/ratgeber/was-ist-bei-der-finanzierung-zu-beachten/zinsen/'
            print(f"Versuche Interhyp: {url}")
            
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                text = soup.get_text()
                
                # Suche nach Zinssätzen
                zins_pattern = r'(\d{1,2}[,\.]\d{2})\s*%'
                matches = re.findall(zins_pattern, text)
                
                if matches:
                    print(f"✓ Gefundene Zinssätze auf Interhyp: {matches[:5]}")
                    zinsen = [float(z.replace(',', '.')) for z in matches[:5]]
                    # Nimm einen mittleren Wert
                    return sum(zinsen) / len(zinsen) if zinsen else None
                    
        except Exception as e:
            print(f"✗ Fehler bei Interhyp: {e}")
            
        return None
    
    def load_current_zinsen(self):
        """Lädt die aktuellen Zinssätze aus der JSON"""
        try:
            with open('zinssaetze.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"✗ Fehler beim Laden der aktuellen Zinssätze: {e}")
            return None
    
    def save_zinsen(self, data):
        """Speichert die Zinssätze in die JSON"""
        try:
            with open('zinssaetze.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print("✓ Zinssätze erfolgreich gespeichert")
            return True
        except Exception as e:
            print(f"✗ Fehler beim Speichern: {e}")
            return False
    
    def run(self):
        """Hauptfunktion"""
        print("=" * 60)
        print("KfW Zinssatz-Scraper gestartet")
        print("=" * 60)
        
        # Lade aktuelle Daten
        current_data = self.load_current_zinsen()
        if not current_data:
            print("✗ Konnte aktuelle Daten nicht laden - Abbruch")
            sys.exit(1)
        
        updates = False
        
        # Versuche KfW-Zinsen zu scrapen
        kfw_zinsen = self.scrape_kfw_zinsen()
        if kfw_zinsen:
            if kfw_zinsen['eh40_kfn']:
                old_value = current_data['kfw']['eh40_kfn']
                new_value = kfw_zinsen['eh40_kfn']
                if abs(old_value - new_value) > 0.01:  # Nur bei relevanter Änderung
                    print(f"📊 EH40 Zins: {old_value}% → {new_value}%")
                    current_data['kfw']['eh40_kfn'] = new_value
                    updates = True
                else:
                    print(f"✓ EH40 Zins unverändert: {old_value}%")
            
            if kfw_zinsen['eh55_befristet']:
                old_value = current_data['kfw']['eh55_befristet']
                new_value = kfw_zinsen['eh55_befristet']
                if abs(old_value - new_value) > 0.01:
                    print(f"📊 EH55 Zins: {old_value}% → {new_value}%")
                    current_data['kfw']['eh55_befristet'] = new_value
                    updates = True
                else:
                    print(f"✓ EH55 Zins unverändert: {old_value}%")
        else:
            print("⚠ KfW-Zinsen konnten nicht gescraped werden - behalte alte Werte")
        
        # Versuche Marktzinsen zu scrapen
        markt_zins = self.scrape_interhyp_zinsen()
        if markt_zins:
            old_value = current_data['markt']['zehn_jahre_unter_90']
            if abs(old_value - markt_zins) > 0.01:
                print(f"📊 Marktzins: {old_value}% → {markt_zins}%")
                current_data['markt']['zehn_jahre_unter_90'] = markt_zins
                updates = True
            else:
                print(f"✓ Marktzins unverändert: {old_value}%")
        else:
            print("⚠ Marktzinsen konnten nicht gescraped werden - behalte alte Werte")
        
        # Aktualisiere Datum und Quelle
        current_data['stand'] = datetime.now().strftime('%Y-%m-%d')
        current_data['quelle'] = 'Automatisch aktualisiert via GitHub Actions'
        
        # Speichere nur wenn es Änderungen gab
        if updates:
            if self.save_zinsen(current_data):
                print("=" * 60)
                print("✅ Zinssätze wurden erfolgreich aktualisiert!")
                print("=" * 60)
                sys.exit(0)
            else:
                sys.exit(1)
        else:
            print("=" * 60)
            print("ℹ️  Keine Änderungen - Zinssätze sind aktuell")
            print("=" * 60)
            # Speichere trotzdem um Datum zu aktualisieren
            self.save_zinsen(current_data)
            sys.exit(0)

if __name__ == '__main__':
    scraper = ZinsScraper()
    scraper.run()
