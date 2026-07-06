### 5.2.6 Schere-Stein-Papier

#### 5.2.6.1 Übersicht

![Img](./media/top1.png)

Hier spielen wir Schere-Stein-Papier über die drahtlose Kommunikation des micro:bit. Spieler wählen ihren Zug (Stein, Papier oder Schere) über die Tasten, wobei Daten zwischen den Geräten ausgetauscht werden. Das Spiel folgt dem Best-of-Three-Prinzip; wenn alle drei Runden unentschieden enden oder in einem Sieg-Niederlage-Unentschieden, wird ein viertes Spiel ausgelöst.

Jedes Ergebnis wird auf der micro:bit-Matrix angezeigt (W für Sieg, L für Niederlage, = für Unentschieden) und durch die RGB-Lichter (grün für Sieg, rot für Niederlage, gelb für Unentschieden) an Pin P8 enthüllt. Nach Abschluss einer Runde setzen die beiden Geräte alle Daten und Lichter zurück und bereiten sich auf das nächste Spiel vor.

Das Gameplay integriert nahtlos drahtlose Interaktion mit dem Mehrrunden-Kampf.

![Img](./media/bottom1.png)

#### 5.2.6.2 Komponentenwissen

![Img](./media/2top.png)

**Microbit drahtlose Kommunikation**

![Img](./media/6001.png)

Das micro:bit-Board integriert zwei praktische drahtlose Kommunikationsfunktionen: **2.4GHz-Radio** und **Low-Power-Bluetooth (BLE)**. Sie können jedoch nicht gleichzeitig verwendet werden.

Ersteres erfordert keine Kopplung und unterstützt bis zu 255 unabhängige Pakete, um Interferenzen zu minimieren, mit einer Kommunikationsreichweite von 10–30 Metern, was eine schnelle Übertragung von digitalen Daten und Zeichenketten ermöglicht. Letzteres wird hauptsächlich zum Koppeln mit Smartphones, Tablets und anderen intelligenten Geräten für IoT-Anwendungen wie Sensor-Daten-Upload und Fernsteuerung über mobile Apps verwendet.

Sie erweitern die kreativen Entwicklungsmöglichkeiten des micro:bit.

#### 5.2.6.3 Benötigte Teile

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 Board** (selbst mitgebracht) ×2 | **micro:bit Smart Gamepad** (montiert) ×2 | **AAA Batterie** (selbst mitgebracht) ×8 |

#### 5.2.6.4 Codeablauf

![Img](./media/6002.png)

#### 5.2.6.5 Testcode

**Vollständiger Code:**


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

# Receive opponent\\'s choice via radio
def on_received_message(receivedMsg):
    global you
    if you == 0:
        # Convert string to integer if needed
        if isinstance(receivedMsg, str) and receivedMsg in [\'1\', \'2\', \'3\']:
            you = int(receivedMsg)
        # Use directly if it\\'s an integer
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

**Kurze Erklärung:**

① Importieren Sie die relevanten Bibliotheken, initialisieren Sie globale Variablen und konfigurieren Sie Pins.
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
② `resetGame` setzt alle Spielzustände zurück.

Es wird normalerweise zu Beginn eines Spiels oder nach Abschluss einer Runde aufgerufen, um alle globalen Variablen, die mit dem Spielfortschritt zusammenhängen – einschließlich Spielerauswahlen, Rundenzählungen, Gewinn-/Verlust-/Unentschieden-Zählungen und historischen Ergebnissen – auf ihre Anfangswerte zurückzusetzen.

`resetLights()` schaltet alle NeoPixel-LEDs aus und zeigt ein Herzsymbol (`Image.HEART`) an, das anzeigt, dass das Spiel bereit ist zu beginnen.

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

③ `on_received_message` verarbeitet die über Funk empfangene Auswahl des Gegners. Es verarbeitet Funkmeldungen von einem anderen Micro:bit (Schere, Stein oder Papier).

Um die Genauigkeit zu gewährleisten, wird der Nachrichtentyp überprüft: Wenn die Nachricht eine Zeichenkette (\'1\', \'2\' oder \'3\') ist, wird sie in eine Ganzzahl umgewandelt; wenn es sich um eine Ganzzahl (1, 2 oder 3) handelt, wird sie direkt verwendet.

Der Wert von `you` wird nur aktualisiert, wenn `you`=0 (keine Gegnerauswahl empfangen), wodurch Mehrfachempfang verhindert wird.

```python
# Receive opponent\\'s choice via radio
def on_received_message(receivedMsg):
    global you
    if you == 0:
        # Convert string to integer if needed
        if isinstance(receivedMsg, str) and receivedMsg in [\'1\', \'2\', \'3\']:
            you = int(receivedMsg)
        # Use directly if it\\'s an integer
        elif isinstance(receivedMsg, int) and receivedMsg in [1, 2, 3]:
            you = receivedMsg
```

④ `resetLights` schaltet alle NeoPixel-LEDs aus. Es durchläuft alle vier LEDs, um ihre Farben auf Schwarz (`(0, 0, 0)`) zu setzen, d.h. aus.

`strip.show()` sendet diese Farbaktualisierungen an den Lichtstreifen, um sicherzustellen, dass alle LEDs ausgeschaltet sind.

```python
# Turn off all LEDs
def resetLights():
    for i in range(4):
        strip[i] = (0, 0, 0)  # Off
    strip.show()
```

⑤ `needFourthRound` bestimmt, ob nach den drei Runden eine vierte Runde erforderlich ist.

Es behandelt zwei Sonderfälle: Wenn alle drei Runden unentschieden enden (`wins == 0 and loses == 0 and draws == 3`), wird `2` für eine vierte Runde zurückgegeben – das endgültige entscheidende Spiel; Wenn es einen Sieg-Niederlage-Unentschieden gibt (`wins == 1 and loses == 1 and draws == 1`), wird ebenfalls `1` für eine zusätzliche Runde zurückgegeben. In allen anderen Fällen (wo es einen klaren Gewinner/Verlierer gibt), wird `0` zurückgegeben (keine 4. Runde erforderlich).

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

⑥ `showRoundResult` zeigt das Ergebnis jeder Runde auf dem LED-Streifen an.

Es akzeptiert die aktuelle Rundennummer (`roundNum`) und das Ergebnis (`result`: 1 für Sieg, 0 für Unentschieden, -1 für Niederlage). Basierend auf dem Ergebnis leuchtet es verschiedene Farben auf der entsprechenden LED auf: grün für Sieg, gelb für Unentschieden und rot für Niederlage.

`roundNum-1` konvertiert die Rundennummer in einen nullbasierten Index für die LEDs.

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
⑦ Initialisierung beim Spielstart.

Es wird einmal ausgeführt, wenn das Programm startet. Es aktiviert die Micro:bit-Radiofunktion und setzt `group=1`. Als Nächstes setzt es `check` auf `1` (selektiv für Spieler), `me` und `you` auf `0` (warten auf Spieler- und Gegnerauswahl).

Der NeoPixel-Lichtstreifen wird gelöscht und aktualisiert, um alle LEDs auszuschalten. Und Micro:bit zeigt ein Herzsymbol (`Image.HEART`) als anfängliche Aufforderung zur Spielereingabe an.

```python
# Game initialization
radio.on()
radio.config(group=1)
check = 1
me = 0
you = 0
strip.clear()
strip.show()
display.show(Image.HEART)
```

⑧ Verarbeiten Sie die Runden-Ergebnisse und steuern Sie den Spielfluss.

Dieser Code repräsentiert die Kernlogik des Spiels, die in einer Endlosschleife läuft. Er überprüft zuerst, ob sowohl Spieler als auch Gegner ihre Entscheidungen getroffen haben (`me != 0 and you != 0`).

Wenn ja, bestimmt er das Ergebnis der aktuellen Runde gemäß den Schere-Stein-Papier-Regeln, aktualisiert die Zähler `wins`, `loses`, `draws` und zeigt das entsprechende Symbol ("W", "L", "=") auf der Matrix an.

`showRoundResult` schaltet die LED auf dem NeoPixel in den entsprechenden Farben für die vorherige Runde ein.

Nachdem die Ergebnisse 3 Sekunden lang angezeigt wurden, wird das Spiel basierend auf der aktuellen Rundenzahl fortgesetzt:

*   Wenn es sich um die 3. Runde handelt (`round2 == 3`), bestimmt `needFourthRound()`, ob die endgültige entscheidende Runde erforderlich ist. Wenn ja, wird die vierte Runde fortgesetzt; andernfalls wird basierend auf dem Gesamtergebnis ein GEWINNER/VERLIERER/UNENTSCHIEDEN angezeigt und das Spiel zurückgesetzt.
*   Wenn es sich um die vierte Runde handelt (`round2 == 4`), wird "GAME OVER" deklariert und das Spiel zurückgesetzt.
*   Wenn es die erste oder zweite Runde ist, wird die Runde um 1 erhöht (`round2 += 1`), das Herzsymbol angezeigt, die Auswahl zurückgesetzt und die Vorbereitung auf die nächste Runde getroffen.
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

⑨ Verarbeiten Sie die Tasten-Eingabe des Spielers.

Es erkennt die Auswahl der Spieler über externe Tasten (verbunden mit `pin13`, `pin15`, `pin16`). Es erkennt einen Tastendruck nur, wenn `check` = `1` (Auswahl ist erlaubt).

*   Wenn `pin13` gedrückt wird (niedrig), wird Papier gewählt (`3`), und Micro:bit sendet `\'3\'` und zeigt ein großes Quadrat an.
*   Wenn `pin15` gedrückt wird, wird Schere gewählt (`1`), sendet `\'1\'` und zeigt ein Schere-Symbol an.
*   Wenn `pin16` gedrückt wird, wird Stein gewählt (`2`), sendet `\'2\'` und zeigt ein kleines Quadrat an.

Nach der Auswahl aktualisieren Sie `me`, `check` = `0` (vermeiden Sie doppelte Auswahl) und verzögern Sie 200 ms zur Entprellung.

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

⑩ Funkdatenempfang und Schleifenverzögerung behandeln.

Es versucht, während jeder Hauptschleife Funkdaten zu empfangen. `radio.receive()` erfasst alle eingehenden Nachrichten. Wenn eine Nachricht empfangen wird (`received is not None`), rufen Sie `on_received_message()` auf, um die Auswahl des Gegners zu verarbeiten.

Um zu verhindern, dass das Programm aufgrund fehlender Nachrichten blockiert wird, fängt `try-except` mögliche Anomalien ab (obwohl `radio.receive()` in MicroPython normalerweise keine Ausnahmen direkt auslöst, ist es eine gute Programmiergewohnheit).

`sleep(100)` pausiert das Programm für 100 ms, reguliert die Ausführungsfrequenz der Hauptschleife, um übermäßigen Prozessorverbrauch zu vermeiden und Zeit für die Tastenerkennung und Bildschirmanzeige zu ermöglichen.

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
#### 5.2.6.6 Testergebnis

![Img](./media/4top.png)

Nach dem Brennen des Codes stecken Sie das micro:bit-Board in den Steckplatz des Gamepads (**Batterien eingelegt**) und schalten Sie den Schalter auf „ON“.

Die Matrix zeigt zunächst ![Img](./media/6004.png) an. Spieler drücken Tasten, um ihren Zug auszuwählen (E für Stein, D für Papier oder C für Schere), wobei die Spieldaten zwischen den beiden Geräten ausgetauscht werden. Sie bestimmen das Ergebnis der aktuellen Runde: Ein Sieg wird durch "W" mit grünem RGB-Licht angezeigt, ein Unentschieden durch "=" mit gelbem Licht und eine Niederlage durch "L" mit rotem Licht (das erste RGB-Licht leuchtet nach der ersten Runde auf usw.). Die nächste Runde folgt, wenn das Spiel nicht beendet ist.

Das Spiel wird im Best-of-Three-Modus gespielt: Wenn alle drei Runden unentschieden enden oder in einem Sieg-Niederlage-Unentschieden, wird ein viertes Spiel ausgelöst.

Wenn es nach drei Runden einen Gewinner gibt, wird "WINNER" für den Sieg und "LOSER" für die Niederlage angezeigt. Sobald das Ergebnis angezeigt wird, erscheint "GAME OVER", um das Spiel zurückzusetzen. Wenn die vierte Runde unentschieden bleibt, ist das Spiel ebenfalls beendet.

![Img](./media/6000.gif)

<span style="color: rgb(0, 209, 0);">**Tipp:** Warten Sie, bis das Herzsymbol erscheint, bevor Sie die nächste Runde fortsetzen. Wenn das Board nicht reagiert, drücken Sie bitte die Reset-Taste auf der Rückseite des micro:bit-Boards.</span>

![Img](./media/4bottom.png)
