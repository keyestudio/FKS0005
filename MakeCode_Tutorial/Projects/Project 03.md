### 4.2.3 Einfaches elektronisches Klavier

#### 4.2.3.1 Übersicht

![Img](./media/top1.png)

In diesem Projekt steuern wir den micro:bit Lautsprecher, um durch Kippen des Joysticks und Drücken der Tasten verschiedene Töne zu erzeugen. Gleichzeitig zeigt die eingebaute LED-Matrix die entsprechenden Zahlen an.

Wenn Sie den Joystick nach rechts bewegen, ertönt "Do (Ton: mittleres C)" und das Display zeigt "1"; bewegen Sie ihn nach links, ertönt "Re (Ton D)" mit "2"; nach oben ergibt "Mi (Ton E)" mit "3"; nach unten ergibt "Fa (Ton F)" mit "4". Drücken Sie die Taste C, ertönt "Sol (Ton G)" mit "5"; D ergibt "La (Ton A)" mit "6"; E ergibt "Si (Ton B)" mit "7"; und bei Druck auf F ertönt ein höheres "Do" und das Display springt wieder auf "1". Joystick, Tasten, Töne und Anzeige sind schön synchronisiert.

![Img](./media/bottom1.png)

#### 4.2.3.2 Komponentenwissen

![Img](./media/2top.png)

**Microbit Lautsprecher**

![Img](./media/j901.png)

Das micro:bit-Board verfügt über einen eingebauten Lautsprecher, mit dem man Geräusche wie Kichern, Begrüßungen, Gähnen oder Ausdruck von Traurigkeit erzeugen kann oder sogar ein Lied komponieren. Durch Programmierung kann er zudem einzelne Töne, Melodien und Rhythmen oder vollständige musikalische Kompositionen erzeugen, z. B. das Lied *Twinkle Twinkle Little Star*.

![Img](./media/2bottom.png)

#### 4.2.3.3 Benötigte Teile

| **micro:bit V2 board** (selbst bereitgestellt) ×1 | **micro:bit Smart Gamepad** (zusammengebaut) ×1 | **AAA-Batterie** (selbst bereitgestellt) ×4 |
| :--: | :--: | :--: |
| ![Img](./media/microbitV2.png)|  ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |

#### 4.2.3.4 Ablauf des Codes

![Img](./media/3009.png)

#### 4.2.3.5 Testcode

⚠️ **Beachten Sie, dass die Empfindlichkeit des Joysticks nach Ihren Bedürfnissen angepasst werden kann.**

**Vollständiger Code:**

![Img](./media/3008.png)

![Img](./media/line1.png)

**Kurze Erklärung:**

① Initialisieren Sie die micro:bit LED-Matrix so, dass sie ![Img](./media/3004.png) anzeigt.

![Img](./media/3005.png)

② Bestimmen Sie die Richtung der Joystick-Bewegung; spielen Sie im Hintergrund für eine halbe Schlagdauer den entsprechenden Ton, und die LED-Matrix zeigt die entsprechende Zahl an.

![Img](./media/3006.png)

③ Prüfen Sie, ob eine Taste gedrückt wird; spielen Sie im Hintergrund für eine halbe Schlagdauer den entsprechenden Ton, und die LED-Matrix zeigt die entsprechende Zahl an.

![Img](./media/3007.png)


#### 4.2.3.6 Testergebnis

![Img](./media/4top.png)

Nachdem Sie den Code aufgespielt haben, stecken Sie das micro:bit-Board in den Schacht des Gamepads (**Batterien eingelegt**), und schalten Sie den Schalter darauf auf „ON“. Die LED-Matrix zeigt zunächst „![Img](./media/3004.png)“ an.

Wenn Sie den Joystick nach rechts bewegen, ertönt "Do (Ton: mittleres C)" und das Display zeigt "1"; nach links ertönt "Re (Ton D)" mit "2"; nach oben "Mi (Ton E)" mit "3"; nach unten "Fa (Ton F)" mit "4". Drücken Sie die Taste C, ertönt "Sol (Ton G)" mit "5"; D ergibt "La (Ton A)" mit "6"; E ergibt "Si (Ton B)" mit "7"; und bei Druck auf F ertönt ein höheres "Do" und das Display springt wieder auf "1".

Sie haben das einfache elektronische Klavier gebaut!

![Img](./media/3010.gif)

<span style="color: rgb(0, 209, 0);">**Tipp:** Wenn das Board nicht reagiert, drücken Sie bitte die Reset-Taste auf der Rückseite des micro:bit-Boards.</span>

![Img](./media/4bottom.png)