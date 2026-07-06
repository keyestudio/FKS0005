### 5.2.3 Semplice Pianoforte Elettronico

#### 5.2.3.1 Panoramica

![Img](./media/top1.png)

In questo progetto, controlliamo l'altoparlante micro:bit per riprodurre toni diversi azionando il joystick e premendo i pulsanti. Nel frattempo, la matrice LED a bordo mostrerà i numeri corrispondenti.

Girando il joystick a destra si produce "Do (Tono Do Centrale)" con la visualizzazione che mostra "1"; girandolo a sinistra si produce "Re (Tono Re)" con "2"; girandolo verso l'alto si produce "Mi (Tono Mi)" con "3"; girandolo verso il basso si produce "Fa (Tono Fa)" con "4". Premendo il pulsante C si produce "Sol (Tono Sol)" con "5", premendo D si produce "La (Tono La)" con "6", E produce "Si (Tono Si)" con "7", e premendo F si produce un "Do (Diesis)" più alto mentre la visualizzazione torna a "1". C'è una bella sincronizzazione tra joystick, pulsanti, toni e display.

![Img](./media/bottom1.png)

#### 5.2.3.2 Conoscenza dei Componenti

Questo progetto utilizza lo stesso altoparlante micro:bit del Progetto 03. Si prega di fare riferimento alla sezione 4.2.3.2 per la conoscenza dei suoi componenti.

#### 5.2.3.3 Parti Richieste

| **Scheda micro:bit V2** (auto-fornita) ×1 | **Smart Gamepad micro:bit** (assemblato) ×1 |**Batteria AAA** (auto-fornita) ×4 |
| :--: | :--: | :--: |
| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |

#### 5.2.3.4 Flusso del Codice

![Img](./media/3009.png)

#### 5.2.3.5 Codice di Test

⚠️ **Nota che la sensibilità del joystick può essere regolata in base alle proprie esigenze.**

**Codice completo:**

```python
from microbit import *

# Calibrazione del joystick (regola questi valori se il joystick non è centrato)
JOYSTICK_CENTER_X = 511
JOYSTICK_CENTER_Y = 511
# Soglia per rilevare il movimento (regola per la sensibilità)
JOYSTICK_THRESHOLD = 100

# Mappatura delle note musicali ai numeri visualizzati
NOTES = {
    "right": (262, "1"),  # Do centrale
    "left": (294, "2"),   # Re
    "up": (330, "3"),     # Mi
    "down": (349, "4"),   # Fa
    "C": (392, "5"),      # Sol
    "D": (440, "6"),      # La
    "E": (494, "7"),      # Si
    "F": (523, "1")       # Do alto
}

# Funzione per riprodurre una nota e visualizzare un numero
def play_note_and_show(note_freq, display_char):
    music.play(music.note(note_freq, 500), wait=False) # Riproduci per 500ms in sottofondo
    display.show(display_char)

# Configura i pin dei pulsanti
pin13.set_pull(pin13.PULL_UP) # Pulsante D
pin15.set_pull(pin15.PULL_UP) # Pulsante C
pin16.set_pull(pin16.PULL_UP) # Pulsante E
pin14.set_pull(pin14.PULL_UP) # Pulsante F (assumendo P14 per F)

display.show(Image.MUSIC)

while True:
    # Leggi i valori analogici del joystick
    x_value = pin0.read_analog()
    y_value = pin1.read_analog()

    # Controlla il joystick
    if x_value > JOYSTICK_CENTER_X + JOYSTICK_THRESHOLD:
        play_note_and_show(NOTES["right"][0], NOTES["right"][1])
    elif x_value < JOYSTICK_CENTER_X - JOYSTICK_THRESHOLD:
        play_note_and_show(NOTES["left"][0], NOTES["left"][1])
    elif y_value < JOYSTICK_CENTER_Y - JOYSTICK_THRESHOLD:
        play_note_and_show(NOTES["up"][0], NOTES["up"][1])
    elif y_value > JOYSTICK_CENTER_Y + JOYSTICK_THRESHOLD:
        play_note_and_show(NOTES["down"][0], NOTES["down"][1])

    # Controlla i pulsanti
    if not pin15.read_digital(): # Pulsante C
        play_note_and_show(NOTES["C"][0], NOTES["C"][1])
    elif not pin13.read_digital(): # Pulsante D
        play_note_and_show(NOTES["D"][0], NOTES["D"][1])
    elif not pin16.read_digital(): # Pulsante E
        play_note_and_show(NOTES["E"][0], NOTES["E"][1])
    elif not pin14.read_digital(): # Pulsante F
        play_note_and_show(NOTES["F"][0], NOTES["F"][1])

    sleep(100) # Breve ritardo per evitare letture eccessive e debounce
```

![Img](./media/line1.png)

**Breve spiegazione:**

① Inizializza la matrice LED micro:bit per mostrare ![Img](./media/3004.png).

```python
from microbit import *

# Calibrazione del joystick (regola questi valori se il joystick non è centrato)
JOYSTICK_CENTER_X = 511
JOYSTICK_CENTER_Y = 511
# Soglia per rilevare il movimento (regola per la sensibilità)
JOYSTICK_THRESHOLD = 100

# Mappatura delle note musicali ai numeri visualizzati
NOTES = {
    "right": (262, "1"),  # Do centrale
    "left": (294, "2"),   # Re
    "up": (330, "3"),     # Mi
    "down": (349, "4"),   # Fa
    "C": (392, "5"),      # Sol
    "D": (440, "6"),      # La
    "E": (494, "7"),      # Si
    "F": (523, "1")       # Do alto
}

# Funzione per riprodurre una nota e visualizzare un numero
def play_note_and_show(note_freq, display_char):
    music.play(music.note(note_freq, 500), wait=False) # Riproduci per 500ms in sottofondo
    display.show(display_char)

# Configura i pin dei pulsanti
pin13.set_pull(pin13.PULL_UP) # Pulsante D
pin15.set_pull(pin15.PULL_UP) # Pulsante C
pin16.set_pull(pin16.PULL_UP) # Pulsante E
pin14.set_pull(pin14.PULL_UP) # Pulsante F (assumendo P14 per F)

display.show(Image.MUSIC)
```

② Determina la direzione del movimento del joystick; riproduci i toni corrispondenti per mezza battuta in sottofondo, e la matrice LED visualizza il numero corrispondente.

```python
while True:
    # Leggi i valori analogici del joystick
    x_value = pin0.read_analog()
    y_value = pin1.read_analog()

    # Controlla il joystick
    if x_value > JOYSTICK_CENTER_X + JOYSTICK_THRESHOLD:
        play_note_and_show(NOTES["right"][0], NOTES["right"][1])
    elif x_value < JOYSTICK_CENTER_X - JOYSTICK_THRESHOLD:
        play_note_and_show(NOTES["left"][0], NOTES["left"][1])
    elif y_value < JOYSTICK_CENTER_Y - JOYSTICK_THRESHOLD:
        play_note_and_show(NOTES["up"][0], NOTES["up"][1])
    elif y_value > JOYSTICK_CENTER_Y + JOYSTICK_THRESHOLD:
        play_note_and_show(NOTES["down"][0], NOTES["down"][1])
```

③ Controlla se un pulsante è premuto, e riproduci il tono corrispondente per mezza battuta in sottofondo, e la matrice LED visualizza il numero corrispondente.

```python
    # Controlla i pulsanti
    if not pin15.read_digital(): # Pulsante C
        play_note_and_show(NOTES["C"][0], NOTES["C"][1])
    elif not pin13.read_digital(): # Pulsante D
        play_note_and_show(NOTES["D"][0], NOTES["D"][1])
    elif not pin16.read_digital(): # Pulsante E
        play_note_and_show(NOTES["E"][0], NOTES["E"][1])
    elif not pin14.read_digital(): # Pulsante F
        play_note_and_show(NOTES["F"][0], NOTES["F"][1])

    sleep(100) # Breve ritardo per evitare letture eccessive e debounce
```

#### 5.2.3.6 Risultato del Test

![Img](./media/4top.png)

Dopo aver caricato il codice, inserisci la scheda micro:bit nello slot del gamepad (**batterie installate**) e sposta l'interruttore su “ON”. La matrice LED mostra “![Img](./media/3004.png)” per prima.

Girando il joystick a destra si produce "Do (Tono Do Centrale)" con la visualizzazione che mostra "1"; girandolo a sinistra si produce "Re (Tono Re)" con "2"; girandolo verso l'alto si produce "Mi (Tono Mi)" con "3"; girandolo verso il basso si produce "Fa (Tono Fa)" con "4". Premendo il pulsante C si produce "Sol (Tono Sol)" con "5", premendo D si produce "La (Tono La)" con "6", E produce "Si (Tono Si)" con "7", e premendo F si produce un "Do (Diesis)" più alto mentre la visualizzazione torna a "1".

Hai costruito il semplice pianoforte elettronico!

![Img](./media/3010.gif)

<span style="color: rgb(0, 209, 0);">**Suggerimento:** Se non c'è risposta sulla scheda, premi il pulsante di reset sul retro della scheda micro:bit.</span>

![Img](./media/4bottom.png)
