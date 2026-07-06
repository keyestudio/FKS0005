### 4.2.4 Musikplayer

#### 4.2.4.1 Übersicht

![Img](./media/top1.png)

Hier bauen wir einen Musikplayer, der Töne über den eingebauten Buzzer des micro:bit-Boards erzeugt (spielt keine Gesangsmusik). Er verfügt über eine Bibliothek von 20 kurzen Titeln und unterstützt sowohl sequenzielle als auch zufällige Wiedergabe.

Im sequentiellen Modus wechselt das Drücken der Taste C (vorheriger Titel) oder E (nächster Titel) die Titel gemäß einer voreingestellten Reihenfolge, bis das Ende der Liste erreicht ist; im Zufallsmodus wählt jeder Tastendruck zufällig einen Titel aus den 20 Sounds aus, während die farbigen Leuchten blinken, und wenn ein Lied beendet ist, stoppt die Wiedergabe sofort.

Währenddessen zeigt die micro:bit LED-Matrix den aktuellen Wiedergabemodus in Echtzeit an.

![Img](./media/bottom1.png)

#### 4.2.4.2 Benötigte Teile

| ![Img](./media/microbitV2.png)|  ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 board** (selbst bereitgestellt) ×1 | **micro:bit Smart Gamepad** (zusammengesetzt) ×1 |**AAA-Batterie** (selbst bereitgestellt) ×4 |

#### 4.2.4.3 Ablauf des Codes

![Img](./media/4001.png)

#### 4.2.4.4 Testcode

**Vollständiger Code:**

![Img](./media/4002.png)

![Img](./media/line1.png)

**Kurze Erklärung:**

① Initialisieren Sie die LED-Matrix und die Lautstärke, verbinden Sie den RGB-Pin mit P8 und setzen Sie die Anzahl der RGB auf 4.

![Img](./media/4003.png)

② Initialisieren Sie das Melodie-Array mit 20 Einträgen und fügen Sie die einzelnen Tracks hinzu; setzen Sie die anfängliche Lautstärke.

![Img](./media/4004.png)

③ Bestimmen Sie, ob Taste D oder F gedrückt wird. Drücken Sie D für '0-sequentielle Wiedergabe', F für '1-zufällige Wiedergabe'.

![Img](./media/4005.png)

④ Im sequentiellen Modus drücken Sie C, um den vorherigen Titel abzuspielen, bzw. E, um zum nächsten Titel zu springen. 

![Img](./media/4006.png)

Da sich nur 20 Titel im Array befinden, können nur Titel mit Nr. 0–19 wiedergegeben werden. Daher fügen wir eine if-Bedingung hinzu, um Überläufe und Unterläufe des Arrays zu vermeiden.

![Img](./media/4007.png)

Im Zufallsmodus hingegen drücken Sie C/E, um unter diesen 20 Titeln zufällig auszuwählen.

![Img](./media/4008.png)

⑤ Überprüfen Sie, ob der vorherige Titel vom aktuellen abweicht. Falls ja, stoppen Sie zuerst die aktuelle Wiedergabe und spielen Sie anschließend den neuen Titel.

![Img](./media/4009.png)

⑥ Überprüfen Sie, ob der Modus '0-sequentielle Wiedergabe' ist, dann wird '![Img](./media/4010.png)' angezeigt, oder '1-zufällige Wiedergabe', dann wird '![Img](./media/4011.png)' angezeigt, mit einer Verzögerung von 100 ms.

![Img](./media/4012.png)

⑦ Lassen Sie die RGB-Leuchten im Hintergrund pulsieren (Breathing-Effekt).

![Img](./media/4013.png)

⑧ Drücken Sie A, um die Lautstärke zu erhöhen (+10); drücken Sie B, um sie zu verringern (-10). Die Lautstärke des micro:bit-Buzzers wird durch die Ausgangsspannung des intern angeschlossenen Pins bestimmt. Wir können die Lautstärke steuern, indem wir digitale Werte von 0–255 mithilfe eines DAC in analoge Werte umwandeln.

![Img](./media/4014.png)

#### 4.2.4.5 Testergebnis

![Img](./media/4top.png)

Nachdem Sie den Code aufgespielt haben, stecken Sie das micro:bit-Board in den Steckplatz des Gamepads (**Batterien eingelegt**) und schalten Sie den Schalter darauf auf “ON”.

Nach dem Einschalten ist standardmäßig der sequentielle Modus aktiv, und es wird der Titel mit Nr. “0” abgespielt. Wenn er beendet ist, können Sie C für den vorherigen Titel oder E für den nächsten drücken.

Drücken Sie F, um in den Zufallsmodus zu wechseln. Und Sie können D drücken, um zum sequentiellen Modus zurückzukehren. Im F-Modus wird bei Drücken von C/E ein zufälliger Titel aus diesen 20 abgespielt. Nach dem Ende stoppt die Wiedergabe.

Die RGB-Leuchten pulsieren (Breathing-Effekt) von dem Moment des Einschaltens an ständig. Gleichzeitig zeigt die micro:bit LED-Matrix in sequentiellem Modus “![Img](./media/4010.png)” und im Zufallsmodus “![Img](./media/4011.png)” an.

Zur Lautstärkeregelung drücken Sie A, um die Lautstärke zu erhöhen, und B, um sie zu verringern.

![Img](./media/4015.gif)

<span style="color: rgb(0, 209, 0);">**Tipp:** Wenn das Board nicht reagiert, drücken Sie bitte die Reset-Taste auf der Rückseite des micro:bit-Boards.</span>

![Img](./media/4bottom.png)