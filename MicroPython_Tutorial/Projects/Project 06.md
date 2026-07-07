### 5.2.6 Steen-papier-schaar

#### 5.2.6.1 Overzicht

![Img](./media/top1.png)

Hierin spelen we steen-papier-schaar via draadloze communicatie van micro:bit. Spelers selecteren hun zet (steen, papier of schaar) via de knoppen, met gegevensuitwisseling tussen apparaten. Het spel volgt best-of-three; als alle drie de rondes eindigen in een gelijkspel of winst-verlies-gelijkspel, wordt een vierde wedstrijd geactiveerd.

Elke uitkomst wordt weergegeven op de micro:bit-matrix (W voor winst, L voor verlies, = voor gelijkspel) en onthuld door de RGB-lampjes (groen voor winst, rood voor verlies, geel voor gelijkspel) op pin P8. Na voltooiing van een ronde resetten de twee apparaten alle gegevens en lampjes, ter voorbereiding op de volgende wedstrijd.

De gameplay integreert naadloos draadloze interactie met de meer-ronde gevechten.

![Img](./media/bottom1.png)

#### 5.2.6.2 Componentkennis

![Img](./media/2top.png)

**Microbit draadloze communicatie**

![Img](./media/6001.png)

Het micro:bit-bord integreert twee handige draadloze communicatiemogelijkheden: **2.4GHz radio** en **low-power Bluetooth (BLE)**. Ze kunnen echter niet gelijktijdig worden gebruikt.

De eerste vereist geen koppeling en ondersteunt tot 255 onafhankelijke pakketten om interferentie te minimaliseren, met een communicatiebereik van 10-30 meter, waardoor snelle overdracht van digitale gegevens en strings mogelijk is. De laatste wordt voornamelijk gebruikt voor koppeling met smartphones, tablets en andere slimme apparaten voor IoT-toepassingen zoals het uploaden van sensorgegevens en afstandsbediening via mobiele apps.

Ze breiden de creatieve ontwikkelingsmogelijkheden van de micro:bit uit.

#### 5.2.6.3 Benodigde onderdelen

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 board** (zelf mee te nemen) ×2 | **micro:bit Smart Gamepad** (gemonteerd) ×2 | **AAA battery** (zelf mee te nemen) ×8 |

#### 5.2.6.4 Codestroom

![Img](./media/6002.png)

#### 5.2.6.5 Testcode

**Volledige code:**

```python
from microbit import *
import neopixel
import radio

# Global Variables
round2 = 1
check = 1
me = 0
you = 0	wins = 0
loses = 0	draws = 0
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
                display.show(Image.YES)
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


![Img](./media/line1.png)

**Korte uitleg:**

① Importeer de relevante bibliotheken, initialiseer globale variabelen en configureer pinnen.
```python
from microbit import *
import neopixel
import radio

# Global Variables
round2 = 1
check = 1
me = 0
you = 0	wins = 0
loses = 0	draws = 0
gameResults = []
strip = None

pin13.set_pull(pin13.PULL_UP)
pin15.set_pull(pin15.PULL_UP)
pin16.set_pull(pin16.PULL_UP)
# Initialize LED strip (4 LEDs, connected to pin P8)
strip = neopixel.NeoPixel(pin8, 4)
```
② `resetGame` reset alle spelstatussen.

Het wordt meestal aangeroepen aan het begin van een spel of nadat een ronde is afgelopen om alle globale variabelen met betrekking tot de spelvoortgang – inclusief spelerkeuzes, beurtentellingen, winst-/verlies-/gelijkspeltellingen en historische resultaten – terug te zetten naar hun beginwaarden.

`resetLights()` schakelt alle NeoPixel-LEDs uit en toont een hartpictogram (`Image.HEART`), wat aangeeft dat het spel klaar is om te beginnen.

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

③ `on_received_message` verwerkt de selectie van de tegenstander die via radio is ontvangen. Het verwerkt radioberichten van een andere Micro:bit (schaar, steen of papier).

Om nauwkeurigheid te garanderen, controleert het het berichttype: als het bericht een string is (\'1\', \'2\' of \'3\'), converteer het dan naar een geheel getal; als het een geheel getal is (1, 2 of 3), gebruik het dan direct.

De waarde van `you` wordt alleen bijgewerkt wanneer `you`=0 (er is geen keuze van de tegenstander ontvangen), waardoor meervoudige ontvangst wordt voorkomen.

```python
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
```

④ `resetLights` schakelt alle NeoPixel-LEDs uit. Het doorloopt alle vier de LEDs om hun kleuren in te stellen op zwart (`(0, 0, 0)`), d.w.z. uit.

`strip.show()` stuurt deze kleurupdates naar de lichtstrip om ervoor te zorgen dat alle LEDs uit zijn.

```python
# Turn off all LEDs
def resetLights():
    for i in range(4):
        strip[i] = (0, 0, 0)  # Off
    strip.show()
```

⑤ `needFourthRound` bepaalt of een vierde ronde nodig is na de drie rondes.

Het behandelt twee speciale gevallen: als alle drie de rondes eindigen in gelijkspel (`wins == 0 and loses == 0 and draws == 3`), retourneer dan `2` voor een vierde ronde --- het uiteindelijke beslissende spel; als er een winst-verlies-gelijkspel is (`wins == 1 and loses == 1 and draws == 1`), retourneer dan ook `1` voor een extra ronde. In alle andere gevallen (waarbij er een duidelijke winnaar/verliezer is), retourneer dan `0` (geen 4e ronde nodig).

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

⑥ `showRoundResult` toont het resultaat van elke ronde op de LED-strip.

Het accepteert het huidige rondenummer (`roundNum`) en het resultaat (`result`: 1 voor winst, 0 voor gelijkspel, -1 voor verlies). Op basis van het resultaat licht het verschillende kleuren op de corresponderende LED op: groen voor winst, geel voor gelijkspel en rood voor verlies.

`roundNum-1` converteert het rondenummer naar een nulgebaseerde index voor de LEDs.

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
⑦ Initialisatie wanneer het spel begint.

Het wordt één keer uitgevoerd wanneer het programma start. Het activeert de Micro:bit radiofunctie en stelt `group=1` in. Vervolgens stelt het `check` in op `1` (selectief voor speler), `me` en `you` op `0` (wachtend op keuzes van speler en tegenstander).

De NeoPixel lichtstrip wordt gewist en bijgewerkt om alle LEDs uit te schakelen. En Micro:bit toont een hartpictogram (`Image.HEART`), wat aangeeft dat het spel klaar is om te beginnen.

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

⑧ Verwerk de beurtresultaten en beheer de spelstroom.

Deze code vertegenwoordigt de kernlogica van het spel, die in een oneindige lus draait. Het controleert eerst of zowel de speler als de tegenstander hun keuzes hebben gemaakt (`me != 0 and you != 0`).

Zo ja, dan bepaalt het de uitkomst van de huidige ronde volgens de steen-papier-schaar-regels, werkt de tellers `wins`, `loses`, `draws` bij en toont het corresponderende pictogram ("W", "L", "=") op de matrix.

`showRoundResult` schakelt de LED op de NeoPixel in de gerelateerde kleuren in voor de vorige ronde.

Na het weergeven van de resultaten gedurende 3 seconden, zal het spel doorgaan op basis van het huidige beurtentelling:

*   Als het momenteel de 3e ronde is (`round2 == 3`), zal `needFourthRound()` bepalen of de uiteindelijke beslissende ronde nodig is. Zo ja, dan gaat de vierde ronde door; anders, op basis van de algehele uitkomst, toont het een WINNAAR/VERLIEZER/GELIJKSPEL en reset het spel.
*   Als het momenteel de vierde ronde is (`round2 == 4`), verklaar dan "GAME OVER" en reset het spel.
*   Als het de eerste of tweede ronde is, ronde +1 (`round2 += 1`), toon het hartpictogram, reset keuzes en bereid je voor op de volgende ronde.
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

⑨ Verwerk de knopinvoer van de speler.

Het detecteert de keuzes van spelers via externe knoppen (verbonden met `pin13`, `pin15`, `pin16`). Het detecteert alleen knopdrukken wanneer `check` = `1` (keuzes zijn toegestaan).

*   Als `pin13` wordt ingedrukt (laag), wordt een papier gekozen (`3`), en Micro:bit stuurt `3` en toont een groot vierkant.
*   Als `pin15` wordt ingedrukt, wordt een schaar gekozen (`1`), stuurt `1` en toont een schaarpictogram.
*   Als `pin16` wordt ingedrukt, wordt een steen gekozen (`2`), stuurt `2` en toont een klein vierkant.

Na het kiezen, werk `me` bij, `check` = `0` (voorkom herhaalde keuze) en vertraag 200 ms voor anti-jitter.

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

⑩ Verwerk radiogegevensontvangst en lusvertraging.

Het probeert radiogegevens te ontvangen tijdens elke hoofdloop. `radio.receive()` vangt alle inkomende berichten op. Als een bericht wordt ontvangen (`received is not None`), roep dan `on_received_message()` aan om de keuze van de tegenstander te verwerken.

Om te voorkomen dat het programma blokkeert door ontbrekende berichten, vangt `try-except` mogelijke afwijkingen op (hoewel `radio.receive()` meestal geen uitzonderingen direct in MicroPython genereert, is het een goede programmeer gewoonte).

`sleep(100)` pauzeert het programma gedurende 100 ms, reguleert de uitvoeringsfrequentie van de hoofdloop om overmatig processorverbruik te voorkomen en geeft tijd voor knopdetectie en schermvernieuwing.

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
#### 5.2.6.6 Testresultaat

![Img](./media/4top.png)

Na het branden van de code, plaatst u het micro:bit-bord in de sleuf van de gamepad (**batterijen geïnstalleerd**), en zet u de schakelaar op “ON”.

De matrix toont aanvankelijk ![Img](./media/6004.png). Spelers drukken op knoppen om hun zet te kiezen (E voor steen, D voor papier of C voor schaar), waarbij matchgegevens worden uitgewisseld tussen de twee apparaten. Ze bepalen de uitkomst van de huidige ronde: een overwinning wordt aangegeven door de "W" met groen RGB-licht, een gelijkspel door de "=" met geel licht, en een verlies door de "L" met rood (het eerste RGB-licht gaat aan na de eerste ronde, enzovoort). De volgende ronde volgt als het spel nog niet voorbij is.

Het spel hanteert best-of-three: als alle drie de rondes eindigen in een gelijkspel of winst-verlies-gelijkspel, wordt een vierde wedstrijd geactiveerd.

Als er een winnaar is na drie rondes, wordt "WINNER" weergegeven voor overwinning en "LOSER" voor nederlaag. Zodra het resultaat wordt getoond, verschijnt "GAME OVER" om het spel te resetten. Als de vierde ronde onbeslist blijft, is het spel ook voorbij.

![Img](./media/6000.gif)

<span style="color: rgb(0, 209, 0);">**Tip:** Wacht tot het hartpictogram verschijnt voordat u doorgaat met de volgende ronde. Als er geen reactie is op het bord, druk dan op de resetknop aan de achterkant van het micro:bit-bord.</span>

![Img](./media/4bottom.png)
