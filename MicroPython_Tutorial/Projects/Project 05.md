### 5.2.5 Éviter les briques

#### 5.2.5.1 Aperçu

![Img](./media/top1.png)

Dans ce projet, nous jouons à un jeu d'évitement de briques où les joueurs utilisent un Micro:bit gamepad pour déplacer leur indicateur LED à gauche et à droite tout en évitant les briques qui tombent depuis le haut. Il y a trois états : a) une icône animée au démarrage, b) des actions d'évitement en temps réel pendant la partie, et c) un score final après collision.

Les joueurs gagnent 1 point après chaque évitement (lorsque la brique atteint le bas), et la partie se termine lorsqu'ils entrent en collision avec une brique ; le score final est affiché avec un effet de défilement.

Le jeu peut être démarré ou réinitialisé en appuyant simultanément sur A+B. Ce mécanisme de jeu simple combine réactivité en temps réel et anticipation stratégique.

![Img](./media/bottom1.png)

#### 5.2.5.2 Pièces requises

| ![Img](./media/microbitV2.png)|  ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 board** (à fournir) ×1 | **micro:bit Smart Gamepad** (assemblé) ×1 | **AAA battery** (à fournir) ×4 |

#### 5.2.5.3 Flux du code

![Img](./media/5001.png)

#### 5.2.5.4 Code de test

⚠️ **Remarque : le seuil initial ''brick_move_speed=300'' peut être modifié selon vos besoins. Plus la valeur est élevée, plus la chute de la brique sera lente.**

**Code complet :**


```python
import utime
import random
from microbit import *

# ===================== Global Configuration & Variables =====================
# Player initial configuration (micro:bit pixel coordinates: col=column(0-4, left-right), row=row(0-4, top-bottom))
player_fixed_row = 4    # Player's fixed row (bottom row)
player_init_col = 4     # Player's initial column (rightmost)
brick_move_speed = 300  # Brick falling interval (ms)

# Game state: 0=not started 1=running 2=game over
game_state = 0
brick_x = 0             # Brick current column (left-right)
brick_y = 0             # Brick current row (top-bottom)
score = 0               # Score counter
a_pressed_flag = False  # Left move button debounce flag
b_pressed_flag = False  # Right move button debounce flag
collision_x = False     # Collision detection - same column
collision_y = False     # Collision detection - same row
flash_count = 0         # End screen flash counter
time_passed = 0         # Time difference (for brick falling)
current_time = 0        # Current timestamp
last_brick_time = 0     # Last brick falling timestamp
start_flag = 0          # Start button debounce flag
can_start = False       # Game start flag
ab_pressed = False      # A+B pressed simultaneously flag
player_col = player_init_col  # Player's current column

# Initialize pins with pull-up (PULL_UP: pressed=low level 0, released=high level 1)
pin13.set_pull(pin13.PULL_UP)  # Right move button
pin15.set_pull(pin15.PULL_UP)  # Left move button
```

**Brève explication :**

① Importation des bibliothèques, configuration des constantes et initialisation.

Le programme importe d'abord `utime` pour les opérations liées au temps (par ex. délais), `random` pour générer des nombres aléatoires, et `microbit` pour accéder au matériel du Micro:bit.

Il définit ensuite des variables et constantes globales pour configurer le jeu :

*   `player_fixed_row` et `player_init_col` définissent la position initiale du joueur (à la colonne la plus à droite de la ligne du bas).
*   `brick_move_speed` règle l'intervalle de temps (en millisecondes) de la chute des briques.
*   `game_state` suit l'état du jeu (0=initial, 1=en cours, 2=fin de jeu).
*   `brick_x`, `brick_y` stockent les coordonnées actuelles de la brique.
*   `score` enregistre le score.
*   `a_pressed_flag`, `b_pressed_flag` évitent les rebonds des boutons.
*   `collision_x`, `collision_y` détectent les collisions.
*   `flash_count` crée un effet de clignotement en fin de partie.
*   `time_passed`, `current_time`, `last_brick_time` servent à temporiser la chute des briques.
*   `start_flag`, `can_start`, `ab_pressed` servent au démarrage du jeu et à l'anti-rebond des boutons.
*   `player_col` stocke la colonne actuelle du joueur.

Enfin, il configure `pin13` et `pin15` (utilisés pour les mouvements gauche/droite) en résistance pull-up interne (`pinX.PULL_UP`), ce qui signifie que les broches maintiennent un niveau haut (1) lorsque les boutons ne sont pas pressés et un niveau bas (0) lorsque pressés.

```python
import utime
import random
from microbit import *

# ===================== Global Configuration & Variables =====================
# Player initial configuration (micro:bit pixel coordinates: col=column(0-4, left-right), row=row(0-4, top-bottom))
player_fixed_row = 4    # Player's fixed row (bottom row)
player_init_col = 4     # Player's initial column (rightmost)
brick_move_speed = 300  # Brick falling interval (ms)

# Game state: 0=not started 1=running 2=game over
game_state = 0
brick_x = 0             # Brick current column (left-right)
brick_y = 0             # Brick current row (top-bottom)
score = 0               # Score counter
a_pressed_flag = False  # Left move button debounce flag
b_pressed_flag = False  # Right move button debounce flag
collision_x = False     # Collision detection - same column
collision_y = False     # Collision detection - same row
flash_count = 0         # End screen flash counter
time_passed = 0         # Time difference (for brick falling)
current_time = 0        # Current timestamp
last_brick_time = 0     # Last brick falling timestamp
start_flag = 0          # Start button debounce flag
can_start = False       # Game start flag
ab_pressed = False      # A+B pressed simultaneously flag
player_col = player_init_col  # Player's current column

# Initialize pins with pull-up (PULL_UP: pressed=low level 0, released=high level 1)
pin13.set_pull(pin13.PULL_UP)  # Right move button
pin15.set_pull(pin15.PULL_UP)  # Left move button
```

② Définitions des fonctions principales.

Les fonctions principales du jeu sont :

*   `on_start()` : Appelée au démarrage du programme. Elle initialise principalement la colonne de départ de la brique, en choisissant aléatoirement une valeur entre 0 et 4.
*   `draw_game()` : Responsable du rendu des éléments de jeu sur la matrice LED 5x5 du Micro:bit. Elle efface l'affichage et montre le joueur à la luminosité maximale (9) sur la ligne `player_fixed_row` avec la colonne déterminée par `player_col`. Lorsque le jeu est en cours (`game_state == 1`), elle affiche la brique avec une luminosité moyenne (7).
*   `reset_game()` : Remet le jeu à son état initial. Elle place `game_state` à 1, réinitialise le joueur, la brique et le score, remet à zéro les flags anti-rebond des boutons et efface l'affichage.
*   `check_collision()` : Détecte si une collision se produit entre la brique et le joueur. Cela se fait en comparant l'axe `x` (`brick_x == player_col`) et l'axe `y` (`brick_y == player_fixed_row`). Si les deux correspondent, une collision est détectée, `game_state` passe à 2 (fin de jeu), l'affichage est effacé et `flash_count` est remis à zéro.

```python
# ===================== Core Functions =====================
def on_start():
    """Initialization on power-up: randomly generate initial brick column"""
    global brick_x
    brick_x = random.randint(0, 4)

def draw_game():
    """Draw game screen: player (bright) + brick (dim)"""
    global game_state, player_col, brick_x, brick_y
    display.clear()
    # Draw player (fixed at bottom row, brightness 9 = brightest)
    display.set_pixel(player_col, player_fixed_row, 9)
    # Draw brick during gameplay (brightness 3 = dim)
    if game_state == 1:
        display.set_pixel(brick_x, brick_y, 7)

def reset_game():
    """Reset all game states"""
    global game_state, player_col, brick_x, brick_y, score
    global a_pressed_flag, b_pressed_flag
    game_state = 1
    player_col = player_init_col
    brick_x = random.randint(0, 4)
    brick_y = 0
    score = 0
    a_pressed_flag = False
    b_pressed_flag = False
    display.clear()

def check_collision():
    """Collision detection: game over if brick is in same column and row as player"""
    global collision_x, collision_y, game_state, flash_count
    collision_x = (brick_x == player_col)
    collision_y = (brick_y == player_fixed_row)
    if collision_x and collision_y:
        game_state = 2
        display.clear()
        flash_count = 0
```

③ Boucle principale : logique de démarrage / réinitialisation.

`on_forever()` vérifie d'abord si les boutons A et B de la carte Micro:bit sont pressés (`button_a.is_pressed() and button_b.is_pressed()`). Le flag `can_start` est vrai lorsque A et B sont pressés simultanément et que le jeu n'est pas en cours.

Si `can_start` est vrai et que `start_flag == 0` (première détection de la pression simultanée A+B), on place `start_flag` à 1 et on effectue un court délai (`utime.sleep_ms(20)`).

On vérifie à nouveau si A+B restent pressés (anti-rebond). Si oui, `reset_game()` redémarre la partie et `last_brick_time` est enregistré. Si A+B ne sont pas pressés simultanément, `start_flag` est remis à 0.

```python
# ===================== Main Loop =====================
def on_forever():
    """Main game logic loop"""
    global ab_pressed, can_start, start_flag, last_brick_time
    global flash_count, player_col, a_pressed_flag, b_pressed_flag
    global current_time, time_passed, brick_x, brick_y, score

    # 1. A+B pressed simultaneously: start/reset game (debounced)
    ab_pressed = button_a.is_pressed() and button_b.is_pressed()
    can_start = ab_pressed and (game_state != 1)
    if can_start:
        if start_flag == 0:
            start_flag = 1
            utime.sleep_ms(20)
            if button_a.is_pressed() and button_b.is_pressed():
                reset_game()
                last_brick_time = running_time()
    else:
        start_flag = 0
```

④ Boucle principale : affichage des états « non démarré » et « fin de jeu ».

*   **Jeu non démarré (`game_state == 0`)** : Dans cet état, la matrice affiche des petits diamants (`Image.DIAMOND_SMALL`) et des diamants pleins (`Image.DIAMOND`) chacun pendant 500 ms, pour inviter le joueur à démarrer.
*   **Fin de jeu (`game_state == 2`)** : Lorsque la partie se termine, le programme entre dans une boucle qui fait clignoter le score. `flash_count` limite le nombre de clignotements (ici 3). À chaque clignotement le score est défilé, l'affichage est effacé avec un court délai. Ensuite, le score final est de nouveau affiché pendant 500 ms.

```python
    # 2. Game not started state
    if game_state == 0:
        display.show(Image.DIAMOND_SMALL)
        utime.sleep_ms(500)
        display.show(Image.DIAMOND)
        utime.sleep_ms(500)

    # 3. Game over state
    if game_state == 2:
        if flash_count < 3:
            display.scroll(score)
            utime.sleep_ms(300)
            display.clear()
            utime.sleep_ms(200)
            flash_count += 1
        else:
            display.scroll(score)
            utime.sleep_ms(500)
```

⑤ Boucle principale : logique pendant la partie.

Lorsque `game_state == 1` (en jeu), exécuter la logique suivante :

*   **Déplacement du joueur à gauche et à droite :**
    *   `pin15` (bouton gauche) : si `pin15` est pressé (lecture 0), que `a_pressed_flag` est `False` (évite les déclenchements consécutifs), et que le joueur n'est pas à l'extrême gauche (`player_col > 0`), le joueur se déplace d'une case à gauche (`player_col -= 1`) et `a_pressed_flag` est mis à `True`, avec un délai de 50 ms. Si `pin15` n'est pas pressé, `a_pressed_flag` est réinitialisé à `False`.
    *   `pin13` (bouton droit) : si `pin13` est pressé (lecture 0), que `b_pressed_flag` est `False` (évite les déclenchements consécutifs), et que le joueur n'est pas à l'extrême droite (`player_col < 4`), le joueur se déplace d'une case à droite (`player_col += 1`) et `b_pressed_flag` devient `True`, avec un délai de 50 ms. Si `pin13` n'est pas pressé, `b_pressed_flag` est réinitialisé à `False`.
*   **Chute des briques :**
    *   `current_time` récupère le temps courant, `time_passed` calcule le temps écoulé depuis la dernière chute de brique.
    *   Si `time_passed > brick_move_speed`, on met à jour `last_brick_time` et la brique descend d'une case (`brick_y += 1`).
    *   Si une brique atteint le bas (`brick_y > 4`), elle est réinitialisée dans une colonne aléatoire en haut (`brick_x = random.randint(0, 4)`), `brick_y` est remis à 0 et `score` est incrémenté de 1.
*   **Détection de collision et rafraîchissement de l'affichage :**
    *   `check_collision()` détecte si le joueur et la brique sont en collision.
    *   `draw_game()` met à jour l'affichage sur la matrice du Micro:bit.

```python
    # 4. Game running logic
    if game_state == 1:
        # Left move button (pin15): fix level detection + set flag only on successful move
        if not pin15.read_digital():  # Pressed = low level 0, trigger left move
            if not a_pressed_flag:
                if player_col > 0:
                    player_col -= 1
                    a_pressed_flag = True  # Only set flag on successful move
                    utime.sleep_ms(50)
        else:
            a_pressed_flag = False  # Reset flag immediately when button is released

        # Right move button (pin13): fix level detection + set flag only on successful move
        if not pin13.read_digital():  # Pressed = low level 0, trigger right move
            if not b_pressed_flag:
                if player_col < 4:
                    player_col += 1
                    b_pressed_flag = True  # Only set flag on successful move
                    utime.sleep_ms(50)
        else:
            b_pressed_flag = False  # Reset flag immediately when button is released

        # Brick falling logic
        current_time = running_time()
        time_passed = current_time - last_brick_time
        if time_passed > brick_move_speed:
            last_brick_time = current_time
            brick_y += 1
            if brick_y > 4:
                brick_x = random.randint(0, 4)
                brick_y = 0
                score += 1

        # Collision detection + screen refresh
        check_collision()
        draw_game()
```

⑥ Point d'entrée du programme.

Ceci est le point de départ réel de l'exécution du programme.

`if __name__ == "__main__":` garantit que ce code n'est exécuté que lorsque le script est lancé comme programme principal.

Dans cette section, `on_start()` effectue une initialisation unique.
Ensuite, une boucle infinie (`while True`) est lancée, où à chaque itération :

*   `on_forever()` exécute toute la logique principale du jeu.
*   Un délai de 10 ms (`utime.sleep_ms(10)`) contrôle la fréquence d'exécution, réduit la charge CPU et assure une vitesse de mise à jour modérée du jeu.

```python
# ===================== Program Entry Point =====================
if __name__ == "__main__":
    on_start()
    while True:
        on_forever()
        utime.sleep_ms(10)
```
#### 5.2.5.5 Résultat du test

![Img](./media/4top.png)

Après avoir téléversé le code, insérez la carte micro:bit dans l'emplacement de la manette (**piles installées**), et mettez l'interrupteur sur “ON”.

Après la mise sous tension, l'état est **0-initial** et la matrice clignote deux icônes en forme de losange.

Appuyez sur A et B (pendant au moins 1 seconde) pour démarrer la partie (état **1-en cours**), et une brique tombera dans une colonne aléatoire. Vous pouvez maintenant vous déplacer à gauche/droite en appuyant sur C/E. À chaque fois que vous évitez une brique, le score augmente de 1.

La partie se termine en cas de collision (**2-fin de partie**), et le score final sera affiché sur la matrice. Si vous voulez rejouer, appuyez de nouveau sur A et B. Pour quitter le jeu, éteignez l'appareil (positionnez l'interrupteur DIP sur “OFF”).

![Img](./media/5000.gif)

<span style="color: rgb(0, 209, 0);">**Conseil :** Si la carte ne répond pas, veuillez appuyer sur le bouton reset à l'arrière de la carte micro:bit.</span>

![Img](./media/4bottom.png)