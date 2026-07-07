### 5.2.7 Raad het nummer

#### 5.2.7.1 Overzicht

![Img](./media/top1.png)

In dit project spelen we een nummerspel met een Micro:bit-bord, een gamepad-besturingsbord en een OLED-display. Wanneer het juiste nummer is geraden, toont de OLED "Great!!!"; als de gok te hoog of te laag is, toont het respectievelijk "To High!"/"To Low!", samen met het corresponderende bereik van mogelijke nummers.

![Img](./media/bottom1.png)

#### 5.2.7.2 Benodigde onderdelen

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 board** (zelf mee te nemen) ×1 | **micro:bit Smart Gamepad** (gemonteerd) ×1 | **AAA battery** (zelf mee te nemen) ×4 |
|![Img](./media/OLED.png)|![Img](./media/7008.png)|
|    **OLED display** (zelf mee te nemen)×1     |   **F-F DuPont wire**(zelf mee te nemen) x4    |

#### 5.2.7.3 Bedradingsschema

![Img](./media/jiexian8.png)

**Na het bedraden zoals hierboven weergegeven, plaatst u de micro:bit in de sleuf op het gamepad-besturingsbord.**

| OLED display | micro:bit gamepad control board | micro:bit board pin |
| :----------: | :-----------------------------: | :-----------------: |
|     GND      |               GND               |         GND         |
|     VCC      |               3V                |         3V          |
|     SDA      |               SDA               |         P20         |
|     SCL      |               SCL               |         P19         |

#### 5.2.7.4 Codestroom

![Img](./media/8001.png)

#### 5.2.7.5 Testcode

⚠️ **Merk op dat hier OLED wordt gebruikt, dus we moeten de bibliotheek importeren.**

![Img](./media/t7000.png)

**Volledige code:**

```python
# Import required libraries
from microbit import *
from oled_ssd1306 import *
from random import *

# Initialize OLED and pins
initialize()
clear_oled()

# Game core variables (defined outside loop to avoid resetting)
mode = 0          # 0: Game init, 1: Game running
min_num = 1       # Minimum guess number
max_num = 100     # Maximum guess number
current_guess = 50# Current guess value
target_num = 0    # Random target number
state = 0         # 0: Initial, 1: Too high, 2: Too low, 3: Correct
update_display = True  # Display update flag

# Enable pull-up resistors for buttons (active low)
pin13.set_pull(pin13.PULL_UP)
pin15.set_pull(pin15.PULL_UP)
pin16.set_pull(pin16.PULL_UP)

while True:
    # 1. Game initialization: generate random number and reset state
    if mode == 0:
        min_num = 1
        max_num = 100
        current_guess = 50
        target_num = randint(min_num, max_num)  # Generate target number
        state = 0
        mode = 1  # Switch to running mode
        update_display = True

    # 2. Game running logic
    if mode == 1:
        # Check buttons (independent detection to avoid blocking)
        if pin15.read_digital() == 0:  # Pin15 pressed: increase number
            current_guess += 1
            if current_guess > max_num:
                current_guess = max_num
            update_display = True
            sleep(50)  # Debounce delay

        elif pin13.read_digital() == 0:  # Pin13 pressed: decrease number
            current_guess -= 1
            if current_guess < min_num:
                current_guess = min_num
            update_display = True
            sleep(50)  # Debounce delay

        elif pin16.read_digital() == 0:  # Pin16 pressed: confirm guess
            if current_guess > target_num:
                state = 1
                max_num = current_guess  # Narrow range: max = current
            elif current_guess < target_num:
                state = 2
                min_num = current_guess  # Narrow range: min = current
            else:
                state = 3  # Correct guess
                mode = 0   # Reset game
            update_display = True
            sleep(50)  # Debounce delay

        # 3. Update OLED display (only when needed)
        if update_display:
            clear_oled()  # Clear screen
            # Display number range
            add_text(0, 0, "num:" + str(min_num) + "~" + str(max_num))
            # Display current guess
            add_text(0, 2, str(current_guess))
            # Display status message
            if state == 1:
                add_text(0, 4, "TO High")
            elif state == 2:
                add_text(0, 4, "TO Low")
            elif state == 3:
                add_text(0, 4, "Great!!!")

            # Reset update flag
            update_display = False

    # 4. Delay after correct guess to show message
    if state == 3:
        sleep(1000)
        state = 0
```

![Img](./media/line1.png)

**Korte uitleg:**

① Importeer bibliotheken, initialiseer OLED, definieer globale variabelen en configureer knoppinnen.

Drie bibliotheken zijn vereist: `microbit` (voor toegang tot Micro:bit-hardware), `oled_ssd1306` (voor het aansturen van het aangesloten OLED-display), `random` (voor het genereren van willekeurige nummers in het spel).

`initialize()` en `clear_oled()` initialiseren en wissen de OLED.

Een reeks globale variabelen wordt gedefinieerd om spelstatusparameters te beheren, waaronder spelmodus (`mode`), nummerbereik (`min_num`, `max_num`), de huidige gokwaarde (`current_guess`), het doelnummer (`target_num`), spelfeedback (`state`) en een vlag die display-updates regelt (`update_display`).

`pin13`, `pin15` en `pin16` zijn geconfigureerd in pull-up-modus – hoog blijven wanneer de knop niet is ingedrukt en laag wanneer deze is ingedrukt.

```python
# Import required libraries
from microbit import *
from oled_ssd1306 import *
from random import *

# Initialize OLED and pins
initialize()
clear_oled()

# Game core variables (defined outside loop to avoid resetting)
mode = 0          # 0: Game init, 1: Game running
min_num = 1       # Minimum guess number
max_num = 100     # Maximum guess number
current_guess = 50# Current guess value
target_num = 0    # Random target number
state = 0         # 0: Initial, 1: Too high, 2: Too low, 3: Correct
update_display = True  # Display update flag

# Enable pull-up resistors for buttons (active low)
pin13.set_pull(pin13.PULL_UP)
pin15.set_pull(pin15.PULL_UP)
pin16.set_pull(pin16.PULL_UP)
```
② Spelinitialisatielogica in de hoofdloop.

Het is het eerste logische blok van de hoofdloop van het programma, specifiek verantwoordelijk voor spelinitialisatie of herstart.

`mode` = `0`: het spel vereist initialisatie. In dit geval reset het het gokbereik naar 1–100 en stelt het de huidige gokwaarde in op 50. Het gebruikt `randint(min_num, max_num)` om willekeurig een geheel getal tussen 1 en 100 te genereren als het doelnummer (`target_num`).

Vervolgens, `state` = `0` (initiële staat) en `mode` = `1` (lopend). En stel `update_display` in op `True` om ervoor te zorgen dat de OLED de nieuwste spelinformatie onmiddellijk bijwerkt tijdens het draaien.

```python
while True:
    # 1. Game initialization: generate random number and reset state
    if mode == 0:
        min_num = 1
        max_num = 100
        current_guess = 50
        target_num = randint(min_num, max_num)  # Generate target number
        state = 0
        mode = 1  # Switch to running mode
        update_display = True
```
③ Verwerk knopinvoer en besluitvorming op basis van de gok.

Wanneer het spel in werking is (`mode == 1`), beheert het spelerinteracties en spellogica. Het detecteert onafhankelijk invoer van drie externe knoppen:

*   **`pin15` is ingedrukt**: (laag niveau gedetecteerd); `current_guess` + 1. Om te voorkomen dat de waarde het bereik overschrijdt, controleert en beperkt het `current_guess` < of = `max_num`.
*   **`pin13` is ingedrukt**: `current_guess` - 1. Het controleert ook `current_guess` niet groter dan `min_num`.
*   **`pin16` is ingedrukt**: Als `pin16` is ingedrukt, betekent dit dat de speler de gokwaarde heeft ingediend. Deze wordt vergeleken met `target_num`:
    *   `current_guess` > `target_num`: `state` = `1` (te hoog) en stel het bereikmaximum `max_num` in op `current_guess`.
    *   `current_guess` < `target_num`: `state` = `2` (te laag) en stel het minimum `min_num` in op `current_guess`.
    *   `current_guess` = `target_num`: `state` = `3` (Geweldig) en stel `mode` in op `0` om je voor te bereiden op de volgende ronde.

Na elke knopdruk wordt `update_display` ingesteld op `True` om de OLED bij te werken, met een vertraging van 50 ms voor anti-jitter.

```python
    # 2. Game running logic
    if mode == 1:
        # Check buttons (independent detection to avoid blocking)
        if pin15.read_digital() == 0:  # Pin15 pressed: increase number
            current_guess += 1
            if current_guess > max_num:
                current_guess = max_num
            update_display = True
            sleep(50)  # Debounce delay

        elif pin13.read_digital() == 0:  # Pin13 pressed: decrease number
            current_guess -= 1
            if current_guess < min_num:
                current_guess = min_num
            update_display = True
            sleep(50)  # Debounce delay

        elif pin16.read_digital() == 0:  # Pin16 pressed: confirm guess
            if current_guess > target_num:
                state = 1
                max_num = current_guess  # Narrow range: max = current
            elif current_guess < target_num:
                state = 2
                min_num = current_guess  # Narrow range: min = current
            else:
                state = 3  # Correct guess
                mode = 0   # Reset game
            update_display = True
            sleep(50)  # Debounce delay
```
④ OLED-updatelogica.

Het toont de huidige status en informatie van het spel op de OLED. Het wordt alleen uitgevoerd wanneer `update_display` = `True` om onnodige vernieuwingen te voorkomen.

Elke uitvoering roept eerst `clear_oled()` aan om het display te wissen. Het huidige gokbereik (bijv. "num:1~100") verschijnt op de eerste regel. De huidige gok van de speler (`current_guess`) wordt weergegeven op de derde regel.

Op basis van `state` verschijnt het corresponderende feedbackbericht ("TO High," "TO Low," of "Great!!!") op de vijfde regel.

Na het voltooien van alle weergaven wordt `update_display` gereset naar `False` om klaar te zijn om de volgende spelstatuswijziging bij te werken.

```python
        # 3. Update OLED display (only when needed)
        if update_display:
            clear_oled()  # Clear screen
            # Display number range
            add_text(0, 0, "num:" + str(min_num) + "~" + str(max_num))
            # Display current guess
            add_text(0, 2, str(current_guess))
            # Display status message
            if state == 1:
                add_text(0, 4, "TO High")
            elif state == 2:
                add_text(0, 4, "TO Low")
            elif state == 3:
                add_text(0, 4, "Great!!!")

            # Reset update flag
            update_display = False
```
⑤ Verwerk vertragingen na correcte gissingen.

Het wordt alleen uitgevoerd wanneer de speler het doelnummer correct raadt (`state == 3`). Vervolgens pauzeert het 1000 ms (1 s) zodat spelers de "Great!!!" kunnen controleren.

Vervolgens wordt `state` gereset naar `0`. Aangezien `mode` al is gereset naar `0`, zal het spel bij een correcte gok opnieuw starten vanaf de initialisatie.

```python
    # 4. Delay after correct guess to show message
    if state == 3:
        sleep(1000)
        state = 0
```

#### 5.2.7.6 Testresultaat

![Img](./media/4top.png)

Na het branden van de code, plaatst u het micro:bit-bord in de sleuf van de gamepad (**batterijen geïnstalleerd**), en zet u de schakelaar op "ON".

Na het uploaden van de code initialiseert de OLED en toont het het waardebereik van "num: 1 ~ 100" en de initiële gok van 50. U kunt op C drukken om temp+1 (maximaal 100) of op E om temp-1 (minimaal 1) om uw gokwaarde op de OLED te wijzigen.

Druk op D om uw waarde in te dienen, en temp wordt vergeleken met de willekeurige doelwaarde. Als temp>waarde, toon "To High!" en wijs temp toe aan max_num; als temp<waarde, toon "To Low!" en wijs het toe aan min_num. Als u te veel geluk heeft dat temp=waarde, ziet u "Great!!!" gedurende 1s.

Daarna wordt het spel gereset en wordt een nieuwe doelwaarde ingesteld. Laten we nog een ronde spelen!

![Img](./media/t7000.gif)

⚠️ **De bouwsteen in Testresultaat is niet inbegrepen in deze productkit.**

<span style="color: rgb(0, 209, 0);">**Tip:** Als er geen reactie is op het bord, druk dan op de resetknop aan de achterkant van het micro:bit-bord.</span>

![Img](./media/4bottom.png)
