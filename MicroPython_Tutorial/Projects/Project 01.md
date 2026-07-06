### 5.2.1 Indicateur de direction

#### 5.2.1.1 Aperçu

![Img](./media/top1.png)

Lorsque vous déplacez le joystick, la matrice de points affiche en temps réel des flèches dans la direction correspondante : gauche, droite, haut, bas, vous fournissant une référence de direction claire.

![Img](./media/bottom1.png)

#### 5.2.1.2 Connaissance des composants

![Img](./media/2top.png)

**Matrice LED de Micro:bit :**

![Img](./media//1001.png)

La matrice de diodes électroluminescentes (LED) de la carte micro:bit se compose d'un total de 25 diodes, groupées par 5, correspondant aux axes X et Y, formant une matrice 5×5. Chacune est placée à l'intersection de la ligne (X) et de la colonne (Y). Nous pouvons contrôler une ou plusieurs LED en définissant les points de coordonnées.

**Joystick :**

| ![Img](./media/1002.png)| ![Img](./media//1003.png)  |
| :--: | :--: |
|       Produit réel       |     Schéma     |

La structure interne de ce joystick est composée de deux résistances ajustables (potentiomètres) d'une valeur de 10KΩ chacune.

Il détecte les directions (et l'amplitude) de la poussée via la broche analogique ADC du microcontrôleur pour délivrer des signaux électriques analogiques correspondant à chaque dimension. Lors de la lecture réelle du signal, lorsque les valeurs analogiques des axes X et Y du joystick se situent dans la plage 450~600, on peut déterminer que le joystick est en position neutre (stationnaire) sans basculement actif.

![Img](./media/2bottom.png)

#### 5.2.1.3 Pièces requises

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png)  |![Img](./media/dianchi.png)|
| :--: | :--: | :--: |
| **micro:bit V2 board** (fourni par l'utilisateur) ×1 | **micro:bit Smart Gamepad** (assemblé) ×1 | **Pile AAA** (fourni par l'utilisateur) ×4 |

#### 5.2.1.4 Flux du code

![Img](./media/1004.png)


#### 5.2.1.5 Code de test

**Code complet:**

```Python
# import related libraries
from microbit import *

display.show(Image.HOUSE)

while True:
    #Read the toggle state of the joystick
    x = pin2.read_analog()
    y = pin1.read_analog()
    #Determine the direction in which the joystick is toggled
    if x > 600 and (400 < y < 600):
        display.show(Image.ARROW_E)
    elif x < 400 and (400 < y < 600):
        display.show(Image.ARROW_W)
    elif y > 600 and (400 < x < 600):
        display.show(Image.ARROW_S)
    elif y < 400 and (400 < x < 600):
        display.show(Image.ARROW_N)
    else:
        display.show(Image.HOUSE)
```

![Img](./media/line1.png)

**Explication brève :**

① Importer la bibliothèque et afficher l'image initiale.

Commencez par importer la bibliothèque `microbit`, qui est la bibliothèque de base nécessaire pour Micro:bit sous MicroPython. Elle donne un accès complet au matériel de Micro:bit (y compris l'affichage LED et les broches). Après l'importation, une icône maison(`Image.HOUSE`) s'affiche sur la matrice comme état initial / écran de veille.

```python
# import related libraries
from microbit import *

display.show(Image.HOUSE)
```
② Boucle : lire la valeur analogique du joystick.

Le programme entre dans une boucle infinie (`while True`). Au début de la boucle, il lit les valeurs d'entrée analogiques de `pin2` et `pin1`, correspondant typiquement à l'axe X (gauche-droite) et à l'axe Y (haut-bas) du joystick.

`read_analog()` renvoie un entier entre 0 et 1023, représentant la position du joystick le long de cet axe. Il est généralement proche de 511–512 lorsque le joystick est centré.

```python
while True:
    #Read the toggle state of the joystick
    x = pin2.read_analog()
    y = pin1.read_analog()
```
③ Déterminer la direction du joystick et afficher la flèche correspondante.

Ici, on détermine la direction du mouvement du joystick en se basant sur les valeurs analogiques `x` et `y`. Nous fixons des seuils (400 et 600) pour déterminer si le joystick est incliné.

*   [ `x` > 600 , 400 <  `y` < 600 ] : (sur l'axe Y central) le joystick est à droite et affiche la flèche orientée vers l'est (`Image.ARROW_E`).
*   [ `x` < 400 , 400 <  `y` < 600 ] : le joystick est à gauche et affiche la flèche orientée vers l'ouest (`Image.ARROW_W`).
*   [ `y` >  600 , 400 < `x` < 600 ] : le joystick est poussé vers le bas et affiche la flèche orientée vers le sud (`Image.ARROW_S`).
*   [ `y` < 400 ,400 < `x` < 600 ] : le joystick est poussé vers le haut et affiche la flèche orientée vers le nord (`Image.ARROW_N`).

```python
    #Determine the direction in which the joystick is toggled
    if x > 600 and (400 < y < 600):
        display.show(Image.ARROW_E)
    elif x < 400 and (400 < y < 600):
        display.show(Image.ARROW_W)
    elif y > 600 and (400 < x < 600):
        display.show(Image.ARROW_S)
    elif y < 400 and (400 < x < 600):
        display.show(Image.ARROW_N)
```
④ Le motif "maison" est affiché lorsque le joystick est centré.

Si aucune des conditions ci‑dessus n'est remplie — c'est‑à‑dire que le joystick ne se déplace pas de façon significative dans une quelconque direction (ce qui indique généralement qu'il est en position centrale) — la Micro:bit affichera à nouveau la "maison" (`Image.HOUSE`), ce qui signifie que le joystick est immobile.

```python
    else:
        display.show(Image.HOUSE)
```

#### 5.2.1.6 Résultat du test

![Img](./media/4top.png)

Après avoir transféré le code, insérez la carte micro:bit dans la fente du gamepad (**piles installées**), et basculez l'interrupteur dessus sur « ON ».

Lorsque vous poussez le joystick du gamepad, vous verrez les flèches correspondantes sur la matrice. Si vous le ramenez au centre, une icône maison apparaîtra sur la matrice.

![Img](./media/1009.gif)

<span style="color: rgb(0, 209, 0);">**Astuce :** Si aucune réponse n'apparaît sur la carte, veuillez appuyer sur le bouton de réinitialisation à l'arrière de la carte micro:bit.</span>

![Img](./media/4bottom.png)