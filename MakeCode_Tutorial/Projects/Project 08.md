### 4.2.8 Deviner le nombre

#### 4.2.8.1 Vue d'ensemble

![Img](./media/top1.png)

Dans ce projet, nous jouons à un jeu de devinette de nombre avec une carte micro:bit, une carte de contrôle gamepad et un écran OLED. Lorsqu'on devine le bon nombre, l'OLED affiche "Génial !!!" ; si la supposition est trop haute ou trop basse, il affiche respectivement "Trop haut !" / "Trop bas !", ainsi que la plage correspondante des nombres possibles.

![Img](./media/bottom1.png)

#### 4.2.8.2 Connaissances des composants

Ce projet utilise le même écran OLED que le Projet 07. Veuillez vous référer à la section 4.2.7.2 pour ses connaissances sur les composants.

#### 4.2.8.3 Pièces requises

| ![Img](./media/microbitV2.png)|  ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 board** (fourni par l'utilisateur) ×1 | **micro:bit Smart Gamepad** (assemblé) ×1 |**AAA battery** (fourni par l'utilisateur) ×4 |
|![Img](./media/OLED.png)|![Img](./media/7008.png)||
|**OLED display** (fourni par l'utilisateur)×1 |**F-F DuPont wire**(fourni par l'utilisateur) x4||

#### 4.2.8.4 Schéma de câblage

![Img](./media/jiexian8.png)

**Après avoir câblé comme montré ci-dessus, insérez la micro:bit dans la fente de la carte de contrôle gamepad.**

| OLED display | micro:bit gamepad control board | micro:bit board pin |
| :--: | :--: | :--: |
| GND |  GND | GND |
| VCC |  3V | 3V |
| SDA |  SDA | P20 |
| SCL |  SCL | P19 |

#### 4.2.8.5 Flux du code

![Img](./media/8001.png)

#### 4.2.8.6 Code de test

⚠️ **Remarque : la bibliothèque OLED est incluse ici, nous devons donc importer : https://github.com/keyestudio/pxt-environment-kit-master**.

**Code complet :**

![Img](./media/8002.png)

![Img](./media/line1.png)

**Brève explication :**

① Initialiser le bit du drapeau de mise à jour de l'écran, définir la variable mode à 0 (0 - prêt du jeu, 1 - jeu en cours), et initialiser l'écran OLED.

![Img](./media/8003.png)

② Pendant la préparation du jeu, définir la plage de devinettes, la valeur initiale de l'estimation, la valeur cible et l'estimation.

![Img](./media/8004.png)

③ Mettre à jour la plage de valeurs et la valeur d'estimation sur l'OLED. Afficher les invites correspondantes lorsque le bit de drapeau d'état du résultat change : "Trop haut !" lorsque state=1 ; "Trop bas !" lorsque state=2 ; et "Génial !!!" lorsque state=3.

Et définir le mode sur prêt du jeu et attendre 1000 millisecondes (1 s).

![Img](./media/8005.png)

④ Appuyer sur C pour temp+1 ; si la valeur d'estimation dépasse le maximum, la définir comme nouveau maximum.

Appuyer sur E pour temp-1 ; si la valeur d'estimation est inférieure au minimum, la définir comme nouveau minimum.

![Img](./media/8006.png)

⑤ Appuyer sur D pour comparer la valeur d'estimation avec la valeur cible. Si temp est plus grand, enregistrer le nouveau maximum max2 et entrer en State 1 ; si temp est plus petit, enregistrer le nouveau minimum min2 et entrer en State 2 ; si les deux valeurs sont égales, aller en State 3.

Enfin, mettre à jour l'affichage avec un délai de 1000 millisecondes.

![Img](./media/8007.png)

#### 4.2.8.7 Résultat du test

![Img](./media/4top.png)

Après avoir transféré le code, insérez la carte micro:bit dans la fente du gamepad (**piles installées**), et mettez l'interrupteur sur "ON".

Après le téléchargement du code, l'OLED s'initialise et affiche la plage de valeurs “num : 1 ~ 100” et une estimation initiale de 50. Vous pouvez appuyer sur C pour temp+1 (maximum 100) ou sur E pour temp-1 (minimum 1) afin de changer votre valeur d'estimation sur l'OLED.

Appuyez sur D pour soumettre votre valeur, et temp sera comparé à la valeur cible aléatoire. Si temp>value, afficher « Trop haut ! » et assigner temp à max2 ; si temp<value, afficher « Trop bas ! » et l'assigner à min2. Si vous avez la chance que temp=value, vous verrez « Génial !!! » pendant 1 s.

Après cela, le jeu sera réinitialisé et une nouvelle valeur cible sera définie. Jouons une autre partie !

![Img](./media/8000.gif)

⚠️ **Les blocs de construction montrés dans le Résultat du test ne sont pas inclus dans ce kit produit.**

<span style="color: rgb(0, 209, 0);">**Astuce :** Si la carte ne répond pas, veuillez appuyer sur le bouton de réinitialisation à l'arrière de la carte micro:bit.</span>

![Img](./media/4bottom.png)