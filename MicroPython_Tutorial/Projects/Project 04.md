### 5.2.4 Lettore Musicale

#### 5.2.4.1 Panoramica

![Img](./media/top1.png)

Qui costruiamo un lettore musicale che genera suoni tramite il buzzer integrato sulla scheda micro:bit (non riproduce musica vocale). Dispone di una libreria di 20 brevi tracce e supporta sia la riproduzione sequenziale che casuale.

In modalità sequenziale, premendo il pulsante C (Canzone precedente) o E (Canzone successiva) si cambiano le tracce secondo una sequenza preimpostata fino a raggiungere la fine dell'elenco; mentre in modalità casuale, ogni pressione seleziona una traccia a caso tra i 20 suoni con le luci colorate che lampeggiano, e quando una canzone finisce si ferma immediatamente.

Nel frattempo, la matrice LED micro:bit visualizza la modalità di riproduzione corrente in tempo reale.

![Img](./media/bottom1.png)

#### 5.2.4.2 Parti Richieste

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **Scheda micro:bit V2** (auto-fornita) ×1 | **Smart Gamepad micro:bit** (assemblato) ×1 | **Batteria AAA** (auto-fornita) ×4 |

#### 5.2.4.3 Flusso del Codice

![Img](./media/4001.png)

#### 5.2.4.4 Codice di Test

**Codice completo:**

```python
from microbit import *
import music
import random
import neopixel
import utime

# Configurazione dei NeoPixel (collegati a P8, 4 LED)
np = neopixel.NeoPixel(pin8, 4)

# Definizioni delle melodie (20 tracce)
melodies = [
    music.DADADADUM,
    music.ENTERTAINER,
    music.PRELUDE,
    music.ODE,
    music.NYAN,
    music.RINGTONE,
    music.FUNK,
    music.BLUES,
    music.BIRTHDAY,
    music.WEDDING,
    music.FUNERAL,
    music.PUNCHLINE,
    music.PYTHON,
    music.BADDY,
    music.CHASE,
    music.WAWAWAWAA,
    music.JUMP_UP,
    music.JUMP_DOWN,
    music.POWER_UP,
    music.POWER_DOWN
]

# Variabili di stato del lettore musicale
current_melody_index = 0
play_mode = 0  # 0: sequenziale, 1: casuale
volume = 128   # Volume iniziale (0-255)

# Variabili per l'animazione delle luci RGB
hue = 0

# Funzione per impostare tutti i LED su nero (spenti)
def clear_lights():
    for i in range(len(np)):
        np[i] = (0, 0, 0)
    np.show()

# Funzione per convertire HSV in RGB (per l'effetto respiro)
def hsv_to_rgb(h, s, v):
    # h: 0-359, s: 0-99, v: 0-99
    h_i = int(h * 6 / 100)
    f = h * 6 / 100 - h_i
    p = v * (100 - s) / 100
    q = v * (100 - f * s) / 100
    t = v * (100 - (1 - f) * s) / 100

    r, g, b = 0, 0, 0
    if h_i == 0: r, g, b = v, t, p
    if h_i == 1: r, g, b = q, v, p
    if h_i == 2: r, g, b = p, v, t
    if h_i == 3: r, g, b = p, q, v
    if h_i == 4: r, g, b = t, p, v
    if h_i == 5: r, g, b = v, p, q

    return (int(r * 2.55), int(g * 2.55), int(b * 2.55))

# Configura i pin dei pulsanti
pin13.set_pull(pin13.PULL_UP) # Pulsante D (modalità sequenziale)
pin15.set_pull(pin15.PULL_UP) # Pulsante C (canzone precedente/casuale)
pin16.set_pull(pin16.PULL_UP) # Pulsante E (canzone successiva/casuale)
pin14.set_pull(pin14.PULL_UP) # Pulsante F (modalità casuale)
pin5.set_pull(pin5.PULL_UP)   # Pulsante A (volume su)
pin11.set_pull(pin11.PULL_UP)  # Pulsante B (volume giù)

# Inizializzazione
clear_lights()
music.set_volume(volume)
display.show(Image.MUSIC)

last_button_press_time = utime.ticks_ms()
BTN_DEBOUNCE = 200 # Debounce per i pulsanti

while True:
    current_time = utime.ticks_ms()

    # Gestione del debounce dei pulsanti
    if utime.ticks_diff(current_time, last_button_press_time) > BTN_DEBOUNCE:
        # Pulsante D: Modalità sequenziale
        if not pin13.read_digital():
            play_mode = 0
            display.show(Image.ARROW_N)
            last_button_press_time = current_time
        # Pulsante F: Modalità casuale
        elif not pin14.read_digital():
            play_mode = 1
            display.show(Image.RABBIT)
            last_button_press_time = current_time
        # Pulsante C: Canzone precedente / Casuale
        elif not pin15.read_digital():
            if play_mode == 0: # Sequenziale
                current_melody_index = (current_melody_index - 1 + len(melodies)) % len(melodies)
            else: # Casuale
                current_melody_index = random.randint(0, len(melodies) - 1)
            music.stop()
            music.play(melodies[current_melody_index], wait=False)
            last_button_press_time = current_time
        # Pulsante E: Canzone successiva / Casuale
        elif not pin16.read_digital():
            if play_mode == 0: # Sequenziale
                current_melody_index = (current_melody_index + 1) % len(melodies)
            else: # Casuale
                current_melody_index = random.randint(0, len(melodies) - 1)
            music.stop()
            music.play(melodies[current_melody_index], wait=False)
            last_button_press_time = current_time
        # Pulsante A: Volume su
        elif not pin5.read_digital():
            volume = min(255, volume + 10)
            music.set_volume(volume)
            last_button_press_time = current_time
        # Pulsante B: Volume giù
        elif not pin11.read_digital():
            volume = max(0, volume - 10)
            music.set_volume(volume)
            last_button_press_time = current_time

    # Animazione delle luci RGB (effetto respiro)
    hue = (hue + 1) % 360
    rgb_color = hsv_to_rgb(hue, 99, 20) # Saturazione alta, luminosità bassa
    for i in range(len(np)):
        np[i] = rgb_color
    np.show()

    # Se la musica è finita in modalità casuale, fermala
    if play_mode == 1 and not music.is_playing():
        music.stop()

    sleep(50) # Breve ritardo per il loop principale
```

![Img](./media/line1.png)

**Breve spiegazione:**

① Inizializza la matrice LED e il volume del suono, collega il pin RGB a P8 e imposta il numero di RGB a 4.

```python
from microbit import *
import music
import random
import neopixel
import utime

# Configurazione dei NeoPixel (collegati a P8, 4 LED)
np = neopixel.NeoPixel(pin8, 4)

# Definizioni delle melodie (20 tracce)
melodies = [
    music.DADADADUM,
    music.ENTERTAINER,
    music.PRELUDE,
    music.ODE,
    music.NYAN,
    music.RINGTONE,
    music.FUNK,
    music.BLUES,
    music.BIRTHDAY,
    music.WEDDING,
    music.FUNERAL,
    music.PUNCHLINE,
    music.PYTHON,
    music.BADDY,
    music.CHASE,
    music.WAWAWAWAA,
    music.JUMP_UP,
    music.JUMP_DOWN,
    music.POWER_UP,
    music.POWER_DOWN
]

# Variabili di stato del lettore musicale
current_melody_index = 0
play_mode = 0  # 0: sequenziale, 1: casuale
volume = 128   # Volume iniziale (0-255)

# Variabili per l'animazione delle luci RGB
hue = 0

# Funzione per impostare tutti i LED su nero (spenti)
def clear_lights():
    for i in range(len(np)):
        np[i] = (0, 0, 0)
    np.show()

# Funzione per convertire HSV in RGB (per l'effetto respiro)
def hsv_to_rgb(h, s, v):
    # h: 0-359, s: 0-99, v: 0-99
    h_i = int(h * 6 / 100)
    f = h * 6 / 100 - h_i
    p = v * (100 - s) / 100
    q = v * (100 - f * s) / 100
    t = v * (100 - (1 - f) * s) / 100

    r, g, b = 0, 0, 0
    if h_i == 0: r, g, b = v, t, p
    if h_i == 1: r, g, b = q, v, p
    if h_i == 2: r, g, b = p, v, t
    if h_i == 3: r, g, b = p, q, v
    if h_i == 4: r, g, b = t, p, v
    if h_i == 5: r, g, b = v, p, q

    return (int(r * 2.55), int(g * 2.55), int(b * 2.55))

# Configura i pin dei pulsanti
pin13.set_pull(pin13.PULL_UP) # Pulsante D (modalità sequenziale)
pin15.set_pull(pin15.PULL_UP) # Pulsante C (canzone precedente/casuale)
pin16.set_pull(pin16.PULL_UP) # Pulsante E (canzone successiva/casuale)
pin14.set_pull(pin14.PULL_UP) # Pulsante F (modalità casuale)
pin5.set_pull(pin5.PULL_UP)   # Pulsante A (volume su)
pin11.set_pull(pin11.PULL_UP)  # Pulsante B (volume giù)

# Inizializzazione
clear_lights()
music.set_volume(volume)
display.show(Image.MUSIC)

last_button_press_time = utime.ticks_ms()
BTN_DEBOUNCE = 200 # Debounce per i pulsanti
```

② Determina se il pulsante D o F è premuto. Premi D per '0-riproduzione sequenziale', F per '1-riproduzione casuale'.

```python
    # Pulsante D: Modalità sequenziale
    if not pin13.read_digital():
        play_mode = 0
        display.show(Image.ARROW_N)
        last_button_press_time = current_time
    # Pulsante F: Modalità casuale
    elif not pin14.read_digital():
        play_mode = 1
        display.show(Image.RABBIT)
        last_button_press_time = current_time
```

③ In modalità sequenziale, premi C per riprodurre la canzone precedente, E per passare alla canzone successiva.

```python
    # Pulsante C: Canzone precedente / Casuale
    elif not pin15.read_digital():
        if play_mode == 0: # Sequenziale
            current_melody_index = (current_melody_index - 1 + len(melodies)) % len(melodies)
        else: # Casuale
            current_melody_index = random.randint(0, len(melodies) - 1)
        music.stop()
        music.play(melodies[current_melody_index], wait=False)
        last_button_press_time = current_time
    # Pulsante E: Canzone successiva / Casuale
    elif not pin16.read_digital():
        if play_mode == 0: # Sequenziale
            current_melody_index = (current_melody_index + 1) % len(melodies)
        else: # Casuale
            current_melody_index = random.randint(0, len(melodies) - 1)
        music.stop()
        music.play(melodies[current_melody_index], wait=False)
        last_button_press_time = current_time
```

④ Fai respirare le luci RGB in sottofondo.

```python
    # Animazione delle luci RGB (effetto respiro)
    hue = (hue + 1) % 360
    rgb_color = hsv_to_rgb(hue, 99, 20) # Saturazione alta, luminosità bassa
    for i in range(len(np)):
        np[i] = rgb_color
    np.show()

    # Se la musica è finita in modalità casuale, fermala
    if play_mode == 1 and not music.is_playing():
        music.stop()

    sleep(50) # Breve ritardo per il loop principale
```

⑤ Premi A per aumentare il volume (+10); premi B per diminuirlo (-10). Il volume del buzzer micro:bit è deciso dalla tensione di uscita del pin interno collegato. Possiamo controllare il volume convertendo i valori digitali 0~255 in valori analogici tramite DAC.

```python
    # Pulsante A: Volume su
    elif not pin5.read_digital():
        volume = min(255, volume + 10)
        music.set_volume(volume)
        last_button_press_time = current_time
    # Pulsante B: Volume giù
    elif not pin11.read_digital():
        volume = max(0, volume - 10)
        music.set_volume(volume)
        last_button_press_time = current_time
```

#### 5.2.4.5 Risultato del Test

![Img](./media/4top.png)

Dopo aver caricato il codice, inserisci la scheda micro:bit nello slot del gamepad (**batterie installate**) e sposta l'interruttore su “ON”.

Dopo l'accensione, è in modalità sequenziale per impostazione predefinita e riprodurrà la canzone al N.O. “0”. Una volta terminata, puoi premere C per l'ultima canzone o E per la successiva.

Premi F per passare alla modalità casuale. E puoi premere D per tornare a quella sequenziale. In modalità F, una traccia casuale di queste 20 verrà riprodotta se premi C/E. Dopo aver terminato, si ferma.

Le luci RGB respirano sempre dal momento dell'accensione. Nel frattempo, la matrice LED micro:bit mostra “![Img](./media/4010.png)” in modalità sequenziale e “![Img](./media/4011.png)” in modalità casuale.

Per il volume, premi A per aumentare e B per diminuire.

![Img](./media/4015.gif)

<span style="color: rgb(0, 209, 0);">**Suggerimento:** Se non c'è risposta sulla scheda, premi il pulsante di reset sul retro della scheda micro:bit.</span>

![Img](./media/4bottom.png)
