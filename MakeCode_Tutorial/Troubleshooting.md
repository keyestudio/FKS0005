## Troubleshooting
### 4.3.1 USB Driver Installation (Optional)

**Micro:bit is free of driver installation. However, in case your computer fail to recognize the main board, you can install the diver too.**

#### 4.3.1.1 USB Driver Download

Klicken Sie, um die [USB driver](./USB_driver.7z) herunterzuladen.

#### 4.3.1.2 USB Driver Installation

⚠️ Bitte beachten Sie, dass hier gezeigt wird, wie der Treiber unter Windows installiert wird; dies kann als Referenz für MacOS-Benutzer dienen.

1\. Verbinden Sie die micro:bit Hauptplatine mit dem Computer über ein USB Kabel.

![Img](./media/A800.png)

2\. Suchen Sie die Treiberdatei, klicken Sie darauf und klicken Sie auf **Install**.

![Img](./media/A323.png)

![Img](./media/A327.png)

3\. Klicken Sie auf “**Install**” und “**Next**”.

![Img](./media/A347.png)

4\. Klicken Sie auf “**Install**” und “**Finish**”.

![Img](./media/A408.png)

![Img](./media/A349.png)

5\. Klicken Sie “**Computer**” → “**Properties**” → “**Device manager**” und Sie werden sehen:

![Img](./media/A427.png)

### 4.3.2 FAQ
Lösungen für das Problem, wenn Microbit beim Herunterladen von Programmen fehlschlägt und MAINTENANCE anzeigt.

#### 4.3.2.1 Problems

Viele neue Benutzer sind in letzter Zeit auf dieses Problem gestoßen: Wenn sie das Micro:bit-Board mit einem Micro USB Kabel an den Computer anschließen und auf “**Download**” klicken, schlägt der Download fehl und das Board reagiert nicht.

Wenn Sie aus Versehen die Reset-Taste auf der Rückseite des Micro:bit-Boards gedrückt hielten, als Sie das Programm darauf kopierten, würde dies das Board in den Wartungsmodus versetzen. Oder möglicherweise ist durch einen Ihrer Fehler die Firmware auf dem Board verloren gegangen.

Infolgedessen erscheint ein neues “**MAINTENANCE**” Laufwerk in Ihrem Dateimanager, sodass die micro:bit Ihren Benutzercode nicht akzeptiert.

Das MAINTENANCE-Laufwerk sieht je nach Computer so aus:

![Img](./media/158.png)

 #### 4.3.2.2 Solutions

(1) Laden Sie die <span style="color: rgb(255, 76, 65);">.hex</span>-Datei, die für Ihre Version des micro:bit geeignet ist, von dieser Seite auf Ihren Computer herunter.

Laden Sie [the latest Micro:bit firmware -0255 .hex file](https://www.microbit.org/get-started/user-guide/firmware/) herunter, das wir ebenfalls im Ordner zur Verfügung gestellt haben.

(2) Ziehen Sie die .hex-Datei, die Sie von dieser Seite heruntergeladen haben, per Drag & Drop auf das **MAINTENANCE**-Laufwerk. <span style="color: rgb(255, 76, 65);">Beachten Sie, dass die Firmware je nach Modell des Micro:bit V2-Boards variiert. Hier ist Firmware für V2.20_V2.21.</span> Wenn das Upgrade abgeschlossen ist, wird sich die micro:bit zurücksetzen, sich vom Computer auswerfen und im normalen **MICROBIT**-Laufwerksmodus wieder erscheinen.

![Img](./media/326.png)

![Img](./media/331.png)

#### 4.3.2.3 Avoid “MAINTENANCE” Mode

(1) Drücken Sie nicht die Reset-Taste auf der Rückseite des Micro:bit-Boards, wenn es mit einem Micro USB Kabel verbunden ist.

Wenn die Reset-Taste beim Einschalten gedrückt wird, geht die micro:bit in den Wartungsmodus. (**<span style="color: rgb(255, 76, 65);">Häufige Fehler von Anfängerinnen und Anfängern</span>**)

![Img](./media/228.png)

(2) Trennen Sie es während des Programmdownloads nicht plötzlich. Andernfalls kann die Firmware verloren gehen und die micro:bit wechselt dann in den MAINTENANCE-Modus.

(3) Falsche Verkabelung während des Experiments kann ebenfalls zu einem Kurzschluss führen, sodass die micro:bit-Firmware verloren gehen kann. Anfängerinnen und Anfänger müssen beim Arbeiten sorgfältig sein.

#### 4.3.2.4 Download with WebUSB

Ihr micro:bit scheint einen Fehler mit WebUSB (/ device/ usb/ webusb) entwickelt zu haben? Versuchen wir, den Grund herauszufinden.

**Step 1: Test on micro USB cable**

Stecken Sie das micro:bit mit einem micro USB Kabel in Ihren Computer. Es sollte als ein MICROBIT Laufwerk erscheinen.

![Img](./media/321.png)

Wenn MICROBIT unter Devices and drives als Laufwerk erscheint, gehen Sie zu Schritt 2.

Wenn nicht, versuchen Sie bitte: (a) ein anderes Kabel; (b) einen anderen USB Anschluss an Ihrem Computer; (c) schließen Sie das micro:bit an einen anderen Computer an.

Einige micro USB Kabel bieten möglicherweise nur eine Stromverbindung und übertragen tatsächlich keine Daten, und einige Computer schalten aus irgendeinem Grund ihre USB Anschlüsse ab.

Sie sehen das MICROBIT Laufwerk immer noch nicht? Hm, vielleicht liegt ein Problem mit Ihrer micro:bit Platine vor. Lesen Sie den Artikel zu [troubleshooting](https://support.microbit.org/solution/articles/19000024000-fault-finding-with-a-micro-bit) auf microbit.org oder öffnen Sie ein [support ticket](https://support.microbit.org/support/tickets/new), um die Micro:bit Foundation über das Problem zu informieren. Und überspringen Sie alle folgenden Schritte.

**Step 2: Checking your firmware version**

Um herauszufinden, welche Firmware-Version auf Ihrer micro:bit installiert ist:

① Stecken Sie sie mit dem USB Kabel in einen Computer und öffnen Sie das **MICROBIT** Laufwerk.

![Img](./media/A8491.png)

② Öffnen Sie die Datei **DETAILS.TXT**.

![Img](./media/0452.png)

③ Suchen Sie nach der Nummer in der Zeile, die mit “Interface/Bootloader Version” beginnt.

![Img](./media/501.png)

Wenn es 0234/0241/0243 ist, müssen Sie die Firmware auf Ihrem micro:bit V2-Board aktualisieren. Gehen Sie für das Update zu Schritt 3.

Wenn es 0249/0257 oder höher ist, gehen Sie zu Schritt 4.

**Step 3: How to update the firmware**

Wenn Sie die Firmware aktualisieren müssen, um auf eine neue Funktion zuzugreifen oder ein Problem zu beheben, gehen Sie wie folgt vor:

① Trennen Sie das USB Kabel und das Batteriepack vom micro:bit。

② Halten Sie die Reset-Taste auf der Rückseite des micro:bit gedrückt und stecken Sie das USB Kabel in das micro:bit und Ihren Computer. Sie sollten ein Laufwerk namens **MAINTENANCE** (anstelle von MICROBIT) im Dateimanager sehen und die gelbe LED-Anzeige auf der Rückseite sollte leuchten.

![Img](./media/551.png)

![Img](./media/AAC1.webp)

③ Laden Sie die [firmware .hex file](https://microbit.org/guide/firmware/) herunter, die für Ihre Version des micro:bit geeignet ist. <span style="color: rgb(255, 76, 65);">Hier ist Firmware für V2.20_V2.21.</span>

![Img](./media/0629.png)

④ Ziehen Sie die <span style="color: rgb(255, 76, 65);">.hex</span>-Firmware per Drag & Drop auf das **MAINTENANCE**-Laufwerk.

![Img](./media/331.png)

⑤ Warten Sie, bis die gelbe LED auf der Rückseite aufhört zu blinken. Nach dem Kopieren erlischt die LED und die micro:bit wird sich zurücksetzen. MAINTENANCE wird wieder zu MICROBIT.

⑥ Überprüfen Sie abschließend die Datei <span style="color: rgb(255, 76, 65);">DETAILS.TXT</span>, die sich auf dem **MICROBIT** Laufwerk befindet, und stellen Sie sicher, dass sie dieselbe Versionsnummer wie die .hex-Firmware enthält.

Bei Problemen mit der Platine, dem Wartungsmodus und Firmware-Updates konsultieren Sie bitte das [Firmware Guide](https://microbit.org/guide/firmware/).

**Step 4: Checking your browser version**

WebUSB ist eine relativ neue Funktion; möglicherweise müssen Sie Ihren Browser aktualisieren. Prüfen Sie, ob Ihr Browser: (a) mit Android, Chrome OS kompatibel ist; (b) Microsoft Edge; (c) Chrome 65+ für Linux, macOS und Windows 10.

**Step 5: Connecting a device**

Öffnen Sie Google Chrome / Microsoft Edge, gehen Sie zum MakeCode editor und klicken Sie auf “**Connect Device**”. Wie man ein Gerät koppelt, entnehmen Sie bitte [WebUSB (/ device/ usb/ webusb)](https://microbit.org/get-started/user-guide/web-usb/).

Viel Erfolg beim schnellen Herunterladen!