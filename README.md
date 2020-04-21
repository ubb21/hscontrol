# Readme
Dies ist ein Telegrambot - Remote Controll für den Home Server.
Es erlaubt bestimmte vordefinierte Optionen auszuführen. Ohne den Service per SSH zu starten.

## Allgemeine Commands:
* info - Laufzeit des Bots/Servers
* start - Der Nutzer startet die Chatverbindung mit diesen Befehl
* myip - gibt die ID des Senders zurück
* mcstart - Startet den Minecraft Server im diesen Ordner

## Spezielle Start CMDS

## Installation
Führe die Datei: install.sh aus
CMD: ./install.sh

## Starten des Telegram Bots
### Erster Start
Trage deinen Bot-Token in die config.py ein
Kopiere dazu die Example zur richtigen config.
* cp configEXAMPLE.py config.py
* nano config.py
Und trage es dort ein

### Bot erstellen
Schreibe auf Telegram den @BotFather an
Erstelle dort einen neuen Bot und notiere den Token in der config.py

### Bot starten
Starte den Bot mithilfe der Datei start.sh
CMD:
* ./start.sh
Führe Ihren BOT_TOKEN in der config.py hinzu.

## Wie startet man den Server
kopiere den Minecraft Server hier hinrein, also wo du diesen Bot installierst hast und füge einen StartSkript an mit den Namen "StartOnce.sh"
Und gebe dort die Parameter zum starten an

## Für:
* Telegram
