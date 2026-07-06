### 5.2.6 Pierre-Papier-Ciseaux

#### 5.2.6.1 Aperçu

![Img](./media/top1.png)

Ici, jouons au pierre-papier-ciseaux par communication sans fil entre deux micro:bit. Les joueurs sélectionnent leur coup (pierre, papier ou ciseaux) via les boutons, avec échange de données entre les appareils. Le jeu se joue en meilleur des trois ; si les trois manches se terminent toutes par des égalités ou par un cas victoire-défaite-nul, une quatrième manche est déclenchée.

Chaque résultat est affiché sur la matrice du micro:bit (W pour victoire, L pour défaite, = pour nul) et révélé par les lumières RGB (vert pour victoire, rouge pour défaite, jaune pour nul) sur le pin P8. À la fin d’une manche, les deux appareils réinitialisent toutes les données et les lumières, se préparant pour la manche suivante.

Le gameplay intègre de manière transparente l’interaction sans fil avec des affrontements multi-manches.

![Img](./media/bottom1.png)

#### 5.2.6.2 Connaissances des composants

![Img](./media/2top.png)

**Microbit wireless communication**

![Img](./media/6001.png)

La carte micro:bit intègre deux capacités de communication sans fil pratiques : **2.4GHz radio** et **low-power Bluetooth (BLE)**. Cependant, elles ne peuvent pas être utilisées simultanément.

La première ne nécessite pas d’appairage et prend en charge jusqu’à 255 paquets indépendants pour minimiser les interférences, avec une portée de communication de 10–30 mètres, permettant une transmission rapide de données numériques et de chaînes. Tandis que la seconde est principalement utilisée pour l’appariement avec des smartphones, tablettes et autres appareils intelligents pour des applications IoT telles que le téléversement de données capteurs et le contrôle à distance via une application mobile.

Elles élargissent les possibilités créatives de développement du micro:bit.

#### 5.2.6.3 Pièces requises

| ![Img](./media/microbitV2.png)|  ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 board** (self-provided) ×2 | **micro:bit Smart Gamepad** (assembled) ×2 | **AAA battery** (self-provided) ×8 |

#### 5.2.6.4 Flux du code

![Img](./media/6002.png)

#### 5.2.6.5 Code de test

**Code complet :**


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

# Receive opponent's choice via radio
def on_received_message(receivedMsg):
    global you
    if you == 0:
        # Convert string to integer if needed
        if isinstance(receivedMsg, str) and receivedMsg in ['1', '2', '3']:
            you = int(receivedMsg)
        # Use directly if it's an integer
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
            # Paper -> send '3'
            radio.send('3')
            display.show(Image.SQUARE)
            me = 3
            check = 0
            sleep(200)
        elif pin15.read_digital() == 0:
            # Scissors -> send '1'
            radio.send('1')
            display.show(Image('99009:'
                                '99090:'
                                '00900:'
                                '99090:'
                                '99009'))
            me = 1
            check = 0
            sleep(200)
        elif pin16.read_digital() == 0:
            # Rock -> send '2'
            radio.send('2')
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


# Receive opponent's choice via radio
def on_received_message(receivedMsg):
    global you
    if you == 0:
        # Convert string to integer if needed
        if isinstance(receivedMsg, str) and receivedMsg in ['1', '2', '3']:
            you = int(receivedMsg)
        # Use directly if it's an integer
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
            # Paper -> send '3'
            radio.send('3')
            display.show(Image.SQUARE)
            me = 3
            check = 0
            sleep(200)
        elif pin15.read_digital() == 0:
            # Scissors -> send '1'
            radio.send('1')
            display.show(Image('99009:'
                                '99090:'
                                '00900:'
                                '99090:'
                                '99009'))
            me = 1
            check = 0
            sleep(200)
        elif pin16.read_digital() == 0:
            # Rock -> send '2'
            radio.send('2')
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

**Brève explication :**

① Importer les bibliothèques pertinentes, initialiser les variables globales et configurer les pins.
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
② `resetGame` réinitialise tous les états du jeu.

Il est généralement appelé au démarrage d’un jeu ou après la fin d’une manche pour remettre à leurs valeurs initiales toutes les variables globales liées à la progression du jeu — y compris les sélections des joueurs, le nombre de manches, les comptes de victoires/défaites/égalité et l’historique des résultats.

`resetLights()` éteint tous les NeoPixel et affiche une icône en forme de cœur (`Image.HEART`), indiquant que le jeu est prêt à commencer.

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

③ `on_received_message` traite la sélection de l’adversaire reçue via la radio. Il gère les messages radio provenant d’un autre micro:bit (ciseaux, pierre ou papier).

Pour garantir l’exactitude, il vérifie le type du message : si le message est une chaîne ('1', '2' ou '3'), le convertir en entier ; si c’est déjà un entier (1, 2 ou 3), l’utiliser directement.

La valeur de `you` est mise à jour uniquement lorsque `you` = 0 (aucun choix de l’adversaire reçu), empêchant les réceptions multiples.

```python
# Receive opponent's choice via radio
def on_received_message(receivedMsg):
    global you
    if you == 0:
        # Convert string to integer if needed
        if isinstance(receivedMsg, str) and receivedMsg in ['1', '2', '3']:
            you = int(receivedMsg)
        # Use directly if it's an integer
        elif isinstance(receivedMsg, int) and receivedMsg in [1, 2, 3]:
            you = receivedMsg
```

④ `resetLights` éteint tous les NeoPixel. Il itère sur les quatre LEDs pour définir leur couleur en noir (`(0, 0, 0)`), c’est-à-dire éteint.

`strip.show()` envoie ces mises à jour de couleur à la bande lumineuse pour s’assurer que toutes les LEDs sont éteintes.

```python
# Turn off all LEDs
def resetLights():
    for i in range(4):
        strip[i] = (0, 0, 0)  # Off
    strip.show()
```

⑤ `needFourthRound` détermine si une quatrième manche est nécessaire après les trois manches.

Elle gère deux cas particuliers : si les trois manches se terminent par des égalités (`wins == 0 and loses == 0 and draws == 3`), retourner `2` pour une quatrième manche — la partie décisive finale ; si on a un cas victoire-défaite-nul (`wins == 1 and loses == 1 and draws == 1`), retourner aussi `1` pour une manche supplémentaire. Dans tous les autres cas (où il y a un gagnant clair/perdant clair), retourner `0` (pas de 4ᵉ manche nécessaire).

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

⑥ `showRoundResult` affiche le résultat de chaque manche sur la bande LED.

Elle accepte le numéro de la manche en cours (`roundNum`) et le résultat (`result` : 1 pour victoire, 0 pour nul, -1 pour défaite). Selon le résultat, elle allume différentes couleurs sur la LED correspondante : vert pour victoire, jaune pour nul, et rouge pour défaite.

`roundNum-1` convertit le numéro de manche en un index zéro-basé pour les LEDs.

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
⑦ Initialisation au démarrage du jeu.

Elle s’exécute une fois au démarrage du programme. Elle active la fonction radio du micro:bit et définit `group=1`. Ensuite, elle met `check` à `1` (sélectionnable pour le joueur), `me` et `you` à `0` (en attente des choix du joueur et de l’adversaire).

La bande NeoPixel est effacée et mise à jour pour éteindre toutes les LEDs. Et le micro:bit affiche une icône cœur (`Image.HEART`) comme invite initiale en attente de l’entrée du joueur.

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

⑧ Traiter les résultats des manches et contrôler le flux du jeu.

Ce code représente la logique principale du jeu, exécutée dans une boucle infinie. Il vérifie d’abord si le Joueur et l’Adversaire ont fait leurs choix (`me != 0 and you != 0`).

Si oui, il détermine l’issue de la manche en cours selon les règles du pierre-papier-ciseaux, met à jour les compteurs `wins`, `loses`, `draws`, et affiche l’icône correspondante ("W", "L", "=") sur la matrice.

`showRoundResult` allume la LED NeoPixel correspondante dans les couleurs liées pour la manche précédente.

Après avoir affiché les résultats pendant 3s, le jeu poursuit son cours selon le numéro de manche actuel :

*   Si c’est la 3ᵉ manche (`round2 == 3`), `needFourthRound()` déterminera si la manche décisive finale est requise. Si oui, la quatrième manche se déroule ; sinon, selon le résultat global, afficher "WINNER"/"LOSER"/"TIE" et réinitialiser le jeu.
*   Si c’est la quatrième manche (`round2 == 4`), déclarer "GAME OVER" et réinitialiser le jeu.
*   Si c’est la première ou la deuxième manche, incrémenter la manche (`round2 += 1`), afficher l’icône cœur, réinitialiser les choix et se préparer pour la manche suivante.
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

⑨ Traiter l’entrée des boutons du joueur.

Il détecte les choix des joueurs via des boutons externes (connectés à `pin13`, `pin15`, `pin16`). Il détecte l’appui uniquement lorsque `check` = `1` (les choix sont autorisés).

*   Si `pin13` est pressé (low), Papier est choisi (`3`), et le micro:bit envoie `'3'` et affiche un grand carré.
*   Si `pin15` est pressé, Ciseaux est choisi (`1`), envoie `'1'` et affiche une icône de ciseaux.
*   Si `pin16` est pressé, Pierre est choisi (`2`), envoie `'2'` et affiche un petit carré.

Après le choix, mettre à jour `me`, `check` = `0` (éviter les choix répétés) et attendre 200 ms pour anti-rebond.

```python
    # Check button input
    if check == 1:
        if pin13.read_digital() == 0:
            # Paper -> send '3'
            radio.send('3')
            display.show(Image.SQUARE)
            me = 3
            check = 0
            sleep(200)
        elif pin15.read_digital() == 0:
            # Scissors -> send '1'
            radio.send('1')
            display.show(Image('99009:'
                                '99090:'
                                '00900:'
                                '99090:'
                                '99009'))
            me = 1
            check = 0
            sleep(200)
        elif pin16.read_digital() == 0:
            # Rock -> send '2'
            radio.send('2')
            display.show(Image.SQUARE_SMALL)
            me = 2
            check = 0
            sleep(200)
```

⑩ Gérer la réception des données radio et la temporisation de la boucle.

Il tente de recevoir des données radio à chaque itération de la boucle principale. `radio.receive()` capture les messages entrants. Si un message est reçu (`received is not None`), appeler `on_received_message()` pour traiter le choix de l’adversaire.

Pour éviter que le programme ne se bloque en cas de messages manquants, un `try-except` capture d’éventuelles anomalies (bien que `radio.receive()` ne lance généralement pas d’exceptions directement en MicroPython, c’est une bonne pratique).

`sleep(100)` met le programme en pause pendant 100 ms, régulant la fréquence d’exécution de la boucle principale pour éviter une consommation excessive du processeur et permettant le temps nécessaire à la détection des boutons et au rafraîchissement de l’affichage.

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
#### 5.2.6.6 Résultat du test

![Img](./media/4top.png)

Après avoir téléversé le code, insérez la carte micro:bit dans le logement du gamepad (**piles installées**) et basculez son interrupteur sur “ON”.

La matrice affiche ![Img](./media/6004.png) initialement. Les joueurs appuient sur les boutons pour sélectionner leur coup (E pour pierre, D pour papier, ou C pour ciseaux), avec échange des données de la manche entre les deux appareils. Ils déterminent l’issue de la manche actuelle : une victoire est indiquée par le "W" avec la LED RGB devenant verte, une égalité par le "=" avec la LED jaune, et une défaite par le "L" avec la LED rouge (la première LED RGB s’allume après la première manche, et ainsi de suite). La manche suivante commence si le jeu n’est pas terminé.

Le jeu adopte le meilleur des trois : si les trois manches se terminent toutes par des égalités ou par un cas victoire-défaite-nul, une quatrième manche est déclenchée.

S’il y a un gagnant après trois manches, il affichera "WINNER" pour la victoire et "LOSER" pour la défaite. Une fois le résultat affiché, "GAME OVER" apparaîtra pour réinitialiser le jeu. Si la quatrième manche reste indécise, le jeu se terminera également.

![Img](./media/6000.gif)

<span style="color: rgb(0, 209, 0);">**Astuce :** Attendez que l’icône cœur apparaisse avant de poursuivre la manche suivante. Si aucune réponse n’apparaît sur la carte, veuillez appuyer sur le bouton de réinitialisation au dos de la carte micro:bit.</span>

![Img](./media/4bottom.png)