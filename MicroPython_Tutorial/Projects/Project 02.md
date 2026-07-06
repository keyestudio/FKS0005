### 5.2.2 Luces de Colores

#### 5.2.2.1 Resumen

![Img](./media/top1.png)

Los LED RGB son un tipo de fuente de luz LED que crea imágenes mezclando la luz de los tres colores primarios: rojo, verde y azul, cuya intersección produce varios tonos. Los métodos comunes incluyen la mezcla directa de los colores primarios, el uso de un LED azul combinado con fósforo amarillo, o el empleo de un LED ultravioleta junto con fósforo RGB. En comparación con los LED que emiten luz blanca directamente, los LED RGB ofrecen una gama más amplia de posibilidades de mezcla de colores porque los tres colores primarios se pueden controlar de forma independiente.

En este proyecto, cada botón corresponde a un modo diferente de los LED RGB. Cuando se presiona el botón C, las luces parpadean alternativamente en el orden de "rojo, verde, azul, amarillo y púrpura"; presione D para cambiar a luces de respiración; presione E para luces de flujo de agua; presione F para luces de marquesina.

Cadenas de luces de colores para decoraciones festivas, luces de árboles de Navidad, tiras RGB para el ambiente diario, luces decorativas LED en parques de atracciones y centros comerciales... Todos son ejemplos comunes de luces multimodo en nuestra vida diaria.

![Img](./media/bottom1.png)

#### 5.2.2.2 Conocimiento de Componentes

![Img](./media/2top.png)

**LED RGB SK6812**

| ![Img](./media//2001.png)| ![Img](./media//2002.png)|
| :--: | :--: |
| Producto real | Diagrama esquemático |

El SK6812 es una fuente de luz LED controlada externamente que integra circuitos de control e iluminación. Su parte principal son perlas LED iluminadas en superficie de 5x5 mm, cada una funcionando como un píxel independiente que incorpora múltiples circuitos centrales: un circuito de enganche de datos de interfaz digital inteligente, un circuito de accionamiento de conformación y amplificación de señal, un circuito de regulación de potencia, un circuito de corriente constante incorporado y un oscilador RC de alta precisión.

Su comunicación emplea un protocolo de código de retorno a cero de polaridad única. Al reiniciar el encendido, cada píxel recibe datos del controlador a través del puerto DIN. Los primeros 24 bits de datos son extraídos por el píxel inicial y almacenados en el enganche de datos interno, mientras que los restantes son conformados y amplificados internamente antes de ser transmitidos a través del puerto DOUT a los píxeles subsiguientes. Con cada píxel procesado, el tamaño de la señal transmitida disminuye en 24 bits.

En el gamepad, hay cuatro luces RGB SK6812. Todas ellas admiten un ajuste de brillo de 256 niveles en sus canales rojo, verde y azul, lo que permite 256×256×256 combinaciones de colores. Debido a esto, ofrece diversos efectos de iluminación, como parpadeos alternos, gradientes de respiración y animaciones de desplazamiento, proporcionando interacciones más intuitivas y vívidas.

**Botón**

| ![Img](./media//2003.png)| ![Img](./media//2004.png)|
| :--: | :--: |
| Producto real | Diagrama esquemático |

El botón, que apareció por primera vez en Japón, se conocía como un interruptor sensible. Durante el funcionamiento, presione el interruptor para aplicar fuerza y cerrar el circuito. Al liberar la presión, el interruptor se abre. Su lámina de resorte metálica interna cambia su estado de conectado/desconectado en respuesta a la fuerza aplicada.

Hay cuatro botones, cada uno conectado de forma independiente a un pin de la placa micro:bit. Cuando se presiona un botón, el circuito genera una señal de bajo nivel correspondiente, lo que permite a la micro:bit responder rápidamente a los comandos y mejora significativamente la comodidad y precisión de la interacción.

![Img](./media/2bottom.png)

#### 5.2.2.3 Piezas Requeridas

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **Placa micro:bit V2** (suministrada por el usuario) ×1 | **Smart Gamepad micro:bit** (ensamblado) ×1 | **Pila AAA** (suministrada por el usuario) ×4 |

#### 5.2.2.4 Flujo del Código

![Img](./media/2006.png)

#### 5.2.2.5 Código de Prueba

⚠️ **Tenga en cuenta que el tiempo de retardo de MODE\*_DELAY en los códigos se puede modificar según sus necesidades.**

**Código completo:**

```python
from microbit import *
import neopixel
import utime

# ===================== Global Configuration & Variables =====================
# Disable micro:bit's default LED display to avoid conflicts
display.set_display_mode(display.DISPLAY_MODE_BLACK_AND_WHITE)

# LED strip configuration
NUM_LEDS = 4
LED_PIN = pin8
strip = neopixel.NeoPixel(LED_PIN, NUM_LEDS)

# Button debounce time (ms)
BTN_DEBOUNCE_TIME = 20

# Mode delays (ms)
MODE1_DELAY = 500
MODE2_DELAY = 5
MODE3_DELAY = 50
MODE4_DELAY = 50

# Game state variables
mode = 0  # 0: initial, 1: mode1, 2: mode2, 3: mode3, 4: mode4
mode_step = 0
last_button_press_time = 0
last_mode_change_time = 0

# Initialize pins with pull-up (PULL_UP: pressed=low level 0, released=high level 1)
pin13.set_pull(pin13.PULL_UP)  # Button C
pin15.set_pull(pin15.PULL_UP)  # Button D
pin16.set_pull(pin16.PULL_UP)  # Button E
pin14.set_pull(pin14.PULL_UP)  # Button F

# Function to set all LEDs to a specific color
def set_all_leds(r, g, b):
    for i in range(NUM_LEDS):
        strip[i] = (r, g, b)
    strip.show()

# Function to clear all LEDs
def clear_leds():
    set_all_leds(0, 0, 0)

# Function to convert HSL to RGB
def hsl_to_rgb(h, s, l):
    h /= 360.0
    s /= 100.0
    l /= 100.0
    if s == 0:
        r = g = b = l
    else:
        def hue2rgb(p, q, t):
            if t < 0: t += 1
            if t > 1: t -= 1
            if t < 1/6: return p + (q - p) * 6 * t
            if t < 1/2: return q
            if t < 2/3: return p + (q - p) * (2/3 - t) * 6
            return p
        q = l * (1 + s) if l < 0.5 else l + s - l * s
        p = 2 * l - q
        r = hue2rgb(p, q, h + 1/3)
        g = hue2rgb(p, q, h)
        b = hue2rgb(p, q, h - 1/3)
    return (int(r * 255), int(g * 255), int(b * 255))

# ===================== Main Loop =====================
while True:
    current_time = utime.ticks_ms()

    # Button C (Mode 1: alternating colors)
    if not pin13.read_digital() and (current_time - last_button_press_time) > BTN_DEBOUNCE_TIME:
        mode = 1
        mode_step = 0
        clear_leds()
        last_mode_change_time = current_time
        last_button_press_time = current_time

    # Button D (Mode 2: breathing light)
    if not pin15.read_digital() and (current_time - last_button_press_time) > BTN_DEBOUNCE_TIME:
        mode = 2
        mode_step = 0
        clear_leds()
        last_mode_change_time = current_time
        last_button_press_time = current_time

    # Button E (Mode 3: flowing water light)
    if not pin16.read_digital() and (current_time - last_button_press_time) > BTN_DEBOUNCE_TIME:
        mode = 3
        mode_step = 0
        clear_leds()
        last_mode_change_time = current_time
        last_button_press_time = current_time

    # Button F (Mode 4: marquee light)
    if not pin14.read_digital() and (current_time - last_button_press_time) > BTN_DEBOUNCE_TIME:
        mode = 4
        mode_step = 0
        clear_leds()
        last_mode_change_time = current_time
        last_button_press_time = current_time

    # Mode logic
    if mode == 1:  # Alternating colors (Red, Green, Blue, Yellow, Purple)
        if (current_time - last_mode_change_time) > MODE1_DELAY:
            last_mode_change_time = current_time
            clear_leds()
            if mode_step == 0: # Red
                set_all_leds(255, 0, 0)
            elif mode_step == 1: # Green
                set_all_leds(0, 255, 0)
            elif mode_step == 2: # Blue
                set_all_leds(0, 0, 255)
            elif mode_step == 3: # Yellow
                set_all_leds(255, 255, 0)
            elif mode_step == 4: # Purple
                set_all_leds(128, 0, 128)
            mode_step = (mode_step + 1) % 5

    elif mode == 2:  # Breathing light (smooth hue change)
        if (current_time - last_mode_change_time) > MODE2_DELAY:
            last_mode_change_time = current_time
            clear_leds()
            hue = mode_step % 360
            r, g, b = hsl_to_rgb(hue, 99, 20) # High saturation, low brightness
            set_all_leds(r, g, b)
            mode_step += 1

    elif mode == 3:  # Flowing water light (random color, shifting)
        if (current_time - last_mode_change_time) > MODE3_DELAY:
            last_mode_change_time = current_time
            # Shift all pixels
            for i in range(NUM_LEDS - 1, 0, -1):
                strip[i] = strip[i-1]
            # New random color for the first pixel
            hue = random.randint(0, 359)
            r, g, b = hsl_to_rgb(hue, 99, 20)
            strip[0] = (r, g, b)
            strip.show()

    elif mode == 4:  # Marquee light (single LED, random color)
        if (current_time - last_mode_change_time) > MODE4_DELAY:
            last_mode_change_time = current_time
            clear_leds()
            hue = random.randint(0, 359)
            r, g, b = hsl_to_rgb(hue, 99, 20)
            strip[mode_step] = (r, g, b)
            strip.show()
            mode_step = (mode_step + 1) % NUM_LEDS

    utime.sleep_ms(10) # Small delay for main loop
```

![Img](./media/line1.png)

**Breve explicación:**

① Al principio, deshabilite la función de los LED (establezca led enable en false).

Y defina 4 retrasos de LED (por ejemplo, establezca 5 en el modo 2, establezca 500 en el modo 1...), establezca el antirebote del botón en 20. Inicialice cuatro LED RGB en el pin P8 sin color (establezca todos los valores en 0), es decir, apáguelos.

```python
from microbit import *
import neopixel
import utime

# ===================== Global Configuration & Variables =====================
# Disable micro:bit's default LED display to avoid conflicts
display.set_display_mode(display.DISPLAY_MODE_BLACK_AND_WHITE)

# LED strip configuration
NUM_LEDS = 4
LED_PIN = pin8
strip = neopixel.NeoPixel(LED_PIN, NUM_LEDS)

# Button debounce time (ms)
BTN_DEBOUNCE_TIME = 20

# Mode delays (ms)
MODE1_DELAY = 500
MODE2_DELAY = 5
MODE3_DELAY = 50
MODE4_DELAY = 50

# Game state variables
mode = 0  # 0: initial, 1: mode1, 2: mode2, 3: mode3, 4: mode4
mode_step = 0
last_button_press_time = 0
last_mode_change_time = 0

# Initialize pins with pull-up (PULL_UP: pressed=low level 0, released=high level 1)
pin13.set_pull(pin13.PULL_UP)  # Button C
pin15.set_pull(pin15.PULL_UP)  # Button D
pin16.set_pull(pin16.PULL_UP)  # Button E
pin14.set_pull(pin14.PULL_UP)  # Button F

# Function to set all LEDs to a specific color
def set_all_leds(r, g, b):
    for i in range(NUM_LEDS):
        strip[i] = (r, g, b)
    strip.show()

# Function to clear all LEDs
def clear_leds():
    set_all_leds(0, 0, 0)

# Function to convert HSL to RGB
def hsl_to_rgb(h, s, l):
    h /= 360.0
    s /= 100.0
    l /= 100.0
    if s == 0:
        r = g = b = l
    else:
        def hue2rgb(p, q, t):
            if t < 0: t += 1
            if t > 1: t -= 1
            if t < 1/6: return p + (q - p) * 6 * t
            if t < 1/2: return q
            if t < 2/3: return p + (q - p) * (2/3 - t) * 6
            return p
        q = l * (1 + s) if l < 0.5 else l + s - l * s
        p = 2 * l - q
        r = hue2rgb(p, q, h + 1/3)
        g = hue2rgb(p, q, h)
        b = hue2rgb(p, q, h - 1/3)
    return (int(r * 255), int(g * 255), int(b * 255))
```

② Durante el bucle, la operación anti-jitter se implementa comprobando si la diferencia entre el tiempo de ejecución actual y el tiempo de pulsación anterior excede el umbral anti-jitter preestablecido (BTN_DEBOUNCE), evitando así las pulsaciones repetidas causadas por el jitter físico.

```python
while True:
    current_time = utime.ticks_ms()

    # Button C (Mode 1: alternating colors)
    if not pin13.read_digital() and (current_time - last_button_press_time) > BTN_DEBOUNCE_TIME:
        mode = 1
        mode_step = 0
        clear_leds()
        last_mode_change_time = current_time
        last_button_press_time = current_time

    # Button D (Mode 2: breathing light)
    if not pin15.read_digital() and (current_time - last_button_press_time) > BTN_DEBOUNCE_TIME:
        mode = 2
        mode_step = 0
        clear_leds()
        last_mode_change_time = current_time
        last_button_press_time = current_time

    # Button E (Mode 3: flowing water light)
    if not pin16.read_digital() and (current_time - last_button_press_time) > BTN_DEBOUNCE_TIME:
        mode = 3
        mode_step = 0
        clear_leds()
        last_mode_change_time = current_time
        last_button_press_time = current_time

    # Button F (Mode 4: marquee light)
    if not pin14.read_digital() and (current_time - last_button_press_time) > BTN_DEBOUNCE_TIME:
        mode = 4
        mode_step = 0
        clear_leds()
        last_mode_change_time = current_time
        last_button_press_time = current_time
```

③ Cuando se presiona C(/D/E/F), el modo se establece en 1(2/3/4), mientras que los pasos de animación y los puntos de inicio de temporización para el modo correspondiente se restablecen, las luces se borran y la marca de tiempo del botón se actualiza. Esto permite un cambio preciso y el funcionamiento inicial de diferentes modos de LED.

```python
    # Mode logic
    if mode == 1:  # Alternating colors (Red, Green, Blue, Yellow, Purple)
        if (current_time - last_mode_change_time) > MODE1_DELAY:
            last_mode_change_time = current_time
            clear_leds()
            if mode_step == 0: # Red
                set_all_leds(255, 0, 0)
            elif mode_step == 1: # Green
                set_all_leds(0, 255, 0)
            elif mode_step == 2: # Blue
                set_all_leds(0, 0, 255)
            elif mode_step == 3: # Yellow
                set_all_leds(255, 255, 0)
            elif mode_step == 4: # Purple
                set_all_leds(128, 0, 128)
            mode_step = (mode_step + 1) % 5
```

④ Cuando el modo se establece en 1 y el intervalo entre el tiempo actual y el tiempo del modo anterior excede MODE1Delay, actualice primero la marca de tiempo del modo y muestre las luces según los diferentes valores de model_step (0–4) en secuencia: rojo, verde, azul, amarillo y púrpura. Después de actualizar la pantalla, reinicie el bucle model_step mediante una operación de módulo para cambiar regularmente estos cinco colores.

```python
    elif mode == 2:  # Breathing light (smooth hue change)
        if (current_time - last_mode_change_time) > MODE2_DELAY:
            last_mode_change_time = current_time
            clear_leds()
            hue = mode_step % 360
            r, g, b = hsl_to_rgb(hue, 99, 20) # High saturation, low brightness
            set_all_leds(r, g, b)
            mode_step += 1
```

⑤ Cuando el modo es 2 y el intervalo entre el tiempo actual y el tiempo del modo anterior excede MODE2_DELAY, actualice primero la marca de tiempo del modo e incremente el valor del color (tono) cíclicamente por módulo (rango 0–359). Luego, borre la luz y muestre el tono correspondiente con alta saturación (99) y bajo brillo (20), y los colores degradados cambiarán suavemente. (Los valores de brillo y saturación en los códigos se pueden ajustar según sea necesario).

```python
    elif mode == 3:  # Flowing water light (random color, shifting)
        if (current_time - last_mode_change_time) > MODE3_DELAY:
            last_mode_change_time = current_time
            # Shift all pixels
            for i in range(NUM_LEDS - 1, 0, -1):
                strip[i] = strip[i-1]
            # New random color for the first pixel
            hue = random.randint(0, 359)
            r, g, b = hsl_to_rgb(hue, 99, 20)
            strip[0] = (r, g, b)
            strip.show()
```

⑥ Cuando el modo es 3 y el intervalo entre el tiempo actual y el tiempo del modo anterior excede MODE3_DELAY, actualice primero la marca de tiempo del modo y desplace todos los píxeles de la tira de luz en 1 bit, asigne un tono aleatorio (0–359), alta saturación (99) y bajo brillo (20) al píxel 0. Actualice la pantalla y podrá ver una luz que fluye: las luces se mueven secuencialmente y cambian de color aleatoriamente. (Los valores de brillo y saturación en el código se pueden ajustar según sea necesario).

```python
    elif mode == 4:  # Marquee light (single LED, random color)
        if (current_time - last_mode_change_time) > MODE4_DELAY:
            last_mode_change_time = current_time
            clear_leds()
            hue = random.randint(0, 359)
            r, g, b = hsl_to_rgb(hue, 99, 20)
            strip[mode_step] = (r, g, b)
            strip.show()
            mode_step = (mode_step + 1) % NUM_LEDS

    utime.sleep_ms(10) # Small delay for main loop
```

⑦ Cuando el modo es 4 y el intervalo entre el tiempo actual y el tiempo del modo anterior excede MODE4_DELAY, actualice primero la marca de tiempo del modo y borre la tira de luz, asigne un tono aleatorio (0–359), alta saturación (99) y bajo brillo (20) a los píxeles correspondientes a model_step, y actualice la pantalla. Finalmente, cíclico model_step dentro de 0-3 a través de módulo, y verá que un solo LED se enciende secuencialmente en colores aleatorios. (Los valores de brillo y saturación en el código se pueden ajustar según sea necesario).

![Img](./media/2018.png)

#### 5.2.2.6 Resultado de la Prueba

![Img](./media/4top.png)

Después de grabar el código, inserte la placa micro:bit en la ranura del gamepad (**pilas instaladas**), y active el interruptor a “ON”.

Presione **C**: las luces alternan entre **rojo-verde-azul-amarillo-púrpura** en secuencia.

Presione **D**: el tono de color de las luces aumentará y, finalmente, los colores degradados cambiarán suavemente.

Presione **E**: las luces generan un color aleatorio a partir del píxel 0 y desplazan el color un píxel secuencialmente, por lo que puede ver una luz que fluye.

Presione **F**: cada píxel se ilumina en colores aleatorios en secuencia.

![Img](./media/2019.gif)

<span style="color: rgb(0, 209, 0);">**Consejo:** Si no hay respuesta en la placa, presione el botón de reinicio en la parte posterior de la placa micro:bit.</span>

![Img](./media/4bottom.png)
