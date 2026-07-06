### 5.2.6 Piedra-Papel-Tijera

#### 5.2.6.1 Resumen

![Img](./media/top1.png)

Aquí, juguemos a piedra-papel-tijera mediante comunicación inalámbrica de micro:bit. Los jugadores seleccionan su movimiento (piedra, papel o tijera) a través de los botones, con intercambio de datos entre dispositivos. El juego sigue el formato al mejor de tres; si las tres rondas terminan en empate total o en victoria-derrota-empate, se activa un cuarto partido.

Cada resultado se muestra en la matriz de micro:bit (W para victoria, L para derrota, = para empate) y se revela mediante las luces RGB (verde para victoria, rojo para derrota, amarillo para empate) en el pin P8. Al finalizar una ronda, los dos dispositivos reinician todos los datos y luces, preparándose para el siguiente partido.

El juego integra a la perfección la interacción inalámbrica con el combate de varias rondas.

![Img](./media/bottom1.png)

#### 5.2.6.2 Conocimiento de Componentes

![Img](./media/2top.png)

**Comunicación inalámbrica de Micro:bit**

![Img](./media/6001.png)

La placa micro:bit integra dos cómodas capacidades de comunicación inalámbrica: **radio de 2.4GHz** y **Bluetooth de baja energía (BLE)**. Sin embargo, no se pueden usar simultáneamente.

La primera no requiere emparejamiento y admite hasta 255 paquetes independientes para minimizar las interferencias, con un rango de comunicación de 10 a 30 metros, lo que permite la transmisión rápida de datos digitales y cadenas. Mientras que la segunda se utiliza principalmente para emparejar con teléfonos inteligentes, tabletas y otros dispositivos inteligentes para aplicaciones de IoT, como la carga de datos de sensores y el control remoto de aplicaciones móviles.

Amplían las posibilidades de desarrollo creativo de la micro:bit.

#### 5.2.6.3 Piezas Requeridas

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **Placa micro:bit V2** (suministrada por el usuario) ×2 | **Smart Gamepad micro:bit** (ensamblado) ×2 | **Pila AAA** (suministrada por el usuario) ×8 |

#### 5.2.6.4 Flujo del Código

![Img](./media/6002.png)

#### 5.2.6.5 Código de Prueba

**Código completo:**

```python
from microbit import *
import neopixel
import radio

# Global Variables
round2 = 1
check = 1
me = 0
you = 0
wins = 0
loses = 0
draws = 0
gameResults = []
strip = None

pin13.set_pull(pin13.PULL_UP)
pin15.set_pull(pin15.PULL_UP)
pin16.set_pull(pin16.PULL_UP)
# Initialize LED strip (4 LEDs, connected to pin P8)
strip = neopixel.NeoPixel(pin8, 4)

# Reset game state
def resetGame():
    global me, you, round2, wins, loses, draws, gameResults, check
    me = 0
    you = 0
    round2 = 1
    wins = 0
    loses = 0
    draws = 0
    gameResults = []
    check = 1
    resetLights()
    display.show(Image.HEART)

# Receive opponent\'s choice via radio
def on_received_message(receivedMsg):
    global you
    if you == 0:
        # Convert string to integer if needed
        if isinstance(receivedMsg, str) and receivedMsg in [\'1\', \'2\', \'3\']:
            you = int(receivedMsg)
        # Use directly if it\'s an integer
        elif isinstance(receivedMsg, int) and receivedMsg in [1, 2, 3]:
            you = receivedMsg

# Turn off all LEDs
def resetLights():
    for i in range(4):
        strip[i] = (0, 0, 0)  # Off
    strip.show()

# Check if a 4th round is needed
def needFourthRound():
    # Case 1: All 3 draws -> need 4th round, return 2
    if wins == 0 and loses == 0 and draws == 3:
        return 2
    # Case 2: 1 win, 1 loss, 1 draw -> need 4th round, return 1
    if wins == 1 and loses == 1 and draws == 1:
        return 1
    # No 4th round needed
    return 0

# Show round result on LED strip
def showRoundResult(roundNum, result):
    if roundNum <= 4:
        if result == 1:
            # Win: Green
            strip[roundNum - 1] = (0, 255, 0)
        elif result == 0:
            # Draw: Yellow
            strip[roundNum - 1] = (255, 255, 0)
        else:
            # Lose: Red
            strip[roundNum - 1] = (255, 0, 0)
        strip.show()

# Game initialization
radio.on()
radio.config(group=1)
check = 1
me = 0
you = 0
strip.clear()
strip.show()
display.show(Image.HEART)

# Main game loop
while True:

    # Process result when both players have chosen
    if me != 0 and you != 0:
        # Current round result: 1=win, 0=draw, -1=lose
        resultSymbol = "="
        # Determine round outcome
        if me == you:
            resultSymbol = "="
            # Draw
            result2 = 0
            draws += 1
        elif me == 2 and you == 1 or (me == 3 and you == 2 or me == 1 and you == 3):
            resultSymbol = "W"
            # Win
            result2 = 1
            wins += 1
        else:
            resultSymbol = "L"
            # Lose
            result2 = -1
            loses += 1

        # Save round result
        gameResults.append(result2)

        # Display result symbol
        display.show(resultSymbol)

        # Update LED strip
        showRoundResult(round2, result2)

        sleep(3000)

        # Check if game continues
        if round2 == 3:
            # After 3 rounds, check for 4th round
            fourth_round_needed = needFourthRound()
            if fourth_round_needed:
                # Go to 4th round
                round2 = 4
                if fourth_round_needed == 2:
                    display.scroll("FINAL")
                sleep(1000)
                display.show(Image.HEART)
                check = 1
                me = 0
                you = 0
            else:
                # End game
                if wins > loses:
                    display.scroll("WINNER")
                elif loses > wins:
                    display.scroll("LOSER")
                else:
                    display.scroll("TIE")
                sleep(3000)
                resetGame()
        elif round2 == 4:
            # 4th round finished, game over
            display.scroll("GAME OVER")
            sleep(3000)
            resetGame()
        else:
            # Next round (1st or 2nd)
            round2 += 1
            display.show(Image.HEART)
            check = 1
            me = 0
            you = 0

    # Check button input
    if check == 1:
        if pin13.read_digital() == 0:
            # Paper -> send \'3\'
            radio.send(\'3\')
            display.show(Image.SQUARE)
            me = 3
            check = 0
            sleep(200)
        elif pin15.read_digital() == 0:
            # Scissors -> send \'1\'
            radio.send(\'1\')
            display.show(Image(\'99009:\'
                                \'99090:\'
                                \'00900:\'
                                \'99090:\'
                                \'99009\'))
            me = 1
            check = 0
            sleep(200)
        elif pin16.read_digital() == 0:
            # Rock -> send \'2\'
            radio.send(\'2\')
            display.show(Image.SQUARE_SMALL)
            me = 2
            check = 0
            sleep(200)

    # Receive radio data
    try:
        received = radio.receive()
        if received is not None:
            on_received_message(received)
    except:
        pass

    sleep(100)
```

![Img](./media/line1.png)

**Breve explicación:**

① Inicie la radio y establezca el grupo en '1'; establezca el número de rondas, el estado, el oponente y el resultado de piedra-papel-tijera de los jugadores; conecte las cuatro luces RGB al pin P8 y actualice la pantalla, establezca la matriz para que muestre ![Img](./media/6004.png).

```python
from microbit import *
import neopixel
import radio

# Global Variables
round2 = 1
check = 1
me = 0
you = 0
wins = 0
loses = 0
draws = 0
gameResults = []
strip = None

pin13.set_pull(pin13.PULL_UP)
pin15.set_pull(pin15.PULL_UP)
pin16.set_pull(pin16.PULL_UP)
# Initialize LED strip (4 LEDs, connected to pin P8)
strip = neopixel.NeoPixel(pin8, 4)
```

② Determine el resultado de la ronda actual: si su elección coincide con la del oponente (**1/2/3 para tijera/piedra/papel**), es un empate; de lo contrario, seleccione un ganador (tijera contra papel contra piedra contra tijera), el valor de la ronda +1 y almacene el resultado.

```python
# Main game loop
while True:

    # Process result when both players have chosen
    if me != 0 and you != 0:
        # Current round result: 1=win, 0=draw, -1=lose
        resultSymbol = "="
        # Determine round outcome
        if me == you:
            resultSymbol = "="
            # Draw
            result2 = 0
            draws += 1
        elif me == 2 and you == 1 or (me == 3 and you == 2 or me == 1 and you == 3):
            resultSymbol = "W"
            # Win
            result2 = 1
            wins += 1
        else:
            resultSymbol = "L"
            # Lose
            result2 = -1
            loses += 1

        # Save round result
        gameResults.append(result2)

        # Display result symbol
        display.show(resultSymbol)

        # Update LED strip
        showRoundResult(round2, result2)

        sleep(3000)
```

③ Almacene los resultados en un array y muestre la cadena correspondiente. Si este es el tercer juego, determine si se necesita un cuarto juego (en caso de empate total o victoria-derrota-empate). Si es así, muestre "FINAL" y espere 1 segundo antes de borrar la selección de piedra-papel-tijera.

```python
        # Check if game continues
        if round2 == 3:
            # After 3 rounds, check for 4th round
            fourth_round_needed = needFourthRound()
            if fourth_round_needed:
                # Go to 4th round
                round2 = 4
                if fourth_round_needed == 2:
                    display.scroll("FINAL")
                sleep(1000)
                display.show(Image.HEART)
                check = 1
                me = 0
                you = 0
            else:
                # End game
                if wins > loses:
                    display.scroll("WINNER")
                elif loses > wins:
                    display.scroll("LOSER")
                else:
                    display.scroll("TIE")
                sleep(3000)
                resetGame()
        elif round2 == 4:
            # 4th round finished, game over
            display.scroll("GAME OVER")
            sleep(3000)
            resetGame()
        else:
            # Next round (1st or 2nd)
            round2 += 1
            display.show(Image.HEART)
            check = 1
            me = 0
            you = 0
```

De lo contrario, muestre "WINNER" para la victoria, "LOSER" para la derrota y "TIE" para un empate. Después de un retraso de 3 segundos, llame a la función resetGame para borrar todas las variables del juego.

Si el partido consta de cuatro juegos, muestre "GAME OVER" y llame a la función resetGame nuevamente después de un retraso de 3 segundos para reiniciar todas las variables del juego.

Si el juego no ha terminado, muestra ![Img](./media/6004.png) y borra las elecciones de ambos.

④ Presione C y la placa envía "1" como tijera, y la matriz muestra ![Img](./media/6011.png); presione D y la placa envía "3" como papel, y la matriz muestra ![Img](./media/6012.png); presione E y envía "2" como piedra y muestra ![Img](./media/6013.png).

```python
    # Check button input
    if check == 1:
        if pin13.read_digital() == 0:
            # Paper -> send \'3\'
            radio.send(\'3\')
            display.show(Image.SQUARE)
            me = 3
            check = 0
            sleep(200)
        elif pin15.read_digital() == 0:
            # Scissors -> send \'1\'
            radio.send(\'1\')
            display.show(Image(\'99009:\'
                                \'99090:\'
                                \'00900:\'
                                \'99090:\'
                                \'99009\'))
            me = 1
            check = 0
            sleep(200)
        elif pin16.read_digital() == 0:
            # Rock -> send \'2\'
            radio.send(\'2\')
            display.show(Image.SQUARE_SMALL)
            me = 2
            check = 0
            sleep(200)
```

⑤ Reciba datos de radio (elección del oponente).

```python
    # Receive radio data
    try:
        received = radio.receive()
        if received is not None:
            on_received_message(received)
    except:
        pass

    sleep(100)
```

⑥ Determine si se requiere una cuarta ronda. Si los tres juegos terminan en empate total o victoria-derrota-empate, es necesario un cuarto juego; de lo contrario, no es necesario.

```python
# Check if a 4th round is needed
def needFourthRound():
    # Case 1: All 3 draws -> need 4th round, return 2
    if wins == 0 and loses == 0 and draws == 3:
        return 2
    # Case 2: 1 win, 1 loss, 1 draw -> need 4th round, return 1
    if wins == 1 and loses == 1 and draws == 1:
        return 1
    # No 4th round needed
    return 0
```

⑦ Las luces RGB muestran los colores correspondientes según el resultado: verde para la victoria, rojo para la derrota y amarillo para un empate.

```python
# Show round result on LED strip
def showRoundResult(roundNum, result):
    if roundNum <= 4:
        if result == 1:
            # Win: Green
            strip[roundNum - 1] = (0, 255, 0)
        elif result == 0:
            # Draw: Yellow
            strip[roundNum - 1] = (255, 255, 0)
        else:
            # Lose: Red
            strip[roundNum - 1] = (255, 0, 0)
        strip.show()
```

⑧ Cuando el juego termina, borre la visualización de las cuatro luces RGB.

```python
# Turn off all LEDs
def resetLights():
    for i in range(4):
        strip[i] = (0, 0, 0)  # Off
    strip.show()
```

⑨ Reinicie el estado del juego, borre todos los valores de las variables del juego, reinicie las luces RGB y muestre ![Img](./media/6004.png).

```python
# Reset game state
def resetGame():
    global me, you, round2, wins, loses, draws, gameResults, check
    me = 0
    you = 0
    round2 = 1
    wins = 0
    loses = 0
    draws = 0
    gameResults = []
    check = 1
    resetLights()
    display.show(Image.HEART)
```

#### 5.2.6.6 Resultado de la Prueba

![Img](./media/4top.png)

Después de grabar el código, inserte la placa micro:bit en la ranura del gamepad (**pilas instaladas**), y active el interruptor a “ON”.

La matriz muestra ![Img](./media/6004.png) inicialmente. Los jugadores presionan los botones para seleccionar su movimiento (E para piedra, D para papel o C para tijera), con intercambio de datos entre los dos dispositivos. Determinan el resultado de la ronda actual: una victoria se indica con la "W" con la luz RGB volviéndose verde, un empate con el "=" con la luz amarilla y una derrota con la "L" con la luz roja (la primera luz RGB se enciende después de la primera ronda, y así sucesivamente). La siguiente ronda seguirá si el juego no ha terminado.

El juego adopta el formato al mejor de tres: si las tres rondas terminan en empate total o victoria-derrota-empate, se activa un cuarto partido.

Si hay un ganador después de tres rondas, mostrará "WINNER" para la victoria y "LOSER" para la derrota. Una vez que se muestre el resultado, aparecerá "GAME OVER" para reiniciar el juego. Si la cuarta ronda sigue sin decidirse, el juego también terminará.

![Img](./media/6000.gif)

<span style="color: rgb(0, 209, 0);">**Consejo:** Espere a que aparezca el icono del corazón antes de continuar con la siguiente ronda. Si no hay respuesta en la placa, presione el botón de reinicio en la parte posterior de la placa micro:bit.</span>

![Img](./media/4bottom.png)
