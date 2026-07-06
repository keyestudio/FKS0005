### 4.2.4 Music Player

#### 4.2.4.1 Overview

![Img](./media/top1.png)

Ici, nous construisons un lecteur de musique qui génère du son via le buzzer intégré sur la micro:bit (ne joue pas de musique vocale). Il dispose d'une bibliothèque de 20 courts morceaux et prend en charge la lecture séquentielle et aléatoire.

En mode séquentiel, appuyer sur C (chanson précédente) ou E (chanson suivante) change de piste selon une séquence prédéfinie jusqu'à atteindre la fin de la liste ; tandis qu'en mode aléatoire, chaque pression sélectionne une piste au hasard parmi les 20 sons avec les voyants colorés qui clignotent, et lorsque la chanson se termine, la lecture s'arrête immédiatement.

Pendant ce temps, la matrice LED de la micro:bit affiche en temps réel le mode de lecture actuel.

![Img](./media/bottom1.png)

#### 4.2.4.2 Required Parts

| ![Img](./media/microbitV2.png)|  ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 board** (self-provided) ×1 | **micro:bit Smart Gamepad** (assembled) ×1 |**pile AAA** (à fournir) ×4 |

#### 4.2.4.3 Code Flow

![Img](./media/4001.png)

#### 4.2.4.4 Test Code

**Complete code:**

![Img](./media/4002.png)

![Img](./media/line1.png)

**Brief explanation:**

① Initialiser la matrice LED et le volume sonore, connecter la broche RGB à P8 et définir le nombre de LED RGB à 4.

![Img](./media/4003.png)

② Initialiser le tableau des mélodies à 20 éléments et ajouter leurs pistes détaillées, et définir son volume initial.

![Img](./media/4004.png)

③ Déterminer si le bouton D ou F est pressé. Appuyer sur D pour '0-lecture séquentielle', sur F pour '1-lecture aléatoire'.

![Img](./media/4005.png)

④ En mode séquentiel, appuyer sur C pour jouer la chanson précédente, E pour passer à la chanson suivante.

![Img](./media/4006.png)

Comme il n'y a que 20 pistes dans le tableau, seules les musiques N.O. 0-19 peuvent être jouées. Nous ajoutons donc une condition if pour éviter les débordements et sous-dépassements du tableau.

![Img](./media/4007.png)

Cependant, en mode aléatoire, appuyer sur C/E pour mélanger ces 20 chansons.

![Img](./media/4008.png)

⑤ Déterminer si la chanson précédente est différente de la chanson actuelle. Si oui, arrêter d'abord la chanson en cours puis jouer la nouvelle.

![Img](./media/4009.png)

⑥ Vérifier si le mode est '0-lecture séquentielle', affichant '![Img](./media/4010.png)', ou '1-lecture aléatoire', affichant '![Img](./media/4011.png)', avec un délai de 100 ms.

![Img](./media/4012.png)

⑦ Faire l'effet de respiration des lumières RGB en arrière-plan.

![Img](./media/4013.png)

⑧ Appuyer sur A pour augmenter le volume (+10) ; appuyer sur B pour le diminuer (-10). Le volume du buzzer de la micro:bit est déterminé par la tension de sortie de la broche interne connectée. Nous pouvons contrôler le volume en convertissant des valeurs numériques 0~255 en valeurs analogiques via le DAC.

![Img](./media/4014.png)

#### 4.2.4.5 Test Result

![Img](./media/4top.png)

Après avoir téléversé le code, insérer la micro:bit dans le logement du gamepad (**piles installées**), et mettre l'interrupteur sur “ON”.

Au démarrage, il est en mode séquentiel par défaut, et jouera la chanson N.O. “0”. À la fin de celle-ci, vous pouvez appuyer sur C pour la chanson précédente ou sur E pour la suivante.

Appuyer sur F pour passer en mode aléatoire. Et vous pouvez appuyer sur D pour revenir au mode séquentiel. En mode F, une piste aléatoire parmi ces 20 sera jouée si vous appuyez sur C/E. Après la fin, la lecture s'arrête.

Les lumières RGB effectuent constamment l'effet de respiration dès la mise sous tension. Parallèlement, la matrice LED de la micro:bit affiche “![Img](./media/4010.png)” en mode séquentiel et “![Img](./media/4011.png)” en mode aléatoire.

Pour le volume, appuyez sur A pour augmenter et sur B pour diminuer.

![Img](./media/4015.gif)

<span style="color: rgb(0, 209, 0);">**Conseil :** Si la carte ne répond pas, veuillez appuyer sur le bouton reset à l'arrière de la micro:bit.</span>

![Img](./media/4bottom.png)