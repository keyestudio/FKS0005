### 5.2.5 Ziegelsteine vermeiden

#### 5.2.5.1 Übersicht

![Img](./media/top1.png)

In diesem Projekt spielen wir ein Ziegelstein-Vermeidungsspiel, bei dem die Spieler ein Micro:bit-Gamepad verwenden, um ihren LED-Indikator nach links und rechts zu bewegen, während sie von oben fallenden Ziegelsteinen ausweichen. Es gibt drei Zustände: a) ein dynamisches Symbol beim Start, b) Echtzeit-Vermeidungsaktionen während des Spiels und c) eine Endpunktzahl nach Kollisionen.

Spieler erhalten 1 Punkt nach jeder Vermeidung (wenn der Ziegelstein den Boden erreicht), und das Spiel ist beendet, wenn sie mit einem Ziegelstein kollidieren; die Endpunktzahl wird mit einem Scrolleffekt angezeigt.

Das Spiel kann durch gleichzeitiges Drücken von A+B gestartet oder zurückgesetzt werden. Dieser unkomplizierte Spielmechanismus kombiniert Echtzeit-Reaktionsfähigkeit mit strategischer Antizipation.

![Img](./media/bottom1.png)

#### 5.2.5.2 Benötigte Teile

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 Board** (selbst mitgebracht) ×1 | **micro:bit Smart Gamepad** (montiert) ×1 | **AAA Batterie** (selbst mitgebracht) ×4 |

#### 5.2.5.3 Codeablauf

![Img](./media/5001.png)

#### 5.2.5.4 Testcode

⚠️ **Beachten Sie, dass der anfängliche Schwellenwert „brick_move_speed=300“ je nach Bedarf geändert werden kann. Je höher der Wert ist, desto langsamer fällt der Ziegelstein.**

**Vollständiger Code:**


```python
import utime
import random
from microbit import *

# ===================== Global Configuration & Variables =====================
# Player initial configuration (micro:bit pixel coordinates: col=column(0-4, left-right), row=row(0-4, top-bottom))
player_fixed_row = 4    # Player's fixed row (bottom row)
player_init_col = 4     # Player's initial column (rightmost)
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
player_col = player_init_col  # Player's current column

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

**Kurze Erklärung:**

① Bibliotheken importieren, Konstanten konfigurieren und initialisieren.

Es importiert zuerst `utime` für zeitbezogene Operationen (z. B. Verzögerungen), `random` zum Generieren von Zufallszahlen, `microbit` für den Zugriff auf die Hardware des Micro:bit.

Anschließend werden globale Variablen und Konstanten zur Konfiguration des Spiels definiert:

*   `player_fixed_row` und `player_init_col` definieren die anfängliche Position des Spielers (in der rechtesten Spalte der untersten Reihe).
*   `brick_move_speed` legt das Zeitintervall (in Millisekunden) des Falls des Ziegelsteins fest.
*   `game_state` verfolgt den Spielstatus (0=initial, 1=spielend, 2=Spiel vorbei).
*   `brick_x`, `brick_y` speichern die aktuellen Koordinaten des Ziegelsteins.
*   `score` zählt die Punkte.
*   `a_pressed_flag`, `b_pressed_flag` eliminieren Tastenprellen.
*   `collision_x`, `collision_y` erkennen Kollisionen.
*   `flash_count` erzeugt einen Flackereffekt am Ende des Spiels.
*   `time_passed`, `current_time`, `last_brick_time` dienen zur Zeitmessung des Falls der Ziegelsteine.
*   `start_flag`, `can_start`, `ab_pressed` werden für den Spielstart und zum Zurücksetzen des Anti-Jitters und des Tastenstatus verwendet.
*   `player_col` speichert die aktuelle Spaltenposition des Spielers.

Schließlich konfiguriert es `pin13` und `pin15` (für linke und rechte Tastenbewegungen verwendet) als interne Pull-up-Widerstände (`pinX.PULL_UP`), was bedeutet, dass die Pins einen hohen Pegel (1) beibehalten, wenn die Tasten nicht gedrückt werden, und einen niedrigen Pegel (0), wenn sie gedrückt werden.

```python
import utime
import random
from microbit import *

# ===================== Global Configuration & Variables =====================
# Player initial configuration (micro:bit pixel coordinates: col=column(0-4, left-right), row=row(0-4, top-bottom))
player_fixed_row = 4    # Player's fixed row (bottom row)
player_init_col = 4     # Player's initial column (rightmost)
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
player_col = player_init_col  # Player's current column

# Initialize pins with pull-up (PULL_UP: pressed=low level 0, released=high level 1)
pin13.set_pull(pin13.PULL_UP)  # Right move button
pin15.set_pull(pin15.PULL_UP)  # Left move button
```

② Definitionen der Kernfunktionen.

Es gibt drei Kernfunktionen, die das Spiel benötigt:

*   `on_start()` : Wird beim Programmstart aufgerufen. Es initialisiert hauptsächlich die Startspaltenposition der Ziegelsteine und stellt sicher, dass einer zufällig zwischen 0 und 4 erscheint.
*   `draw_game()` : Verantwortlich für das Rendern von Spielelementen auf der Micro:bit 5x5 LED-Matrix. Es löscht die Anzeige und zeigt den Spieler mit maximaler Helligkeit (9) in der untersten Reihe `player_fixed_row` mit Spalten, die durch `player_col` bestimmt werden. Wenn das Spiel läuft (`game_state == 1`), rendert es Ziegelsteine mit mittlerer Helligkeit (7).
*   `reset_game()` : Setzt das Spiel in seinen Ausgangszustand zurück. Es setzt `game_state` auf 1, setzt Spieler und Ziegelstein sowie Punkte zurück, löscht das Tasten-Anti-Jitter-Flag und die Anzeige.
*   `check_collision()` : Erkennt, ob eine Kollision zwischen dem Ziegelstein und dem Spieler auftritt. Dies wird durch den Vergleich der Achsen `x` (`brick_x == player_col`) und `y` (`brick_y == player_fixed_row`) bestimmt. Wenn beide übereinstimmen, wird eine Kollision erkannt und `game_state` = 2 (Spiel vorbei), die Anzeige wird gelöscht und `flash_count` zurückgesetzt.

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

③ Hauptschleife: Spielstart-/Reset-Logik.

`on_forever()` überprüft zuerst, ob sowohl die A- als auch die B-Taste auf dem Micro:bit-Board gedrückt sind (`button_a.is_pressed() and button_b.is_pressed()`). Das Flag `can_start` ist wahr, wenn sowohl A als auch B gleichzeitig gedrückt werden und das Spiel nicht läuft.

Wenn `can_start` wahr ist und `start_flag` = 0 (der erste erkannte gleichzeitige Druck von A+B), setzen Sie `start_flag` auf 1 mit einer kurzen Verzögerung (`utime.sleep_ms(20)`).

Überprüfen Sie erneut, ob die A+B-Tasten gedrückt bleiben (zur Entprellung). Wenn ja, startet `reset_game()` das Spiel neu, und `last_brick_time` wird aufgezeichnet. Wenn A+B nicht gleichzeitig gedrückt werden, ist `start_flag` = 0.

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

④ Hauptschleife: Anzeige des Spiel-nicht-gestartet- und Spiel-vorbei-Status.
*   **Spiel noch nicht gestartet (`game_state == 0`)**: In diesem Zustand zeigt die Matrix kleine Diamanten (`Image.DIAMOND_SMALL`) und große Diamanten (`Image.DIAMOND`) an, die jeweils 500 ms dauern, als Hinweis für die Spieler, vor dem Start zu warten.
*   **Spiel ist vorbei (`game_state == 2`)**: Wenn das Spiel endet, tritt das Programm in eine Schleife ein, die die Punktzahl blinken lässt. `flash_count` begrenzt die Anzahl der Blitze (hier 3). Jeder Blitz scrollt die aktuelle Punktzahl und löscht sie mit einer kurzen Verzögerung. Danach wird die Endpunktzahl für 500 Millisekunden erneut angezeigt.

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

⑤ Hauptschleife: Die Logik während des Spiels.

`game_state == 1` (spielend), führen Sie die folgende Logik aus:

*   **Spieler bewegt sich nach links und rechts.**:
    *   `pin15` (linke Bewegungstaste): Wenn `pin15` gedrückt wird (Lesewert 0), `a_pressed_flag` `False` ist (vermeidet aufeinanderfolgende Auslöser) und der Spieler nicht ganz links ist (`player_col > 0`), bewegt sich der Spieler einen Platz nach links (`player_col -= 1`) und `a_pressed_flag` wird `True`, mit einer Verzögerung von 50 ms. Wenn `pin15` nicht gedrückt wird, wird `a_pressed_flag` sofort auf `False` zurückgesetzt.
    *   `pin13` (rechte Bewegungstaste): Wenn `pin13` gedrückt wird (Lesewert 0), `a_pressed_flag` `False` ist (vermeidet aufeinanderfolgende Auslöser) und der Spieler nicht ganz rechts ist (`player_col < 4`), bewegt sich der Spieler einen Platz nach rechts (`player_col += 1`) und `b_pressed_flag` wird `True`, mit einer Verzögerung von 50 ms. Wenn `pin13` nicht gedrückt wird, wird `b_pressed_flag` sofort auf `False` zurückgesetzt.
*   **Ziegelstein fällt herunter**:
    *   `current_time` erhält die aktuelle Zeit, `time_passed` berechnet die seit dem letzten Ziegelsteinfall verstrichene Zeit.
    *   Wenn `time_passed` > `brick_move_speed`, aktualisieren Sie `last_brick_time` und der Ziegelstein bewegt sich einen Platz nach unten (`brick_y += 1`).
    *   Wenn ein Ziegelstein bis zum Boden fällt (`brick_y > 4`), setzen Sie ihn auf eine zufällige Spalte oben zurück (`brick_x = random.randint(0, 4)`), und setzen Sie `brick_y` auf Null und `score` +1.
*   **Kollision erkennen und Bild rendern**:
    *   `check_collision()` erkennt, ob der Spieler und der Ziegelstein kollidieren.
    *   `draw_game()` aktualisiert die Anzeige auf der Micro:bit-Matrix.

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

⑥ Programmeinstiegspunkt.

Dies ist der eigentliche Startpunkt für die Ausführung des Programms.

`if __name__ == "__main__":` stellt sicher, dass dieser Code nur ausgeführt wird, wenn das Skript als Hauptprogramm läuft.

Darunter führt `on_start()` eine einmalige Initialisierung durch.
Dann tritt es in eine Endlosschleife (`while True`) ein, wobei jede Iteration:

*   `on_forever()` die gesamte Kernlogik des Spiels ausführt.
*   Eine Verzögerung von 10 ms (`utime.sleep_ms(10)`) steuert die Ausführungsfrequenz, reduziert die CPU-Last und sorgt für eine moderate Spielaktualisierungsgeschwindigkeit.

```python
# ===================== Program Entry Point =====================
if __name__ == "__main__":
    on_start()
    while True:
        on_forever()
        utime.sleep_ms(10)
```
#### 5.2.5.5 Testergebnis

![Img](./media/4top.png)

Nach dem Brennen des Codes stecken Sie das micro:bit-Board in den Steckplatz des Gamepads (**Batterien eingelegt**) und schalten Sie den Schalter auf „ON“.

Es befindet sich nach dem Einschalten im **0-Initialzustand** und die Matrix blinkt zwei quadratische Symbole.

Drücken Sie A und B (für mindestens 1 Sekunde), um das Spiel zu starten (im **1-Spielzustand**), und ein Ziegelstein fällt in einer zufälligen Spalte. Jetzt können Sie sich durch Drücken von C/E nach links/rechts bewegen. Jedes Mal, wenn Sie einem Ziegelstein ausweichen, erhöht sich die Punktzahl um 1.

Spiel vorbei bei Kollision (**2-Spiel vorbei**), und die Endpunktzahl wird auf der Matrix angezeigt. Wenn Sie eine weitere Runde spielen möchten, drücken Sie A und B erneut. Schalten Sie das Gerät aus, um das Spiel zu beenden (schalten Sie den DIP-Schalter auf „OFF“).

![Img](./media/5000.gif)

<span style="color: rgb(0, 209, 0);">**Tipp:** Wenn das Board nicht reagiert, drücken Sie bitte die Reset-Taste auf der Rückseite des micro:bit-Boards.</span>

![Img](./media/4bottom.png)
