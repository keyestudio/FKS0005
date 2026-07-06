### 5.2.7 Indovina il Numero

#### 5.2.7.1 Panoramica

![Img](./media/top1.png)

In questo progetto, giochiamo a un gioco di indovinazione del numero con una scheda Micro:bit, una scheda di controllo gamepad e un display OLED. Quando il numero corretto viene indovinato, l'OLED visualizza "Great!!!"; se l'ipotesi è troppo alta o troppo bassa, mostra rispettivamente "To High!"/"To Low!", insieme all'intervallo corrispondente di numeri possibili.

![Img](./media/bottom1.png)

#### 5.2.7.2 Parti Richieste

| ![Img](./media/microbitV2.png)|  ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **Scheda micro:bit V2** (auto-fornita) ×1 | **Smart Gamepad micro:bit** (assemblato) ×1 | **Batteria AAA** (auto-fornita) ×4 |
|![Img](./media/OLED.png)|![Img](./media/7008.png)||
|    **Display OLED** (auto-fornito)×1     |   **Cavo DuPont F-F**(auto-fornito) x4    ||

#### 5.2.7.3 Schema di Cablaggio

![Img](./media/jiexian8.png)

**Dopo aver cablato come mostrato sopra, inserisci la micro:bit nello slot sulla scheda di controllo del gamepad.**

| Display OLED | Scheda di controllo gamepad micro:bit | Pin scheda micro:bit |
| :----------: | :-----------------------------: | :-----------------: |
|     GND      |               GND               |         GND         |
|     VCC      |               3V                |         3V          |
|     SDA      |               SDA               |         P20         |
|     SCL      |               SCL               |         P19         |

#### 5.2.7.4 Flusso del Codice

![Img](./media/8001.png)

#### 5.2.7.5 Codice di Test

⚠️ **Nota che qui è inclusa la libreria OLED, quindi dobbiamo importare: https://github.com/keyestudio/pxt-environment-kit-master**.

**Codice completo:**

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

**Breve spiegazione:**

① Importa le librerie, inizializza l'OLED, definisci le variabili globali e configura i pin dei pulsanti.

Sono richieste tre librerie: `microbit` (per accedere all'hardware Micro:bit), `oled_ssd1306` (per controllare il display OLED collegato), `random` (per generare numeri casuali nel gioco).

`initialize()` e `clear_oled()` inizializzano e cancellano l'OLED.

Una serie di variabili globali sono definite per gestire i parametri dello stato del gioco, inclusi la modalità di gioco (`mode`), l'intervallo numerico (`min_num`, `max_num`), il valore di ipotesi corrente (`current_guess`), il numero target (`target_num`), il feedback del gioco (`state`) e un flag che controlla gli aggiornamenti del display (`update_display`).

`pin13`, `pin15` e `pin16` sono configurati in modalità pull-up — mantenendo un livello alto quando il pulsante non è premuto e un livello basso quando premuto.

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

② Logica di inizializzazione del gioco nel loop principale.

È il primo blocco logico del loop principale del programma, specificamente responsabile dell'inizializzazione o del riavvio del gioco.

`mode` = `0` : il gioco richiede l'inizializzazione. In questo caso, resetta l'intervallo di ipotesi a 1–100 e imposta il valore di ipotesi corrente a 50. Utilizza `randint(min_num, max_num)` per generare casualmente un numero intero tra 1 e 100 come numero target (`target_num`).

Quindi, `state` = `0` (stato iniziale) e `mode` = `1` (in esecuzione). E imposta `update_display` su `True` per garantire che l'OLED aggiorni immediatamente le ultime informazioni di gioco durante l'esecuzione.

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

③ Gestisci gli input dei pulsanti e il processo decisionale basato sull'ipotesi.

Quando il gioco è in funzione (`mode == 1`), gestisce le interazioni del giocatore e la logica del gioco. Rileva indipendentemente gli input da tre pulsanti esterni:

*   **`pin15` è premuto**: (livello basso rilevato); `current_guess` + 1. Per evitare che il valore superi l'intervallo, controlla e limita `current_guess` < o = `max_num`.
*   **`pin13` è premuto**: `current_guess` - 1. Controlla anche che `current_guess` non sia maggiore di `min_num`.
*   **`pin16` è premuto**: Se `pin16` è premuto, significa che il giocatore ha inviato il valore di ipotesi. Verrà confrontato con `target_num`:
    *   `current_guess` > `target_num` : `state` = `1` (troppo alto) e imposta il massimo dell'intervallo `max_num` su `current_guess`.
    *   `current_guess` < `target_num `: `state` = `2` (troppo basso) e imposta il minimo `min_num` su `current_guess`.
    *   `current_guess` = `target_num` : `state` = `3` (Ottimo) e imposta `mode` su `0` per prepararsi al round successivo.

Dopo ogni pressione del pulsante, `update_display` viene impostato su `True` per aggiornare l'OLED, con un ritardo di 50ms per l'anti-jitter.

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

④ Logica di aggiornamento dell'OLED.

Visualizza lo stato e le informazioni attuali del gioco sull'OLED. Viene eseguito solo quando `update_display` = `True` per evitare aggiornamenti non necessari.

Ogni esecuzione chiama prima `clear_oled()` per cancellare il display. L'intervallo di ipotesi corrente (ad esempio, "num:1~100") appare sulla prima riga. L'ipotesi corrente del giocatore (`current_guess`) viene visualizzata sulla terza riga.

Basandosi su `state`, il messaggio di feedback corrispondente ("TO High," "TO Low," o "Great!!!") appare sulla quinta riga.

Dopo aver completato tutte le visualizzazioni, `update_display` viene resettato su `False` per essere pronto ad aggiornare la prossima modifica dello stato del gioco.

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

⑤ Gestisci i ritardi dopo le ipotesi corrette.

Viene eseguito solo quando il giocatore indovina correttamente il numero target (`state == 3`). Quindi, mette in pausa per 1000ms (1s) affinché i giocatori controllino il "Great!!!".

Quindi, `state` viene resettato a `0`. Poiché `mode` è già stato resettato a `0`, in caso di ipotesi corretta, il gioco ripartirà dall'inizializzazione.

```python
    # 4. Delay after correct guess to show message
    if state == 3:
        sleep(1000)
        state = 0
```

#### 5.2.7.6 Risultato del Test

![Img](./media/4top.png)

Dopo aver caricato il codice, inserisci la scheda micro:bit nello slot del gamepad (**batterie installate**) e sposta l'interruttore su “ON”.

Dopo aver caricato il codice, l'OLED si inizializza e mostra l'intervallo di valori di “num: 1 ~ 100” e l'ipotesi iniziale di 50. Puoi premere C per temp+1 (max di 100) o E per temp-1 (min di 1) per cambiare il tuo valore di ipotesi sull'OLED.

Premi D per inviare il tuo valore, e temp verrà confrontato con il valore target casuale. Se temp>value, mostra “To High!” e assegna temp a max_num; se temp<value, mostra “To Low!” e assegnale a min_num. Se sei troppo fortunato che temp=value, vedrai “Great!!!” per 1s.

Dopo di che, il gioco verrà resettato e verrà impostato un nuovo valore target. Giochiamo un altro round!

![Img](./media/t7000.gif)

⚠️ **Il blocco di costruzione nel Risultato del Test non è incluso in questo kit di prodotti.**

<span style="color: rgb(0, 209, 0);">**Suggerimento:** Se non c'è risposta sulla scheda, premi il pulsante di reset sul retro della scheda micro:bit.</span>

![Img](./media/4bottom.png)
