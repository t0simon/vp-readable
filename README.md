# vp-readable
Ein inoffizielles Projekt, welches das Herunterladen der Vertretungsplandaten von "indiware mobil"-Plänen in eine maschinenlesbare Form (Verschachtelte Liste: Elternebene mit *Stunden*, Tochterebene mit den Informationen *Stunde, Fach, Lehrer_in, Raum, Anmerkungen*) ermöglicht.

## Softwareabhängigkeiten
### Firefox mit `geckodriver`
[Firefox](https://getfirefox.com)

Linux (getestet): [geckodriver](https://github.com/mozilla/geckodriver)

### Oder: Chrome/Chromium
[Chrome](https://www.google.com/chrome/index.html)

[Chromium](https://www.chromium.org/Home)
Linux: Chromium für das Skript im Chrome-Pfad zur verfügung stellen: `sudo ln -s /usr/lib/chromium-browser/chromium-browser /usr/bin/google-chrome`

### Python 3
[Python 3](https://www.python.org/)

##### Module
Selenium (lokal): `pip install --user selenium`
Oder aus der Paketquelle der Distribution

## Benutzung
1. `git clone https://github.com/t0simon/vp-readable.git` oder Download des [Skripts für Firefox](https://github.com/t0simon/vp-readable/blob/master/firefox_dl.py) oder [für Chrome/Chromium](https://github.com/t0simon/vp-readable/blob/master/chrome_dl.py)
2. Variable `url` ausfüllen:
  - `url` entspricht der URL des Vertretungsplans in der *Stundenansicht*
3. Variable `AuswahlKl` bestimmen (für Klassenstufe 11 auch `AbwahlKurseJG11`)
  - `AuswahlKl` entspricht dem Wert des Cookies `AuswahlKl` (unter Firefox: Vertretungsplan öffnen -> Klasse wählen -> SHIFT + F5 -> Tab `Storage` öffnen -> Cookie (URL) auswählen -> Wert von `AuswahlKl`)
  - `AbwahlKurseJG11` entspricht dem Wert des Cookies `AbwahlKurseJG11`, wenn Kurse in den Websiteeinstellungen ausgewählt wurden
4. Script ausführen (Firefox) `python /pfad/zu/firefox_dl.py "<AuswahlKl>" "<optional: AbwahlKurseJG11>"`
(Chrome/Chromium: `python /pfad/zu/chrome_dl.py "<AuswahlKl>" "<optional: AbwahlKurseJG11>"`)

(optional: output in Datei schreiben (Linux mit Firefox): `python /pfad/zu/firefox_dl.py "<AuswahlKl>" "<optional: AbwahlKurseJG11>" > output.txt` (Linux mit Chrome/Chromium: `python /pfad/zu/chrome_dl.py "<AuswahlKl>" "<optional: AbwahlKurseJG11>" > output.txt`))


## Lizenz

Das Projekt steht unter der [MIT Lizenz](https://github.com/t0simon/vp-readable/blob/master/LICENSE).
