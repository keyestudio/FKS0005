### 5.2.2 Kleurrijke Lichten

#### 5.2.2.1 Overzicht

![Img](./media/top1.png)

RGB-LED's zijn een type LED-lichtbron dat beelden creëert door licht van de drie primaire kleuren te mengen: rood, groen en blauw, waarvan de combinatie verschillende tinten produceert. Veelvoorkomende methoden omvatten directe menging van de primaire kleuren, het gebruik van een blauwe LED gecombineerd met gele fosfor, of het gebruik van een ultraviolette LED samen met RGB-fosfor. Vergeleken met LED's die direct wit licht uitstralen, bieden RGB-LED's een breder scala aan kleurmengmogelijkheden omdat de drie primaire kleuren onafhankelijk kunnen worden geregeld.

In dit project komt elke knop overeen met een andere modus van de RGB-LED's. Wanneer knop C wordt ingedrukt, knipperen de lichten afwisselend in de volgorde "rood, groen, blauw, geel en paars"; Druk op D om over te schakelen naar ademende lichten; Druk op E voor waterstromende lichten; Druk op F voor markeerlichten.

Kleurrijke lichtslingers voor feestdecoraties, kerstboomverlichting, RGB-strips voor dagelijkse sfeer, LED-decoratieve verlichting in pretparken en winkelcentra... Dit zijn allemaal veelvoorkomende voorbeelden van multimode verlichting in ons dagelijks leven.

![Img](./media/bottom1.png)

#### 5.2.2.2 Componentenkennis

![Img](./media/2top.png)

**SK6812 RGB LED**

| ![Img](./media//2001.png)| ![Img](./media//2002.png)|
| :--: | :--: |
|       Werkelijk product        |     Schematisch diagram     |

De SK6812 is een extern gestuurde LED-lichtbron die besturings- en verlichtingscircuits integreert. Het belangrijkste onderdeel zijn 5x5mm oppervlakte-verlichte LED-kralen, elk functionerend als een onafhankelijke pixel die meerdere kerncircuits bevat: een slim digitaal interface-datalatchcircuit, signaalvormings- en versterkingsaandrijfcircuit, stroomregelcircuit, ingebouwd constantstroomcircuit en een zeer nauwkeurige RC-oscillator.

De communicatie maakt gebruik van een enkelpolig nul-retourcode protocol. Na het opstarten ontvangt elke pixel gegevens van de controller via de DIN-poort. De eerste 24 bits aan gegevens worden door de initiële pixel geëxtraheerd en opgeslagen in de interne datalatch, terwijl de overige intern worden gevormd en versterkt voordat ze via de DOUT-poort naar volgende pixels worden verzonden. Bij elke verwerkte pixel neemt de verzonden signaalgrootte met 24 bits af.

Op de gamepad bevinden zich vier SK6812 RGB-lampjes. Deze ondersteunen allemaal 256-niveaus helderheidsaanpassing over hun rode, groene en blauwe kanalen, waardoor 256×256×256 kleurencombinaties mogelijk zijn. Hierdoor levert het diverse lichteffecten zoals afwisselende flitsen, ademende gradiënten en scrollende animaties, wat zorgt voor meer intuïtieve en levendige interacties.

**Knop**

| ![Img](./media//2003.png)| ![Img](./media//2004.png)|
| :--: | :--: |
|       Werkelijk product        |     Schematisch diagram     |

De knop, voor het eerst verschenen in Japan, werd aangeduid als een gevoelige schakelaar. Tijdens de bediening drukt u op de schakelaar om kracht uit te oefenen om het circuit te sluiten. Bij het loslaten van de druk opent de schakelaar. De interne metalen veerklem verandert van verbonden/niet-verbonden toestand als reactie op de uitgeoefende kracht.

Er zijn vier knoppen, elk onafhankelijk verbonden met een pin op het micro:bit-bord. Wanneer een knop wordt ingedrukt, genereert het circuit een overeenkomstig laag niveau signaal, waardoor de micro:bit snel kan reageren op commando's en de interactie gemak en nauwkeurigheid aanzienlijk verbetert.

![Img](./media/2bottom.png)

#### 5.2.2.3 Benodigde onderdelen

| ![Img](./media/microbitV2.png)|  ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 board** (zelf mee te nemen) ×1 | **micro:bit Smart Gamepad** (gemonteerd) ×1 | **AAA batterij** (zelf mee te nemen) ×4 |


#### 5.2.2.4 Codestroom

![Img](./media/2006.png)

#### 5.2.2.5 Testcode

⚠️ **Let op: de vertragingstijd van de MODE\*_DELAY in de codes kan naar behoefte worden aangepast.**

**Volledige code:**

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
**Korte uitleg:**

① Bibliotheken importeren, constanten configureren, NeoPixel-strips en knoppinnen initialiseren.

Het importeert eerst de kernbibliotheek `microbit` die nodig is voor MicroPython, `neopixel` om NeoPixel LED-lampjes te bedienen, `random` voor het genereren van willekeurige getallen en `utime` voor tijdgerelateerde bewerkingen (zoals het verkrijgen van de huidige tijdstempel en het vertragen van de tijd).

Vervolgens worden verschillende belangrijke configuratieconstanten gedefinieerd: `BRIGHTNESS` regelt de globale helderheid van de LED (0.0~0.9), `NP_NUM` specificeert het aantal LED's op de NeoPixel-strip (in dit geval 4), en het `strip`-object wordt geïnitialiseerd, verbonden met `pin8` en bevat `NP_NUM` LED's.

De `KEYS`-lijst specificeert de Micro:bit-pinnen die overeenkomen met de vier knoppen die zijn verbonden met het JoyBit-uitbreidingsbord. Door pull-up weerstanden (`p.PULL_UP`) op deze pinnen in een lus toe te passen, behouden de pinnen een hoog niveau wanneer de knoppen niet worden ingedrukt en een laag niveau wanneer ze worden ingedrukt (voor eenvoudige detectie).

Ten slotte worden de volgende globale statusvariabelen gedefinieerd: `mode` houdt de momenteel actieve verlichtingsmodus bij (0 voor stand-by; 1–4 zijn verschillende lichteffecten), `last_btn_time` slaat de tijdstempel op voor knop-ontdemping, en `mode_data` is een woordenboek dat statusinformatie bevat die wordt gedeeld of onderhouden tussen modi (bijv. index, laatste update tijd, waarde).

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

② Hulpprogrammafunctie: Converteert HSL-kleuren naar RGB en schakelt tussen verschillende kleurmodi.

Dit deel definieert twee hulpfuncties:

*   `get_rgb(h, s, l)`: converteert kleuren. Het accepteert HSL (Hue, Saturation, Lightness) waarden en converteert deze naar RGB-formaat. Het past ook een globale helderheidsfactor `BRIGHTNESS` toe, zodat alle kleuren worden aangepast aan de helderheidslimiet. Deze functie maakt het erg handig om lichteffecten in verschillende kleuren te genereren.
*   `update_mode(new_mode)`: maakt veilig schakelen tussen verlichtingsmodi mogelijk. Roep het aan om naar een nieuwe modus te schakelen, en het zal de globale `mode`-variabele bijwerken, de `idx` en `val` in het `mode_data`-woordenboek resetten naar 0, en `last_t` instellen op de huidige tijd zodat de nieuwe modus vanaf nul kan beginnen met timen. Bovendien wist het de NeoPixel-lichtstrip om ervoor te zorgen dat er geen resterende oude lichteffecten achterblijven tijdens de modusschakeling.

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

③ Lichtpatroon gedragsdefinitie en patroonmapping.

Er zijn vier verschillende verlichtingsmodusfuncties, die elk een uniek lichteffect implementeren:

*   `run_m1()` (Modus 1: Effen kleurcyclus): De strip toont regelmatig een vooraf ingestelde reeks effen kleuren (rood, groen, blauw, geel, paars), waarbij één kleur tegelijk wordt gewisseld.
*   `run_m2()` (Modus 2: Vloeiende regenbooggradiënt): De strip toont een vloeiende regenbooggradiënt door constant van tint te veranderen (`mode_data["val"]`).
*   `run_m3()` (Modus 3: Pixelverschuiving met willekeurige kleuren): De pixels op de strip bewegen naar rechts, en de meest linkse pixel wordt gevuld met een nieuwe willekeurige kleur, als een stromende beweging.
*   `run_m4()` (Modus 4: Jagende enkele pixel): Slechts één pixel op de strip licht op en beweegt rond de lichtstrip, telkens met een willekeurige kleur wanneer deze wordt verlicht.

Ten slotte koppelt het `MODES`-woordenboek elke modus-ID (1–4) aan de bijbehorende uitvoeringsfunctie en werkt het elke vertragingstijd (in milliseconden) bij, zodat de hoofdlus gemakkelijk een geschikte functie kan aanroepen op basis van de huidige modus en de updatefrequentie ervan kan regelen.

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

④ Hoofdlus: knopscanning, modusuitvoering en stand-by verwerking.
1.  Knopscanning: Het scant elke knoppin in de `KEYS`-lijst om te detecteren of een knop is ingedrukt (pin-uitlezing is `0`). Om meerdere triggers veroorzaakt door knopjitter te voorkomen, wordt een softwarematig anti-jittermechanisme gebruikt: een nieuwe knopdruk wordt alleen gedetecteerd als er meer dan 200 milliseconden zijn verstreken sinds de vorige bewerking. Bij detectie van een geldige druk, roept het `update_mode()` aan voor een overeenkomstige verlichtingsmodus (de modus-ID wordt verkregen door 1 toe te voegen aan de knopindex `i`) en werkt het `last_btn_time` bij.
2.  Modusuitvoering: Als de huidige `mode` in het `MODES`-woordenboek staat (d.w.z. geen stand-bymodus), haalt het de overeenkomstige uitvoeringsfunctie en updatevertraging op. Het controleert vervolgens of de opgegeven vertragingsperiode is verstreken sinds de laatste update van die modus. Zo ja, dan werkt het `mode_data["last_t"]` bij, roept het de `func()` van de modus aan om de kleurgegevens bij te werken, en stuurt het de updates naar de lichtstrip via `strip.show()`.
3.  Stand-by verwerking: Als `mode` = `0` (stand-by), wist het de lichtstrip (`strip.fill((0,0,0))`), toont het een uit-status, met een korte vertraging via `utime.sleep_ms(20)` om CPU-cycli te besparen.

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

#### 5.2.2.6 Testresultaat

![Img](./media/4top.png)

Na het branden van de code, plaatst u het micro:bit-bord in de sleuf van de gamepad (**batterijen geïnstalleerd**) en zet u de schakelaar op “ON”. 

Druk op **C**: de lichten wisselen af tussen **rood-groen-blauw-geel-paars** in volgorde. 

Druk op **D**: de kleurtint van de lichten zal toenemen, en uiteindelijk zullen de gradiëntkleuren vloeiend veranderen. 

Druk op **E**: de lichten genereren een willekeurige kleur beginnend bij de 0e pixel, en verschuiven de kleur sequentieel één pixel, zodat u een waterstromend licht ziet.

Druk op **F**: elke pixel licht op in willekeurige kleuren in volgorde.

![Img](./media/2019.gif)

<span style="color: rgb(0, 209, 0);">**Tip:** Als er geen reactie is op het bord, drukt u op de resetknop aan de achterkant van het micro:bit-bord.</span>

![Img](./media/4bottom.png)
