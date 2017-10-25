# BENUTZUNG:
#
# python download.py "<AuswahlKl>" "<optional: AbwahlKurseJG11>"
# AuswahlKl: Inhalt des Cookies "AuswahlKl" (einsehbar unter Firefox: SHIFT + F5 -> Storage -> Cookies -> Value des Cookies 'AuswahlKl')
# AbwahlKurseJG11: Inhalt des Cookies "AuswahlKl" (einsehbar unter Firefox: SHIFT + F5 -> Storage -> Cookies -> Value des Cookies 'AbwahlKurseJG11')

# Import von Selenium
from selenium import webdriver
import os
import sys

# AUSFUELLEN:
#
# url = '<URL der Seite, welche den Vertretungsplan zeigt>'
url = ''

# Oeffnen der Website in Firefox und Auslesen der Daten
os.environ['MOZ_HEADLESS'] = '1'
browser = webdriver.Firefox()
browser.get(url)
# Argument "Klasse" auslesen und Cookie setzten
value_Klasse = sys.argv[1]
browser.add_cookie({'name':'AuswahlKl', 'value': value_Klasse, 'path':'/'})
# optionales Argument "Abwahlkurse" auslesen und Cookie setzten
if len(sys.argv) == 3:
    value_AbwahlKurs = sys.argv[2]
    browser.add_cookie({'name':'AbwahlKurseJG11', 'value': value_AbwahlKurs, 'path':'/'})
browser.get(url)

# HTML-Tags auslesen
keine_daten = browser.find_elements_by_css_selector("li.mobilauswahlkl")
stunde = browser.find_elements_by_css_selector("span.mobstunde")
fach = browser.find_elements_by_css_selector("span.mobfach")
lehrer = browser.find_elements_by_css_selector("span.moblehrer")
raum = browser.find_elements_by_css_selector("span.mobraum")
info = browser.find_elements_by_css_selector("span.mobinfo")

# Verarbeitung und Ausgabe der Daten
if keine_daten == []:
    zeile = []
    i = 0
    i_max = len(stunde) - 1
    while i <= i_max:
        zeile.append([stunde[i].text, fach[i].text, lehrer[i].text, raum[i].text, info[i].text])
        i += 1
    print(zeile)
else:
    print("keine_daten")


browser.quit()
