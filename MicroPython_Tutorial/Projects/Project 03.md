### 5.2.3 Einfaches elektronisches Klavier

#### 5.2.3.1 Übersicht

![Img](./media/top1.png)

In diesem Projekt steuern wir den micro:bit-Lautsprecher, um verschiedene Töne durch Betätigen des Joysticks und Drücken der Tasten zu spielen. Gleichzeitig zeigt die integrierte LED-Matrix entsprechende Zahlen an.

Wenn Sie den Joystick nach rechts drehen, ertönt „Do (Ton C)“ und die Anzeige zeigt „1“; wenn Sie ihn nach links drehen, ertönt „Re (Ton D)“ mit „2“; wenn Sie ihn nach oben drehen, ertönt „Mi (Ton E)“ mit „3“; wenn Sie ihn nach unten drehen, ertönt „Fa (Ton F)“ mit „4“. Das Drücken der Taste C erzeugt „Sol (Ton G)“ mit „5“, das Drücken von D erzeugt „La (Ton A)“ mit „6“, E erzeugt „Si (Ton B)“ mit „7“, und das Drücken von F erzeugt ein höheres „Do (Sharp)“, während die Anzeige wieder auf „1“ wechselt. Es gibt eine schöne Synchronisation von Joystick, Tasten, Tönen und Anzeige.

![Img](./media/bottom1.png)

#### 5.2.3.2 Komponentenwissen

![Img](./media/2top.png)

**Microbit-Lautsprecher**

![Img](./media/j901.png)

Das micro:bit-Board verfügt über einen eingebauten Lautsprecher zur Klangerzeugung, wie Kichern, Begrüßungen, Gähnen oder Ausdruck von Traurigkeit, oder sogar zum Komponieren eines Liedes. Durch Programmierung kann es sogar einzelne Noten, Melodien und Rhythmen oder sogar musikalische Kompositionen, wie das Lied *Ode an die Freude*, erzeugen.

![Img](./media/2bottom.png)

#### 5.2.3.3 Benötigte Teile

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 Board** (selbst mitgebracht) ×1 | **micro:bit Smart Gamepad** (montiert) ×1 | **AAA Batterie** (selbst mitgebracht) ×4 |

#### 5.2.3.4 Codeablauf

![Img](./media/3009.png)

#### 5.2.3.5 Testcode

⚠️ **Beachten Sie, dass die Empfindlichkeit des Joysticks je nach Bedarf angepasst werden kann.**

**Vollständiger Code:**

```python
# import related libraries
from microbit import *
import music

# --- Configuration Constants ---
# Joystick and Button Mapping (Pin, Note, Display Character)
# For Joystick: (Pin, Threshold, Note, Character)
JOY_MAP = [(pin2, 600, 'c4:2', '1'), (pin2, 400, 'd4:2', '2'), 
           (pin1, 600, 'e4:2', '3'), (pin1, 400, 'f4:2', '4')]

# For Buttons: (Pin, Note, Character)
BTN_MAP = [(pin15, 'g4:2', '5'), (pin16, 'a4:2', '6'), 
           (pin13, 'b4:2', '7'), (pin14, 'c5:2', '1')]

# ==================== Initialization ====================
# Enable internal pull-up resistors for all button pins
for p, n, d in BTN_MAP: 
    p.set_pull(p.PULL_UP)

# Visual feedback on startup
display.show(Image.MUSIC_CROTCHET)

# ==================== Main Loop ====================
while True:
    # 1. Joystick Logic: Iterate through map and check analog thresholds
    for pin, thresh, note, disp in JOY_MAP:
        val = pin.read_analog()
        # Trigger if value exceeds high threshold or drops below low threshold
        if (thresh == 600 and val > 600) or (thresh == 400 and val < 400):
            music.play(note, wait=False)
            display.show(disp)

    # 2. Button Logic: Check for digital presses (Active Low)
    for pin, note, disp in BTN_MAP:
        if pin.read_digital() == 0: 
            music.play(note, wait=False)
            display.show(disp)
            # Debounce/Stutter protection: Wait until the button is released
            while pin.read_digital() == 0: 
                sleep(10)

    # Small delay to maintain system stability and reduce CPU load
    sleep(20)

```
![Img](./media/line1.png)

**Kurze Erklärung:**

① Bibliotheken importieren, Konstanten konfigurieren und initialisieren.

Es importiert die `microbit`-Bibliothek, um auf die Hardwarefunktionen des Micro:bit zuzugreifen, und `music` zum Abspielen von Musik. Anschließend werden zwei wesentliche Listen von Konfigurationskonstanten definiert:

*   `JOY_MAP`: Wird zur Konfiguration der Joystick-Zuordnung verwendet. Jedes Tupel enthält die mit dem Joystick verbundenen Pins, Schwellenwerte (z. B. über 600 oder unter 400), die abzuspielende Musiknote (z. B. 'c4:2' ist das zentrale C, das zwei Schläge dauert) und das auf der Micro:bit-LED-Matrix angezeigte Zeichen.
*   `BTN_MAP`: Die Zuordnung zur Konfiguration externer Tasten. Jedes Tupel enthält die mit der Taste verbundenen Pins, die abzuspielenden Musiknoten und die auf der Micro:bit-LED-Matrix angezeigten Zeichen.

Während der Initialisierung scannt das Programm alle Tasten-Pins in `BTN_MAP` und stellt deren interne Pull-up-Widerstände (`p.PULL_UP`) ein. Dies stellt sicher, dass die Pins einen hohen Pegel beibehalten, wenn die Taste nicht gedrückt wird, und auf einen niedrigen Pegel fallen, wenn sie gedrückt wird.

Schließlich erscheint ein Musiknotensymbol (`Image.MUSIC_CROTCHET`) auf der LED-Matrix.

```python
# import related libraries
from microbit import *
import music

# --- Configuration Constants ---
# Joystick and Button Mapping (Pin, Note, Display Character)
# For Joystick: (Pin, Threshold, Note, Character)
JOY_MAP = [(pin2, 600, 'c4:2', '1'), (pin2, 400, 'd4:2', '2'), 
           (pin1, 600, 'e4:2', '3'), (pin1, 400, 'f4:2', '4')]

# For Buttons: (Pin, Note, Character)
BTN_MAP = [(pin15, 'g4:2', '5'), (pin16, 'a4:2', '6'), 
           (pin13, 'b4:2', '7'), (pin14, 'c5:2', '1')]

# ==================== Initialization ====================
# Enable internal pull-up resistors for all button pins
for p, n, d in BTN_MAP: 
    p.set_pull(p.PULL_UP)

# Visual feedback on startup
display.show(Image.MUSIC_CROTCHET)
```

② Hauptschleife: Joystick-Eingaben verarbeiten.

Es ist eine Endlosschleife (`while True`). Sie verarbeitet zuerst die Joystick-Eingabe, indem sie die `JOY_MAP`-Liste durchläuft und jede Joystick-Richtung überprüft. Für jeden Joystick-Pin liest sie dessen Analogwert (`pin.read_analog()`).

Der Joystick wird dann basierend auf einem voreingestellten Schwellenwert (`thresh`) als aktiviert bestimmt: Wenn der Schwellenwert 600 beträgt und der aktuelle Analogwert 600 überschreitet (Joystick gedrückt), oder wenn der Schwellenwert 400 beträgt und der aktuelle Analogwert unter 400 liegt (in die entgegengesetzte Richtung gedrückt), spielt es die entsprechende Musiknote (`music.play(note, wait=False)`), wobei `wait=False` sicherstellt, dass die Musikwiedergabe die Hauptschleife nicht blockiert, was die gleichzeitige Erkennung anderer Eingaben ermöglicht.

Und die Micro:bit-LED-Anzeige zeigt das dem Joystick entsprechende Zeichen an.

```python
# ==================== Main Loop ====================
while True:
    # 1. Joystick Logic: Iterate through map and check analog thresholds
    for pin, thresh, note, disp in JOY_MAP:
        val = pin.read_analog()
        # Trigger if value exceeds high threshold or drops below low threshold
        if (thresh == 600 and val > 600) or (thresh == 400 and val < 400):
            music.play(note, wait=False)
            display.show(disp)
```

③ Hauptschleife: Tasten-Eingaben verarbeiten.

Nach der Joystick-Eingabe sind nun die externen Tasten-Eingaben an der Reihe. Es durchläuft jede Taste in der `BTN_MAP`-Liste. Für jeden Tasten-Pin überprüft es, ob sein digitaler Lesewert `0` ist (`pin.read_digital() == 0`, bedeutet Taste gedrückt). Wenn die Taste gedrückt wird, ist der Pin aufgrund seines Pull-up-Widerstands auf niedrigem Pegel, das Programm spielt die entsprechende Musiknote (`music.play(note, wait=False)`) und zeigt das Zeichen auf der Micro:bit-LED-Matrix an.

Um Tastenprellen oder mehrfache Erkennungen eines einzelnen Tastendrucks zu verhindern, gibt es eine `while`-Schleife, die wartet, bis die aktuelle Taste losgelassen wird (`while pin.read_digital() == 0: sleep(10)`). Diese Wartezeit blockiert das Programm vorübergehend, bis die Taste losgelassen wird.

```python
    # 2. Button Logic: Check for digital presses (Active Low)
    for pin, note, disp in BTN_MAP:
        if pin.read_digital() == 0: 
            music.play(note, wait=False)
            display.show(disp)
            # Debounce/Stutter protection: Wait until the button is released
            while pin.read_digital() == 0: 
                sleep(10)
```

④ Hauptschleife: Schleifenverzögerung.

Nach allen Eingabeerkennungen pausiert das Programm für 20 Millisekunden (`sleep(20`), um das System zu stabilisieren, die CPU-Last zu reduzieren und ein Zeitintervall für die nächste Schleifen-Eingabeerkennung bereitzustellen.

```python
    # Small delay to maintain system stability and reduce CPU load
    sleep(20)
```

#### 5.2.3.6 Testergebnis

![Img](./media/4top.png)

Nach dem Brennen des Codes stecken Sie das micro:bit-Board in den Steckplatz des Gamepads (**Batterien eingelegt**) und schalten Sie den Schalter auf „ON“. Die LED-Matrix zeigt zuerst „![Img](./media/3004.png)“ an.

Wenn Sie den Joystick nach rechts drehen, ertönt „Do (Ton C)“ und die Anzeige zeigt „1“; wenn Sie ihn nach links drehen, ertönt „Re (Ton D)“ mit „2“; wenn Sie ihn nach oben drehen, ertönt „Mi (Ton E)“ mit „3“; wenn Sie ihn nach unten drehen, ertönt „Fa (Ton F)“ mit „4“. Das Drücken der Taste C erzeugt „Sol (Ton G)“ mit „5“, das Drücken von D erzeugt „La (Ton A)“ mit „6“, E erzeugt „Si (Ton B)“ mit „7“, und das Drücken von F erzeugt ein höheres „Do (Sharp)“, während die Anzeige wieder auf „1“ wechselt.

Sie haben das einfache elektronische Klavier gebaut!

![Img](./media/3010.gif)

<span style="color: rgb(0, 209, 0);">**Tipp:** Wenn das Board nicht reagiert, drücken Sie bitte die Reset-Taste auf der Rückseite des micro:bit-Boards.</span>

![Img](./media/4bottom.png)
