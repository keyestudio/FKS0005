### 5.2.4 Muziekspeler

#### 5.2.4.1 Overzicht

![Img](./media/top1.png)

Hierin bouwen we een muziekspeler die geluid genereert via de ingebouwde buzzer op het micro:bit-bord (speelt geen vocale muziek af). Het beschikt over een bibliotheek van 20 korte nummers en ondersteunt zowel sequentiële als willekeurige weergave.

In de sequentiële modus schakelt het indrukken van knop C (Vorig nummer) of E (Volgend nummer) nummers volgens een vooraf ingestelde volgorde totdat het einde van de lijst is bereikt; terwijl in de willekeurige modus elke druk een nummer willekeurig selecteert uit de 20 geluiden met knipperende kleurenlichten, en wanneer een nummer is afgelopen, stopt het onmiddellijk.

Ondertussen geeft de micro:bit LED-matrix de huidige afspeelmodus in realtime weer.

![Img](./media/bottom1.png)

#### 5.2.4.2 Benodigde onderdelen

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 board** (zelf mee te nemen) ×1 | **micro:bit Smart Gamepad** (gemonteerd) ×1 | **AAA battery** (zelf mee te nemen) ×4 |

#### 5.2.4.3 Codestroom

![Img](./media/4001.png)

#### 5.2.4.4 Testcode

**Volledige code:**

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

**Korte uitleg:**

① Importeer bibliotheken, configureer constanten en initialisatie.

Het importeert eerst de `microbit`-bibliotheek om toegang te krijgen tot de kernfuncties van de Micro:bit, `music` voor het afspelen van ingebouwde muziek, `neopixel` voor het aansturen van de NeoPixel LED-strip en `random` voor het genereren van willekeurige getallen.

Vervolgens definieert het een reeks globale variabelen en constanten: `vol` stelt het initiële volume in op 50; `mode` regelt de afspeelmodus van de muziek (0 voor handmatige selectie, 1 voor willekeurige weergave); `idx` slaat de huidige muziekindex op; houdt de vorige afspeelindex bij om dubbele afspeelacties te voorkomen; `hue` regelt de kleur van de NeoPixel-strip; `strip` initialiseert een NeoPixel-strip die is aangesloten op `pin8` van vier LED\'s; en `melodies` geeft alle `music`-titels van MicroPython weer.

Daarna definieert de `btns`-lijst de vier externe knoppinnen van `pin13` tot `pin16`, en wijst deze in een lus interne pull-up-weerstanden (`p.PULL_UP`) toe – wat resulteert in hoog-niveau pinnen wanneer knoppen worden losgelaten en laag-niveau pinnen wanneer ze worden ingedrukt.

`set_volume (vol)` stelt het volume in op de standaardwaarde.

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

② Kleurconversiefunctie en stabilisatievariabele.

`get_rgb(h)` is een vereenvoudigde HSL (Hue, Saturation, Lightness) naar RGB-kleurconversiefunctie. Het accepteert een tintwaarde `h` (0–359) en converteert deze naar een RGB-triplet. De helderheid `v` is vastgesteld op 76 (ongeveer 255 × 0.3, overeenkomend met de `BRIGHTNESS`-coëfficiënt). Deze functie vergemakkelijkt het genereren van regenboogkleuren op basis van de tintwaarde.

De `last_states`-lijst slaat de vorige statussen van de vier knoppen op, aanvankelijk allemaal ingesteld op 1 (hoog niveau voor niet ingedrukt). `last_press_t` registreert de tijd van de laatste knopdruk. Samen implementeren deze variabelen software-anti-jitter om meerdere detecties van een enkele knopdruk te voorkomen.

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

③ Hoofdloop: Volumeregeling.

Er is een oneindige lus (`while True`) die de huidige looptijd `curr_t` ophaalt. Vervolgens verwerkt het de A- en B-knoppen op het Micro:bit-bord:

*   Als `button_a` wordt ingedrukt (`button_a.was_pressed()`), wordt het volume `vol` + 10, maar niet meer dan 250. `set_volume(vol)` wordt vervolgens gebruikt om het systeemvolume bij te werken.
*   Als `button_b` wordt ingedrukt (`button_b.was_pressed()`), wordt `vol` - 10, maar blijft het niet minder dan 20. `set_volume(vol)` wordt vervolgens gebruikt om het systeemvolume bij te werken.

`was_pressed()` retourneert slechts één keer `True` wanneer de knop overgaat van een niet-ingedrukte naar een ingedrukte staat, wat een inherente anti-jitter biedt.

```python
while True:
    curr_t = running_time()
    
    # 1. Volume Control (Buttons A/B)
    if button_a.was_pressed(): vol = min(250, vol + 10); set_volume(vol)
    if button_b.was_pressed(): vol = max(20, vol - 10); set_volume(vol)
```

④ Hoofdloop: detectie van knopinvoer en moduswisseling.

Het doorloopt de vier externe knoppen (`pin13` tot `pin16`) in de `btns`-lijst en detecteert hun ingedrukte statussen. De knop wordt alleen gereageerd wanneer deze van hoog (niet ingedrukt) naar laag (ingedrukt) gaat en het meer dan 50 milliseconden geleden is sinds de laatste geldige toetsaanslag.

*   Als `pin16` wordt ingedrukt (`i == 3`), wordt `mode` = 0 (handmatige modus) en pauzeert het 500 ms.
*   Als `pin14` wordt ingedrukt (`i == 1`), wordt `mode` = 1 (willekeurige modus) en pauzeert het 500 ms.
*   Als `pin15` wordt ingedrukt (`i == 2`), wordt de muziekindex `idx` bijgewerkt volgens het huidige patroon: één muziek wordt willekeurig geselecteerd in de willekeurige modus; de volgende muziek wordt afgespeeld in de handmatige modus.
*   Als `pin13` wordt ingedrukt (`i == 0`), wordt de muziekindex `idx` bijgewerkt volgens het huidige patroon: één muziek wordt willekeurig geselecteerd in de willekeurige modus; de volgende muziek wordt afgespeeld in de handmatige modus.

Aan het einde van elke lus werkt `last_states[i] = v` de huidige status van de knop bij ter voorbereiding op de volgende stabiliteitscontrole.

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

⑤ Hoofdloop: logica voor het afspelen van muziek.

Het regelt het afspelen van de muziek door te controleren of de huidige muziekindex `idx` verschilt van de vorige `last_idx`. Als dit het geval is, moet de muziek worden gewisseld:

1.  `music.stop()` stopt de muziek die momenteel wordt afgespeeld.
2.  `music.play(getattr(music, melodies[idx]), wait=False)` probeert een nieuwe muziek af te spelen. `getattr(music, melodies[idx])` verkrijgt dynamisch de muziekgegevens van de overeenkomstige naam in `music`, en `wait=False` zorgt ervoor dat het afspelen van muziek de hoofdloop niet blokkeert.
3.  Als het afspelen succesvol is, werk `last_idx = idx` bij.
4.  `try...except` vangt potentiële fouten op; er kunnen bijvoorbeeld ongeldige muziektitels in de `melodies`-lijst staan.

```python
    # 3. Music Playback Logic
    if idx != last_idx:
        music.stop()
        try:
            music.play(getattr(music, melodies[idx]), wait=False)
            last_idx = idx
        except: pass
```

⑥ Hoofdloop: Licht- en display-updates.

Hier is een update over de kleur van de NeoPixel-strip en de weergave van de Micro:bit LED-matrix:

1.  `hue = (hue + 1) % 360` verhoogt `hue` continu om het te laten cyclen tussen 0 en 359 voor een regenbooggradiëntlicht.
2.  `strip.fill(get_rgb(hue))` gebruikt `get_rgb` om een kleur te genereren op basis van de huidige `hue` en vult de hele NeoPixel-strip met deze kleur.
3.  `strip.show()` stuurt de bijgewerkte kleur naar de NeoPixel-strip voor weergave.
4.  `display.show(...)` geeft het display weer, afhankelijk van de huidige `mode`. `mode` = 1 (willekeurig): toon een aangepaste 
X”; `mode` = 0 (handmatig), toon een pijl die naar rechts wijst (`Image.ARROW_E`).

Vervolgens introduceert `sleep(10)` een korte vertraging voor een geschikte uitvoeringssnelheid, lagere CPU-belasting en een vloeiender effect.

```python
    # 4. Lighting & Display Updates
    hue = (hue + 1) % 360
    strip.fill(get_rgb(hue))
    strip.show()
    
    # Show Mode Icon: "X" for Random, Arrow for Manual
    display.show(Image("00000:99099:00900:99099:00000") if mode else Image.ARROW_E)
    
    sleep(10)
```
#### 5.2.4.5 Testresultaat

![Img](./media/4top.png)

Na het branden van de code, plaatst u het micro:bit-bord in de sleuf van de gamepad (**batterijen geïnstalleerd**), en zet u de schakelaar op 
“ON”.

Na het inschakelen bevindt het zich standaard in de sequentiële modus en speelt het het nummer op N.O. “0” af. Zodra het is afgelopen, kunt u op C drukken voor het vorige nummer of op E voor het volgende. 

Druk op F om over te schakelen naar de willekeurige modus. En u kunt op D drukken om terug te gaan naar de sequentiële modus. In de F-modus wordt een willekeurig nummer van deze 20 afgespeeld als u op C/E drukt. Nadat het is afgelopen, stopt het. 

De RGB-lampjes ademen altijd vanaf het moment van inschakelen. Ondertussen toont de micro:bit LED-matrix “![Img](./media/4010.png)” in de sequentiële modus en “![Img](./media/4011.png)” in de willekeurige modus. 

Voor het volume drukt u op A om het volume te verhogen en op B om het te verlagen.

![Img](./media/4015.gif)

<span style="color: rgb(0, 209, 0);">**Tip:** Als er geen reactie is op het bord, druk dan op de resetknop aan de achterkant van het micro:bit-bord.</span>

![Img](./media/4bottom.png)
