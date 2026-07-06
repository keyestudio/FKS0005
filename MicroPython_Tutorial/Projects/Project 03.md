### 5.2.3 Simple Electronic Piano

#### 5.2.3.1 Overview

![Img](./media/top1.png)

Dans ce projet, nous contrôlons le haut-parleur micro:bit pour jouer différentes tonalités en basculant le joystick et en appuyant sur les boutons. Pendant ce temps, la matrice de LED intégrée affichera les chiffres correspondants.

Tourner le joystick vers la droite produit « Do (Tone Central C) » avec l'affichage montrant « 1 » ; le tourner vers la gauche produit « Re (Tone D) » avec « 2 » ; le pousser vers le haut produit « Mi (Tone E) » avec « 3 » ; le pousser vers le bas produit « Fa (Tone F) » avec « 4 ». Appuyer sur le bouton C produit « Sol (Tone G) » avec « 5 », appuyer sur D produit « La (Tone A) » avec « 6 », E produit « Si (Tone B) » avec « 7 », et appuyer sur F produit un Do aigu tandis que l'affichage revient à « 1 ». Il y a une belle synchronisation entre le joystick, les boutons, les tonalités et l'affichage.

![Img](./media/bottom1.png)

#### 5.2.3.2 Component Knowledge

![Img](./media/2top.png)

**Microbit haut-parleur**

![Img](./media/j901.png)

La carte micro:bit dispose d'un haut-parleur intégré pour produire des sons, comme des rires, des salutations, des bâillements, ou des expressions de tristesse, ou même pour composer une chanson. Par programmation, il peut même générer des notes individuelles, des mélodies et des rythmes, ou même des compositions musicales, telles que la chanson *Ode à la joie*.

![Img](./media/2bottom.png)

#### 5.2.3.3 Required Parts

| ![Img](./media/microbitV2.png)|  ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 board** (self-provided) ×1 | **micro:bit Smart Gamepad** (assembled) ×1 | **AAA battery** (self-provided) ×4 |

#### 5.2.3.4 Code Flow

![Img](./media/3009.png)

#### 5.2.3.5 Test Code

⚠️ **Remarque : la sensibilité du joystick peut être ajustée selon vos besoins.**

**Code complet:**

```python
# import related libraries
from microbit import *
import music

# --- Configuration Constants ---
# Joystick and Button Mapping (Pin, Note, Display Character)
# For Joystick: (Pin, Threshold, Note, Character)
JOY_MAP = [(pin2, 600, 'c4:2', '1'), (pin2, 400, 'd4:2', '2'), 
           (pin1, 600, 'e4:2', '3'), (pin1, 400, 'f4:2', '4')]

# For Buttons: (Pin, Note, Character)
BTN_MAP = [(pin15, 'g4:2', '5'), (pin16, 'a4:2', '6'), 
           (pin13, 'b4:2', '7'), (pin14, 'c5:2', '1')]

# ==================== Initialization ====================
# Enable internal pull-up resistors for all button pins
for p, n, d in BTN_MAP: 
    p.set_pull(p.PULL_UP)

# Visual feedback on startup
display.show(Image.MUSIC_CROTCHET)

# ==================== Main Loop ====================
while True:
    # 1. Joystick Logic: Iterate through map and check analog thresholds
    for pin, thresh, note, disp in JOY_MAP:
        val = pin.read_analog()
        # Trigger if value exceeds high threshold or drops below low threshold
        if (thresh == 600 and val > 600) or (thresh == 400 and val < 400):
            music.play(note, wait=False)
            display.show(disp)

    # 2. Button Logic: Check for digital presses (Active Low)
    for pin, note, disp in BTN_MAP:
        if pin.read_digital() == 0: 
            music.play(note, wait=False)
            display.show(disp)
            # Debounce/Stutter protection: Wait until the button is released
            while pin.read_digital() == 0: 
                sleep(10)

    # Small delay to maintain system stability and reduce CPU load
    sleep(20)

```
![Img](./media/line1.png)

**Brève explication:**

① Importer les bibliothèques, configurer les constantes et initialiser.

Il importe la bibliothèque `microbit` pour accéder aux capacités matérielles de la micro:bit et `music` pour jouer de la musique. Il définit ensuite deux listes essentielles de constantes de configuration :

*   `JOY_MAP` : Sert à configurer le mappage du joystick. Chaque tuple contient les broches connectées au joystick, les seuils (par exemple, au-dessus de 600 ou en dessous de 400), la note musicale à jouer (par exemple, 'c4:2' est le do central durant deux temps), et le caractère affiché sur la matrice LED de la micro:bit.
*   `BTN_MAP` : Le mappage utilisé pour configurer les boutons externes. Chaque tuple contient les broches connectées aux boutons, les notes musicales à jouer, et les caractères affichés sur la matrice LED de la micro:bit.

Lors de l'initialisation, le programme parcourt toutes les broches de bouton dans `BTN_MAP` et active leurs résistances pull-up internes (`p.PULL_UP`). Cela garantit que les broches restent à un niveau haut lorsque le bouton n'est pas pressé et passent à un niveau bas lorsqu'il est pressé.

Enfin, une icône de note musicale (`Image.MUSIC_CROTCHET`) apparaît sur la matrice LED.

```python
# import related libraries
from microbit import *
import music

# --- Configuration Constants ---
# Joystick and Button Mapping (Pin, Note, Display Character)
# For Joystick: (Pin, Threshold, Note, Character)
JOY_MAP = [(pin2, 600, 'c4:2', '1'), (pin2, 400, 'd4:2', '2'), 
           (pin1, 600, 'e4:2', '3'), (pin1, 400, 'f4:2', '4')]

# For Buttons: (Pin, Note, Character)
BTN_MAP = [(pin15, 'g4:2', '5'), (pin16, 'a4:2', '6'), 
           (pin13, 'b4:2', '7'), (pin14, 'c5:2', '1')]

# ==================== Initialization ====================
# Enable internal pull-up resistors for all button pins
for p, n, d in BTN_MAP: 
    p.set_pull(p.PULL_UP)

# Visual feedback on startup
display.show(Image.MUSIC_CROTCHET)
```

② Boucle principale : Gérer les entrées du joystick.

Il s'agit d'une boucle infinie (`while True`). Il traite d'abord l'entrée du joystick en itérant sur la liste `JOY_MAP` et en vérifiant chaque direction du joystick. Pour chaque broche du joystick, il lit sa valeur analogique (`pin.read_analog()`).

Le joystick est ensuite considéré comme activé en fonction d'un seuil prédéfini (`thresh`) : si le seuil est 600 et que la valeur analogique actuelle dépasse 600 (joystick poussé), ou si le seuil est 400 et que la valeur analogique actuelle est inférieure à 400 (poussée dans la direction opposée), il joue la note musicale correspondante (`music.play(note, wait=False)`), où `wait=False` garantit que la lecture musicale ne bloque pas la boucle principale, permettant la détection simultanée d'autres entrées.

Et l'affichage LED de la micro:bit affiche le caractère correspondant à la direction du joystick.

```python
# ==================== Main Loop ====================
while True:
    # 1. Joystick Logic: Iterate through map and check analog thresholds
    for pin, thresh, note, disp in JOY_MAP:
        val = pin.read_analog()
        # Trigger if value exceeds high threshold or drops below low threshold
        if (thresh == 600 and val > 600) or (thresh == 400 and val < 400):
            music.play(note, wait=False)
            display.show(disp)
```

③ Boucle principale : Traiter les entrées des boutons.

Après l'entrée du joystick, c'est au tour des boutons externes. Il parcourt chaque bouton dans la liste `BTN_MAP`. Pour chaque broche de bouton, il vérifie si la lecture numérique est `0` (`pin.read_digital() == 0`, ce qui signifie bouton pressé). Lorsque le bouton est pressé, la broche est à l'état bas en raison de sa résistance pull-up, le programme joue la note musicale correspondante (`music.play(note, wait=False)`) et affiche le caractère sur la matrice LED de la micro:bit.

Pour éviter les rebonds ou les détections multiples d'une seule pression, il y a une boucle `while` qui attend la libération du bouton courant (`while pin.read_digital() == 0: sleep(10)`). Cette période d'attente bloque temporairement le programme jusqu'à ce que le bouton soit relâché.

```python
    # 2. Button Logic: Check for digital presses (Active Low)
    for pin, note, disp in BTN_MAP:
        if pin.read_digital() == 0: 
            music.play(note, wait=False)
            display.show(disp)
            # Debounce/Stutter protection: Wait until the button is released
            while pin.read_digital() == 0: 
                sleep(10)
```

④ Boucle principale : Délai de boucle.

Après toutes les détections d'entrée, le programme fait une pause de 20 millisecondes (`sleep(20)`) pour stabiliser le système, réduire la charge CPU et fournir un intervalle pour la prochaine détection d'entrée de la boucle.

```python
    # Small delay to maintain system stability and reduce CPU load
    sleep(20)
```

#### 5.2.3.6 Test Result

![Img](./media/4top.png)

Après avoir transféré le code, insérez la carte micro:bit dans la fente du gamepad (**batteries installées**), et mettez l'interrupteur sur « ON ». La matrice LED affiche d'abord « ![Img](./media/3004.png) ».

Tourner le joystick vers la droite produit « Do (Tone Central C) » avec l'affichage montrant « 1 » ; le tourner vers la gauche produit « Re (Tone D) » avec « 2 » ; le pousser vers le haut produit « Mi (Tone E) » avec « 3 » ; le pousser vers le bas produit « Fa (Tone F) » avec « 4 ». Appuyer sur le bouton C produit « Sol (Tone G) » avec « 5 », appuyer sur D produit « La (Tone A) » avec « 6 », E produit « Si (Tone B) » avec « 7 », et appuyer sur F produit un Do aigu tandis que l'affichage revient à « 1 ».

Vous avez construit le simple piano électronique !

![Img](./media/3010.gif)

<span style="color: rgb(0, 209, 0);">**Conseil :** Si la carte ne répond pas, veuillez appuyer sur le bouton de réinitialisation au dos de la carte micro:bit.</span>

![Img](./media/4bottom.png)