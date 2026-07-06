## 4.1.1 About MakeCode

⚠️ **Die folgenden Schritte werden unter dem Betriebssystem Windows ausgeführt. Wenn Sie ein anderes Betriebssystem verwenden, können Sie diese als Referenz nehmen. Hier wird Google Chrome / Microsoft Edge demonstriert.**

**MakeCode Programming Environment:**

Öffnen Sie die [online version of MakeCode editor](https://makecode.microbit.org/#editor).

MakeCode Hauptoberfläche:

![Img](./media/A637.png)

Im Code-Bearbeitungsbereich befinden sich die Blöcke “**on start**” und “**forever**”. Wenn die Stromversorgung eingesteckt oder das Gerät zurückgesetzt wird, bedeutet “on start”, dass der Code im Block nur einmal ausgeführt wird, während “forever” impliziert, dass der Code zyklisch ausgeführt wird.

Klicken Sie auf “**JS JavaScript**”, um den JavaScript-Code zu sehen:

![Img](./media/A754.png)

Oder klicken Sie auf “**Python**”, um zu Python-Code zu wechseln:

![Img](./media/A814.png)

**Language settings:**

![Img](./media/Animation-3.gif)

Schritte:

Step 1: Klicken Sie auf die Einstellungen ![Img](./media/A806.png).

![Img](./media/A301.png)

Step 2: Klicken Sie auf “Language”.

![Img](./media/A302.png)

Step 3: Wählen Sie die gewünschte Sprache aus. Hier stellen wir sie auf “English”.

![Img](./media/A303.png)

## 4.1.2 Makecode Extension Library

### 4.1.2.1 Add Library

⚠️ **Wir stellen Code-Dateien (.hex) für jedes Projekt zur Verfügung, sodass Sie diese direkt in den MakeCode-Editor laden können. Oder wenn Sie möchten, können Sie die Codeblöcke auch selbst bauen. Beachten Sie, dass Bibliotheken erforderlich sind, wenn Sie sie manuell erstellen.**

⚠️ **<span style="color: rgb(255, 76, 65);">Hinweis:</span>** Kopieren Sie den Link und fügen Sie ihn in das Suchfeld ein: `https://github.com/keyestudio2019/pxt-creative-inventors-kit-master.git`.

![Img](./media/Animation-4.gif)

Schritte:

1\. Klicken Sie auf ![Img](./media/A806.png), um “**Extensions**” auszuwählen.

![Img](./media/A842.png)

Oder klicken Sie auf “**Extensions**” oberhalb der **Advanced**-Blöcke.

![Img](./media/A900.png)

2\. Suchen Sie nach Schlüsselwörtern oder fügen Sie den GitHub-Link ein.

![Img](./media/A909.png)

3\. Hier geben wir die URL: `https://github.com/keyestudio2019/KEYES-Smart-Gamepad-master.git` in das Suchfeld ein und klicken auf ![Img](./media/A3257.png), um die Erweiterung “**Smart-Gamepad**” zu laden.

![Img](./media/A306.png)

4\. Laden:

![Img](./media/A3316.png)

5\. Geladen:

![Img](./media/A335.png)

### 4.1.2.2 Update/Delete Library

⚠️ **Im Allgemeinen ist es nicht nötig, Bibliotheken zu entfernen, es sei denn, sie werden nicht mehr benötigt.**

![Img](./media/Animation-4.gif)

Schritte:

1\. Klicken Sie auf “**JavaScript**”, um zu Textcodes zu wechseln.

![Img](./media/A724.png)

2\. Klicken Sie auf “**Explorer**”.

![Img](./media/A749.png)

3\. Finden Sie das “**Smart-Gamepad**” und klicken Sie auf den Papierkorb ![Img](./media/A813.png), um es zu entfernen.

![Img](./media/A824.png)

4\. “**Remove it**”.

![Img](./media/A727.png)

## 4.1.3 MakeCode Program

### 4.1.3.1 Import Program in MakeCode

Wir nehmen das Projekt “**heatbeat**” als Beispiel.

![Img](./media/Animation-2.gif)

Schritte:

1\. Schließen Sie das micro:bit-Board mit dem micro USB-Kabel an Ihren Computer an.

![Img](./media/A800.png)

Wenn das micro:bit eingeschaltet ist, leuchtet die rote LED-Anzeige auf seiner Rückseite.

Auf dem micro:bit-Board befindet sich eine gelbe LED-Anzeige, die blinkt, wenn das Board über micro USB mit Ihrem Computer kommuniziert.

Öffnen Sie Finder(Mac) / Devices and drives(Windows), und Sie sehen ein USB-Laufwerk mit dem Namen "MICROBIT". Beachten Sie jedoch, dass es sich nicht um eine normale Festplatte handelt!

![Img](./media/A849.png)

2\. Klicken Sie auf “**Import**”:

![Img](./media/A956.png)

3\. Und wählen Sie “**Import File...**”.

![Img](./media/A042.png)

4\. “**Choose File**”, um die benötigte Datei zu öffnen.

![Img](./media/A06.png)

5\. Hier wählen wir “**heartbeat.hex**”.

![Img](./media/A28.png)

6\. “**Go ahead √**”.

![Img](./media/A149.png)

Oder Sie können die hex-Datei direkt in die Makecode-Hauptoberfläche ziehen:

![Img](./media/A202.png)

7\. Importiert:

![Img](./media/A217.png)

### 4.1.3.2 Download Code (WebUSB)

Für Browser wie **Google Chrome/Microsoft Edge** erlaubt deren WebUSB den direkten Zugriff auf das micro USB-Hardwaregerät über eine Online-Webseite. Klicken Sie auf “Connect Device”, um das Gerät zu koppeln. Danach klicken Sie auf “**Download**”, um den Code auf das micro:bit-Board zu laden.

![Img](./media/Animation.gif)

Schritte:

#### 4.1.3.2.1 Pair device

1\. Schließen Sie das micro:bit-Board mit dem micro USB-Kabel an Ihren Computer an.

![Img](./media/A951.png)

2\. Klicken Sie auf die drei Punkte “**...**” hinter “**Download**” und wählen Sie “**Connect device**”.

![Img](./media/A028.png)

3\. “**Next**”.

![Img](./media/A046.png)

4\. “**Pair**”.

![Img](./media/A104.png)

5\. Verbinden Sie mit einem “**Device**” und klicken Sie auf “**Connect**”.

![Img](./media/A127.png)

6\. “**Done**” und verbunden.

![Img](./media/A144.png)

#### 4.1.3.2.2 Download code

Nach der Verbindung klicken Sie auf “**Download**” und der Code wird auf das micro:bit-Board heruntergeladen, und ![Img](./media/A212.png) wird zu ![Img](./media/A220.png).

![Img](./media/A232.png)

⚠️ **Tipps**

Wenn kein Gerät zum Koppeln in der Oberfläche vorhanden ist, siehe [device-webusb-troubleshoot](https://makecode.microbit.org/device/usb/webusb/troubleshoot).

Wenn die micro:bit-Firmware ein Update benötigt, siehe [how-to-update-the-firmware](https://microbit.org/guide/firmware/).

### 4.1.3.3 Download Code (none WebUSB)

1\. Schließen Sie das micro:bit-Board mit dem micro USB-Kabel an Ihren Computer an.

![Img](./media/A800.png)

Wenn das micro:bit eingeschaltet ist, leuchtet die rote LED-Anzeige auf seiner Rückseite.

Auf dem micro:bit-Board befindet sich eine gelbe LED-Anzeige, die blinkt, wenn das Board über micro USB mit Ihrem Computer kommuniziert.

Öffnen Sie Finder(Mac) / Devices and drives(Windows), und Sie sehen ein USB-Laufwerk mit dem Namen "MICROBIT". Beachten Sie jedoch, dass es sich nicht um eine normale Festplatte handelt!

![Img](./media/A849.png)

2\. Für Browser laden Sie bitte den Code wie folgt auf das micro:bit-Board:

![Img](./media/Animations-1.gif)

Schritte:

① Klicken Sie auf die “**Download**”-Schaltfläche und eine “**.hex**”-Datei wird heruntergeladen, die vom micro:bit-Board gelesen werden kann. Kopieren Sie diese anschließend auf das Board.

Für Windows können Sie “**Send to→MICROBIT**” verwenden und die “**.hex**” auf das micro:bit-Board laden. Während dieses Vorgangs blinkt die gelbe Anzeige auf der Rückseite des Boards. Nach Abschluss bleibt die Anzeige an.

![Img](./media/A319.png)

![Img](./media/A449.png)

Oder Sie können die “**.hex**”-Datei direkt in das MICROBIT ziehen:

![Img](./media/A341.png)

![Img](./media/A345.png)

② Danach verbinden Sie das micro: bit-Board per micro USB-Kabel mit dem Computer und schalten es ein; Sie sehen, dass die eingebaute 5 x 5 LED-Matrix wiederholt ![Img](./media/A903.png) und ![Img](./media/A910.png) anzeigt.

![Img](./media/A22.png)

⚠️ Während jedes Programmierens wird die MICROBIT-Festplatte automatisch ausgeworfen und zurückgegeben, und die **.hex**-Dateien, die Sie darauf kopiert haben, werden nicht angezeigt. Das liegt daran, dass das micro:bit-Board nur das zuletzt hochgeladene Programm empfängt und ausführt, anstatt sie zu speichern.