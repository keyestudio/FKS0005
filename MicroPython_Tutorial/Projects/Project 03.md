### 5.2.3 Piano Electrónico Simple

#### 5.2.3.1 Resumen

![Img](./media/top1.png)

En este proyecto, controlamos el altavoz de la micro:bit para reproducir diferentes tonos moviendo el joystick y presionando los botones. Mientras tanto, la matriz de LED a bordo mostrará los números correspondientes.

Al girar el joystick a la derecha se produce "Do (Tono Central C)" con la pantalla mostrando "1"; al girarlo a la izquierda se produce "Re (Tono D)" con "2"; al girarlo hacia arriba se produce "Mi (Tono E)" con "3"; al girarlo hacia abajo se produce "Fa (Tono F)" con "4". Al presionar el botón C se produce "Sol (Tono G)" con "5", al presionar D se produce "La (Tono A)" con "6", E produce "Si (Tono B)" con "7", y al presionar F se produce un "Do(Sostenido)" más alto mientras la pantalla vuelve a "1". Hay una bonita sincronización del joystick, los botones, los tonos y la pantalla.

![Img](./media/bottom1.png)

#### 5.2.3.2 Conocimiento de Componentes

![Img](./media/2top.png)

**Altavoz de Micro:bit**

![Img](./media/j901.png)

La placa micro:bit cuenta con un altavoz incorporado para emitir sonidos, como risas, saludos, bostezos o expresiones de tristeza, o incluso componer una canción. Mediante programación, puede incluso generar notas individuales, melodías y ritmos, o incluso composiciones musicales, como la canción *Twinkle Twinkle Little Star*.

![Img](./media/2bottom.png)

#### 5.2.3.3 Piezas Requeridas

| **Placa micro:bit V2** (suministrada por el usuario) ×1 | **Smart Gamepad micro:bit** (ensamblado) ×1 |**Pila AAA** (suministrada por el usuario) ×4 |
| :--: | :--: | :--: |
| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |

#### 5.2.3.4 Flujo del Código

![Img](./media/3009.png)

#### 5.2.3.5 Código de Prueba

⚠️ **Tenga en cuenta que la sensibilidad del joystick se puede ajustar según sus necesidades.**

**Código completo:**

```python
from microbit import *

# ===================== Global Configuration & Variables =====================
# Joystick threshold for movement detection
JOYSTICK_THRESHOLD = 200

# Note frequencies (Hz) for C, D, E, F, G, A, B, High C
NOTES = {
    "C": 262,
    "D": 294,
    "E": 330,
    "F": 349,
    "G": 392,
    "A": 440,
    "B": 494,
    "HC": 523  # High C
}

# ===================== Main Loop =====================
while True:
    # Read joystick X and Y values
    joystick_x = pin1.read_analog()
    joystick_y = pin2.read_analog()

    # Clear display
    display.clear()

    # Determine direction and play note
    if joystick_x < 512 - JOYSTICK_THRESHOLD:  # Left (D note)
        music.play(music.note(NOTES["D"], music.HALF), wait=False)
        display.show("2")
    elif joystick_x > 512 + JOYSTICK_THRESHOLD:  # Right (C note)
        music.play(music.note(NOTES["C"], music.HALF), wait=False)
        display.show("1")
    elif joystick_y < 512 - JOYSTICK_THRESHOLD:  # Up (E note)
        music.play(music.note(NOTES["E"], music.HALF), wait=False)
        display.show("3")
    elif joystick_y > 512 + JOYSTICK_THRESHOLD:  # Down (F note)
        music.play(music.note(NOTES["F"], music.HALF), wait=False)
        display.show("4")
    elif not pin13.read_digital():  # Button C (G note)
        music.play(music.note(NOTES["G"], music.HALF), wait=False)
        display.show("5")
    elif not pin15.read_digital():  # Button D (A note)
        music.play(music.note(NOTES["A"], music.HALF), wait=False)
        display.show("6")
    elif not pin16.read_digital():  # Button E (B note)
        music.play(music.note(NOTES["B"], music.HALF), wait=False)
        display.show("7")
    elif not pin14.read_digital():  # Button F (High C note)
        music.play(music.note(NOTES["HC"], music.HALF), wait=False)
        display.show("1")
    else:  # No input, show initial image
        display.show(Image.MUSIC_CROTCHET)

    sleep(100)  # Small delay to prevent flickering and rapid note re-triggering
```

![Img](./media/line1.png)

**Breve explicación:**

① Inicialice la matriz de LED de la micro:bit para que muestre ![Img](./media/3004.png).

```python
from microbit import *

# ===================== Global Configuration & Variables =====================
# Joystick threshold for movement detection
JOYSTICK_THRESHOLD = 200

# Note frequencies (Hz) for C, D, E, F, G, A, B, High C
NOTES = {
    "C": 262,
    "D": 294,
    "E": 330,
    "F": 349,
    "G": 392,
    "A": 440,
    "B": 494,
    "HC": 523  # High C
}
```

② Determine la dirección del movimiento del joystick; reproduzca los tonos correspondientes durante medio tiempo en segundo plano, y la matriz de LED mostrará el número correspondiente.

```python
# ===================== Main Loop =====================
while True:
    # Read joystick X and Y values
    joystick_x = pin1.read_analog()
    joystick_y = pin2.read_analog()

    # Clear display
    display.clear()

    # Determine direction and play note
    if joystick_x < 512 - JOYSTICK_THRESHOLD:  # Left (D note)
        music.play(music.note(NOTES["D"], music.HALF), wait=False)
        display.show("2")
    elif joystick_x > 512 + JOYSTICK_THRESHOLD:  # Right (C note)
        music.play(music.note(NOTES["C"], music.HALF), wait=False)
        display.show("1")
    elif joystick_y < 512 - JOYSTICK_THRESHOLD:  # Up (E note)
        music.play(music.note(NOTES["E"], music.HALF), wait=False)
        display.show("3")
    elif joystick_y > 512 + JOYSTICK_THRESHOLD:  # Down (F note)
        music.play(music.note(NOTES["F"], music.HALF), wait=False)
        display.show("4")
    elif not pin13.read_digital():  # Button C (G note)
        music.play(music.note(NOTES["G"], music.HALF), wait=False)
        display.show("5")
    elif not pin15.read_digital():  # Button D (A note)
        music.play(music.note(NOTES["A"], music.HALF), wait=False)
        display.show("6")
    elif not pin16.read_digital():  # Button E (B note)
        music.play(music.note(NOTES["B"], music.HALF), wait=False)
        display.show("7")
    elif not pin14.read_digital():  # Button F (High C note)
        music.play(music.note(NOTES["HC"], music.HALF), wait=False)
        display.show("1")
    else:  # No input, show initial image
        display.show(Image.MUSIC_CROTCHET)

    sleep(100)  # Small delay to prevent flickering and rapid note re-triggering
```

③ Compruebe si se presiona un botón, y reproduzca el tono correspondiente durante medio tiempo en segundo plano, y la matriz de LED mostrará el número correspondiente.

![Img](./media/3007.png)


#### 5.2.3.6 Resultado de la Prueba

![Img](./media/4top.png)

Después de grabar el código, inserte la placa micro:bit en la ranura del gamepad (**pilas instaladas**), y active el interruptor a “ON”. La matriz de LED mostrará “![Img](./media/3004.png)” primero.

Al girar el joystick a la derecha se produce "Do (Tono Central C)" con la pantalla mostrando "1"; al girarlo a la izquierda se produce "Re (Tono D)" con "2"; al girarlo hacia arriba se produce "Mi (Tono E)" con "3"; al girarlo hacia abajo se produce "Fa (Tono F)" con "4". Al presionar el botón C se produce "Sol (Tono G)" con "5", al presionar D se produce "La (Tono A)" con "6", E produce "Si (Tono B)" con "7", y al presionar F se produce un "Do(Sostenido)" más alto mientras la pantalla vuelve a "1".

¡Ha construido el piano electrónico simple!

![Img](./media/3010.gif)

<span style="color: rgb(0, 209, 0);">**Consejo:** Si no hay respuesta en la placa, presione el botón de reinicio en la parte posterior de la placa micro:bit.</span>

![Img](./media/4bottom.png)
