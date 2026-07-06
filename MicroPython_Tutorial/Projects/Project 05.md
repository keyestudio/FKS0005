### 5.2.5 Evita i Mattoni

#### 5.2.5.1 Panoramica

![Img](./media/top1.png)

In questo progetto, giochiamo a un gioco di evitamento dei mattoni in cui i giocatori usano un gamepad Micro:bit per muovere il loro indicatore LED a sinistra e a destra mentre evitano i mattoni che cadono dall'alto. Ci sono tre stati: a) un'icona dinamica all'avvio, b) azioni di evitamento in tempo reale durante il gioco, e c) un punteggio finale dopo le collisioni.

I giocatori guadagnano 1 punto dopo ogni evitamento (quando il mattone raggiunge il fondo), e il gioco finisce quando si scontrano con un mattone; il punteggio finale viene visualizzato con un effetto di scorrimento.

Il gioco può essere avviato o resettato premendo entrambi i pulsanti A+B. Questo meccanismo di gioco semplice combina la reattività in tempo reale con l'anticipazione strategica.

![Img](./media/bottom1.png)

#### 5.2.5.2 Parti Richieste

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **Scheda micro:bit V2** (auto-fornita) ×1 | **Smart Gamepad micro:bit** (assemblato) ×1 | **Batteria AAA** (auto-fornita) ×4 |

#### 5.2.5.3 Flusso del Codice

![Img](./media/5001.png)

#### 5.2.5.4 Codice di Test

⚠️ **Nota che la soglia iniziale 300 nel codice può essere modificata in base alle proprie esigenze. Più alto è il valore, più lentamente cadrà il mattone.**

**Codice completo:**

```python
from microbit import *
import random
import utime

# Variabili di gioco
game_state = 0  # 0: Iniziale, 1: In gioco, 2: Game Over
player_col = 2  # Colonna iniziale del giocatore
brick_x = random.randint(0, 4) # Colonna iniziale del mattone
brick_y = 0     # Riga iniziale del mattone
score = 0
brick_move_speed = 300 # Velocità di caduta del mattone (ms)
last_brick_time = utime.ticks_ms()
flash_count = 0 # Conteggio lampeggi per Game Over

# Flag per il debounce dei pulsanti
a_pressed_flag = False
b_pressed_flag = False
start_button_pressed = False

# Configura i pin dei pulsanti
pin13.set_pull(pin13.PULL_UP) # Pulsante E (destra)
pin15.set_pull(pin15.PULL_UP) # Pulsante C (sinistra)
pin5.set_pull(pin5.PULL_UP)   # Pulsante A
pin11.set_pull(pin11.PULL_UP)  # Pulsante B

# Funzione per disegnare il gioco sulla matrice LED
def draw_game():
    display.clear()
    if game_state == 1: # In gioco
        display.set_pixel(player_col, 4, 9) # Giocatore in basso
        display.set_pixel(brick_x, brick_y, 5) # Mattone
    elif game_state == 0: # Iniziale
        if utime.ticks_ms() % 1000 < 500: # Lampeggia
            display.show(Image.SQUARE)
        else:
            display.show(Image.SQUARE_SMALL)
    elif game_state == 2: # Game Over
        if flash_count < 3:
            display.scroll(str(score))
            utime.sleep(0.5)
            display.clear()
            utime.sleep(0.5)
        else:
            display.scroll(str(score))

# Funzione per resettare il gioco
def reset_game():
    global game_state, player_col, brick_x, brick_y, score, flash_count
    game_state = 1
    player_col = 2
    brick_x = random.randint(0, 4)
    brick_y = 0
    score = 0
    flash_count = 0
    display.clear()

# Funzione per controllare le collisioni
def check_collision():
    global game_state
    if brick_y == 4 and brick_x == player_col:
        game_state = 2 # Game Over
        display.clear()

# Loop principale del gioco
while True:
    # Gestione dei pulsanti A+B per avviare/resettare il gioco
    if not pin5.read_digital() and not pin11.read_digital(): # A e B premuti
        if not start_button_pressed:
            start_button_pressed = True
            utime.sleep_ms(50) # Debounce
            if not pin5.read_digital() and not pin11.read_digital(): # Conferma pressione
                reset_game()
    else:
        start_button_pressed = False

    if game_state == 1: # In gioco
        # Movimento del giocatore (C per sinistra, E per destra)
        if not pin15.read_digital(): # Pulsante C (sinistra)
            if not a_pressed_flag:
                if player_col > 0:
                    player_col -= 1
                    a_pressed_flag = True
                    utime.sleep_ms(50)
        else:
            a_pressed_flag = False

        if not pin13.read_digital(): # Pulsante E (destra)
            if not b_pressed_flag:
                if player_col < 4:
                    player_col += 1
                    b_pressed_flag = True
                    utime.sleep_ms(50)
        else:
            b_pressed_flag = False

        # Caduta del mattone
        current_time = utime.ticks_ms()
        if utime.ticks_diff(current_time, last_brick_time) > brick_move_speed:
            last_brick_time = current_time
            brick_y += 1
            if brick_y > 4: # Mattone ha raggiunto il fondo
                brick_x = random.randint(0, 4)
                brick_y = 0
                score += 1

        check_collision()

    draw_game()
    utime.sleep_ms(10) # Breve ritardo per il loop
```

![Img](./media/line1.png)

**Breve spiegazione:**

① Inizializza le variabili correlate, inclusa la colonna iniziale del giocatore, la riga e la velocità del mattone, e imposta la posizione del giocatore sulla colonna iniziale.

Chiama una funzione on_start.

```python
from microbit import *
import random
import utime

# Variabili di gioco
game_state = 0  # 0: Iniziale, 1: In gioco, 2: Game Over
player_col = 2  # Colonna iniziale del giocatore
brick_x = random.randint(0, 4) # Colonna iniziale del mattone
brick_y = 0     # Riga iniziale del mattone
score = 0
brick_move_speed = 300 # Velocità di caduta del mattone (ms)
last_brick_time = utime.ticks_ms()
flash_count = 0 # Conteggio lampeggi per Game Over

# Flag per il debounce dei pulsanti
a_pressed_flag = False
b_pressed_flag = False
start_button_pressed = False

# Configura i pin dei pulsanti
pin13.set_pull(pin13.PULL_UP) # Pulsante E (destra)
pin15.set_pull(pin15.PULL_UP) # Pulsante C (sinistra)
pin5.set_pull(pin5.PULL_UP)   # Pulsante A
pin11.set_pull(pin11.PULL_UP)  # Pulsante B

# Funzione per disegnare il gioco sulla matrice LED
def draw_game():
    display.clear()
    if game_state == 1: # In gioco
        display.set_pixel(player_col, 4, 9) # Giocatore in basso
        display.set_pixel(brick_x, brick_y, 5) # Mattone
    elif game_state == 0: # Iniziale
        if utime.ticks_ms() % 1000 < 500: # Lampeggia
            display.show(Image.SQUARE)
        else:
            display.show(Image.SQUARE_SMALL)
    elif game_state == 2: # Game Over
        if flash_count < 3:
            display.scroll(str(score))
            utime.sleep(0.5)
            display.clear()
            utime.sleep(0.5)
        else:
            display.scroll(str(score))

# Funzione per resettare il gioco
def reset_game():
    global game_state, player_col, brick_x, brick_y, score, flash_count
    game_state = 1
    player_col = 2
    brick_x = random.randint(0, 4)
    brick_y = 0
    score = 0
    flash_count = 0
    display.clear()

# Funzione per controllare le collisioni
def check_collision():
    global game_state
    if brick_y == 4 and brick_x == player_col:
        game_state = 2 # Game Over
        display.clear()
```

② Per quanto riguarda questa funzione, fa apparire il mattone in una colonna casuale da 0 a 4 all'inizio del gioco.

```python
# Loop principale del gioco
while True:
    # Gestione dei pulsanti A+B per avviare/resettare il gioco
    if not pin5.read_digital() and not pin11.read_digital(): # A e B premuti
        if not start_button_pressed:
            start_button_pressed = True
            utime.sleep_ms(50) # Debounce
            if not pin5.read_digital() and not pin11.read_digital(): # Conferma pressione
                reset_game()
    else:
        start_button_pressed = False
```

③ Determina se “A+B è premuto e il gioco non è iniziato”. Se sì e l'avvio è contrassegnato come stato iniziale, contrassegna prima lo stato di avvio e conferma di nuovo se i pulsanti sono ancora premuti dopo un breve ritardo. Se lo sono, resetta il gioco (chiama la funzione reset_game) e registra il tempo. Altrimenti, annulla il contrassegno di avvio.

```python
    if game_state == 0: # Iniziale
        if utime.ticks_ms() % 1000 < 500: # Lampeggia
            display.show(Image.SQUARE)
        else:
            display.show(Image.SQUARE_SMALL)
```

④ La seguente funzione resetta il gioco allo stato iniziale. Imposta lo stato su “gaming” (game_state=1) e posiziona il giocatore nella posizione iniziale. E il mattone apparirà in una colonna casuale (0~4) e nella riga 0, e i punteggi si azzerano. Infine, la pressione di A/B è contrassegnata come non attivata, e la matrice viene quindi cancellata.

```python
# Funzione per resettare il gioco
def reset_game():
    global game_state, player_col, brick_x, brick_y, score, flash_count
    game_state = 1
    player_col = 2
    brick_x = random.randint(0, 4)
    brick_y = 0
    score = 0
    flash_count = 0
    display.clear()
```

⑤ Quando lo stato del gioco è **0-stato iniziale** (non in gioco dopo l'accensione), l'icona visualizzata lampeggerà.

```python
    elif game_state == 0: # Iniziale
        if utime.ticks_ms() % 1000 < 500: # Lampeggia
            display.show(Image.SQUARE)
        else:
            display.show(Image.SQUARE_SMALL)
```

⑥ Quando è **2-game over**, il punteggio sarà controllato in base al conteggio dei lampeggi (flash_count). Se il conteggio <3, ripete “mostra punteggio → breve ritardo → cancella display → breve ritardo → conteggio+1”; quando il conteggio raggiunge 3, mostra sempre il punteggio ed estende il ritardo.

```python
    elif game_state == 2: # Game Over
        if flash_count < 3:
            display.scroll(str(score))
            utime.sleep(0.5)
            display.clear()
            utime.sleep(0.5)
        else:
            display.scroll(str(score))
```

⑦ Nello stato **1-gaming**, quando si preme C senza attivare il contrassegno di pressione e la colonna del giocatore > 0, la colonna del giocatore -1 e contrassegna il pulsante C come attivato (con ritardo per anti-jitter); premere E senza attivare e quando la colonna del giocatore < 4, e la colonna +1 con E attivato (ritardo); se non viene eseguita alcuna azione, il contrassegno di attivazione dei pulsanti corrispondenti viene resettato.

```python
    if game_state == 1: # In gioco
        # Movimento del giocatore (C per sinistra, E per destra)
        if not pin15.read_digital(): # Pulsante C (sinistra)
            if not a_pressed_flag:
                if player_col > 0:
                    player_col -= 1
                    a_pressed_flag = True
                    utime.sleep_ms(50)
        else:
            a_pressed_flag = False

        if not pin13.read_digital(): # Pulsante E (destra)
            if not b_pressed_flag:
                if player_col < 4:
                    player_col += 1
                    b_pressed_flag = True
                    utime.sleep_ms(50)
        else:
            b_pressed_flag = False
```

⑧ Calcola la differenza tra il tempo corrente e l'ultimo tempo di movimento del mattone. Se questa differenza supera la soglia di velocità del mattone, aggiorna il tempo di movimento del mattone e la riga del mattone +1. Se la riga > 4 (raggiungendo il bordo), resetta il mattone a una colonna casuale con la sua riga=zero, e punteggio+1.

Chiama le funzioni di rilevamento delle collisioni e di rendering della grafica del gioco per far cadere i mattoni, resettare dopo aver raggiunto il bordo, accumulare il punteggio e aggiornare lo stato del gioco in tempo reale.

Invoca le funzioni di rilevamento delle collisioni e di rendering della grafica del gioco per ottenere l'avanzamento automatico dei mattoni, il reset del bordo, l'accumulo del punteggio e gli aggiornamenti dello stato del gioco in tempo reale.

```python
        # Caduta del mattone
        current_time = utime.ticks_ms()
        if utime.ticks_diff(current_time, last_brick_time) > brick_move_speed:
            last_brick_time = current_time
            brick_y += 1
            if brick_y > 4: # Mattone ha raggiunto il fondo
                brick_x = random.randint(0, 4)
                brick_y = 0
                score += 1

        check_collision()
```

⑨ Determina se il gioco è finito: prima controlla se “la colonna del mattone corrisponde a quella del giocatore” e “se la riga del mattone corrisponde a quella del giocatore”. Se entrambe le condizioni sono soddisfatte (cioè, i mattoni si sovrappongono al giocatore), imposta il gioco allo stato 2 (game over), cancella il display e resetta il conteggio dei lampeggi.

“Game over in caso di collisione.”

```python
# Funzione per controllare le collisioni
def check_collision():
    global game_state
    if brick_y == 4 and brick_x == player_col:
        game_state = 2 # Game Over
        display.clear()
```

⑩ Renderizza gli elementi visivi del gioco: prima cancella il display, e poi traccia i punti con una luminosità di 255 (Giocatore) alle posizioni fisse della riga e della colonna corrente del giocatore; se il gioco è iniziato (game_state=1), traccia i punti con una luminosità di 85 (mattone) alla riga e alla colonna del mattone. Così possiamo distinguere i mattoni dal giocatore in base alla loro luminosità.

```python
def draw_game():
    display.clear()
    if game_state == 1: # In gioco
        display.set_pixel(player_col, 4, 9) # Giocatore in basso
        display.set_pixel(brick_x, brick_y, 5) # Mattone
    elif game_state == 0: # Iniziale
        if utime.ticks_ms() % 1000 < 500: # Lampeggia
            display.show(Image.SQUARE)
        else:
            display.show(Image.SQUARE_SMALL)
    elif game_state == 2: # Game Over
        if flash_count < 3:
            display.scroll(str(score))
            utime.sleep(0.5)
            display.clear()
            utime.sleep(0.5)
        else:
            display.scroll(str(score))
```

#### 5.2.5.5 Risultato del Test

![Img](./media/4top.png)

Dopo aver caricato il codice, inserisci la scheda micro:bit nello slot del gamepad (**batterie installate**) e sposta l'interruttore su “ON”.

È nello **stato iniziale 0** dopo l'accensione e la matrice lampeggia due icone quadrate.

Premi A e B (per almeno 1 secondo) per avviare il gioco (nello **stato 1-gaming**), e un mattone cadrà in una colonna casuale. Ora puoi muoverti a sinistra/destra premendo C/E. Ogni volta che eviti un mattone, il punteggio +1.

Game over in caso di collisione (**2-game over**), e il punteggio finale verrà visualizzato sulla matrice. Se vuoi giocare un altro round, premi di nuovo A e B. Spegni per uscire dal gioco (sposta l'interruttore DIP su “OFF”).

![Img](./media/5000.gif)

<span style="color: rgb(0, 209, 0);">**Suggerimento:** Se non c'è risposta sulla scheda, premi il pulsante di reset sul retro della scheda micro:bit.</span>

![Img](./media/4bottom.png)
