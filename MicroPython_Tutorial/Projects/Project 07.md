### 5.2.7 Deviner le nombre

#### 5.2.7.1 Aperçu

![Img](./media/top1.png)

Dans ce projet, nous jouons à un jeu de devinette de nombre à l'aide d'une carte Micro:bit, d'une carte de contrôle gamepad et d'un OLED display. Lorsque le nombre correct est deviné, l'OLED affiche "Great!!!" ; si la supposition est trop élevée ou trop basse, il affiche respectivement "To High!"/"To Low!", ainsi que la plage correspondante des nombres possibles.

![Img](./media/bottom1.png)

#### 5.2.7.2 Pièces requises

| ![Img](./media/microbitV2.png)|  ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 board** (fourni par vos soins) ×1 | **micro:bit Smart Gamepad** (assemblé) ×1 | **AAA battery** (fourni par vos soins) ×4 |
|![Img](./media/OLED.png)|![Img](./media/7008.png)||
|    **OLED display** (fourni par vos soins) ×1     |   **F-F DuPont wire** (fourni par vos soins) ×4    ||

#### 5.2.7.3 Schéma de câblage

![Img](./media/jiexian8.png)

**Après avoir câblé comme indiqué ci-dessus, insérez le micro:bit dans la fente de la carte de contrôle du gamepad.**

| OLED display | micro:bit gamepad control board | micro:bit board pin |
| :----------: | :-----------------------------: | :-----------------: |
|     GND      |               GND               |         GND         |
|     VCC      |               3V                |         3V          |
|     SDA      |               SDA               |         P20         |
|     SCL      |               SCL               |         P19         |

#### 5.2.7.4 Flux du code

![Img](./media/8001.png)

#### 5.2.7.5 Code de test

⚠️ **Notez que l'OLED est utilisé ici, donc nous devons importer sa bibliothèque.**

![Img](./media/t7000.png)

**Code complet :**

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

**Brève explication :**

① Importez les bibliothèques, initialisez l'OLED, définissez les variables globales et configurez les broches des boutons.

Trois bibliothèques sont nécessaires : `microbit` (pour accéder au matériel Micro:bit), `oled_ssd1306` (pour contrôler l'OLED display connecté), `random` (pour générer des nombres aléatoires dans le jeu).

`initialize()` et `clear_oled()` initialisent et effacent l'OLED.

Une série de variables globales est définie pour gérer les paramètres de l'état du jeu, y compris le mode du jeu (`mode`), la plage de nombres (`min_num`, `max_num`), la valeur actuelle devinée (`current_guess`), le nombre cible (`target_num`), le retour du jeu (`state`) et un drapeau contrôlant les mises à jour de l'affichage (`update_display`).

`pin13`, `pin15` et `pin16` sont configurés en mode pull-up — maintiennent un niveau haut lorsque le bouton n'est pas pressé et bas lorsqu'il est pressé.

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
② Logique d'initialisation du jeu dans la boucle principale.

C'est le premier bloc logique de la boucle principale du programme, responsable de l'initialisation ou du redémarrage du jeu.

`mode` = `0` : le jeu nécessite une initialisation. Dans ce cas, il réinitialise la plage de devinette à 1–100 et définit la valeur de devinette actuelle à 50. Il utilise `randint(min_num, max_num)` pour générer aléatoirement un entier entre 1 et 100 comme nombre cible (`target_num`).

Ensuite, `state` = `0` (état initial) et `mode` = `1` (en cours). Et il définit `update_display` sur `True` pour garantir que l'OLED affiche immédiatement les dernières informations du jeu pendant l'exécution.

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
③ Gestion des entrées des boutons et prise de décision selon la supposition.

Lorsque le jeu est en fonctionnement (`mode == 1`), il gère les interactions du joueur et la logique du jeu. Il détecte indépendamment les entrées des trois boutons externes :

*   **`pin15` est pressé** : (niveau bas détecté) ; `current_guess` + 1. Pour empêcher la valeur de dépasser la plage, il vérifie et limite `current_guess` ≤ `max_num`.
*   **`pin13` est pressé** : `current_guess` - 1. Il vérifie aussi que `current_guess` ≥ `min_num`.
*   **`pin16` est pressé** : le joueur soumet la valeur devinée. Elle est comparée avec `target_num` :
    *   `current_guess` > `target_num` : `state` = `1` (trop grand) et définit la borne maximale `max_num` sur `current_guess`.
    *   `current_guess` < `target_num` : `state` = `2` (trop petit) et définit la borne minimale `min_num` sur `current_guess`.
    *   `current_guess` = `target_num` : `state` = `3` (Correct) et définit `mode` à `0` pour préparer la manche suivante.

Après chaque appui de bouton, `update_display` est mis à `True` pour mettre à jour l'OLED, avec un délai de 50 ms pour anti-rebond.

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
④ Logique de mise à jour de l'OLED.

Elle affiche l'état et les informations courantes du jeu sur l'OLED. Elle s'exécute uniquement lorsque `update_display` = `True` afin d'éviter des rafraîchissements inutiles.

Chaque exécution appelle d'abord `clear_oled()` pour effacer l'affichage. La plage de devinette actuelle (par ex. "num:1~100") apparaît sur la première ligne. La devinette actuelle du joueur (`current_guess`) est affichée sur la troisième ligne.

Selon `state`, le message de retour correspondant ("TO High", "TO Low", ou "Great!!!") apparaît sur la cinquième ligne.

Après avoir effectué toutes les affichages, `update_display` est remis à `False` pour être prêt à mettre à jour au prochain changement d'état du jeu.

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
⑤ Gestion des délais après une bonne réponse.

Cette partie s'exécute uniquement lorsque le joueur devine correctement le nombre cible (`state == 3`). Ensuite, une pause de 1000 ms (1 s) est effectuée pour permettre aux joueurs de voir "Great!!!".

Puis, `state` est réinitialisé à `0`. Comme `mode` a déjà été remis à `0`, après une bonne réponse le jeu redémarrera depuis l'initialisation.

```python
    # 4. Delay after correct guess to show message
    if state == 3:
        sleep(1000)
        state = 0
```

#### 5.2.7.6 Résultat du test

![Img](./media/4top.png)

Après avoir flashé le code, insérez la carte micro:bit dans la fente du gamepad (**batteries installées**), et mettez l'interrupteur de celui-ci sur "ON".

Après l'upload du code, l'OLED s'initialise et affiche la plage de valeurs "num: 1 ~ 100" et la devinette initiale de 50. Vous pouvez appuyer sur C pour augmenter la valeur devinée de +1 (jusqu'à 100) ou sur E pour diminuer la valeur devinée de -1 (jusqu'à 1) afin de changer la valeur affichée sur l'OLED.

Appuyez sur D pour soumettre votre valeur ; la devinette sera comparée avec la valeur cible aléatoire. Si la devinette > valeur, affiche "To High!" et assigne la devinette à max_num ; si la devinette < valeur, affiche "To Low!" et l'assigne à min_num. Si par chance la devinette = valeur, vous verrez "Great!!!" pendant 1 seconde.

Ensuite, le jeu sera réinitialisé et une nouvelle valeur cible sera définie. Rejouez une autre manche !

![Img](./media/t7000.gif)

⚠️ **Les blocs de construction montrés dans Résultat du test ne sont pas inclus dans ce kit de produit.**

<span style="color: rgb(0, 209, 0);">**Astuce :** Si la carte ne répond pas, appuyez sur le bouton reset à l'arrière de la carte micro:bit.</span>

![Img](./media/4bottom.png)