### 4.2.3 Simple Electronic Piano

#### 4.2.3.1 Overview

![Img](./media/top1.png)

Dans ce projet, nous contrôlons le micro:bit speaker pour jouer différentes tonalités en basculant le joystick et en appuyant sur les boutons. Pendant ce temps, la matrice LED embarquée affichera les numéros correspondants.

Tourner le joystick vers la droite produit « Do (note Do centrale) » avec l'affichage montrant « 1 » ; le tourner vers la gauche produit « Ré (note Ré) » avec « 2 » ; le tourner vers le haut produit « Mi (note Mi) » avec « 3 » ; le tourner vers le bas produit « Fa (note Fa) » avec « 4 ». Appuyer sur le bouton C produit « Sol (note Sol) » avec « 5 », C D produit « La (note La) » avec « 6 », E produit « Si (note Si) » avec « 7 », et appuyer sur F produit un « Do » plus aigu tandis que l'affichage revient à « 1 ». Il y a une belle synchronisation entre le joystick, les boutons, les tonalités et l'affichage.

![Img](./media/bottom1.png)

#### 4.2.3.2 Component Knowledge

![Img](./media/2top.png)

**Microbit speaker**

![Img](./media/j901.png)

La carte micro:bit board dispose d'un haut-parleur intégré pour produire des sons, comme des rires, des salutations, des bâillements, ou des expressions de tristesse, ou même pour composer une chanson. Par programmation, il peut même générer des notes individuelles, des mélodies et des rythmes, ou même des compositions musicales, comme la chanson *Brille, brille, petite étoile*.

![Img](./media/2bottom.png)

#### 4.2.3.3 Required Parts

| **micro:bit V2 board** (à fournir) ×1 | **micro:bit Smart Gamepad** (pré-assemblé) ×1 |**AAA battery** (à fournir) ×4 |
| :--: | :--: | :--: |
| ![Img](./media/microbitV2.png)|  ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |

#### 4.2.3.4 Code Flow

![Img](./media/3009.png)

#### 4.2.3.5 Test Code

⚠️ **Remarque : la sensibilité du joystick peut être ajustée selon vos besoins.**

**Complete code:**

![Img](./media/3008.png)

![Img](./media/line1.png)

**Brève explication :**

① Initialiser la matrice LED du micro:bit pour afficher ![Img](./media/3004.png).

![Img](./media/3005.png)

② Déterminer la direction du mouvement du joystick ; jouer en arrière-plan les tons correspondants pendant un demi-temps, et la matrice LED affiche le numéro correspondant.

![Img](./media/3006.png)

③ Vérifier si un bouton est pressé, jouer en arrière-plan le ton correspondant pendant un demi-temps, et la matrice LED affiche le numéro correspondant.

![Img](./media/3007.png)


#### 4.2.3.6 Test Result

![Img](./media/4top.png)

Après avoir téléversé le code, insérez le micro:bit board dans la fente du gamepad (**batteries installées**), et basculez l'interrupteur sur “ON”. La matrice LED affiche d'abord « ![Img](./media/3004.png) ».

Tourner le joystick vers la droite produit « Do (note Do centrale) » avec l'affichage montrant « 1 » ; le tourner vers la gauche produit « Ré (note Ré) » avec « 2 » ; le tourner vers le haut produit « Mi (note Mi) » avec « 3 » ; le tourner vers le bas produit « Fa (note Fa) » avec « 4 ». Appuyer sur le bouton C produit « Sol (note Sol) » avec « 5 », appuyer sur D produit « La (note La) » avec « 6 », E produit « Si (note Si) » avec « 7 », et appuyer sur F produit un « Do » plus aigu tandis que l'affichage revient à « 1 ».

Vous avez construit le simple piano électronique !

![Img](./media/3010.gif)

<span style="color: rgb(0, 209, 0);">**Astuce :** Si la carte ne répond pas, veuillez appuyer sur le bouton de réinitialisation à l'arrière du micro:bit board.</span>

![Img](./media/4bottom.png)