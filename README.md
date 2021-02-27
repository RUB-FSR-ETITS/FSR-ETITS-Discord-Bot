# FSR-ETITS-Discord-Bot

Ein wirklich kleiner Discord Bot der das Problem mit den Abstimmungen und der Beteiligung im Voicechat löst. Duch den Bot können nur noch Servermitglieder abstimmen, die auch bei der Sitzung im Voicechat sind.

## Anleitung:
1. [Python](https://www.python.org/downloads/) installieren.
2. [Discord.py](https://discordpy.readthedocs.io/en/latest/) installieren.
3. Ein gültiges [Bot-Token](https://discordpy.readthedocs.io/en/latest/discord.html) erzeugen, welches unter **token** eingetragen werden muss. Es reicht ein Discord Account um das Token zu erzeugen.
4. Den Bot wie im vorherigen Link den Server beitreten lassen.
5. Den Textchannel umstellen, sodass Nachriten by default keine Reaktionen hinzugefügt werden dürfen
6. Eine Rolle erstellen, die Nutzern die Berechtigung gibt in diesem Textchannel Reaktionen hinzuzufügen. Sollte in der Hirarchie unter der Bot-Rolle sein, um Berechtigungsprobleme zu vermeiden
7. Über die Befehle des Bots können die ID aller Voicechannel und die ID aller Rollen ausgegeben werden. Den Befehl am besten in einem temporären Kanal ausführen, da es je nach Server recht viele Nachrichten sind. Dort die ID der erstellten Rollte und des genutzten Voicechannels raussuchen
8. Die ID vom Voicechannel unter **channel_id** und die ID der Rolle unter **role_id** eintragen.
9. Testen und hoffen

## Befehle
- **$about** Eine kleine Info zum Bot
- **$roles** Gibt alle verfügbaren Rollen mit Name und ID aus
- **$server** Gibt Name und ID des Server aus
- **$vchannels** Gibt alle verfügbaren Voicechannels mit Name und ID aus

## Mögliche Features
Wenn noch jemand Zeit hat könnte man vielleicht noch einen der folgenden Punkte umsetzen:
- Befehl um die Sitzung zu starten und zu beenden
- Automatisches loggen der Teilnehmer für das Protokoll während einer aktiven Sitzung
- Abstimmung und Auswertung der Abstimmung über Bot-Befehl
- ...
