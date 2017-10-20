# Module importieren
from selenium import webdriver
import os



# Variablen beinhalten die Werte:
# url: URL der Seite, welche den Vertretungsplan zeigt
url = ''

# cookie_AbwahlKurs: 'value' sollte mit dem Inhalt des Cookies belegt werden (einsehbar unter Firefox: SHIFT + F5 -> Storage -> Cookies -> Value des Cookies 'AbwahlKurseJG11')
cookie_AbwahlKurs = {'name':'AbwahlKurseJG11', 'value':'', 'path':'/'}

# cookie_AbwahlKurs: 'value' sollte mit dem Inhalt des Cookies belegt werden (einsehbar unter Firefox: SHIFT + F5 -> Storage -> Cookies -> Value des Cookies 'AuswahlKl')
cookie_Klasse = {'name':'AuswahlKl', 'value':'', 'path':'/'}



# Oeffnen der Website in Firefox und Auslesen der Daten
os.environ['MOZ_HEADLESS'] = '1'
browser = webdriver.Firefox()
browser.get(url)
browser.add_cookie(cookie_AbwahlKurs)
browser.add_cookie(cookie_Klasse)
browser.get(url)
stunde = browser.find_elements_by_css_selector("span.mobstunde")
fach = browser.find_elements_by_css_selector("span.mobfach")
lehrer = browser.find_elements_by_css_selector("span.moblehrer")
raum = browser.find_elements_by_css_selector("span.mobraum")



# Verarbeitung und Ausgabe der Daten
if keine_daten == []:
    zeile = []
    i = 0
    i_max = len(stunde) - 1
    while i <= i_max:
        zeile.append([stunde[i].text, fach[i].text, lehrer[i].text, raum[i].text])
        i += 1
    print(zeile)
else:
    print("keine_daten")


browser.quit()
