### 4.2.9 Micro:bit Gamepad gesteuertes 4WD Mecanum Roboterauto

#### 4.2.9.1 Übersicht

![Img](./media/top1.png)
In diesem Projekt steuern wir ein 4WD Mecanum Robot Car mit einer Gamepad-Steuerplatine und einem Micro:bit board. Der Joystick ermöglicht es dem Auto, vorwärts, rückwärts, links und rechts zu fahren; die C-Taste bewegt das Auto seitlich nach links, die D-Taste seitlich nach rechts, die E-Taste beschleunigt und die F-Taste verzögert (mit einem Geschwindigkeitsbereich von 20–95). Wenn keine Bedienung erfolgt, bleibt das Auto stehen.

![Img](./media/bottom1.png)

#### 4.2.9.2 Benötigte Teile

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 board** (selbst mitzubringen) ×1 | **micro:bit Smart Gamepad** (montiert) ×1 |**AAA battery** (selbst mitzubringen) ×4 |
| ![Img](./media/che.png) | ![Img](./media/18650.png) ||
| **KS4034 kit**(selbst mitzubringen) ×1 | **18650 battery**(selbst mitzubringen) ×2 ||

Für detaillierte Informationen zum 4WD Mecanum Robot Car**(KS4034)** besuchen Sie bitte [hier](https://docs.keyestudio.com/projects/KS4034/en/latest/).
#### 4.2.9.3 Schaltplan

Bitte beachten Sie die Verdrahtungsanweisungen in der KS4034 Dokumentation für den Anschluss des 4WD Mecanum Robot Car und des Gamepads über radio communication. Es ist keine physische Verkabelung zwischen den beiden erforderlich; beide Geräte kommunizieren drahtlos.

#### 4.2.9.4 Code-Ablauf
⚠️ **Beachten Sie, dass die folgende library beim Programmieren des Autos importiert werden muss: https://github.com/keyestudio2019/mecanum_robot_v2**.

**Code-Ablauf des Gamepads:**

![Img](./media/9001.png)

**Code-Ablauf des Autos:**

![Img](./media/9002.png)

#### 4.2.9.5 Testcode

**Vollständiger Code des Gamepads:**

![Img](./media/9003.png)

![Img](./media/line1.png)

**Kurze Erklärung:**

① Initialisieren Sie die radio group auf 1 mit einer Signalübertragungsstärke von 7; zeigen Sie ein Herzsymbol an und setzen Sie die Variablen SEND_INTERCAL auf 100 und BTN_DEBOUNCE_TIME auf 20.

![Img](./media/9004.png)

② Setzen Sie die Variable currentCmd (Anweisungs-Inhaltsvariable) auf das Zeichen '0' und weisen Sie die Achsen X und Y Werte des Joysticks den Variablen rockerX bzw. rockerY zu.

![Img](./media/9005.png)

③ Überprüfen Sie, ob der Joystick oder eine Taste eine entsprechende Operation hat. Wenn eine Operation auftritt, setzen Sie die Variable currentCmd (Anweisungs-Inhaltsvariable) auf das entsprechende Zeichen (R/U/L/D/A/B/Z/X); andernfalls bleibt sie unverändert.

![Img](./media/9006.png)

④ Überprüfen Sie, ob currentCmd (Anweisungs-Inhaltsvariable) sich von lastCmd (speichert den vorherigen Anweisungsinhalt) unterscheidet. Wenn ja, senden Sie currentCmd, setzen Sie lastCmd auf currentCmd und warten Sie eine angegebene Verzögerung.

![Img](./media/9007.png)

**Vollständiger Code des Autos:**

![Img](./media/9008.png)

![Img](./media/line1.png)

**Kurze Erklärung:**

① Initialisieren Sie die radio group auf 1 mit einer Signalübertragungsstärke von 7; zeigen Sie ein Herzsymbol an und setzen Sie die Variablen SPEED auf 50, MIN_SPEED auf 20 und MAX_speed auf 95.

![Img](./media/9009.png)

② Empfangen Sie den vom radio gesendeten Befehlswert und speichern Sie den Befehl in der Variable item.

![Img](./media/9010.png)

③ Basierend auf den von item empfangenen Zeichenbefehlen (U/L/D/R/A/B) rufen Sie die entsprechenden Funktionen auf, um das Auto vorwärts, rückwärts, links, rechts, und seitlich links und rechts zu steuern.

![Img](./media/9011.png)

④ Basierend auf dem von item empfangenen Zeichenbefehl (Z/X) wird das Auto entsprechend beschleunigt oder verzögert.

Während der Beschleunigung wird die Geschwindigkeit auf das Minimum von SPEED+5 und MAX_speed gesetzt (um ein Überschreiten von MAX_speed zu verhindern); während der Verzögerung wird die Geschwindigkeit auf das Maximum von SPEED-5 und MIN_speed gesetzt (um ein Unterschreiten von MIN_speed zu verhindern).

![Img](./media/9012.png)

⑤ Hier werden sechs Funktionen zur Steuerung der Fahrzeugbewegung definiert:

- car_back steuert alle vier Motoren zum Rückwärtsfahren; 
- car_forward steuert alle vier Motoren zum Vorwärtsfahren; 
- car_left erreicht das Linksabbiegen des Autos, indem die linken Motoren rückwärts und die rechten Motoren vorwärts gedreht werden; 
- car_right erreicht das Rechtsabbiegen, indem die rechten Motoren rückwärts und die linken Motoren vorwärts gedreht werden; 
- car_left_move und car_right_move ermöglichen das seitliche Verschieben nach links und rechts durch koordinierte Rotation der diagonalen Motoren.

Alle Funktionen verwenden die Variable SPEED als Motor-Geschwindigkeitsparameter.

![Img](./media/9013.png)

#### 4.2.9.6 Testergebnis

![Img](./media/4top.png)

Nach dem Brennen des Codes stecken Sie das micro:bit board in den Steckplatz des Gamepads (**Batterien eingelegt**) und schalten Sie es auf „ON“.

Laden Sie diese Codes auf zwei Micro:bit boards, das des Gamepads und das des Autos, hoch und stellen Sie sicher, dass die Batterien ausreichend geladen sind. Stecken Sie die entsprechenden Micro:bit boards in das Gamepad und das Auto und schalten Sie beide auf "ON". 

Jetzt können Sie das Auto mit dem Gamepad steuern: Drücken Sie den Joystick nach oben, und das Auto fährt vorwärts; drücken Sie ihn nach unten, um rückwärts zu fahren; links dreht es nach links, und rechts dreht es nach rechts. Wir können das Auto auch beschleunigen (Taste E drücken)/verzögern (Taste F drücken), seitlich nach links (C) und seitlich nach rechts (D) bewegen. Beachten Sie, dass der Geschwindigkeitsbereich 20–95 beträgt.

![Img](./media/9000.gif)

<span style="color: rgb(0, 209, 0);">**Tipp:** Wenn das Board nicht reagiert, drücken Sie bitte die Reset-Taste auf der Rückseite des micro:bit board.</span>

![Img](./media/4bottom.png)
