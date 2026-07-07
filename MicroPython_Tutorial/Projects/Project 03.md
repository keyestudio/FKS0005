### 5.2.3 Eenvoudige Elektronische Piano

#### 5.2.3.1 Overzicht

![Img](./media/top1.png)

In dit project bedienen we de micro:bit-luidspreker om verschillende tonen af te spelen door de joystick te bewegen en op de knoppen te drukken. Tegelijkertijd zal de ingebouwde LED-matrix overeenkomstige nummers tonen.

De joystick naar rechts draaien produceert "Do (Toon Centrale C)" met de weergave "1"; naar links draaien produceert "Re (Toon D)" met "2"; naar boven draaien produceert "Mi (Toon E)" met "3"; naar beneden draaien produceert "Fa (Toon F)" met "4". Op knop C drukken produceert "Sol (Toon G)" met "5", op D drukken produceert "La (Toon A)" met "6", E produceert "Si (Toon B)" met "7", en op F drukken produceert een hogere "Do(Scherp)" terwijl de weergave terugkeert naar "1". Er is een mooie synchronisatie van de joystick, knoppen, tonen en weergave.

![Img](./media/bottom1.png)

#### 5.2.3.2 Componentenkennis

![Img](./media/2top.png)

**Microbit luidspreker**

![Img](./media/j901.png)

Het micro:bit-bord beschikt over een ingebouwde luidspreker voor het maken van geluid, zoals gegiechel, groeten, geeuwen of uitingen van verdriet, of zelfs het componeren van een lied. Door te programmeren kan het zelfs individuele noten, melodieën en ritmes genereren, of zelfs muzikale composities, zoals het lied *Ode aan de Vreugde*.

![Img](./media/2bottom.png)

#### 5.2.3.3 Benodigde onderdelen

| ![Img](./media/microbitV2.png)|  ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 board** (zelf mee te nemen) ×1 | **micro:bit Smart Gamepad** (gemonteerd) ×1 | **AAA batterij** (zelf mee te nemen) ×4 |

#### 5.2.3.4 Codestroom

![Img](./media/3009.png)

#### 5.2.3.5 Testcode

⚠️ **Let op: de gevoeligheid van de joystick kan naar behoefte worden aangepast.**

**Volledige code:**

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

**Korte uitleg:**

① Bibliotheken importeren, constanten configureren en initialiseren.

Het importeert de `microbit`-bibliotheek om toegang te krijgen tot de hardwaremogelijkheden van Micro:bit en `music` voor het afspelen van muziek. Vervolgens definieert het twee essentiële lijsten met configuratieconstanten:

*   `JOY_MAP`: Wordt gebruikt om de joystick-mapping te configureren. Elke tuple bevat joystick-verbonden pinnen, drempels (bijv. boven 600 of onder 400), de af te spelen muzieknoot (bijv. 'c4:2' is centrale C die twee tellen duurt), en het teken dat wordt weergegeven op de Micro:bit LED-matrix.
*   `BTN_MAP`: De mapping die wordt gebruikt om externe knoppen te configureren. Elke tuple bevat de knop-verbonden pinnen, de af te spelen muzieknoten en de tekens die worden weergegeven op de Micro:bit LED-matrix.

Tijdens de initialisatie scant het programma alle knoppinnen in `BTN_MAP` en stelt hun interne pull-up weerstanden (`p.PULL_UP`) in. Dit zorgt ervoor dat de pinnen hoog blijven wanneer de knop niet wordt ingedrukt en naar een laag niveau vallen wanneer deze wordt ingedrukt.

Ten slotte verschijnt er een muzieknootpictogram (`Image.MUSIC_CROTCHET`) op de LED-matrix.

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

② Hoofdlus: Verwerk joystick-ingangen.

Het is een oneindige lus (`while True`). Het verwerkt eerst de joystick-ingang door de `JOY_MAP`-lijst te doorlopen en elke joystick-richting te controleren. Voor elke joystick-pin leest het de analoge waarde (`pin.read_analog()`).

De joystick wordt vervolgens geacht geactiveerd te zijn op basis van een vooraf ingestelde drempel (`thresh`): als de drempel 600 is en de huidige analoge waarde 600 overschrijdt (joystick ingedrukt), of als de drempel 400 is en de huidige analoge waarde onder 400 ligt (in de tegenovergestelde richting geduwd), speelt het de overeenkomstige muzieknoot af (`music.play(note, wait=False)`), waarbij `wait=False` ervoor zorgt dat het afspelen van muziek de hoofdlus niet blokkeert, waardoor gelijktijdige detectie van andere ingangen mogelijk is.

En de Micro:bit LED-display toont het teken dat overeenkomt met de joystick-richting.

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

③ Hoofdlus: Verwerk knop-ingangen.

Na de joystick-ingang is het nu de beurt aan de externe knop-ingangen. Het doorloopt elke knop in de `BTN_MAP`-lijst. Voor elke knop-pin controleert het of de digitale uitleeswaarde `0` is (`pin.read_digital() == 0`, betekent knop ingedrukt). Wanneer de knop wordt ingedrukt, is de pin laag vanwege de pull-up weerstand, speelt het programma de overeenkomstige muzieknoot af (`music.play(note, wait=False)`) en toont het teken op de Micro:bit LED-matrix.

Om knopjitter of meerdere detecties van een enkele druk te voorkomen, is er een `while`-lus die blijft wachten totdat de huidige knop wordt losgelaten (`while pin.read_digital() == 0: sleep(10)`). Deze wachttijd blokkeert het programma tijdelijk totdat de knop wordt losgelaten.

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

④ Hoofdlus: Lusvertraging.

Na alle ingangsdetecties pauzeert het programma 20 milliseconden (`sleep(20)`) om het systeem te stabiliseren, de CPU-belasting te verminderen en een tijdsinterval te bieden voor de volgende lus-ingangsdetectie.

```python
    # Small delay to maintain system stability and reduce CPU load
    sleep(20)
```

#### 5.2.3.6 Testresultaat

![Img](./media/4top.png)

Na het branden van de code, plaatst u het micro:bit-bord in de sleuf van de gamepad (**batterijen geïnstalleerd**) en zet u de schakelaar op “ON”. De LED-matrix toont eerst “![Img](./media/3004.png)”.

De joystick naar rechts draaien produceert "Do (Toon Centrale C)" met de weergave "1"; naar links draaien produceert "Re (Toon D)" met "2"; naar boven draaien produceert "Mi (Toon E)" met "3"; naar beneden draaien produceert "Fa (Toon F)" met "4". Op knop C drukken produceert "Sol (Toon G)" met "5", op D drukken produceert "La (Toon A)" met "6", E produceert "Si (Toon B)" met "7", en op F drukken produceert een hogere "Do(Scherp)" terwijl de weergave terugkeert naar "1".

U hebt de eenvoudige elektronische piano gebouwd!

![Img](./media/3010.gif)

<span style="color: rgb(0, 209, 0);">**Tip:** Als er geen reactie is op het bord, drukt u op de resetknop aan de achterkant van het micro:bit-bord.</span>

![Img](./media/4bottom.png)
