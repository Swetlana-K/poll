# Django Umfrageanwendung

## Einführung
In diesem Django-Projekt wird eine Umfrageanwendung erstellt, die es Benutzern ermöglicht, Umfragen anzulegen und daran teilzunehmen. Diese Anwendung wurde mithilfe des Django-Frameworks entwickelt und bietet ein Werkzeug sowohl für Umfrageersteller als auch für Wähler.

## Funktionen

1. **Umfrageerstellung:**
   - Die Erstellung und Teilnahme an Umfragen ist nicht auf authentifizierte Benutzer beschränkt.
   - Benutzer können Umfragen mit mehreren Auswahlmöglichkeiten erstellen.
   - Sie können ein oder mehrere Daten angeben und die Uhrzeit festlegen.

2. **Umfrageabstimmung:**
   - Benutzer können in aktiven Umfragen ihre Stimmen abgeben.
   - Benutzer können aus den verfügbaren Optionen auswählen und ihre Stimmen abgeben.

3. **Anzeige der Ergebnisse:**
   - Die Anwendung zeigt Echtzeit-Ergebnisse für jede Umfrage an.
   - Benutzer können die Verteilung der Stimmen anzeigen.

4. **Admin-Panel:**
   - Das integrierte Admin-Panel von Django ermöglicht es Administratoren, Umfragen, Benutzer zu verwalten und die Abstimmungsaktivität zu überwachen.

5. **Ablaufdatum für Umfragen:**
   - Admins können Umfragen manuell schließen oder archivieren.

# Kurzanleitung zur Installation des Projekts
### Schritt 1: Repository klonen
- git clone `repository-url`
- cd `repository-name`

### Schritt 2: Virtuelle Umgebung erstellen und aktivieren
- python -m venv venv
- source venv/bin/activate

### Schritt 3: Abhängigkeiten installieren
- make dev-install

### Schritt 4: .env-Datei erstellen
Erstelle eine Datei namens .env im Hauptverzeichnis des Projekts und füge die folgenden Inhalte hinzu:
- DB_USER: `Benutzer`
- DB_PWD: `Passwort`
- DB_HOST: `Host, Server`
- DB_NAME: `Datenbankname`
- DB_PORT: `Verbindungsport`
- SECRET_KEY: `Geheimschlüssel`
- DB_ENGINE: `Datenbank-Engine`

### Schritt 5: Datenbank einrichten

Stelle sicher, dass die PostgreSQL-Datenbank läuft
Erstelle die Datenbank mit den Informationen aus der .env-Datei

- psql -U postgres
- CREATE DATABASE `Datenbankname`;

### Schritt 6: Datenbankmigrationen durchführen
- make dev-migrate

### Schritt 7: Entwicklungsserver starten
- make dev-start

### Öffne deinen Webbrowser unter http://127.0.0.1:8000/.


