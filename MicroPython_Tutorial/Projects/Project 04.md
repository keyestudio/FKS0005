### 5.2.4 Lecteur de musique

#### 5.2.4.1 Aperçu

![Img](./media/top1.png)

Ici, nous construisons un lecteur de musique qui génère du son via le buzzer intégré sur la carte micro:bit (ne joue pas de musique vocale). Il dispose d’une bibliothèque de 20 pistes courtes et prend en charge la lecture séquentielle et aléatoire.

En mode séquentiel, l’appui sur C (chanson précédente) ou E (chanson suivante) change les pistes selon une séquence prédéfinie jusqu’à la fin de la liste ; tandis qu’en mode aléatoire, chaque pression sélectionne une piste au hasard parmi les 20 sons avec les voyants colorés qui clignotent, et lorsqu’une chanson se termine elle s’arrête immédiatement.

Pendant ce temps, la matrice LED du micro:bit affiche en temps réel le mode de lecture en cours.

![Img](./media/bottom1.png)

#### 5.2.4.2 Pièces requises

| ![Img](./media/microbitV2.png)|  ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 board** (fourni par l'utilisateur) ×1 | **micro:bit Smart Gamepad** (assemblé) ×1 | **AAA battery** (fourni par l'utilisateur) ×4 |

#### 5.2.4.3 Flux du code

![Img](./media/4001.png)

#### 5.2.4.4 Code de test

**Code complet:**

```python
# import related libraries
from microbit import *
import music, neopixel, random

# --- Configuration & Data ---
vol = 50
mode = 0  # 0: Manual, 1: Random
idx = 0
last_idx = -1
hue = 0
strip = neopixel.NeoPixel(pin8, 4)
melodies = ["DADADADUM", "ENTERTAINER", "PRELUDE", "ODE", "NYAN", "RINGTONE", "FUNK", "BLUES", 
            "BIRTHDAY", "WEDDING", "FUNERAL", "PUNCHLINE", "BADDY", "CHASE", "BA_DING", 
            "WAWAWAWAA", "JUMP_UP", "JUMP_DOWN", "POWER_UP", "POWER_DOWN"]

# Pin Initialization (P13-P16)
btns = [pin13, pin14, pin15, pin16]
for p in btns: p.set_pull(p.PULL_UP)
set_volume(vol)

def get_rgb(h):
    """ Simplified HSL to RGB logic """
    h %= 360
    pos = h // 60
    f = (h % 60) / 60.0
    v = 76 # 255 * 0.3 (Brightness coefficient)
    up, down = int(v * f), int(v * (1 - f))
    res = [(v, up, 0), (down, v, 0), (0, v, up), (0, down, v), (up, 0, v), (v, 0, down)]
    return res[pos]

# State tracking (for debouncing)
last_states = [1] * 4
last_press_t = 0

while True:
    curr_t = running_time()
    
    # 1. Volume Control (Buttons A/B)
    if button_a.was_pressed(): vol = min(250, vol + 10); set_volume(vol)
    if button_b.was_pressed(): vol = max(20, vol - 10); set_volume(vol)

    # 2. Joystick/Button Input Detection (with debouncing)
    for i, p in enumerate(btns):
        v = p.read_digital()
        if v == 0 and last_states[i] == 1 and (curr_t - last_press_t > 50):
            last_press_t = curr_t
            if i == 3: mode = 0; sleep(500)     # P16: Manual Mode
            elif i == 1: mode = 1; sleep(500)   # P14: Random Mode
            elif i == 2: # P15: Next track / Random track
                idx = random.randint(0, 19) if mode else (idx + 1) % 20
            elif i == 0: # P13: Previous track / Random track
                idx = random.randint(0, 19) if mode else (idx - 1) % 20
        last_states[i] = v

    # 3. Music Playback Logic
    if idx != last_idx:
        music.stop()
        try:
            music.play(getattr(music, melodies[idx]), wait=False)
            last_idx = idx
        except: pass

    # 4. Lighting & Display Updates
    hue = (hue + 1) % 360
    strip.fill(get_rgb(hue))
    strip.show()
    
    # Show Mode Icon: "X" for Random, Arrow for Manual
    display.show(Image("00000:99099:00900:99099:00000") if mode else Image.ARROW_E)
    
    sleep(10)

```
![Img](./media/line1.png)

**Brève explication :**

① Importer les bibliothèques, configurer les constantes et l'initialisation.

Il importe d’abord la bibliothèque `microbit` pour accéder aux fonctions de base du Micro:bit, `music` pour jouer la musique intégrée, `neopixel` pour contrôler la bande LED NeoPixel, et `random` pour générer des nombres aléatoires.

Il définit ensuite une série de variables et constantes globales : `vol` fixe le volume initial à 50 ; `mode` contrôle le mode de lecture (0 pour sélection manuelle, 1 pour lecture aléatoire) ; `idx` stocke l’indice musical courant ; une variable suit l’indice de lecture précédent pour éviter les lectures en double ; `hue` contrôle la couleur de la bande NeoPixel ; `strip` initialise une bande NeoPixel connectée à `pin8` de quatre LEDs ; et `melodies` énumère tous les titres `music` de MicroPython.

Ensuite, la liste `btns` définit les quatre broches de boutons externes de `pin13` à `pin16`, en leur assignant des résistances pull-up internes (`p.PULL_UP`) dans une boucle — ce qui donne des broches à niveau haut lorsque les boutons sont relâchés et à niveau bas lorsqu’ils sont enfoncés.

`set_volume (vol)` règle le volume à sa valeur par défaut.

```python
# import related libraries
from microbit import *
import music, neopixel, random

# --- Configuration & Data ---
vol = 50
mode = 0  # 0: Manual, 1: Random
idx = 0
last_idx = -1
hue = 0
strip = neopixel.NeoPixel(pin8, 4)
melodies = ["DADADADUM", "ENTERTAINER", "PRELUDE", "ODE", "NYAN", "RINGTONE", "FUNK", "BLUES", 
            "BIRTHDAY", "WEDDING", "FUNERAL", "PUNCHLINE", "BADDY", "CHASE", "BA_DING", 
            "WAWAWAWAA", "JUMP_UP", "JUMP_DOWN", "POWER_UP", "POWER_DOWN"]

# Pin Initialization (P13-P16)
btns = [pin13, pin14, pin15, pin16]
for p in btns: p.set_pull(p.PULL_UP)
set_volume(vol)
```

② Fonction de conversion de couleur et variable de stabilisation.

`get_rgb(h)` est une fonction simplifiée de conversion HSL (Hue, Saturation, Lightness) vers RGB. Elle prend une valeur de teinte `h` (0–359) et la convertit en triplet RGB. La luminosité `v` est fixée à 76 (environ 255 × 0,3, correspondant au coefficient `BRIGHTNESS`). Cette fonction facilite la génération de couleurs arc-en-ciel en fonction de la teinte.

La liste `last_states` stocke les états précédents des quatre boutons, initialement tous à 1 (niveau haut pour non appuyé). `last_press_t` enregistre le temps de la dernière pression de bouton. Ces variables implémentent ensemble un anti-rebond logiciel pour éviter plusieurs détections lors d’une seule pression.

```python
def get_rgb(h):
    """ Simplified HSL to RGB logic """
    h %= 360
    pos = h // 60
    f = (h % 60) / 60.0
    v = 76 # 255 * 0.3 (Brightness coefficient)
    up, down = int(v * f), int(v * (1 - f))
    res = [(v, up, 0), (down, v, 0), (0, v, up), (0, down, v), (up, 0, v), (v, 0, down)]
    return res[pos]

# State tracking (for debouncing)
last_states = [1] * 4
last_press_t = 0
```

③ Boucle principale : Contrôle du volume.

La boucle infinie (`while True`) récupère le temps d’exécution courant `curr_t`. Ensuite, elle gère les boutons A et B de la carte Micro:bit :

- Si `button_a` est pressé (`button_a.was_pressed()`), le volume `vol` augmente de 10, sans dépasser 250. `set_volume(vol)` met à jour le volume système.
- Si `button_b` est pressé (`button_b.was_pressed()`), `vol` diminue de 10, sans descendre en dessous de 20. `set_volume(vol)` met à jour le volume système.

`was_pressed()` renvoie `True` une seule fois lors de la transition de non-appuyé à appuyé, fournissant un anti-rebond intrinsèque.

```python
while True:
    curr_t = running_time()
    
    # 1. Volume Control (Buttons A/B)
    if button_a.was_pressed(): vol = min(250, vol + 10); set_volume(vol)
    if button_b.was_pressed(): vol = max(20, vol - 10); set_volume(vol)
```

④ Boucle principale : détection d'entrée des boutons et changement de mode.

Elle itère sur les quatre boutons externes (`pin13` à `pin16`) dans la liste `btns`, détectant leurs états. Le bouton n’est pris en compte que lorsqu’il passe de haut (non appuyé) à bas (appuyé) et qu’il s’est écoulé plus de 50 millisecondes depuis la dernière pression valide.

- Si `pin16` est pressé (`i == 3`), `mode = 0` (mode manuel) et pause de 500 ms.
- Si `pin14` est pressé (`i == 1`), `mode = 1` (mode aléatoire) et pause de 500 ms.
- Si `pin15` est pressé (`i == 2`), mettre à jour l’indice musical `idx` selon le mode en cours : sélection aléatoire en mode aléatoire ; morceau suivant en mode manuel.
- Si `pin13` est pressé (`i == 0`), mettre à jour l’indice musical `idx` selon le mode en cours : sélection aléatoire en mode aléatoire ; morceau précédent en mode manuel.

À la fin de chaque boucle, `last_states[i] = v` met à jour l’état courant du bouton en préparation du prochain contrôle de stabilisation.

```python
    # 2. Joystick/Button Input Detection (with debouncing)
    for i, p in enumerate(btns):
        v = p.read_digital()
        if v == 0 and last_states[i] == 1 and (curr_t - last_press_t > 50):
            last_press_t = curr_t
            if i == 3: mode = 0; sleep(500)     # P16: Manual Mode
            elif i == 1: mode = 1; sleep(500)   # P14: Random Mode
            elif i == 2: # P15: Next track / Random track
                idx = random.randint(0, 19) if mode else (idx + 1) % 20
            elif i == 0: # P13: Previous track / Random track
                idx = random.randint(0, 19) if mode else (idx - 1) % 20
        last_states[i] = v
```

⑤ Boucle principale : logique de lecture musicale.

Elle contrôle la lecture en vérifiant si l’indice musical courant `idx` est différent du précédent `last_idx`. Si oui, il faut changer la musique :

1. `music.stop()` arrête la musique en cours.
2. `music.play(getattr(music, melodies[idx]), wait=False)` tente de lancer une nouvelle musique. `getattr(music, melodies[idx])` obtient dynamiquement les données musicales du nom correspondant dans `music`, et `wait=False` empêche la lecture de bloquer la boucle principale.
3. Si la lecture est lancée avec succès, mettre à jour `last_idx = idx`.
4. Le bloc `try...except` capture d’éventuelles erreurs ; par exemple, il pourrait y avoir des titres invalides dans la liste `melodies`.

```python
    # 3. Music Playback Logic
    if idx != last_idx:
        music.stop()
        try:
            music.play(getattr(music, melodies[idx]), wait=False)
            last_idx = idx
        except: pass
```

⑥ Boucle principale : mises à jour des lumières et de l'affichage.

Mise à jour de la couleur de la bande NeoPixel et de l’affichage de la matrice LED Micro:bit :

1. `hue = (hue + 1) % 360` incrémente continuellement `hue` pour lui faire parcourir 0 à 359 et obtenir un dégradé arc-en-ciel.
2. `strip.fill(get_rgb(hue))` utilise `get_rgb` pour générer une couleur basée sur la `hue` courante et remplit toute la bande NeoPixel avec cette couleur.
3. `strip.show()` envoie la couleur mise à jour à la bande NeoPixel pour affichage.
4. `display.show(...)` affiche une image selon le `mode` courant. `mode = 1` (aléatoire) : affiche un “X” personnalisé ; `mode = 0` (manuel) : affiche une flèche pointant à droite (`Image.ARROW_E`).

Ensuite, `sleep(10)` introduit un court délai pour une vitesse d’exécution adaptée, une charge CPU réduite et un effet plus fluide.

```python
    # 4. Lighting & Display Updates
    hue = (hue + 1) % 360
    strip.fill(get_rgb(hue))
    strip.show()
    
    # Show Mode Icon: "X" for Random, Arrow for Manual
    display.show(Image("00000:99099:00900:99099:00000") if mode else Image.ARROW_E)
    
    sleep(10)
```
#### 5.2.4.5 Résultat du test

![Img](./media/4top.png)

Après avoir gravé le code, insérez la carte micro:bit dans la fente du gamepad (**piles installées**), et positionnez l’interrupteur sur « ON ».

Au démarrage, il est en mode séquentiel par défaut et jouera le morceau numéro 0. Lorsqu’il se termine, vous pouvez appuyer sur C pour le morceau précédent ou sur E pour le suivant.

Appuyez sur F pour passer en mode aléatoire. Et vous pouvez appuyer sur D pour revenir au mode séquentiel. En mode F, une piste aléatoire parmi ces 20 sera jouée si vous appuyez sur C/E. Après la fin, la lecture s’arrête.

Les lumières RGB font toujours un effet "respiration" dès la mise sous tension. Pendant ce temps, la matrice LED du micro:bit affiche “![Img](./media/4010.png)” en mode séquentiel et “![Img](./media/4011.png)” en mode aléatoire.

Pour le volume, appuyez sur A pour augmenter et B pour diminuer.

![Img](./media/4015.gif)

<span style="color: rgb(0, 209, 0);">**Astuce :** Si la carte ne répond pas, appuyez sur le bouton reset à l’arrière de la carte micro:bit.</span>

![Img](./media/4bottom.png)