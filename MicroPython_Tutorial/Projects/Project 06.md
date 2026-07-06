### 5.2.6 Sasso-Carta-Forbici

#### 5.2.6.1 Panoramica

![Img](./media/top1.png)

Qui, giochiamo a sasso-carta-forbici tramite comunicazione wireless di micro:bit. I giocatori selezionano la loro mossa (sasso, carta o forbici) tramite i pulsanti, con scambio di dati tra i dispositivi. Il gioco segue il meglio di tre; se tutti e tre i round finiscono in parità o vittoria-sconfitta-parità, viene attivata una quarta partita.

Ogni risultato viene visualizzato sulla matrice micro:bit (W per vittoria, L per sconfitta, = per parità) e rivelato dalle luci RGB (verde per vittoria, rosso per sconfitta, giallo per parità) sul pin P8. Al completamento di un round, i due dispositivi resettano tutti i dati e le luci, preparandosi per la partita successiva.

Il gameplay integra perfettamente l'interazione wireless con il combattimento multi-round.

![Img](./media/bottom1.png)

#### 5.2.6.2 Conoscenza dei Componenti

Questo progetto utilizza la stessa comunicazione wireless Microbit, LED RGB SK6812 e pulsanti del Progetto 06. Si prega di fare riferimento alla sezione 4.2.6.2 per la conoscenza dei suoi componenti.

#### 5.2.6.3 Parti Richieste

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **Scheda micro:bit V2** (auto-fornita) ×2 | **Smart Gamepad micro:bit** (assemblato) ×2 | **Batteria AAA** (auto-fornita) ×8 |

#### 5.2.6.4 Flusso del Codice

![Img](./media/6002.png)

#### 5.2.6.5 Codice di Test

**Codice completo:**

```python
from microbit import *
import neopixel
import radio
import utime

# Variabili globali
round_num = 1
my_choice = 0
your_choice = 0
wins = 0
losses = 0
draws = 0
game_results = []

# Configurazione dei NeoPixel (collegati a P8, 4 LED)
np = neopixel.NeoPixel(pin8, 4)

# Configura i pin dei pulsanti
pin13.set_pull(pin13.PULL_UP) # Pulsante D (Carta)
pin15.set_pull(pin15.PULL_UP) # Pulsante C (Forbici)
pin16.set_pull(pin16.PULL_UP) # Pulsante E (Sasso)

# Funzione per resettare lo stato del gioco
def reset_game_state():
    global my_choice, your_choice, round_num, wins, losses, draws, game_results
    my_choice = 0
    your_choice = 0
    round_num = 1
    wins = 0
    losses = 0
    draws = 0
    game_results = []
    clear_lights()
    display.show(Image.HEART)

# Funzione per spegnere tutti i LED
def clear_lights():
    for i in range(len(np)):
        np[i] = (0, 0, 0)
    np.show()

# Funzione per mostrare il risultato del round sui LED
def show_round_result_lights(round_index, result):
    if round_index < len(np):
        if result == 1: # Vittoria: Verde
            np[round_index] = (0, 255, 0)
        elif result == 0: # Pareggio: Giallo
            np[round_index] = (255, 255, 0)
        else: # Sconfitta: Rosso
            np[round_index] = (255, 0, 0)
        np.show()

# Funzione per determinare se è necessario un quarto round
def needs_fourth_round():
    if draws == 3: # Tutti pareggi
        return 2 # Quarto round decisivo
    if wins == 1 and losses == 1 and draws == 1: # Vittoria-sconfitta-pareggio
        return 1 # Quarto round
    return 0 # Nessun quarto round

# Gestore messaggi radio
def on_received_message(msg):
    global your_choice
    if your_choice == 0:
        try:
            choice = int(msg)
            if choice in [1, 2, 3]:
                your_choice = choice
        except ValueError:
            pass

# Inizializzazione radio
radio.on()
radio.config(group=1)
radio.receive_full = True # Ricevi messaggi completi

reset_game_state()

while True:
    # Processa i messaggi radio in arrivo
    incoming = radio.receive()
    if incoming:
        on_received_message(incoming.decode())

    # Se entrambi i giocatori hanno fatto una scelta
    if my_choice != 0 and your_choice != 0:
        result_symbol = "="
        current_round_result = 0 # 0: pareggio, 1: vittoria, -1: sconfitta

        if my_choice == your_choice:
            result_symbol = "="
            draws += 1
        elif (my_choice == 1 and your_choice == 3) or \
             (my_choice == 2 and your_choice == 1) or \
             (my_choice == 3 and your_choice == 2):
            result_symbol = "W"
            current_round_result = 1
            wins += 1
        else:
            result_symbol = "L"
            current_round_result = -1
            losses += 1

        game_results.append(current_round_result)
        display.show(result_symbol)
        show_round_result_lights(round_num - 1, current_round_result)
        utime.sleep_ms(3000)

        if round_num == 3:
            fourth_round_needed = needs_fourth_round()
            if fourth_round_needed:
                round_num = 4
                if fourth_round_needed == 2:
                    display.scroll("FINAL")
                utime.sleep_ms(1000)
                display.show(Image.HEART)
                my_choice = 0
                your_choice = 0
            else:
                if wins > losses:
                    display.scroll("WINNER")
                elif losses > wins:
                    display.scroll("LOSER")
                else:
                    display.scroll("TIE")
                utime.sleep_ms(3000)
                reset_game_state()
        elif round_num == 4:
            display.scroll("GAME OVER")
            utime.sleep_ms(3000)
            reset_game_state()
        else:
            round_num += 1
            display.show(Image.HEART)
            my_choice = 0
            your_choice = 0

    # Gestione dei pulsanti per la scelta del giocatore
    if my_choice == 0:
        if not pin15.read_digital(): # Pulsante C (Forbici = 1)
            my_choice = 1
            radio.send(str(my_choice))
            display.show(Image("99009:99090:00900:99090:99009"))
            utime.sleep_ms(200)
        elif not pin16.read_digital(): # Pulsante E (Sasso = 2)
            my_choice = 2
            radio.send(str(my_choice))
            display.show(Image.SQUARE_SMALL)
            utime.sleep_ms(200)
        elif not pin13.read_digital(): # Pulsante D (Carta = 3)
            my_choice = 3
            radio.send(str(my_choice))
            display.show(Image.SQUARE)
            utime.sleep_ms(200)

    utime.sleep_ms(100)
```

![Img](./media/line1.png)

**Breve spiegazione:**

① Inizializza la radio e imposta il gruppo su '1'; imposta il numero di round, lo stato, l'avversario e il risultato di sasso-carta-forbici dei giocatori; collega le quattro luci RGB al pin P8 e aggiorna il display, imposta la matrice per mostrare ![Img](./media/6004.png).

```python
from microbit import *
import neopixel
import radio
import utime

# Variabili globali
round_num = 1
my_choice = 0
your_choice = 0
wins = 0
losses = 0
draws = 0
game_results = []

# Configurazione dei NeoPixel (collegati a P8, 4 LED)
np = neopixel.NeoPixel(pin8, 4)

# Configura i pin dei pulsanti
pin13.set_pull(pin13.PULL_UP) # Pulsante D (Carta)
pin15.set_pull(pin15.PULL_UP) # Pulsante C (Forbici)
pin16.set_pull(pin16.PULL_UP) # Pulsante E (Sasso)

# Funzione per resettare lo stato del gioco
def reset_game_state():
    global my_choice, your_choice, round_num, wins, losses, draws, game_results
    my_choice = 0
    your_choice = 0
    round_num = 1
    wins = 0
    losses = 0
    draws = 0
    game_results = []
    clear_lights()
    display.show(Image.HEART)

# Funzione per spegnere tutti i LED
def clear_lights():
    for i in range(len(np)):
        np[i] = (0, 0, 0)
    np.show()

# Funzione per mostrare il risultato del round sui LED
def show_round_result_lights(round_index, result):
    if round_index < len(np):
        if result == 1: # Vittoria: Verde
            np[round_index] = (0, 255, 0)
        elif result == 0: # Pareggio: Giallo
            np[round_index] = (255, 255, 0)
        else: # Sconfitta: Rosso
            np[round_index] = (255, 0, 0)
        np.show()

# Funzione per determinare se è necessario un quarto round
def needs_fourth_round():
    if draws == 3: # Tutti pareggi
        return 2 # Quarto round decisivo
    if wins == 1 and losses == 1 and draws == 1: # Vittoria-sconfitta-pareggio
        return 1 # Quarto round
    return 0 # Nessun quarto round

# Gestore messaggi radio
def on_received_message(msg):
    global your_choice
    if your_choice == 0:
        try:
            choice = int(msg)
            if choice in [1, 2, 3]:
                your_choice = choice
        except ValueError:
            pass

# Inizializzazione radio
radio.on()
radio.config(group=1)
radio.receive_full = True # Ricevi messaggi completi

reset_game_state()
```

② Determina l'esito del round corrente: se la tua scelta corrisponde a quella dell'avversario (**1/2/3 per forbici/sasso/carta**), è un pareggio; altrimenti, seleziona un vincitore (forbici contro carta contro sasso contro forbici), il valore del round +1 e memorizza il risultato.

```python
    # Se entrambi i giocatori hanno fatto una scelta
    if my_choice != 0 and your_choice != 0:
        result_symbol = "="
        current_round_result = 0 # 0: pareggio, 1: vittoria, -1: sconfitta

        if my_choice == your_choice:
            result_symbol = "="
            draws += 1
        elif (my_choice == 1 and your_choice == 3) or \
             (my_choice == 2 and your_choice == 1) or \
             (my_choice == 3 and your_choice == 2):
            result_symbol = "W"
            current_round_result = 1
            wins += 1
        else:
            result_symbol = "L"
            current_round_result = -1
            losses += 1

        game_results.append(current_round_result)
        display.show(result_symbol)
        show_round_result_lights(round_num - 1, current_round_result)
        utime.sleep_ms(3000)
```

③ Memorizza i risultati in un array e visualizza la stringa corrispondente. Se questa è la terza partita, determina se è necessaria una quarta partita (in caso di parità o vittoria-sconfitta-parità). In tal caso, visualizza "FINAL" e attendi 1 secondo prima di cancellare la selezione sasso-carta-forbici.

```python
        if round_num == 3:
            fourth_round_needed = needs_fourth_round()
            if fourth_round_needed:
                round_num = 4
                if fourth_round_needed == 2:
                    display.scroll("FINAL")
                utime.sleep_ms(1000)
                display.show(Image.HEART)
                my_choice = 0
                your_choice = 0
            else:
                if wins > losses:
                    display.scroll("WINNER")
                elif losses > wins:
                    display.scroll("LOSER")
                else:
                    display.scroll("TIE")
                utime.sleep_ms(3000)
                reset_game_state()
        elif round_num == 4:
            display.scroll("GAME OVER")
            utime.sleep_ms(3000)
            reset_game_state()
        else:
            round_num += 1
            display.show(Image.HEART)
            my_choice = 0
            your_choice = 0
```

④ Premi C e la scheda invia "1" come forbici, e la matrice mostra ![Img](./media/6011.png); premi D e la scheda invia "3" come carta, e la matrice mostra ![Img](./media/6012.png); Premi E e invia "2" come sasso e mostra ![Img](./media/6013.png).

```python
    # Gestione dei pulsanti per la scelta del giocatore
    if my_choice == 0:
        if not pin15.read_digital(): # Pulsante C (Forbici = 1)
            my_choice = 1
            radio.send(str(my_choice))
            display.show(Image("99009:99090:00900:99090:99009"))
            utime.sleep_ms(200)
        elif not pin16.read_digital(): # Pulsante E (Sasso = 2)
            my_choice = 2
            radio.send(str(my_choice))
            display.show(Image.SQUARE_SMALL)
            utime.sleep_ms(200)
        elif not pin13.read_digital(): # Pulsante D (Carta = 3)
            my_choice = 3
            radio.send(str(my_choice))
            display.show(Image.SQUARE)
            utime.sleep_ms(200)
```

⑤ Ricevi i dati radio (scelta dell'avversario).

```python
    # Processa i messaggi radio in arrivo
    incoming = radio.receive()
    if incoming:
        on_received_message(incoming.decode())
```

⑥ Determina se è necessario un quarto round. Se tutti e tre i giochi finiscono in parità o vittoria-sconfitta-parità, è necessario un quarto gioco; altrimenti, non è necessario.

```python
def needs_fourth_round():
    if draws == 3: # Tutti pareggi
        return 2 # Quarto round decisivo
    if wins == 1 and losses == 1 and draws == 1: # Vittoria-sconfitta-pareggio
        return 1 # Quarto round
    return 0 # Nessun quarto round
```

⑦ Le luci RGB visualizzano i colori corrispondenti in base all'esito: verde per la vittoria, rosso per la sconfitta e giallo per un pareggio.

```python
def show_round_result_lights(round_index, result):
    if round_index < len(np):
        if result == 1: # Vittoria: Verde
            np[round_index] = (0, 255, 0)
        elif result == 0: # Pareggio: Giallo
            np[round_index] = (255, 255, 0)
        else: # Sconfitta: Rosso
            np[round_index] = (255, 0, 0)
        np.show()
```

⑧ Quando il gioco finisce, cancella il display delle quattro luci RGB.

```python
def clear_lights():
    for i in range(len(np)):
        np[i] = (0, 0, 0)
    np.show()
```

⑨ Resetta lo stato del gioco, cancella tutti i valori delle variabili di gioco, resetta le luci RGB e mostra ![Img](./media/6004.png).

```python
def reset_game_state():
    global my_choice, your_choice, round_num, wins, losses, draws, game_results
    my_choice = 0
    your_choice = 0
    round_num = 1
    wins = 0
    losses = 0
    draws = 0
    game_results = []
    clear_lights()
    display.show(Image.HEART)
```

#### 5.2.6.6 Risultato del Test

![Img](./media/4top.png)

Dopo aver caricato il codice, inserisci la scheda micro:bit nello slot del gamepad (**batterie installate**) e sposta l'interruttore su “ON”.

La matrice mostra inizialmente ![Img](./media/6004.png). I giocatori premono i pulsanti per selezionare la loro mossa (E per sasso, D per carta o C per forbici), con scambio di dati tra i due dispositivi. Determinano l'esito del round corrente: una vittoria è indicata dalla "W" con la luce RGB che diventa verde, un pareggio dalla "=" con la luce gialla e una sconfitta dalla "L" con la luce rossa (la prima luce RGB si accende dopo il primo round, e così via). Il round successivo seguirà se il gioco non è finito.

Il gioco adotta il meglio di tre: se tutti e tre i round finiscono in parità o vittoria-sconfitta-parità, viene attivata una quarta partita.

Se c'è un vincitore dopo tre round, visualizzerà "WINNER" per la vittoria e "LOSER" per la sconfitta. Una volta mostrato il risultato, apparirà "GAME OVER" per resettare il gioco. Se il quarto round rimane indeciso, anche il gioco sarà finito.

![Img](./media/6000.gif)

<span style="color: rgb(0, 209, 0);">**Suggerimento:** Attendi che l'icona a forma di cuore appaia prima di continuare il round successivo. Se non c'è risposta sulla scheda, premi il pulsante di reset sul retro della scheda micro:bit.</span>

![Img](./media/4bottom.png)
