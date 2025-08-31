# GV100AD - Gemeindeverzeichnis

## Was ist GV100AD?

**GV100AD** ist ein Dateiformat des **Statistischen Bundesamtes (Destatis)** für das amtliche Gemeindeverzeichnis von Deutschland.

### Bedeutung der Bezeichnung:
- **GV** = **Gemeindeverzeichnis**
- **100** = Produktnummer/Kennziffer
- **AD** = **ASCII-Datei** (Textformat)

## Inhalt

Das Gemeindeverzeichnis enthält alle deutschen Gemeinden mit:
- **Amtlicher Regionalschlüssel (ARS)** - 8-stellige eindeutige Kennung
- **Gemeindename** - Offizielle Bezeichnung
- **Verwaltungsebenen** - Zuordnung zu Ländern, Kreisen, etc.
- **Gebietsstand** - Gültigkeitsdatum der Daten

## Dateiname-Format

```
GV100AD_DDMMYYYY.txt
```

**Beispiel:** `GV100AD_31082025.txt` = Gebietsstand vom 31.08.2025

## Datenstruktur

Die Datei verwendet **feste Positionen** pro Zeile:

| Position | Inhalt | Beschreibung |
|----------|--------|--------------|
| 1-2 | Satzart | `06` = Gemeinde |
| 11-18 | ARS | Amtlicher Regionalschlüssel (8-stellig) |
| 23-72 | Gemeindename | Offizielle Gemeindebezeichnung |

### Beispiel-Zeile:
```
06111000000000000000000Koblenz, Stadt                                    
```
- **Satzart:** `06` (Gemeinde)
- **ARS:** `06111000`
- **Name:** `Koblenz, Stadt`

## Verwendung

- **Offizielle Referenz** für deutsche Gemeinden
- **Eindeutige Zuordnung** über ARS-Codes
- **Basis** für statistische Auswertungen
- **Aktualisierung** bei Gebietsreformen

## Quelle

[Statistisches Bundesamt (Destatis)](https://www.destatis.de) - Amtliches Gemeindeverzeichnis