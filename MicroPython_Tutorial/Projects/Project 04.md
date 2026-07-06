### 5.2.4 Musik-Player

#### 5.2.4.1 Übersicht

![Img](./media/top1.png)

Hier bauen wir einen Musik-Player, der über den eingebauten Summer auf dem micro:bit-Board Töne erzeugt (spielt keine Vokalmusik ab). Er verfügt über eine Bibliothek von 20 kurzen Titeln und unterstützt sowohl die sequentielle als auch die zufällige Wiedergabe.

Im sequentiellen Modus wechseln die Tasten C (vorheriger Titel) oder E (nächster Titel) die Titel gemäß einer voreingestellten Reihenfolge, bis das Ende der Liste erreicht ist; im Zufallsmodus wählt jeder Tastendruck einen Titel zufällig aus den 20 Klängen aus, wobei die Farblichter blinken, und wenn ein Lied beendet ist, stoppt es sofort.

In der Zwischenzeit zeigt die micro:bit-LED-Matrix den aktuellen Wiedergabemodus in Echtzeit an.

![Img](./media/bottom1.png)

#### 5.2.4.2 Benötigte Teile

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 Board** (selbst mitgebracht) ×1 | **micro:bit Smart Gamepad** (montiert) ×1 | **AAA Batterie** (selbst mitgebracht) ×4 |

#### 5.2.4.3 Codeablauf

![Img](./media/4001.png)

#### 5.2.4.4 Testcode

**Vollständiger Code:**

```python
# import related libraries
from microbit import *
import music, neopixel, random

# --- Configuration & Data ---
vol = 50
mode = 0  # 0: Manual, 1: Random
idx = 0
last_idx = -1
hue = 0
strip = neopixel.NeoPixel(pin8, 4)
melodies = ["DADADADUM", "ENTERTAINER", "PRELUDE", "ODE", "NYAN", "RINGTONE", "FUNK", "BLUES", 
            "BIRTHDAY", "WEDDING", "FUNERAL", "PUNCHLINE", "BADDY", "CHASE", "BA_DING", 
            "WAWAWAWAA", "JUMP_UP", "JUMP_DOWN", "POWER_UP", "POWER_DOWN"]

# Pin Initialization (P13-P16)
btns = [pin13, pin14, pin15, pin16]
for p in btns: p.set_pull(p.PULL_UP)
set_volume(vol)

def get_rgb(h):
    """ Simplified HSL to RGB logic """
    h %= 360
    pos = h // 60
    f = (h % 60) / 60.0
    v = 76 # 255 * 0.3 (Brightness coefficient)
    up, down = int(v * f), int(v * (1 - f))
    res = [(v, up, 0), (down, v, 0), (0, v, up), (0, down, v), (up, 0, v), (v, 0, down)]
    return res[pos]

# State tracking (for debouncing)
last_states = [1] * 4
last_press_t = 0

while True:
    curr_t = running_time()
    
    # 1. Volume Control (Buttons A/B)
    if button_a.was_pressed(): vol = min(250, vol + 10); set_volume(vol)
    if button_b.was_pressed(): vol = max(20, vol - 10); set_volume(vol)

    # 2. Joystick/Button Input Detection (with debouncing)
    for i, p in enumerate(btns):
        if v == 0 and last_states[i] == 1 and (curr_t - last_press_t > 50):
            last_press_t = curr_t
            if i == 3: mode = 0; sleep(500)     # P16: Manual Mode
            elif i == 1: mode = 1; sleep(500)   # P14: Random Mode
            elif i == 2: # P15: Next track / Random track
                idx = random.randint(0, 19) if mode else (idx + 1) % 20
            elif i == 0: # P13: Previous track / Random track
                idx = random.randint(0, 19) if mode else (idx - 1) % 20
        last_states[i] = v

    # 3. Music Playback Logic
    if idx != last_idx:
        music.stop()
        try:
            music.play(getattr(music, melodies[idx]), wait=False)
            last_idx = idx
        except: pass

    # 4. Lighting & Display Updates
    hue = (hue + 1) % 360
    strip.fill(get_rgb(hue))
    strip.show()
    
    # Show Mode Icon: "X" for Random, Arrow for Manual
    display.show(Image("00000:99099:00900:99099:00000") if mode else Image.ARROW_E)
    
    sleep(10)

```
![Img](./media/line1.png)

**Kurze Erklärung:**

① Bibliotheken importieren, Konstanten konfigurieren und initialisieren.

Es importiert zuerst die `microbit`-Bibliothek, um auf die Kernfunktionen des Micro:bit zuzugreifen, `music` zum Abspielen eingebauter Musik, `neopixel` zur Steuerung des NeoPixel-LED-Streifens und `random` zur Generierung von Zufallszahlen.

Anschließend werden eine Reihe globaler Variablen und Konstanten definiert: `vol` setzt die anfängliche Lautstärke auf 50; `mode` steuert den Musikwiedergabemodus (0 für manuelle Auswahl, 1 für zufällige Wiedergabe); `idx` speichert den aktuellen Musikindex; verfolgt den vorherigen Wiedergabeindex, um doppelte Wiedergaben zu vermeiden; `hue` steuert die Farbe des NeoPixel-Streifens; `strip` initialisiert einen NeoPixel-Streifen, der mit `pin8` von vier LEDs verbunden ist; und `melodies` listet alle MicroPython `music`-Titel auf.

Als Nächstes definiert die `btns`-Liste die vier externen Tasten-Pins von `pin13` bis `pin16` und weist ihnen in einer Schleife interne Pull-up-Widerstände (`p.PULL_UP`) zu – was zu High-Level-Pins führt, wenn die Tasten losgelassen werden, und Low-Level-Pins, wenn sie gedrückt werden.

`set_volume (vol)` setzt die Lautstärke auf ihren Standardwert.

```python
# import related libraries
from microbit import *
import music, neopixel, random

# --- Configuration & Data ---
vol = 50
mode = 0  # 0: Manual, 1: Random
idx = 0
last_idx = -1
hue = 0
strip = neopixel.NeoPixel(pin8, 4)
melodies = ["DADADADUM", "ENTERTAINER", "PRELUDE", "ODE", "NYAN", "RINGTONE", "FUNK", "BLUES", 
            "BIRTHDAY", "WEDDING", "FUNERAL", "PUNCHLINE", "BADDY", "CHASE", "BA_DING", 
            "WAWAWAWAA", "JUMP_UP", "JUMP_DOWN", "POWER_UP", "POWER_DOWN"]

# Pin Initialization (P13-P16)
btns = [pin13, pin14, pin15, pin16]
for p in btns: p.set_pull(p.PULL_UP)
set_volume(vol)
```

② Farbkonvertierungsfunktion und Stabilisierungsvariable.

`get_rgb(h)` ist eine vereinfachte HSL-zu-RGB-Farbkonvertierungsfunktion (Farbton, Sättigung, Helligkeit). Sie akzeptiert einen Farbtonwert `h` (0–359) und konvertiert ihn in ein RGB-Triplett. Die Helligkeit `v` ist auf 76 festgelegt (ungefähr 255 × 0,3, entsprechend dem `BRIGHTNESS`-Koeffizienten). Diese Funktion erleichtert die Erzeugung von Regenbogenfarben basierend auf dem Farbtonwert.

Die `last_states`-Liste speichert die vorherigen Zustände der vier Tasten, die anfänglich alle auf 1 (High-Level für nicht gedrückt) gesetzt sind. `last_press_t` zeichnet die Zeit des letzten Tastendrucks auf. Zusammen implementieren diese Variablen eine Software-Entprellung, um mehrere Erkennungen eines einzelnen Tastendrucks zu verhindern.

```python
def get_rgb(h):
    """ Simplified HSL to RGB logic """
    h %= 360
    pos = h // 60
    f = (h % 60) / 60.0
    v = 76 # 255 * 0.3 (Brightness coefficient)
    up, down = int(v * f), int(v * (1 - f))
    res = [(v, up, 0), (down, v, 0), (0, v, up), (0, down, v), (up, 0, v), (v, 0, down)]
    return res[pos]

# State tracking (for debouncing)
last_states = [1] * 4
last_press_t = 0
```

③ Hauptschleife: Lautstärkeregelung.

Es gibt eine Endlosschleife (`while True`), die die aktuelle Laufzeit `curr_t` abruft. Dann verarbeitet sie die Tasten A und B auf dem Micro:bit-Board:

*   Wenn `button_a` gedrückt wird (`button_a.was_pressed()`), erhöht sich die Lautstärke `vol` um 10, überschreitet aber nicht 250. `set_volume(vol)` wird anschließend aufgerufen, um die Systemlautstärke zu aktualisieren.
*   Wenn `button_b` gedrückt wird (`button_b.was_pressed()`), verringert sich `vol` um 10, bleibt aber nicht unter 20. `set_volume(vol)` wird anschließend aufgerufen, um die Systemlautstärke zu aktualisieren.

`was_pressed()` gibt nur einmal `True` zurück, wenn die Taste von einem nicht gedrückten in einen gedrückten Zustand übergeht, was eine inhärente Entprellung bietet.

```python
while True:
    curr_t = running_time()
    
    # 1. Volume Control (Buttons A/B)
    if button_a.was_pressed(): vol = min(250, vol + 10); set_volume(vol)
    if button_b.was_pressed(): vol = max(20, vol - 10); set_volume(vol)
```

④ Hauptschleife: Tasten-Eingabeerkennung und Moduswechsel.

Es durchläuft die vier externen Tasten (`pin13` bis `pin16`) in der `btns`-Liste und erkennt deren gedrückte Zustände. Die Taste wird nur dann reagiert, wenn sie von High (nicht gedrückt) auf Low (gedrückt) wechselt und seit dem letzten gültigen Tastendruck mehr als 50 Millisekunden vergangen sind.

*   Wenn `pin16` gedrückt wird (`i == 3`), wird `mode` = 0 (manueller Modus) und pausiert für 500 ms.
*   Wenn `pin14` gedrückt wird (`i == 1`), wird `mode` = 1 (Zufallsmodus) und pausiert für 500 ms.
*   Wenn `pin15` gedrückt wird (`i == 2`), wird der Musikindex `idx` entsprechend dem aktuellen Muster aktualisiert: Im Zufallsmodus wird eine Musik zufällig ausgewählt; im manuellen Modus wird die nächste Musik abgespielt.
*   Wenn `pin13` gedrückt wird (`i == 0`), wird der Musikindex `idx` entsprechend dem aktuellen Muster aktualisiert: Im Zufallsmodus wird eine Musik zufällig ausgewählt; im manuellen Modus wird die vorherige Musik abgespielt.

Am Ende jeder Schleife aktualisiert `last_states[i] = v` den aktuellen Status der Taste zur Vorbereitung auf die nächste Stabilisierungsprüfung.

```python
    # 2. Joystick/Button Input Detection (with debouncing)
    for i, p in enumerate(btns):
        v = p.read_digital()
        if v == 0 and last_states[i] == 1 and (curr_t - last_press_t > 50):
            last_press_t = curr_t
            if i == 3: mode = 0; sleep(500)     # P16: Manual Mode
            elif i == 1: mode = 1; sleep(500)   # P14: Random Mode
            elif i == 2: # P15: Next track / Random track
                idx = random.randint(0, 19) if mode else (idx + 1) % 20
            elif i == 0: # P13: Previous track / Random track
                idx = random.randint(0, 19) if mode else (idx - 1) % 20
        last_states[i] = v
```

⑤ Hauptschleife: Musikwiedergabelogik.

Es steuert die Wiedergabe der Musik, indem es überprüft, ob der aktuelle Musikindex `idx` sich vom letzten `last_idx` unterscheidet. Wenn ja, muss die Musik gewechselt werden:

1.  `music.stop()` stoppt die aktuell spielende Musik.
2.  `music.play(getattr(music, melodies[idx]), wait=False)` versucht, eine neue Musik abzuspielen. `getattr(music, melodies[idx])` ruft dynamisch die Musikdaten des entsprechenden Namens in `music` ab, und `wait=False` stellt sicher, dass die Musikwiedergabe die Hauptschleife nicht blockiert.
3.  Wenn die Wiedergabe erfolgreich ist, aktualisieren Sie `last_idx = idx`.
4.  `try...except` fängt potenzielle Fehler ab; zum Beispiel könnten ungültige Musiktitel in der `melodies`-Liste vorhanden sein.

```python
    # 3. Music Playback Logic
    if idx != last_idx:
        music.stop()
        try:
            music.play(getattr(music, melodies[idx]), wait=False)
            last_idx = idx
        except: pass
```

⑥ Hauptschleife: Licht- und Display-Updates.

Hier ist ein Update der Farbe des NeoPixel-Streifens und der Anzeige der Micro:bit-LED-Matrix:

1.  `hue = (hue + 1) % 360` erhöht `hue` kontinuierlich, um es zwischen 0 und 359 zu zyklisieren, für ein Regenbogen-Verlaufslicht.
2.  `strip.fill(get_rgb(hue))` verwendet `get_rgb`, um eine Farbe basierend auf dem aktuellen `hue` zu erzeugen und den gesamten NeoPixel-Streifen mit dieser Farbe zu füllen.
3.  `strip.show()` sendet die aktualisierte Farbe zur Anzeige an den NeoPixel-Streifen.
4.  `display.show(...)` zeigt die Anzeige je nach aktuellem `mode` an. `mode` = 1 (zufällig): zeigt ein benutzerdefiniertes „X“; `mode` = 0 (manuell), zeigt einen Pfeil nach rechts (`Image.ARROW_E`).

Dann führt `sleep(10)` eine kurze Verzögerung für eine geeignete Ausführungsgeschwindigkeit, eine geringere CPU-Last und einen flüssigeren Effekt ein.

```python
    # 4. Lighting & Display Updates
    hue = (hue + 1) % 360
    strip.fill(get_rgb(hue))
    strip.show()
    
    # Show Mode Icon: "X" for Random, Arrow for Manual
    display.show(Image("00000:99099:00900:99099:00000") if mode else Image.ARROW_E)
    
    sleep(10)
```
#### 5.2.4.5 Testergebnis

![Img](./media/4top.png)

Nach dem Brennen des Codes stecken Sie das micro:bit-Board in den Steckplatz des Gamepads (**Batterien eingelegt**) und schalten Sie den Schalter auf „ON“.

Nach dem Einschalten befindet es sich standardmäßig im sequentiellen Modus und spielt das Lied unter N.O. „0“ ab. Wenn es beendet ist, können Sie C für das letzte Lied oder E für das nächste drücken.

Drücken Sie F, um in den Zufallsmodus zu wechseln. Und Sie können D drücken, um zum sequentiellen Modus zurückzukehren. Im F-Modus wird ein zufälliger Titel aus diesen 20 abgespielt, wenn Sie C/E drücken. Nach Beendigung stoppt es.

Die RGB-Lichter atmen immer vom Einschalten an. In der Zwischenzeit zeigt die micro:bit-LED-Matrix im sequentiellen Modus „![Img](./media/4010.png)“ und im Zufallsmodus „![Img](./media/4011.png)“ an.

Für die Lautstärke drücken Sie A zum Erhöhen und B zum Verringern.

![Img](./media/4015.gif)

<span style="color: rgb(0, 209, 0);">**Tipp:** Wenn das Board nicht reagiert, drücken Sie bitte die Reset-Taste auf der Rückseite des micro:bit-Boards.</span>

![Img](./media/4bottom.png)
