### 5.2.1 Richtungsanzeige

#### 5.2.1.1 Übersicht

![Img](./media/top1.png)

Wenn Sie den Joystick betätigen, zeigt die Punktmatrix in Echtzeit Pfeile in der entsprechenden Richtung an: links, rechts, oben, unten, was Ihnen eine klare Richtungsorientierung gibt.

![Img](./media/bottom1.png)

#### 5.2.1.2 Komponentenwissen

![Img](./media/2top.png)

**Micro:bit Punktmatrix:**

![Img](./media//1001.png)

Die LED-Punktmatrix des micro:bit-Boards besteht aus insgesamt 25 Leuchtdioden, einer Gruppe von 5, die der X- und Y-Achse entsprechen und eine 5×5-Matrix bilden. Jede befindet sich am Schnittpunkt der Reihe (X) und der Spalte (Y). Wir können eine oder mehrere davon steuern, indem wir die Koordinatenpunkte festlegen.

**Joystick:**

| ![Img](./media/1002.png)| ![Img](./media//1003.png) |
| :--: | :--: |
| Reales Produkt | Schaltplan |

Die interne Kernstruktur dieses Joysticks besteht aus zwei einstellbaren Widerständen (Potentiometern) mit einem Widerstandswert von jeweils 10KΩ.

Er erkennt Richtungen (und Amplitude) des Drucks über den ADC-Analogpin des Mikrocontrollers, um die analogen elektrischen Signale der entsprechenden Dimension auszugeben. Beim tatsächlichen Signallesen, wenn die analogen Werte der Joystick-X- und Y-Achsen im Bereich von 450~600 erkannt werden, kann davon ausgegangen werden, dass sich der Joystick in einem neutralen (stationären) Zustand ohne aktive Betätigung befindet.

![Img](./media/2bottom.png)

#### 5.2.1.3 Benötigte Teile

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png)|
| :--: | :--: | :--: |
| **micro:bit V2 Board** (selbst mitgebracht) ×1 | **micro:bit Smart Gamepad** (montiert) ×1 | **AAA Batterie** (selbst mitgebracht) ×4 |

#### 5.2.1.4 Codeablauf

![Img](./media/1004.png)


#### 5.2.1.5 Testcode

**Vollständiger Code:**

```Python
# import related libraries
from microbit import *

display.show(Image.HOUSE)

while True:
    #Read the toggle state of the joystick
    x = pin2.read_analog()
    y = pin1.read_analog()
    #Determine the direction in which the joystick is toggled
    if x > 600 and (400 < y < 600):
        display.show(Image.ARROW_E)
    elif x < 400 and (400 < y < 600):
        display.show(Image.ARROW_W)
    elif y > 600 and (400 < x < 600):
        display.show(Image.ARROW_S)
    elif y < 400 and (400 < x < 600):
        display.show(Image.ARROW_N)
    else:
        display.show(Image.HOUSE)
```

![Img](./media/line1.png)

**Kurze Erklärung:**

① Importieren Sie die Bibliothek und zeigen Sie das Startbild an.

Zuerst wird die `microbit`-Bibliothek importiert, die eine notwendige Kernbibliothek von Micro:bit auf MicroPython ist. Sie bietet vollen Zugriff auf die Micro:bit-Hardware (einschließlich LED-Anzeigen und Pins). Nach dem Import wird ein Haussymbol (`Image.HOUSE`) auf der Matrix als Startzustand / Standby-Bildschirm angezeigt.

```python
# import related libraries
from microbit import *

display.show(Image.HOUSE)
```
② Schleife: Lesen Sie den Analogwert des Joysticks.

Das Programm tritt in eine Endlosschleife (`while True`) ein. Zu Beginn der Schleife liest es die analogen Eingangswerte von `pin2` und `pin1`, typischerweise die X-Achse (links-rechts) und die Y-Achse (auf-ab) des Joysticks.

`read_analog()` gibt einen ganzzahligen Wert zwischen 0 und 1023 zurück, der die Position des Joysticks entlang dieser Achse darstellt. Er liegt normalerweise nahe bei 511–512, wenn der Joystick zentriert ist.

```python
while True:
    #Read the toggle state of the joystick
    x = pin2.read_analog()
    y = pin1.read_analog()
```
③ Bestimmen Sie die Richtung des Joysticks und zeigen Sie den entsprechenden Pfeil an.

Hier wird die Bewegungsrichtung des Joysticks basierend auf den analogen Werten `x` und `y` bestimmt. Wir legen Schwellenwerte (400 und 600) fest, um zu bestimmen, ob der Joystick betätigt wird.

*   [ `x` > 600 , 400 < `y` < 600 ] : (an der zentralen Y-Achse) der Joystick ist rechts und zeigt den nach Osten gerichteten Pfeil (`Image.ARROW_E`) an.
*   [ `x` < 400 , 400 < `y` < 600 ] : der Joystick ist links und zeigt den nach Westen gerichteten Pfeil (`Image.ARROW_W`) an.
*   [ `y` > 600 , 400 < `x` < 600 ] : der Joystick wird nach unten gedrückt und zeigt den nach Süden gerichteten Pfeil (`Image.ARROW_S`) an.
*   [ `y` < 400 ,400 < `x` < 600 ] : der Joystick wird nach oben gedrückt und zeigt den nach Norden gerichteten Pfeil (`Image.ARROW_N`) an.

```python
    #Determine the direction in which the joystick is toggled
    if x > 600 and (400 < y < 600):
        display.show(Image.ARROW_E)
    elif x < 400 and (400 < y < 600):
        display.show(Image.ARROW_W)
    elif y > 600 and (400 < x < 600):
        display.show(Image.ARROW_S)
    elif y < 400 and (400 < x < 600):
        display.show(Image.ARROW_N)
```
④ Das Hausmuster wird angezeigt, wenn der Joystick zentriert ist.

Wenn keine der oben genannten Bedingungen erfüllt ist – das heißt, der Joystick bewegt sich nicht wesentlich in eine Richtung (was typischerweise anzeigt, dass er sich in der Mittelposition befindet) – zeigt der Micro:bit wieder das „Haus“ (`Image.HOUSE`) an, was bedeutet, dass der Joystick stationär ist.

```python
    else:
        display.show(Image.HOUSE)
```

#### 5.2.1.6 Testergebnis

![Img](./media/4top.png)

Nach dem Brennen des Codes stecken Sie das micro:bit-Board in den Steckplatz des Gamepads (**Batterien eingelegt**) und schalten Sie den Schalter auf „ON“.

Wenn Sie den Joystick des Gamepads drücken, sehen Sie die entsprechenden Pfeile auf der Matrix. Wenn Sie ihn in die Mitte zurückbringen, erscheint ein Haussymbol auf der Matrix.

![Img](./media/1009.gif)

<span style="color: rgb(0, 209, 0);">**Tipp:** Wenn das Board nicht reagiert, drücken Sie bitte die Reset-Taste auf der Rückseite des micro:bit-Boards.</span>

![Img](./media/4bottom.png)
