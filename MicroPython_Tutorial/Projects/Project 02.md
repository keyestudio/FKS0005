### 5.2.2 Luci Colorate

#### 5.2.2.1 Panoramica

![Img](./media/top1.png)

I LED RGB sono un tipo di sorgente luminosa a LED che crea immagini mescolando la luce dei tre colori primari: rosso, verde e blu, la cui intersezione produce varie tonalità. I metodi comuni includono la miscelazione diretta dei colori primari, l\utilizzo di un LED blu combinato con fosforo giallo, o l\impiego di un LED ultravioletto insieme a fosforo RGB. Rispetto ai LED che emettono luce bianca direttamente, i LED RGB offrono una gamma più ampia di possibilità di miscelazione dei colori perché i tre colori primari possono essere controllati indipendentemente.

In questo progetto, ogni pulsante corrisponde a una diversa modalità dei LED RGB. Quando si preme il pulsante C, le luci lampeggiano alternativamente nell\ordine di "rosso, verde, blu, giallo e viola"; premere D per passare alle luci a respiro; premere E per le luci a flusso d\acqua; premere F per le luci a scorrimento.

Stringhe di luci colorate per decorazioni festive, luci per alberi di Natale, strisce RGB per l\ambiente quotidiano, luci decorative a LED nei parchi di divertimento e nei centri commerciali... Sono tutti esempi comuni di luci multimodali nella nostra vita quotidiana.

![Img](./media/bottom1.png)

#### 5.2.2.2 Conoscenza dei Componenti

Questo progetto utilizza gli stessi LED RGB SK6812 e pulsanti del Progetto 02. Si prega di fare riferimento alla sezione 4.2.2.2 per la conoscenza dei suoi componenti.

#### 5.2.2.3 Parti Richieste

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **Scheda micro:bit V2** (auto-fornita) ×1 | **Smart Gamepad micro:bit** (assemblato) ×1 |**Batteria AAA** (auto-fornita) ×4 |

#### 5.2.2.4 Flusso del Codice

![Img](./media/2006.png)

#### 5.2.2.5 Codice di Test

⚠️ **Nota che il tempo di ritardo di MODE\*_DELAY nei codici può essere modificato in base alle proprie esigenze.**

**Codice completo:**

```python
from microbit import *
import neopixel
import utime

# Configurazione dei LED NeoPixel
# I NeoPixel sono collegati al pin P8 e ci sono 4 LED
np = neopixel.NeoPixel(pin8, 4)

# Variabili di stato
mode = 0  # 0: spento, 1: alternato, 2: respiro, 3: flusso d'acqua, 4: scorrimento
last_mode_change_time = utime.ticks_ms()
last_button_press_time = utime.ticks_ms()

# Tempi di ritardo per le modalità (in ms)
MODE1_DELAY = 500  # Alternato
MODE2_DELAY = 50   # Respiro
MODE3_DELAY = 100  # Flusso d'acqua
MODE4_DELAY = 150  # Scorrimento
BTN_DEBOUNCE = 100 # Debounce del pulsante

# Variabili per le animazioni
color_index = 0
hue = 0
water_flow_pos = 0
scroll_pos = 0

# Colori predefiniti per la modalità alternata (RGB)
colors = [
    (255, 0, 0),    # Rosso
    (0, 255, 0),    # Verde
    (0, 0, 255),    # Blu
    (255, 255, 0),  # Giallo
    (255, 0, 255)   # Viola
]

# Funzione per impostare tutti i LED su nero (spenti)
def clear_lights():
    for i in range(len(np)):
        np[i] = (0, 0, 0)
    np.show()

# Funzione per convertire HSV in RGB
def hsv_to_rgb(h, s, v):
    # h: 0-359, s: 0-99, v: 0-99
    h_i = int(h * 6 / 100)  # Converti h in 0-5 per l'indice del settore
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

    return (int(r * 2.55), int(g * 2.55), int(b * 2.55)) # Scala a 0-255

# Configura i pin dei pulsanti
pin13.set_pull(pin13.PULL_UP) # Pulsante D
pin15.set_pull(pin15.PULL_UP) # Pulsante C
pin16.set_pull(pin16.PULL_UP) # Pulsante E
pin14.set_pull(pin14.PULL_UP) # Pulsante F (assumendo P14 per F)

clear_lights()

while True:
    current_time = utime.ticks_ms()

    # Gestione del debounce dei pulsanti
    if utime.ticks_diff(current_time, last_button_press_time) > BTN_DEBOUNCE:
        if not pin15.read_digital(): # Pulsante C (alternato)
            mode = 1
            color_index = 0
            last_mode_change_time = current_time
            last_button_press_time = current_time
            clear_lights()
        elif not pin13.read_digital(): # Pulsante D (respiro)
            mode = 2
            hue = 0
            last_mode_change_time = current_time
            last_button_press_time = current_time
            clear_lights()
        elif not pin16.read_digital(): # Pulsante E (flusso d'acqua)
            mode = 3
            water_flow_pos = 0
            last_mode_change_time = current_time
            last_button_press_time = current_time
            clear_lights()
        elif not pin14.read_digital(): # Pulsante F (scorrimento)
            mode = 4
            scroll_pos = 0
            last_mode_change_time = current_time
            last_button_press_time = current_time
            clear_lights()

    # Logica delle modalità
    if mode == 1: # Alternato
        if utime.ticks_diff(current_time, last_mode_change_time) > MODE1_DELAY:
            last_mode_change_time = current_time
            clear_lights()
            np[0] = colors[color_index]
            np[1] = colors[(color_index + 1) % len(colors)]
            np[2] = colors[(color_index + 2) % len(colors)]
            np[3] = colors[(color_index + 3) % len(colors)]
            np.show()
            color_index = (color_index + 1) % len(colors)
    elif mode == 2: # Respiro
        if utime.ticks_diff(current_time, last_mode_change_time) > MODE2_DELAY:
            last_mode_change_time = current_time
            hue = (hue + 5) % 360 # Incrementa la tonalità
            rgb_color = hsv_to_rgb(hue, 99, 20) # Saturazione alta, luminosità bassa
            for i in range(len(np)):
                np[i] = rgb_color
            np.show()
    elif mode == 3: # Flusso d'acqua
        if utime.ticks_diff(current_time, last_mode_change_time) > MODE3_DELAY:
            last_mode_change_time = current_time
            clear_lights()
            np[water_flow_pos] = (0, 255, 255) # Ciano
            np.show()
            water_flow_pos = (water_flow_pos + 1) % len(np)
    elif mode == 4: # Scorrimento
        if utime.ticks_diff(current_time, last_mode_change_time) > MODE4_DELAY:
            last_mode_change_time = current_time
            clear_lights()
            np[scroll_pos] = (255, 165, 0) # Arancione
            np.show()
            scroll_pos = (scroll_pos + 1) % len(np)

    sleep(10) # Breve ritardo per il loop principale
```

![Img](./media/line1.png)

**Breve spiegazione:**

① All\inizio, disabilita la funzione dei LED (imposta led enable su false).

E definisci 4 ritardi LED (ad esempio, imposta 5 in modalità 2, imposta 500 in modalità 1...), imposta il debounce del pulsante su 20. Inizializza quattro LED RGB sul pin P8 a nessun colore (imposta tutti i valori a 0), cioè, imposta su spento.

```python
from microbit import *
import neopixel
import utime

# Configurazione dei LED NeoPixel
# I NeoPixel sono collegati al pin P8 e ci sono 4 LED
np = neopixel.NeoPixel(pin8, 4)

# Variabili di stato
mode = 0  # 0: spento, 1: alternato, 2: respiro, 3: flusso d'acqua, 4: scorrimento
last_mode_change_time = utime.ticks_ms()
last_button_press_time = utime.ticks_ms()

# Tempi di ritardo per le modalità (in ms)
MODE1_DELAY = 500  # Alternato
MODE2_DELAY = 50   # Respiro
MODE3_DELAY = 100  # Flusso d'acqua
MODE4_DELAY = 150  # Scorrimento
BTN_DEBOUNCE = 100 # Debounce del pulsante

# Variabili per le animazioni
color_index = 0
hue = 0
water_flow_pos = 0
scroll_pos = 0

# Colori predefiniti per la modalità alternata (RGB)
colors = [
    (255, 0, 0),    # Rosso
    (0, 255, 0),    # Verde
    (0, 0, 255),    # Blu
    (255, 255, 0),  # Giallo
    (255, 0, 255)   # Viola
]

# Funzione per impostare tutti i LED su nero (spenti)
def clear_lights():
    for i in range(len(np)):
        np[i] = (0, 0, 0)
    np.show()

# Funzione per convertire HSV in RGB
def hsv_to_rgb(h, s, v):
    # h: 0-359, s: 0-99, v: 0-99
    h_i = int(h * 6 / 100)  # Converti h in 0-5 per l'indice del settore
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

    return (int(r * 2.55), int(g * 2.55), int(b * 2.55)) # Scala a 0-255

# Configura i pin dei pulsanti
pin13.set_pull(pin13.PULL_UP) # Pulsante D
pin15.set_pull(pin15.PULL_UP) # Pulsante C
pin16.set_pull(pin16.PULL_UP) # Pulsante E
pin14.set_pull(pin14.PULL_UP) # Pulsante F (assumendo P14 per F)

clear_lights()
```

② Durante il ciclo, l\operazione anti-jitter viene implementata controllando se la differenza tra il tempo di esecuzione corrente e il tempo di pressione precedente supera la soglia anti-jitter preimpostata (BTN_DEBOUNCE), prevenendo così pressioni ripetute causate da jitter fisico.

```python
while True:
    current_time = utime.ticks_ms()

    # Gestione del debounce dei pulsanti
    if utime.ticks_diff(current_time, last_button_press_time) > BTN_DEBOUNCE:
        if not pin15.read_digital(): # Pulsante C (alternato)
            mode = 1
            color_index = 0
            last_mode_change_time = current_time
            last_button_press_time = current_time
            clear_lights()
        elif not pin13.read_digital(): # Pulsante D (respiro)
            mode = 2
            hue = 0
            last_mode_change_time = current_time
            last_button_press_time = current_time
            clear_lights()
        elif not pin16.read_digital(): # Pulsante E (flusso d'acqua)
            mode = 3
            water_flow_pos = 0
            last_mode_change_time = current_time
            last_button_press_time = current_time
            clear_lights()
        elif not pin14.read_digital(): # Pulsante F (scorrimento)
            mode = 4
            scroll_pos = 0
            last_mode_change_time = current_time
            last_button_press_time = current_time
            clear_lights()
```

③ Quando C(/D/E/F) viene premuto, la modalità viene impostata su 1(2/3/4), mentre i passaggi dell\animazione e i punti di inizio temporizzazione per la modalità corrispondente vengono resettati, le luci vengono cancellate e il timestamp del pulsante viene aggiornato. Ciò consente una commutazione precisa e un funzionamento iniziale di diverse modalità LED.

```python
    # Logica delle modalità
    if mode == 1: # Alternato
        if utime.ticks_diff(current_time, last_mode_change_time) > MODE1_DELAY:
            last_mode_change_time = current_time
            clear_lights()
            np[0] = colors[color_index]
            np[1] = colors[(color_index + 1) % len(colors)]
            np[2] = colors[(color_index + 2) % len(colors)]
            np[3] = colors[(color_index + 3) % len(colors)]
            np.show()
            color_index = (color_index + 1) % len(colors)
    elif mode == 2: # Respiro
        if utime.ticks_diff(current_time, last_mode_change_time) > MODE2_DELAY:
            last_mode_change_time = current_time
            hue = (hue + 5) % 360 # Incrementa la tonalità
            rgb_color = hsv_to_rgb(hue, 99, 20) # Saturazione alta, luminosità bassa
            for i in range(len(np)):
                np[i] = rgb_color
            np.show()
    elif mode == 3: # Flusso d'acqua
        if utime.ticks_diff(current_time, last_mode_change_time) > MODE3_DELAY:
            last_mode_change_time = current_time
            clear_lights()
            np[water_flow_pos] = (0, 255, 255) # Ciano
            np.show()
            water_flow_pos = (water_flow_pos + 1) % len(np)
    elif mode == 4: # Scorrimento
        if utime.ticks_diff(current_time, last_mode_change_time) > MODE4_DELAY:
            last_mode_change_time = current_time
            clear_lights()
            np[scroll_pos] = (255, 165, 0) # Arancione
            np.show()
            scroll_pos = (scroll_pos + 1) % len(np)

    sleep(10) # Breve ritardo per il loop principale
```

#### 5.2.2.6 Risultato del Test

![Img](./media/4top.png)

Dopo aver caricato il codice, inserisci la scheda micro:bit nello slot del gamepad (**batterie installate**) e sposta l\interruttore su “ON”.

Premi **C**: le luci si alternano tra **rosso-verde-blu-giallo-viola** in sequenza.

Premi **D**: la tonalità del colore delle luci aumenterà, e alla fine i colori sfumati cambieranno fluidamente.

Premi **E**: le luci generano un colore casuale a partire dal pixel 0, e spostano il colore di un pixel sequenzialmente, in modo da poter vedere una luce a flusso d\acqua.

Premi **F**: ogni pixel si accende con colori casuali in sequenza.

![Img](./media/2019.gif)

<span style="color: rgb(0, 209, 0);">**Suggerimento:** Se non c\è risposta sulla scheda, premi il pulsante di reset sul retro della scheda micro:bit.</span>

![Img](./media/4bottom.png)
