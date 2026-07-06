### 5.2.1 Indicatore di Direzione

#### 5.2.1.1 Panoramica

![Img](./media/top1.png)

Quando si muove il joystick, la matrice di punti visualizza frecce nella direzione corrispondente in tempo reale: sinistra, destra, su, giù, fornendo un chiaro riferimento di direzione.

![Img](./media/bottom1.png)

#### 5.2.1.2 Conoscenza dei Componenti

Questo progetto utilizza lo stesso joystick del Progetto 01. Si prega di fare riferimento alla sezione 4.2.1.2 per la conoscenza dei suoi componenti.

#### 5.2.1.3 Parti Richieste

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png)|
| :--: | :--: | :--: |
| **Scheda micro:bit V2** (auto-fornita) ×1 | **Smart Gamepad micro:bit** (assemblato) ×1 |**Batteria AAA** (auto-fornita) ×4 |


#### 5.2.1.4 Flusso del Codice

![Img](./media/1008.png)

#### 5.2.1.5 Codice di Test

⚠️ **Nota che la sensibilità del joystick può essere regolata in base alle proprie esigenze.**

**Codice completo:**

```python
from microbit import *

# Calibrazione del joystick (regola questi valori se il joystick non è centrato)
# I valori tipici per il centro sono intorno a 511 per entrambi gli assi
JOYSTICK_CENTER_X = 511
JOYSTICK_CENTER_Y = 511
# Soglia per rilevare il movimento (regola per la sensibilità)
JOYSTICK_THRESHOLD = 100

# Funzione per visualizzare le frecce
def show_arrow(direction):
    if direction == "up":
        display.show(Image.ARROW_N)
    elif direction == "down":
        display.show(Image.ARROW_S)
    elif direction == "left":
        display.show(Image.ARROW_W)
    elif direction == "right":
        display.show(Image.ARROW_E)
    else:
        display.show(Image.HOUSE)

# Loop principale
while True:
    # Leggi i valori analogici del joystick
    x_value = pin0.read_analog()
    y_value = pin1.read_analog()

    # Determina la direzione in base ai valori del joystick
    if x_value < JOYSTICK_CENTER_X - JOYSTICK_THRESHOLD:
        show_arrow("left")
    elif x_value > JOYSTICK_CENTER_X + JOYSTICK_THRESHOLD:
        show_arrow("right")
    elif y_value < JOYSTICK_CENTER_Y - JOYSTICK_THRESHOLD:
        show_arrow("up")
    elif y_value > JOYSTICK_CENTER_Y + JOYSTICK_THRESHOLD:
        show_arrow("down")
    else:
        show_arrow("center")

    sleep(100) # Breve ritardo per evitare letture eccessive
```

![Img](./media/line1.png)

**Breve spiegazione:**

① Inizializza la matrice LED per farla mostrare ![Img](./media/1006.png).

```python
from microbit import *

# Calibrazione del joystick (regola questi valori se il joystick non è centrato)
# I valori tipici per il centro sono intorno a 511 per entrambi gli assi
JOYSTICK_CENTER_X = 511
JOYSTICK_CENTER_Y = 511
# Soglia per rilevare il movimento (regola per la sensibilità)
JOYSTICK_THRESHOLD = 100

# Funzione per visualizzare le frecce
def show_arrow(direction):
    if direction == "up":
        display.show(Image.ARROW_N)
    elif direction == "down":
        display.show(Image.ARROW_S)
    elif direction == "left":
        display.show(Image.ARROW_W)
    elif direction == "right":
        display.show(Image.ARROW_E)
    else:
        display.show(Image.HOUSE)
```

② Leggi i valori degli assi X e Y per determinare la direzione di movimento. Se viene rilevata, la matrice mostra la freccia corrispondente. In caso contrario, visualizza ![Img](./media/1006.png).

```python
# Loop principale
while True:
    # Leggi i valori analogici del joystick
    x_value = pin0.read_analog()
    y_value = pin1.read_analog()

    # Determina la direzione in base ai valori del joystick
    if x_value < JOYSTICK_CENTER_X - JOYSTICK_THRESHOLD:
        show_arrow("left")
    elif x_value > JOYSTICK_CENTER_X + JOYSTICK_THRESHOLD:
        show_arrow("right")
    elif y_value < JOYSTICK_CENTER_Y - JOYSTICK_THRESHOLD:
        show_arrow("up")
    elif y_value > JOYSTICK_CENTER_Y + JOYSTICK_THRESHOLD:
        show_arrow("down")
    else:
        show_arrow("center")

    sleep(100) # Breve ritardo per evitare letture eccessive
```


#### 5.2.1.6 Risultato del Test

![Img](./media/4top.png)

Dopo aver caricato il codice, inserisci la scheda micro:bit nello slot del gamepad (**batterie installate**) e sposta l\interruttore su “ON”.

Quando spingi il joystick del gamepad, puoi vedere le frecce corrispondenti sulla matrice. Se alzi il dito per riportarlo al centro, apparirà un\icona a forma di casa sulla matrice.

![Img](./media/1009.gif)

<span style="color: rgb(0, 209, 0);">**Suggerimento:** Se non c\è risposta sulla scheda, premi il pulsante di reset sul retro della scheda micro:bit.</span>

![Img](./media/4bottom.png)
