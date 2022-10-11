# Wichtelautomat
Hybrid Automat zum Wichteln in einer Gruppe

# Wie läuft die Sache für den Anwender
* melde dich auf der Whatsapp Web Seite an: `https://web.whatsapp.com/`
* öffne DOS Fenster: `Windowstaste + r -> cmd -> enter`
* ins dos Fenster eingeben: `pushd Z:\Andy\Dokumente\Stauanfang\wichtelautomat\wichtelautomat-main\src\main`
* ins dos Fenster eingeben: `..\..\env\Scripts\activate`
* checke: sind die Telefonliste und Werkzeugliste befüllt: `telefon.txt, werkzeug.txt`
* checke: in der Datei `2_main_sende_wichtel_ergebnis.py`, ob der Text bei `intro_text_for_whatsapp_message` passt
* ins dos Fenster eingeben: `py 1_main_wichteln.py
* checke: die Datei `wichtel_ergebnis.json`
* ins dos Fenster eingeben: `py 2_main_sende_wichtel_ergebnis.py

# Installation unter windows
* python: `C:\Users\Andy\AppData\Local\Programs\Python\Python38\python.exe`

# Python - whatspp Voraussetzungen
* Hier habe ich ein gutes und einfaches Tutorial gefunden: `https://youtu.be/MQQTABNMZCE`
* Python: `pip3 install pywhatkit`
* Man muss im Browser in whatapp eingeloggt sein -> hier muss man herausfinden welchen Browser man am besten nutzt [whatsapp-Web](https://web.whatsapp.com)

# Beispiel
Sende eine Nachricht an einen Kontakt
```python
import pywhatkit

pywhatkit.sendwhatmsg(
    phone_no="+49151XXXX", 
    message="text", 
    time_hour=7, 
    time_min=32)

```

Man kann auch noch eine Nachriht an eine Gruppe senden:
`pywhatkit.sendwhatmsg_to_group()`

# Hauptprogramm
* Input: zwei `txt` Dateien, eine mit Telefonnummern und eine mit Liste an Werkzeugen
* Zufaellige Zuordnung von Telefon und Werkzeug
* Senden der einzelnen Nachricht an Whatsapp

## Skripte
* `1_main_wichteln.py` -> erstellt mir ein zufälliges zuordnen von Telefonnummern und Werkzeuge
* `2_main_sende_wichtel_ergebnis.py` -> hier muss man sich vorher online bei whatsapp anmelden ([whatsapp-Web](https://web.whatsapp.com)) und dann wird für jede Nachricht ein eigener Tab geöffnet und dann gesendet
* `3_main_test_whatsapp.py` -> Einfach zum Testen bevor der echte Lauf gestartet wird

# Backup
`Quelle: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/`

### Wo liegt die Installation
`C:\Users\Andy\AppData\Local\Programs\Python\Python38\python.exe`

### update pip
`C:\Users\Andy\AppData\Local\Programs\Python\Python38\python.exe -m pip install --user --upgrade pip`

### have a look what is installed
Ist nicht unbedingt notwendig
`(C:\Users\Andy\AppData\Local\Programs\Python\Python38\python.exe -m pip --version)`

### install virtualenv module
`C:\Users\Andy\AppData\Local\Programs\Python\Python38\python.exe -m pip install --user virtualenv`

### create a env folder
`C:\Users\Andy\AppData\Local\Programs\Python\Python38\python.exe -m venv env`

### activate venv
`.\env\Scripts\activate`
`py src\main\3_main_test_whatsapp.py`

### which python versions are available
`where python`

### install of requirements
`py -m pip install -r requirements.txt`

### examples for pip installations 
`py -m pip install requests`
`py -m pip install requests==2.18.4`