# Wichtelautomat
Hybrid Automat zum Wichteln in einer Gruppe


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
