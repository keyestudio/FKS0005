### 5.2.2 Farbenfrohe Lichter

#### 5.2.2.1 Übersicht

![Img](./media/top1.png)

RGB-LEDs sind eine Art von LED-Lichtquellen, die Bilder durch Mischen des Lichts der drei Primärfarben Rot, Grün und Blau erzeugen, deren Schnittpunkt verschiedene Farbtöne hervorbringt. Gängige Methoden umfassen das direkte Mischen der Primärfarben, die Verwendung einer blauen LED in Kombination mit gelbem Phosphor oder den Einsatz einer ultravioletten LED zusammen mit RGB-Phosphor. Im Vergleich zu LEDs, die direkt weißes Licht emittieren, bieten RGB-LEDs eine größere Vielfalt an Farbmischmöglichkeiten, da die drei Primärfarben unabhängig voneinander gesteuert werden können.

In diesem Projekt entspricht jede Taste einem anderen Modus der RGB-LEDs. Wenn Taste C gedrückt wird, blinken die Lichter abwechselnd in der Reihenfolge „Rot, Grün, Blau, Gelb und Lila“; Drücken Sie D, um zu Atemlichtern zu wechseln; Drücken Sie E für fließende Lichter; Drücken Sie F für Lauflicht.

Farbenfrohe Lichterketten für Festdekorationen, Weihnachtsbaumlichter, RGB-Streifen für das tägliche Ambiente, LED-Dekorationslichter in Vergnügungsparks und Einkaufszentren... Dies sind alles gängige Beispiele für Multimodus-Lichter in unserem täglichen Leben.

![Img](./media/bottom1.png)

#### 5.2.2.2 Komponentenwissen

![Img](./media/2top.png)

**SK6812 RGB LED**

| ![Img](./media//2001.png)| ![Img](./media//2002.png)|
| :--: | :--: |
| Reales Produkt | Schaltplan |

Die SK6812 ist eine extern gesteuerte LED-Lichtquelle, die Steuer- und Beleuchtungsschaltungen integriert. Ihr Hauptbestandteil sind 5x5mm oberflächenbeleuchtete LED-Perlen, die jeweils als unabhängiger Pixel fungieren und mehrere Kernschaltungen enthalten: eine intelligente digitale Schnittstellen-Datenlatch-Schaltung, eine Signalformungs- und Verstärkungs-Treiberschaltung, eine Leistungsregelungsschaltung, eine eingebaute Konstantstromschaltung und einen hochpräzisen RC-Oszillator.

Ihre Kommunikation verwendet ein unipolares Null-Rückkehr-Code-Protokoll. Nach dem Einschalt-Reset empfängt jeder Pixel Daten vom Controller über den DIN-Port. Die ersten 24 Bit Daten werden vom anfänglichen Pixel extrahiert und im internen Datenlatch gespeichert, während die restlichen intern geformt und verstärkt werden, bevor sie über den DOUT-Port an nachfolgende Pixel übertragen werden. Mit jedem verarbeiteten Pixel verringert sich die übertragene Signalgröße um 24 Bit.

Auf dem Gamepad befinden sich vier SK6812 RGB-Lichter. Diese unterstützen alle eine 256-stufige Helligkeitsanpassung über ihre roten, grünen und blauen Kanäle, was 256×256×256 Farbkombinationen ermöglicht. Dadurch liefert es vielfältige Lichteffekte wie abwechselndes Blinken, Atemverläufe und Lauflichtanimationen, die intuitivere und lebendigere Interaktionen bieten.

**Taste**

| ![Img](./media//2003.png)| ![Img](./media//2004.png)|
| :--: | :--: |
| Reales Produkt | Schaltplan |

Die Taste, die zuerst in Japan aufkam, wurde als empfindlicher Schalter bezeichnet. Während des Betriebs wird der Schalter gedrückt, um Kraft auszuüben und den Stromkreis zu schließen. Beim Loslassen des Drucks öffnet sich der Schalter. Ihr internes Metallfederblatt ändert seinen Verbindungs-/Trennungszustand als Reaktion auf die ausgeübte Kraft.

Es gibt vier Tasten, die jeweils unabhängig mit einem Pin auf dem micro:bit-Board verbunden sind. Wenn eine Taste gedrückt wird, erzeugt die Schaltung ein entsprechendes Low-Level-Signal, wodurch der micro:bit schnell auf Befehle reagieren und die Interaktionsfreundlichkeit und -genauigkeit erheblich verbessern kann.

![Img](./media/2bottom.png)

#### 5.2.2.3 Benötigte Teile

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 Board** (selbst mitgebracht) ×1 | **micro:bit Smart Gamepad** (montiert) ×1 | **AAA Batterie** (selbst mitgebracht) ×4 |


#### 5.2.2.4 Codeablauf

![Img](./media/2006.png)

#### 5.2.2.5 Testcode

⚠️ **Beachten Sie, dass die Verzögerungszeit von MODE\*_DELAY in den Codes je nach Bedarf geändert werden kann.**

**Vollständiger Code:**

```python
# import related libraries
from microbit import *
import neopixel, random, utime

# ==================== Configuration & Initialization ====================
BRIGHTNESS = 0.3        # Global brightness factor (0.0 to 0.9)
NP_NUM = 4              # Number of LEDs in the strip
strip = neopixel.NeoPixel(pin8, NP_NUM)

# Button Pins: Mapping JoyBit buttons to Pins
# C_KEY: Left, D_KEY: Right, E_KEY: Up, F_KEY: Down
KEYS = [pin15, pin16, pin13, pin14] 
for p in KEYS: 
    p.set_pull(p.PULL_UP)

# Global State Variables
mode = 0                # Current active mode (0-4)
last_btn_time = 0       # Global timestamp for button debouncing
# Shared state dictionary to handle indices and timing across modes
mode_data = {"idx": 0, "last_t": 0, "val": 0} 
```

② Hilfsfunktion: Konvertiert HSL-Farben in RGB und wechselt zwischen verschiedenen Farbmodi.

Dieser Teil definiert zwei Hilfsfunktionen:

*   `get_rgb(h, s, l)` : Farben konvertieren. Es akzeptiert HSL-Werte (Farbton, Sättigung, Helligkeit) und konvertiert sie in das RGB-Format. Es wendet auch einen globalen Helligkeitsfaktor `BRIGHTNESS` an, um sicherzustellen, dass alle Farben gemäß der Helligkeitsbegrenzung angepasst werden. Diese Funktion macht es sehr bequem, Lichteffekte in verschiedenen Farben zu erzeugen.
*   `update_mode(new_mode)` : ermöglicht einen sicheren Wechsel zwischen den Beleuchtungsmodi. Rufen Sie es auf, um zu einem neuen Modus zu wechseln, und es aktualisiert die globale Variable `mode`, setzt `idx` und `val` im `mode_data`-Wörterbuch auf 0 und setzt `last_t` auf die aktuelle Zeit, damit der neue Modus von Grund auf neu timen kann. Zusätzlich löscht es den NeoPixel-Lichtstreifen, um sicherzustellen, dass beim Moduswechsel keine alten Lichteffekte zurückbleiben.

```python
# ==================== Utility Functions ====================
def get_rgb(h, s=99, l=15):
    """ Converts HSL to RGB and applies global brightness scaling """
    h %= 360
    s, l = s/100.0, l/100.0
    c = (1 - abs(2 * l - 1)) * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = l - c / 2
    # Determine RGB sector based on Hue
    res = [(c,x,0), (x,c,0), (0,c,x), (0,x,c), (x,0,c), (c,0,x)][int(h/60)]
    return tuple(int((i + m) * 255 * BRIGHTNESS) for i in res)

def update_mode(new_mode):
    """ Resets mode states and clears the strip when switching modes """
    global mode
    mode = new_mode
    mode_data["idx"], mode_data["val"] = 0, 0
    mode_data["last_t"] = utime.ticks_ms()
    strip.fill((0, 0, 0))
    strip.show()
```

③ Definition des Lichtmusterverhaltens und Musterzuordnung.

Es gibt vier verschiedene Lichtmodusfunktionen, von denen jede einen einzigartigen Lichteffekt implementiert:

*   `run_m1()` (Modus 1: Zyklisches Wechseln der Vollfarbe): Der Streifen zeigt regelmäßig einen voreingestellten Satz von Vollfarben (Rot, Grün, Blau, Gelb, Lila) an, wobei jeweils eine Farbe wechselt.
*   `run_m2()` (Modus 2: Sanfter Regenbogenverlauf): Der Streifen zeigt einen sanften Regenbogenverlauf durch ständiges Ändern der Farbtöne (`mode_data["val"]`) an.
*   `run_m3()` (Modus 3: Pixelverschiebung mit zufälligen Farben): Die Pixel auf dem Streifen bewegen sich nach rechts, und der linkeste Pixel wird mit einer neuen zufälligen Farbe gefüllt, wie fließendes Wasser.
*   `run_m4()` (Modus 4: Verfolgung eines einzelnen Pixels): Nur ein Pixel auf dem Streifen leuchtet auf und bewegt sich um den Lichtstreifen herum, wobei jedes Mal, wenn es leuchtet, eine zufällige Farbe angezeigt wird.

Schließlich ordnet das `MODES`-Wörterbuch jede Modus-ID (1–4) ihrer entsprechenden Ausführungsfunktion und aktualisiert jede Verzögerungszeit (in Millisekunden), sodass die Hauptschleife bequem eine geeignete Funktion basierend auf dem aktuellen Modus aufrufen und deren Aktualisierungsfrequenz steuern kann.

```python
# ==================== Mode Behavior Definitions ====================
def run_m1(): # Mode 1: Solid Color Cycling
    colors = [(255,0,0), (0,255,0), (0,0,255), (255,255,0), (128,0,128)]
    rgb = tuple(int(i * BRIGHTNESS) for i in colors[mode_data["idx"]])
    strip.fill(rgb)
    mode_data["idx"] = (mode_data["idx"] + 1) % len(colors)

def run_m2(): # Mode 2: Smooth Rainbow Gradient (HSL)
    mode_data["val"] = (mode_data["val"] + 1) % 360
    strip.fill(get_rgb(mode_data["val"]))

def run_m3(): # Mode 3: Pixel Shifting with Random Colors
    # Shift existing pixels to the right
    for i in range(NP_NUM - 1, 0, -1): 
        strip[i] = strip[i-1]
    # Inject a new random color at the start
    strip[0] = get_rgb(random.randint(0, 360))

def run_m4(): # Mode 4: Chasing Single Pixel
    strip.fill((0,0,0)) # Clear all
    strip[mode_data["idx"]] = get_rgb(random.randint(0, 360), l=18)
    mode_data["idx"] = (mode_data["idx"] + 1) % NP_NUM

# Mode Map: Mode ID -> (Function to execute, delay in milliseconds)
MODES = {
    1: (run_m1, 500), 2: (run_m2, 5), 
    3: (run_m3, 200), 4: (run_m4, 200)
}
```

④ Hauptschleife: Tastenscanning, Modusausführung und Standby-Verarbeitung.
1.  Tastenscanning: Es scannt jeden Tasten-Pin in der `KEYS`-Liste, um zu erkennen, ob eine Taste gedrückt wird (Pin-Lesewert ist `0`). Um mehrere Auslöser durch Tastenprellen zu verhindern, wird ein Software-Entprellmechanismus verwendet: Ein neuer Tastendruck wird nur erkannt, wenn mehr als 200 Millisekunden seit der vorherigen Operation vergangen sind. Beim Erkennen eines gültigen Tastendrucks ruft es `update_mode()` für einen entsprechenden Beleuchtungsmodus auf (die Modus-ID wird durch Addition von 1 zum Tastenindex `i` erhalten) und aktualisiert `last_btn_time`.
2.  Modusausführung: Wenn der aktuelle `mode` im `MODES`-Wörterbuch aufgeführt ist (d.h. kein Standby-Modus), ruft es die entsprechende Ausführungsfunktion und die Aktualisierungsverzögerung ab. Es überprüft dann, ob die angegebene Verzögerungszeit seit der letzten Aktualisierung dieses Modus abgelaufen ist. Wenn ja, aktualisiert es `mode_data["last_t"]`, ruft die `func()` des Modus auf, um die Farbdaten zu aktualisieren, und sendet die Aktualisierungen über `strip.show()` an den Lichtstreifen.
3.  Standby-Verarbeitung: Wenn `mode` = `0` (Standby), löscht es den Lichtstreifen (`strip.fill((0,0,0))`), zeigt einen ausgeschalteten Zustand an, mit einer kurzen Verzögerung über `utime.sleep_ms(20)`, um CPU-Ressourcen zu sparen.

```python
# ==================== Main Loop (Non-Blocking) ====================
while True:
    curr_t = utime.ticks_ms()
    
    # 1. Scan Buttons (Non-blocking debounce)
    for i, pin in enumerate(KEYS):
        if pin.read_digital() == 0 and utime.ticks_diff(curr_t, last_btn_time) > 200:
            last_btn_time = curr_t
            update_mode(i + 1) # i+1 maps 0-3 to modes 1-4
            break 

    # 2. Execute Mode Logic based on Timer
    if mode in MODES:
        func, delay = MODES[mode]
        if utime.ticks_diff(curr_t, mode_data["last_t"]) > delay:
            mode_data["last_t"] = curr_t
            func()
            strip.show()
    elif mode == 0:
        # Standby: Keep strip off and save CPU cycles
        strip.fill((0,0,0))
        strip.show()
        utime.sleep_ms(20)
```

#### 5.2.2.6 Testergebnis

![Img](./media/4top.png)

Nach dem Brennen des Codes stecken Sie das micro:bit-Board in den Steckplatz des Gamepads (**Batterien eingelegt**) und schalten Sie den Schalter auf „ON“.

Drücken Sie **C**: Die Lichter wechseln abwechselnd in der Reihenfolge **Rot-Grün-Blau-Gelb-Lila**.

Drücken Sie **D**: Der Farbton der Lichter erhöht sich, und schließlich ändern sich die Verlaufsfarben sanft.

Drücken Sie **E**: Die Lichter erzeugen eine zufällige Farbe, beginnend mit dem 0. Pixel, und verschieben die Farbe sequentiell um ein Pixel, sodass Sie ein fließendes Licht sehen können.

Drücken Sie **F**: Jedes Pixel leuchtet nacheinander in zufälligen Farben auf.

![Img](./media/2019.gif)

<span style="color: rgb(0, 209, 0);">**Tipp:** Wenn das Board nicht reagiert, drücken Sie bitte die Reset-Taste auf der Rückseite des micro:bit-Boards.</span>

![Img](./media/4bottom.png)
