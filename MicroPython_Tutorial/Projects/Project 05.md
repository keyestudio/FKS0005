### 5.2.5 Vermijd stenen

#### 5.2.5.1 Overzicht

![Img](./media/top1.png)

In dit project spelen we een spel om stenen te ontwijken, waarbij spelers een Micro:bit-gamepad gebruiken om hun LED-indicator naar links en rechts te bewegen terwijl ze stenen ontwijken die van bovenaf vallen. Er zijn drie staten: a) een dynamisch pictogram bij het opstarten, b) real-time ontwijkingsacties tijdens het spelen, en c) een eindscore na botsingen.

Spelers verdienen 1 punt na elke ontwijking (wanneer de steen de onderkant bereikt), en het spel is afgelopen wanneer ze botsen met een steen; de eindscore wordt weergegeven met een scrolleffect.

Het spel kan worden gestart of gereset door zowel A+B in te drukken. Dit eenvoudige gameplay-mechanisme combineert real-time responsiviteit met strategische anticipatie.

![Img](./media/bottom1.png)

#### 5.2.5.2 Benodigde onderdelen

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 board** (zelf mee te nemen) ×1 | **micro:bit Smart Gamepad** (gemonteerd) ×1 | **AAA battery** (zelf mee te nemen) ×4 |

#### 5.2.5.3 Codestroom

![Img](./media/5001.png)

#### 5.2.5.4 Testcode

⚠️ **Merk op dat de initiële drempel `brick_move_speed=300` kan worden aangepast aan uw behoeften. Hoe hoger de waarde, hoe langzamer de steen zal vallen.**

**Volledige code:**

```python
import utime
import random
from microbit import *

# ===================== Global Configuration & Variables =====================
# Player initial configuration (micro:bit pixel coordinates: col=column(0-4, left-right), row=row(0-4, top-bottom))
player_fixed_row = 4    # Player\'s fixed row (bottom row)
player_init_col = 4     # Player\'s initial column (rightmost)
brick_move_speed = 300  # Brick falling interval (ms)

# Game state: 0=not started 1=running 2=game over
game_state = 0
brick_x = 0             # Brick current column (left-right)
brick_y = 0             # Brick current row (top-bottom)
score = 0               # Score counter
a_pressed_flag = False  # Left move button debounce flag
b_pressed_flag = False  # Right move button debounce flag
collision_x = False     # Collision detection - same column
collision_y = False     # Collision detection - same row
flash_count = 0         # End screen flash counter
time_passed = 0         # Time difference (for brick falling)
current_time = 0        # Current timestamp
last_brick_time = 0     # Last brick falling timestamp
start_flag = 0          # Start button debounce flag
can_start = False       # Game start flag
ab_pressed = False      # A+B pressed simultaneously flag
player_col = player_init_col  # Player\'s current column

# Initialize pins with pull-up (PULL_UP: pressed=low level 0, released=high level 1)
pin13.set_pull(pin13.PULL_UP)  # Right move button
pin15.set_pull(pin15.PULL_UP)  # Left move button

# ===================== Core Functions =====================
def on_start():
    """Initialization on power-up: randomly generate initial brick column"""
    global brick_x
    brick_x = random.randint(0, 4)

def draw_game():
    """Draw game screen: player (bright) + brick (dim)"""
    global game_state, player_col, brick_x, brick_y
    display.clear()
    # Draw player (fixed at bottom row, brightness 9 = brightest)
    display.set_pixel(player_col, player_fixed_row, 9)
    # Draw brick during gameplay (brightness 3 = dim)
    if game_state == 1:
        display.set_pixel(brick_x, brick_y, 7)

def reset_game():
    """Reset all game states"""
    global game_state, player_col, brick_x, brick_y, score
    global a_pressed_flag, b_pressed_flag
    game_state = 1
    player_col = player_init_col
    brick_x = random.randint(0, 4)
    brick_y = 0
    score = 0
    a_pressed_flag = False
    b_pressed_flag = False
    display.clear()

def check_collision():
    """Collision detection: game over if brick is in same column and row as player"""
    global collision_x, collision_y, game_state, flash_count
    collision_x = (brick_x == player_col)
    collision_y = (brick_y == player_fixed_row)
    if collision_x and collision_y:
        game_state = 2
        display.clear()
        flash_count = 0

# ===================== Main Loop =====================
def on_forever():
    """Main game logic loop"""
    global ab_pressed, can_start, start_flag, last_brick_time
    global flash_count, player_col, a_pressed_flag, b_pressed_flag
    global current_time, time_passed, brick_x, brick_y, score

    # 1. A+B pressed simultaneously: start/reset game (debounced)
    ab_pressed = button_a.is_pressed() and button_b.is_pressed()
    can_start = ab_pressed and (game_state != 1)
    if can_start:
        if start_flag == 0:
            start_flag = 1
            utime.sleep_ms(20)
            if button_a.is_pressed() and button_b.is_pressed():
                reset_game()
                last_brick_time = running_time()
    else:
        start_flag = 0

    # 2. Game not started state
    if game_state == 0:
        display.show(Image.DIAMOND_SMALL)
        utime.sleep_ms(500)
        display.show(Image.DIAMOND)
        utime.sleep_ms(500)

    # 3. Game over state
    if game_state == 2:
        if flash_count < 3:
            display.scroll(score)
            utime.sleep_ms(300)
            display.clear()
            utime.sleep_ms(200)
            flash_count += 1
        else:
            display.scroll(score)
            utime.sleep_ms(500)

    # 4. Game running logic
    if game_state == 1:
        # Left move button (pin15): fix level detection + set flag only on successful move
        if not pin15.read_digital():  # Pressed = low level 0, trigger left move
            if not a_pressed_flag:
                if player_col > 0:
                    player_col -= 1
                    a_pressed_flag = True  # Only set flag on successful move
                    utime.sleep_ms(50)
        else:
            a_pressed_flag = False  # Reset flag immediately when button is released

        # Right move button (pin13): fix level detection + set flag only on successful move
        if not pin13.read_digital():  # Pressed = low level 0, trigger right move
            if not b_pressed_flag:
                if player_col < 4:
                    player_col += 1
                    b_pressed_flag = True  # Only set flag on successful move
                    utime.sleep_ms(50)
        else:
            b_pressed_flag = False  # Reset flag immediately when button is released

        # Brick falling logic
        current_time = running_time()
        time_passed = current_time - last_brick_time
        if time_passed > brick_move_speed:
            last_brick_time = current_time
            brick_y += 1
            if brick_y > 4:
                brick_x = random.randint(0, 4)
                brick_y = 0
                score += 1

        # Collision detection + screen refresh
        check_collision()
        draw_game()

# ===================== Program Entry Point =====================
if __name__ == "__main__":
    on_start()
    while True:
        on_forever()
        utime.sleep_ms(10)
```

![Img](./media/line1.png)

**Korte uitleg:**

① Importeer bibliotheken, configureer constanten en initialisatie.

Het importeert eerst `utime` voor tijdgerelateerde bewerkingen (bijv. vertragingen), `random` voor het genereren van willekeurige getallen, `microbit` voor toegang tot de hardware van de Micro:bit.

Vervolgens definieert het globale variabelen en constanten om het spel te configureren:

*   `player_fixed_row` en `player_init_col` definiëren de initiële positie van de speler (in de meest rechtse kolom van de onderste rij).
*   `brick_move_speed` stelt het tijdsinterval (in milliseconden) van de val van de steen in.
*   `game_state` houdt de spelstatus bij (0=initieel, 1=spelend, 2=game over).
*   `brick_x`, `brick_y` slaan de huidige coördinaten van de steen op.
*   `score` registreert de score.
*   `a_pressed_flag`, `b_pressed_flag` elimineren knopjitter.
*   `collision_x`, `collision_y` detecteert botsing.
*   `flash_count` creëert een flikkereffect aan het einde van het spel.
*   `time_passed`, `current_time`, `last_brick_time` is voor het timen van de val van stenen.
*   `start_flag`, `can_start`, `ab_pressed` wordt gebruikt voor het starten van het spel en om anti-jitter en knopstatus te resetten.
*   `player_col` slaat de huidige kolompositie van de speler op.

Ten slotte configureert het `pin13` en `pin15` (gebruikt voor linker- en rechterknopbewegingen) als interne pull-up-weerstanden (`pinX.PULL_UP`), wat betekent dat pinnen een hoog niveau (1) behouden wanneer de knoppen niet zijn ingedrukt en een laag niveau (0) wanneer ze zijn ingedrukt.

```python
import utime
import random
from microbit import *

# ===================== Global Configuration & Variables =====================
# Player initial configuration (micro:bit pixel coordinates: col=column(0-4, left-right), row=row(0-4, top-bottom))
player_fixed_row = 4    # Player\'s fixed row (bottom row)
player_init_col = 4     # Player\'s initial column (rightmost)
brick_move_speed = 300  # Brick falling interval (ms)

# Game state: 0=not started 1=running 2=game over
game_state = 0
brick_x = 0             # Brick current column (left-right)
brick_y = 0             # Brick current row (top-bottom)
score = 0               # Score counter
a_pressed_flag = False  # Left move button debounce flag
b_pressed_flag = False  # Right move button debounce flag
collision_x = False     # Collision detection - same column
collision_y = False     # Collision detection - same row
flash_count = 0         # End screen flash counter
time_passed = 0         # Time difference (for brick falling)
current_time = 0        # Current timestamp
last_brick_time = 0     # Last brick falling timestamp
start_flag = 0          # Start button debounce flag
can_start = False       # Game start flag
ab_pressed = False      # A+B pressed simultaneously flag
player_col = player_init_col  # Player\'s current column

# Initialize pins with pull-up (PULL_UP: pressed=low level 0, released=high level 1)
pin13.set_pull(pin13.PULL_UP)  # Right move button
pin15.set_pull(pin15.PULL_UP)  # Left move button
```

② Definitie van kernfunctionele functies.

Er zijn drie kernfuncties die het spel nodig heeft:

*   `on_start()`: Wordt aangeroepen bij het opstarten van het programma. Het initialiseert voornamelijk de startkolompositie van stenen, zodat er willekeurig één verschijnt tussen 0 en 4.
*   `draw_game()`: Verantwoordelijk voor het weergeven van spelelementen op de Micro:bit 5x5 LED-matrix. Het wist het display en toont de speler met maximale helderheid (9) in de onderste rij `player_fixed_row` met kolommen bepaald door `player_col`. Wanneer het spel draait (`game_state == 1`), worden stenen weergegeven met gemiddelde helderheid (7).
*   `reset_game()`: Reset het spel naar de oorspronkelijke staat. Het stelt `game_state` in op 1, reset speler en steen en scores, wist de knop-anti-jitter-vlag en het display.
*   `check_collision()`: Detecteert of er een botsing plaatsvindt tussen de steen en de speler. Dit wordt bepaald door de as `x` (`brick_x == player_col`) en `y` (`brick_y == player_fixed_row`) te vergelijken. Als beide overeenkomen, wordt een botsing gedetecteerd en wordt `game_state` = 2 (game over), wordt het display gewist en wordt `flash_count` gereset.

```python
# ===================== Core Functions =====================
def on_start():
    """Initialization on power-up: randomly generate initial brick column"""
    global brick_x
    brick_x = random.randint(0, 4)

def draw_game():
    """Draw game screen: player (bright) + brick (dim)"""
    global game_state, player_col, brick_x, brick_y
    display.clear()
    # Draw player (fixed at bottom row, brightness 9 = brightest)
    display.set_pixel(player_col, player_fixed_row, 9)
    # Draw brick during gameplay (brightness 3 = dim)
    if game_state == 1:
        display.set_pixel(brick_x, brick_y, 7)

def reset_game():
    """Reset all game states"""
    global game_state, player_col, brick_x, brick_y, score
    global a_pressed_flag, b_pressed_flag
    game_state = 1
    player_col = player_init_col
    brick_x = random.randint(0, 4)
    brick_y = 0
    score = 0
    a_pressed_flag = False
    b_pressed_flag = False
    display.clear()

def check_collision():
    """Collision detection: game over if brick is in same column and row as player"""
    global collision_x, collision_y, game_state, flash_count
    collision_x = (brick_x == player_col)
    collision_y = (brick_y == player_fixed_row)
    if collision_x and collision_y:
        game_state = 2
        display.clear()
        flash_count = 0
```

③ Hoofdloop: Spel Start/Reset Logica.

`on_forever()` controleert eerst of zowel de A- als de B-knoppen op het Micro:bit-bord zijn ingedrukt (`button_a.is_pressed() and button_b.is_pressed()`). De `can_start`-vlag is waar wanneer zowel de A- als de B-knoppen tegelijkertijd zijn ingedrukt en het spel niet draait.

Als `can_start` waar is en `start_flag` = 0 (de eerste gedetecteerde gelijktijdige druk op A+B), stel `start_flag` in op 1 met een korte vertraging (`utime.sleep_ms(20)`).

Controleer opnieuw of de A+B-knoppen ingedrukt blijven (voor anti-jitter). Zo ja, dan zal `reset_game()` het spel opnieuw starten, en `last_brick_time` wordt vastgelegd. Als de A+B niet tegelijkertijd worden ingedrukt, is `start_flag` = 0.

```python
# ===================== Main Loop =====================
def on_forever():
    """Main game logic loop"""
    global ab_pressed, can_start, start_flag, last_brick_time
    global flash_count, player_col, a_pressed_flag, b_pressed_flag
    global current_time, time_passed, brick_x, brick_y, score

    # 1. A+B pressed simultaneously: start/reset game (debounced)
    ab_pressed = button_a.is_pressed() and button_b.is_pressed()
    can_start = ab_pressed and (game_state != 1)
    if can_start:
        if start_flag == 0:
            start_flag = 1
            utime.sleep_ms(20)
            if button_a.is_pressed() and button_b.is_pressed():
                reset_game()
                last_brick_time = running_time()
    else:
        start_flag = 0
```

④ Hoofdloop: Weergave van de niet-gestarte en game-over status van het spel.
*   **Spel is nog niet gestart. (`game_state == 0`)**: In deze staat toont de matrix kleine diamanten (`Image.DIAMOND_SMALL`) en grote diamanten (`Image.DIAMOND`) die elk 500 ms duren, als een indicatie voor spelers om te wachten voordat ze beginnen.
*   **Spel is afgelopen (`game_state == 2`)**: Wanneer het spel eindigt, gaat het programma een lus in die de score laat knipperen. `flash_count` beperkt het aantal flitsen (hier 3). Elke flits toont de huidige score, en wist deze met een korte vertraging. Daarna wordt de eindscore opnieuw 500 milliseconden weergegeven.

```python
    # 2. Game not started state
    if game_state == 0:
        display.show(Image.DIAMOND_SMALL)
        utime.sleep_ms(500)
        display.show(Image.DIAMOND)
        utime.sleep_ms(500)

    # 3. Game over state
    if game_state == 2:
        if flash_count < 3:
            display.scroll(score)
            utime.sleep_ms(300)
            display.clear()
            utime.sleep_ms(200)
            flash_count += 1
        else:
            display.scroll(score)
            utime.sleep_ms(500)
```
⑤ Hoofdloop: De logica tijdens het spelen.

`game_state == 1` (spelend), voer de volgende logica uit:

*   **Speler beweegt naar links en rechts.**:
    *   `pin15` (linkerbewegingsknop): Als `pin15` wordt ingedrukt (leest 0), `a_pressed_flag` is `False` (voorkom opeenvolgende triggers), en de speler is niet helemaal links (`player_col > 0`), zal de speler één spatie naar links bewegen (`player_col -= 1`) en `a_pressed_flag` wordt `True`, met een vertraging van 50 ms. Als `pin15` niet wordt ingedrukt, wordt `a_pressed_flag` gereset naar `False`.
    *   `pin13` (rechterbewegingsknop): Als `pin13` wordt ingedrukt (leest 0), `a_pressed_flag` is `False` (voorkom opeenvolgende triggers), en de speler is niet helemaal rechts (`player_col < 4`), zal de speler één spatie naar rechts bewegen (`player_col += 1`) en `b_pressed_flag` wordt `True`, met een vertraging van 50 ms. Als `pin13` niet wordt ingedrukt, wordt `b_pressed_flag` gereset naar `False`.
*   **Steen valt naar beneden**:
    *   `current_time` krijgt de huidige tijd, `time_passed` berekent de verstreken tijd sinds de laatste steen viel.
    *   Als `time_passed` > `brick_move_speed`, werk `last_brick_time` bij en de steen beweegt één spatie naar beneden (`brick_y += 1`).
    *   Als een steen tot de bodem valt (`brick_y > 4`), reset deze dan naar een willekeurige kolom bovenaan (`brick_x = random.randint(0, 4)`), en zet `brick_y` op nul en `score` +1.
*   **Detecteer botsing en render afbeelding**:
    *   `check_collision()` detecteert of de speler en de steen botsen.
    *   `draw_game()` werkt het display op de Micro:bit-matrix bij.

```python
    # 4. Game running logic
    if game_state == 1:
        # Left move button (pin15): fix level detection + set flag only on successful move
        if not pin15.read_digital():  # Pressed = low level 0, trigger left move
            if not a_pressed_flag:
                if player_col > 0:
                    player_col -= 1
                    a_pressed_flag = True  # Only set flag on successful move
                    utime.sleep_ms(50)
        else:
            a_pressed_flag = False  # Reset flag immediately when button is released

        # Right move button (pin13): fix level detection + set flag only on successful move
        if not pin13.read_digital():  # Pressed = low level 0, trigger right move
            if not b_pressed_flag:
                if player_col < 4:
                    player_col += 1
                    b_pressed_flag = True  # Only set flag on successful move
                    utime.sleep_ms(50)
        else:
            b_pressed_flag = False  # Reset flag immediately when button is released

        # Brick falling logic
        current_time = running_time()
        time_passed = current_time - last_brick_time
        if time_passed > brick_move_speed:
            last_brick_time = current_time
            brick_y += 1
            if brick_y > 4:
                brick_x = random.randint(0, 4)
                brick_y = 0
                score += 1

        # Collision detection + screen refresh
        check_collision()
        draw_game()
```

⑥ Programma-ingangspunt.

Dit is het daadwerkelijke startpunt voor de uitvoering van het programma.

`if __name__ == "__main__":` zorgt ervoor dat deze code alleen wordt uitgevoerd wanneer het script als hoofdprogramma draait.

Daarin voert `on_start()` een eenmalige initialisatie uit.
Vervolgens wordt een oneindige lus (`while True`) ingegaan, waarbij elke iteratie:

*   `on_forever()` alle kernlogica van het spel uitvoert.
*   Een vertraging van 10 ms (`utime.sleep_ms(10)`) regelt de uitvoeringsfrequentie, vermindert de CPU-belasting en zorgt voor een matige updatesnelheid van het spel.

```python
# ===================== Program Entry Point =====================
if __name__ == "__main__":
    on_start()
    while True:
        on_forever()
        utime.sleep_ms(10)
```
#### 5.2.5.5 Testresultaat

![Img](./media/4top.png)

Na het branden van de code, plaatst u het micro:bit-bord in de sleuf van de gamepad (**batterijen geïnstalleerd**), en zet u de schakelaar op “ON”.

Het bevindt zich in de **0-initiële staat** na het inschakelen en de matrix knippert twee vierkante pictogrammen.

Druk op A en B (gedurende ten minste 1 seconde) om het spel te starten (in de **1-spelende** staat), en een steen zal in een willekeurige kolom vallen. Nu kunt u naar links/rechts bewegen door op C/E te drukken. Elke keer dat u een steen ontwijkt, score+1.

Game over bij botsing (**2-game over**), en de eindscore wordt weergegeven op de matrix. Als u nog een ronde wilt spelen, drukt u opnieuw op A en B. Schakel uit om het spel te verlaten (zet de DIP-schakelaar op “OFF”).

![Img](./media/5000.gif)

<span style="color: rgb(0, 209, 0);">**Tip:** Als er geen reactie is op het bord, druk dan op de resetknop aan de achterkant van het micro:bit-bord.</span>

![Img](./media/4bottom.png)
