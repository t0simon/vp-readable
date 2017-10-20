# vp-readable
Ein inoffizielles Projekt, welches das Herunterladen der Vertretungsplandaten von "indiware mobil"-Plänen in eine maschinenlesbare Form (Verschachtelte Liste: Elternebene mit *Stunden*, Tochterebene mit den Informationen *Stunde, Fach, Lehrer_in, Raum*) ermöglicht.

## Softwareabhängigkeiten
### Firefox mit `geckodriver`
[Firefox](https://getfirefox.com)

Linux (getestet): [geckodriver](https://github.com/mozilla/geckodriver)

### Python 3
[Python 3](https://www.python.org/)

##### Module
Selenium (lokal): `pip install --user selenium`
Oder aus der Paketquelle der Distribution

## Benutzung
1. `git clone https://github.com/t0simon/vp-readable.git` oder Download des [Skripts](https://github.com/t0simon/vp-readable/blob/master/download.py)
2. Variablen `url` und `cookie_Klasse` ausfüllen (für Klassenstufe 11 auch `cookie_AbwahlKurs`)
  - `url` entspricht der URL des Vertretungsplans in der *Stundenansicht*
  - `cookie_Klasse` entspricht dem Wert des Cookies `AuswahlKl` (unter Firefox: Vertretungsplan öffnen -> Klasse wählen -> SHIFT + F5 -> Tab `Storage` öffnen -> Cookie (URL) auswählen -> Wert von `AuswahlKl`)
  - `cookie_AbwahlKurs` entspricht dem Wert des Cookies `AbwahlKurseJG11`, wenn Kurse in den Websiteeinstellungen ausgewählt wurden
3. Script ausführen (optional: output in Datei schreiben (Linux): `python download.py > output.txt`)

## Lizenz

Das Projekt steht unter der [MIT Lizenz](https://github.com/t0simon/vp-readable/blob/master/LICENSE).
