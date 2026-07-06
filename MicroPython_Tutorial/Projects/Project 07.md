### 5.2.7 Adivina el Número

#### 5.2.7.1 Resumen

![Img](./media/top1.png)

En este proyecto, jugamos un juego de adivinar números con una placa Micro:bit, una placa de control de gamepad y una pantalla OLED. Cuando se adivina el número correcto, la OLED muestra "¡Genial!"; si la suposición es demasiado alta o demasiado baja, muestra "¡Demasiado alto!" / "¡Demasiado bajo!" respectivamente, junto con el rango correspondiente de números posibles.

![Img](./media/bottom1.png)

#### 5.2.7.2 Piezas Requeridas

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **Placa micro:bit V2** (suministrada por el usuario) ×1 | **Smart Gamepad micro:bit** (ensamblado) ×1 | **Pila AAA** (suministrada por el usuario) ×4 |
|![Img](./media/OLED.png)|![Img](./media/7008.png)||
| **Pantalla OLED** (suministrada por el usuario) ×1 | **Cable DuPont F-F** (suministrado por el usuario) x4 ||

#### 5.2.7.3 Diagrama de Cableado

![Img](./media/jiexian8.png)

**Después de cablear como se muestra arriba, inserte la micro:bit en la ranura de la placa de control del gamepad.**

| Pantalla OLED | Placa de control del gamepad micro:bit | Pin de la placa micro:bit |
| :--: | :--: | :--: |
| GND | GND | GND |
| VCC | 3V | 3V |
| SDA | SDA | P20 |
| SCL | SCL | P19 |

#### 5.2.7.4 Flujo del Código

![Img](./media/8001.png)

#### 5.2.7.5 Código de Prueba

⚠️ **Tenga en cuenta que aquí se utiliza OLED, por lo que necesitamos importar su librería.**

![Img](./media/t7000.png)

**Código completo:**

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

**Breve explicación:**

① Importe librerías, inicialice OLED, defina variables globales y configure pines de botón.

Se requieren tres librerías: `microbit` (para acceder al hardware de Micro:bit), `oled_ssd1306` (para controlar la pantalla OLED conectada), `random` (para generar números aleatorios en el juego).

`initialize()` y `clear_oled()` inicializan y borran la OLED.

Se define una serie de variables globales para gestionar los parámetros del estado del juego, incluyendo el modo de juego (`mode`), el rango de números (`min_num`, `max_num`), el valor de la suposición actual (`current_guess`), el número objetivo (`target_num`), la retroalimentación del juego (`state`) y un indicador que controla las actualizaciones de la pantalla (`update_display`).

`pin13`, `pin15` y `pin16` están configurados en modo pull-up, manteniendo un nivel alto cuando el botón no está presionado y un nivel bajo cuando está presionado.

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

② Lógica de inicialización del juego en el bucle principal.

Es el primer bloque lógico del bucle principal del programa, específicamente responsable de la inicialización o reinicio del juego.

`mode` = `0`: el juego requiere inicialización. En este caso, restablece el rango de adivinanza a 1–100 y establece el valor de adivinanza actual en 50. Utiliza `randint(min_num, max_num)` para generar aleatoriamente un número entero entre 1 y 100 como número objetivo (`target_num`).

Luego, `state` = `0` (estado inicial) y `mode` = `1` (en ejecución). Y establece `update_display` en `True` para asegurar que la OLED actualice la información más reciente del juego inmediatamente durante la ejecución.

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

③ Manejar las entradas de los botones y la toma de decisiones basada en la suposición.

Cuando el juego está en funcionamiento (`mode == 1`), gestiona las interacciones del jugador y la lógica del juego. Detecta de forma independiente las entradas de tres botones externos:

*   **`pin15` está presionado**: (nivel bajo detectado); `current_guess` + 1. Para evitar que el valor exceda el rango, verifica y limita `current_guess` < o = `max_num`.
*   **`pin13` está presionado**: `current_guess` - 1. También verifica que `current_guess` no sea mayor que `min_num`.
*   **`pin16` está presionado**: Si `pin16` está presionado, significa que el jugador envió el valor de la suposición. Se comparará con `target_num`:
    *   `current_guess` > `target_num`: `state` = `1` (demasiado alto) y establece el máximo del rango `max_num` en `current_guess`.
    *   `current_guess` < `target_num`: `state` = `2` (demasiado bajo) y establece el mínimo del rango `min_num` en `current_guess`.
    *   `current_guess` = `target_num`: `state` = `3` (¡Genial!) y establece `mode` en `0` para prepararse para la siguiente ronda.

Después de cada pulsación de botón, `update_display` se establece en `True` para actualizar la OLED, con un retraso de 50ms para anti-rebote.

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

④ Lógica de actualización de OLED.

Muestra el estado actual del juego y la información en la OLED. Se ejecuta solo cuando `update_display` = `True` para evitar actualizaciones innecesarias.

Cada ejecución primero llama a `clear_oled()` para borrar la pantalla. El rango de adivinanza actual (por ejemplo, "num:1~100") aparece en la primera línea. La suposición actual del jugador (`current_guess`) se muestra en la tercera línea.

Basándose en `state`, el mensaje de retroalimentación correspondiente ("¡Demasiado alto!", "¡Demasiado bajo!" o "¡Genial!") aparece en la quinta línea.

Después de completar todas las visualizaciones, `update_display` se restablece a `False` para estar listo para actualizar el siguiente cambio de estado del juego.

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

⑤ Manejar los retrasos después de las suposiciones correctas.

Solo se ejecuta cuando el jugador adivina correctamente el número objetivo (`state == 3`). Luego, se pausa 1000ms (1s) para que los jugadores verifiquen el “¡Genial!”.

Luego, `state` se restablece a `0`. Dado que `mode` ya se ha restablecido a `0`, al adivinar correctamente, el juego se reiniciará desde la inicialización.

```python
    # 4. Delay after correct guess to show message
    if state == 3:
        sleep(1000)
        state = 0
```

#### 5.2.7.6 Resultado de la Prueba

![Img](./media/4top.png)

Después de grabar el código, inserte la placa micro:bit en la ranura del gamepad (**pilas instaladas**), y active el interruptor a “ON”.

Después de cargar el código, la OLED se inicializa y muestra el rango de valores de “num: 1 ~ 100” y la suposición inicial de 50. Puede presionar C para temp+1 (máx. de 100) o E para temp-1 (mín. de 1) para cambiar su valor de suposición en la OLED.

Presione D para enviar su valor, y temp se comparará con el valor objetivo aleatorio. Si temp>valor, muestre "¡Demasiado alto!" y asigne temp a max_num; si temp<valor, muestre "¡Demasiado bajo!" y asígnelo a min_num. Si tiene demasiada suerte y temp=valor, verá "¡Genial!" durante 1s.

Después de eso, el juego se reiniciará y se establecerá un nuevo valor objetivo. ¡Juguemos otra ronda!

![Img](./media/t7000.gif)

⚠️ **El bloque de construcción en el Resultado de la Prueba no está incluido en este kit de producto.**

<span style="color: rgb(0, 209, 0);">**Consejo:** Si no hay respuesta en la placa, presione el botón de reinicio en la parte posterior de la placa micro:bit.</span>

![Img](./media/4bottom.png)
