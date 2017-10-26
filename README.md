# vp-readable
Ein inoffizielles Projekt, welches das Herunterladen der Vertretungsplandaten von "indiware mobil"-Plänen in eine maschinenlesbare Form (Verschachtelte Liste: Elternebene mit *Stunden*, Tochterebene mit den Informationen *Stunde, Fach, Lehrer_in, Raum, Anmerkungen*) ermöglicht.

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
2. Variable `url` ausfüllen:
  - `url` entspricht der URL des Vertretungsplans in der *Stundenansicht*
3. Variable `AuswahlKl` bestimmen (für Klassenstufe 11 auch `AbwahlKurseJG11`)
  - `AuswahlKl` entspricht dem Wert des Cookies `AuswahlKl` (unter Firefox: Vertretungsplan öffnen -> Klasse wählen -> SHIFT + F5 -> Tab `Storage` öffnen -> Cookie (URL) auswählen -> Wert von `AuswahlKl`)
  - `AbwahlKurseJG11` entspricht dem Wert des Cookies `AbwahlKurseJG11`, wenn Kurse in den Websiteeinstellungen ausgewählt wurden
4. Script ausführen `python download.py "<AuswahlKl>" "<optional: AbwahlKurseJG11>"`
(optional: output in Datei schreiben (Linux): `python download.py "<AuswahlKl>" "<optional: AbwahlKurseJG11>" > output.txt`)

## Lizenz

Das Projekt steht unter der [MIT Lizenz](https://github.com/t0simon/vp-readable/blob/master/LICENSE).
