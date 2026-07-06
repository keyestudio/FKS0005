### 4.2.1 Direction Indicator

#### 4.2.1.1 Overview

![Img](./media/top1.png)

Wenn Sie den Joystick kippen, zeigt die Punktmatrix in Echtzeit Pfeile in die entsprechende Richtung an: links, rechts, oben, unten, und bietet Ihnen damit eine klare Richtungsreferenz.

![Img](./media/bottom1.png)

#### 4.2.1.2 Component Knowledge

![Img](./media/2top.png)

**Micro:bit-Punktmatrix:**

![Img](./media/1001.png)

Die LED-Punktmatrix des micro:bit Boards besteht aus insgesamt 25 Leuchtdioden, jeweils in Gruppen zu 5, entsprechend den Achsen X und Y, und bildet so eine 5×5-Matrix. Jede einzelne LED befindet sich an der Schnittstelle der Zeile (X) und der Spalte (Y). Wir können einzelne LEDs durch Festlegen der Koordinatenpunkte ansteuern.

**Joystick:**

| ![Img](./media/1002.png)| ![Img](./media/1003.png)  |
| :--: | :--: |
| Reales Produkt | Schaltbild |

Die innere Kernstruktur dieses Joysticks besteht aus zwei einstellbaren Widerständen (Potentiometern) mit je einem Widerstandswert von 10KΩ.

Er erkennt die Richtung (und Auslenkung) des Drucks über den analogen ADC-Pin des Mikrocontrollers und liefert die entsprechenden analogen elektrischen Signale der jeweiligen Dimension. Bei der tatsächlichen Signalabtastung kann festgestellt werden, dass sich der Joystick in einem neutralen (ruhenden) Zustand ohne aktive Betätigung befindet, wenn die analogen Werte der Joystick-Achsen X und Y im Bereich von 450~600 liegen.

![Img](./media/2bottom.png)

#### 4.2.1.3 Required Parts

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png)  |![Img](./media/dianchi.png)|
| :--: | :--: | :--: |
| **micro:bit V2 board** (selbst bereitgestellt) ×1 | **micro:bit Smart Gamepad** (zusammengebaut) ×1 | **AAA-Batterie** (selbst bereitgestellt) ×4 |


#### 4.2.1.4 Code Flow

![Img](./media/1008.png)

#### 4.2.1.5 Test Code

⚠️ **Bitte beachten Sie, dass die folgenden Codes die Makecode-Bibliotheken des Gamepad enthalten (die Vorgehensweise zum Hinzufügen von Bibliotheken wurde zuvor beschrieben). Die Empfindlichkeit des Joysticks kann nach Ihren Bedürfnissen angepasst werden.**

**Vollständiger Code:**

![Img](./media/1004.png)


![Img](./media/line1.png)

**Kurze Erläuterung:**

① Initialisieren Sie die LED-Matrix, damit sie ![Img](./media/1006.png) anzeigt.


![Img](./media/1005.png)


② Lesen Sie die Werte der Achsen X und Y, um die Betätigungsrichtung zu bestimmen. Wird eine Richtung erkannt, zeigt die Matrix den entsprechenden Pfeil. Andernfalls wird ![Img](./media/1006.png) angezeigt.

![Img](./media/1007.png)


#### 4.2.1.6 Test Result

![Img](./media/4top.png)

Nach dem Aufspielen des Codes stecken Sie das micro:bit Board in den Slot des Gamepads (**Batterien eingelegt**) und schalten dieses auf „ON“.

Wenn Sie den Joystick des Gamepads betätigen, sehen Sie die entsprechenden Pfeile auf der Matrix. Wenn Sie den Finger anheben, sodass der Joystick in die Mitte zurückkehrt, erscheint ein Haus-Symbol auf der Matrix.

![Img](./media/1009.gif)

<span style="color: rgb(0, 209, 0);">**Tipp:** Wenn auf dem Board keine Reaktion erfolgt, drücken Sie bitte die Reset-Taste auf der Rückseite des micro:bit Boards.</span>

![Img](./media/4bottom.png)