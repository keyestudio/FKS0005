## 5.1 Thonny Entwicklungsumgebung

**Bevor Sie mit der Programmierung beginnen, müssen Sie einige wichtige Vorbereitungen treffen.**

### 5.1.1 Thonny installieren

Thonny ist eine kostenlose und quelloffene Softwareplattform mit geringer Größe, einfacher Benutzeroberfläche, einfacher Bedienung und reichhaltigen Funktionen. Es ist eine Python-IDE, die für Anfänger geeignet ist. In diesem Tutorial verwenden wir diese IDE, um einen ESP32 zu entwickeln. Thonny unterstützt mehrere Betriebssysteme, darunter Windows, Mac OS und Linux.

**1. Thonny herunterladen**

(1) Besuchen Sie die Website: [https://thonny.org](https://thonny.org), um die neueste Version von Thonny herunterzuladen. Andere Versionen sind möglicherweise nicht mit microbit-Funktionen kompatibel.
(2) Thonny Open-Source-Codebibliothek: [https://github.com/thonny/thonny](https://github.com/thonny/thonny).

Bitte laden Sie die Version für Ihr Betriebssystem herunter.

| OS | Download |
| :-- | :-- |
| MAC OS： | https://github.com/thonny/thonny/releases/download/v4.1.7/thonny-4.1.7.pkg|
| Windows： | https://github.com/thonny/thonny/releases/download/v4.1.7/thonny-4.1.7.exe|

| OS | Methode | Befehl |
| :-- |---------|--------------|
| Linux | Binärpaket | `bash <(wget -O - https://thonny.org/installer-for-linux)` |
| | Mit pip | `pip3 install thonny` |
| | Distro-Pakete | Debian/Ubuntu：`sudo apt install thonny`<br>Fedora：`sudo dnf install thonny` |

![Img](./media/t001.png)

**2. Windows System**

A. Das heruntergeladene Thonny-Symbol sieht wie folgt aus:

![Img](./media/t002.png)

B. Doppelklicken Sie auf „thonny-4.1.7.exe“ und wählen Sie den Installationsmodus. Hier wählen wir „Install for all users“.

![Img](./media/t003.png)

C. Sie können auch einfach „Next“ auswählen, um die Installation abzuschließen.

![Img](./media/t004.png)

![Img](./media/t005.png)


D. Wenn Sie den Installationspfad von Thonny ändern möchten, klicken Sie einfach auf „Browse...“, um einen neuen Pfad auszuwählen. Wenn nicht, klicken Sie einfach weiter auf „Next“.

![Img](./media/t006.png)

![Img](./media/t007.png)

E. Aktivieren Sie „Create desktop icon“, um Thonny auf Ihrem Desktop anzuzeigen.

![Img](./media/t008.png)

F. „Install“.

![Img](./media/t009.png)

G. Warten Sie einen Moment, aber klicken Sie nicht auf „Cancel“.

![Img](./media/t010.png)

H. Wenn Sie die Erfolgsmeldung sehen, klicken Sie auf „Finish“.

![Img](./media/t011.png)

I. Sie können das Symbol auf Ihrem Desktop sehen, wenn Sie „Create desktop icon“ aktiviert haben:

![Img](./media/t011.png)                    

### 5.1.2 Thonny Grundeinstellungen

A. Doppelklicken Sie auf Thonny, wählen Sie Sprache und Grundeinstellungen und klicken Sie auf „Let’s go!“.

![Img](./media/t013.png)

![Img](./media/t014.png)

![Img](./media/t015.png)

B. Klicken Sie auf „**View**“→„**File**“ und „**Shell**“.

![Img](./media/t016.png)

![Img](./media/t017.png)

![Img](./media/t018.png)

### 5.1.3 MicroPython Firmware brennen (Wichtig)

Um ein Python-Programm auf dem Micro:bit-Board auszuführen, müssen wir zuerst die Firmware darauf brennen.

**Brennen Sie die MicroPython-Firmware:**

Verbinden Sie den Micro:bit mit einem USB-Kabel mit Ihrem PC.

![Img](./media/A800.png)

Stellen Sie sicher, dass der Treiber erfolgreich installiert wurde und der COM-Port korrekt identifiziert werden kann. Öffnen Sie den „**Geräte-Manager**“ und erweitern Sie „**Anschlüsse**“.

![Img](./media/t019.png)

Die COM-Port-Nummer kann je nach Computer variieren.

Öffnen Sie Thonny, klicken Sie auf „**run**“ und „**Configure interpreter...**“

![Img](./media/t020.png)

Wählen Sie „Micropython (BBC micro:bit)“ und „mbeb Serial Port @ COM16“ in seinem Interpreter aus und klicken Sie auf „Install or update firmware“.

![Img](./media/t021.png)

Und Sie werden Folgendes sehen. Stellen Sie „Target volume“ auf „MICROBIT“, „MicroPython family“ auf „nRF52“, „variant“ auf „BBC micro:bit v2 (original simplifiled API)“, „version“ auf „2.1.2“ und dann „Install“ ein.

Wenn die Firmware nicht installiert werden kann, drücken Sie die Reset-Taste auf dem Micro:bit und klicken Sie auf „Install“.

![Img](./media/t022.png)

Danach klicken Sie auf „Close“ und „OK“.

![Img](./media/t023.png)

Schließen Sie alle Fenster und kehren Sie zur Hauptseite zurück und klicken Sie auf das „STOP“-Symbol:

![Img](./media/t024.png)

### 5.1.4 Code hochladen

**Testcode ausführen (online)**

Der Micro:bit führt den Code online aus, wenn er mit dem Computer verbunden sein muss. Benutzer können Programme mit Thonny programmieren und debuggen.

Öffnen Sie Thonny und klicken Sie auf „**Open**“.

![Img](./media/t025.png)

Wenn ein neues Fenster erscheint, öffnen Sie „.\MicroPython_Resource\Codes\Heart beat“, wählen Sie „heartbeat&ZeroWidthSpace;.py“ aus und klicken Sie auf „Run current script“ (falls Fehler gemeldet werden, klicken Sie zuerst auf ![Img](./media/t027.png) und dann auf „Run current script“), und Sie können sehen, dass ein Herz auf dem Micro:bit schlägt.

![Img](./media/t026.png)

Hinweis: Wenn Sie es online ausführen und die Reset-Taste drücken, wird der Code nicht erneut ausgeführt. Wenn Sie möchten, dass er nach dem Zurücksetzen ausgeführt wird, beachten Sie bitte die folgenden Anweisungen zum Offline-Ausführen.

**Testcode ausführen (offline)**

Nach dem Zurücksetzen des Micro:bit wird zuerst die Datei main.py im Stammverzeichnis ausgeführt.

Daher muss der Dateiname, den wir auf den Micro:bit hochladen, in main.py geändert werden, wenn wir möchten, dass der Code nach dem Zurücksetzen ausgeführt wird. Laden Sie dann die Datei hoch, drücken Sie die Reset-Taste, und der Code wird weiterhin ausgeführt.

Hier nehmen wir heartbeat.py als Beispiel. Wählen Sie **heartbeat&ZeroWidthSpace;.py** aus, um es in main.py „**umzubenennen**“, und klicken Sie auf „**OK**“. Jetzt können Sie „**Upload to micro:bit**“ wählen.

![Img](./media/t028.png)

![Img](./media/t029.png)

![Img](./media/t030.png)

Drücken Sie die Reset-Taste und Sie können sehen, dass das Herz auf dem Micro:bit schlägt.

Wenn Sie anderen Code (keine Bibliotheken) ausführen möchten, müssen Sie dessen Namen zuerst in main&ZeroWidthSpace;.py ändern, bevor Sie ihn hochladen.

Bei Bibliotheken klicken Sie mit der rechten Maustaste, um sie direkt auf den Micro:bit hochzuladen (manchmal kann der Upload aufgrund der zu großen Größe der Bibliothek fehlschlagen. Dann müssen Sie sie vereinfachen oder die ungenutzten löschen).

### 5.1.5 Andere gängige Operationen

**Datei unter Micro:bit löschen**

Im „micro:bit“ wählen Sie „main&ZeroWidthSpace;.py“ zum „Delete“ aus, und es wird entfernt.

![Img](./media/t031.png)

Das gleiche Verfahren gilt beim Löschen anderer Dateien.
