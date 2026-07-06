### 4.2.2 Lumières colorées

#### 4.2.2.1 Aperçu

![Img](./media/top1.png)

Les LED RGB sont un type de source lumineuse qui crée des images en mélangeant la lumière des trois couleurs primaires : rouge, vert et bleu, dont l'intersection produit diverses teintes. Les méthodes courantes incluent le mélange direct des couleurs primaires, l'utilisation d'une LED bleue combinée à un phosphore jaune, ou l'emploi d'une LED ultraviolet avec un phosphore RGB. Comparées aux LED qui émettent une lumière blanche directement, les LED RGB offrent une gamme plus large de possibilités de mélange de couleurs car les trois couleurs primaires peuvent être contrôlées indépendamment.

Dans ce projet, chaque bouton correspond à un mode différent des LED RGB. Lorsque le bouton C est pressé, les lumières clignotent alternativement dans l'ordre « rouge, vert, bleu, jaune et violet » ; Appuyez sur D pour passer aux lumières en respiration ; Appuyez sur E pour les lumières à effet d'eau courante ; Appuyez sur F pour les lumières en défilement.

Guirlandes lumineuses colorées pour décorations de fête, éclairages de sapin de Noël, bandes RGB pour l'ambiance quotidienne, éclairages décoratifs LED dans les parcs d'attraction et les centres commerciaux... Ce sont tous des exemples courants de lumières multi-modes dans notre vie quotidienne.

![Img](./media/bottom1.png)

#### 4.2.2.2 Connaissances sur les composants

![Img](./media/2top.png)

**SK6812 RGB LED**

| ![Img](./media//2001.png)| ![Img](./media//2002.png)|
| :--: | :--: |
| Produit réel | Schéma |

Le SK6812 est une source lumineuse LED à contrôle externe qui intègre les circuits de commande et d'éclairage. Sa partie principale est constituée de perles LED à surface 5x5mm, chacune fonctionnant comme un pixel indépendant qui intègre plusieurs circuits centraux : un circuit de verrouillage de données à interface numérique intelligente, un circuit de mise en forme et d'amplification du signal, un circuit de régulation d'alimentation, un circuit à courant constant intégré et un oscillateur RC à haute précision.

Sa communication utilise un protocole de code monopolaire à retour à zéro. Au rétablissement sous tension, chaque pixel reçoit les données du contrôleur via le port DIN. Les 24 premiers bits de données sont extraits par le pixel initial et stockés dans le verrou de données interne, tandis que les bits restants sont mis en forme et amplifiés en interne avant d'être transmis via le port DOUT aux pixels suivants. À mesure que chaque pixel est traité, la taille du signal transmis diminue de 24 bits.

Sur le gamepad, il y a quatre SK6812 RGB. Ceux-ci prennent tous en charge un réglage de luminosité sur 256 niveaux pour leurs canaux rouge, vert et bleu, permettant des combinaisons de couleurs 256×256×256. Grâce à cela, ils produisent des effets d'éclairage variés tels que des clignotements alternés, des dégradés de respiration et des animations de défilement, offrant des interactions plus intuitives et vivantes.

**Bouton**

| ![Img](./media//2003.png)| ![Img](./media//2004.png)|
| :--: | :--: |
| Produit réel | Schéma |

Le bouton, apparu pour la première fois au Japon, était appelé interrupteur sensible. Pendant le fonctionnement, appuyez sur l'interrupteur pour appliquer une force et fermer le circuit. Lors du relâchement de la pression, l'interrupteur s'ouvre. Sa lame ressort métallique interne change son état de connexion/déconnexion en réponse à la force appliquée.

Il y a quatre boutons, chacun connecté indépendamment à une broche de la carte micro:bit. Lorsqu'un bouton est pressé, le circuit génère un signal de niveau bas correspondant, permettant à la micro:bit de répondre rapidement aux commandes et améliorant considérablement la commodité et la précision de l'interaction.

![Img](./media/2bottom.png) 

#### 4.2.2.3 Pièces requises

| ![Img](./media/microbitV2.png)|  ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 board** (fourni par l'utilisateur) ×1 | **micro:bit Smart Gamepad** (assemblé) ×1 |**AAA battery** (fourni par l'utilisateur) ×4 |

#### 4.2.2.4 Flux de code

![Img](./media/2006.png)

#### 4.2.2.5 Code de test

⚠️ **Notez que le temps de délai de MODE*_DELAY dans les codes peut être modifié selon vos besoins.**

**Code complet :**

![Img](./media/2005.png)

![Img](./media/line1.png)

**Brève explication :**

① Au début, désactivez la fonction des LED (Set led enable to false).

Et définissez 4 délais LED (par exemple, définir 5 en mode 2, définir 500 en mode 1...), définissez l'anti-rebond des boutons sur 20. Initialisez quatre LED RGB sur la broche P8 avec aucune couleur (définir toutes les valeurs à 0), c'est-à-dire éteintes.

![Img](./media/2009.png)

② Pendant la boucle, une opération anti-rebond est mise en œuvre en vérifiant si la différence entre le temps d'exécution actuel et le temps d'appui précédent dépasse le seuil anti-rebond prédéfini (BTN_DEBOUNCE), empêchant ainsi les pressions répétées causées par le rebond physique.


![Img](./media/2010.png)


③ Lorsque C(/D/E/F) est pressé, le mode est réglé sur 1(2/3/4), tandis que les étapes d'animation et les points de départ temporels pour le mode correspondant sont réinitialisés, les lumières sont effacées et l'horodatage du bouton est mis à jour. Cela permet un basculement précis et un démarrage initial des différents modes LED.


| ![Img](./media/2011.png)|![Img](./media/2012.png)|
| :--: | :--: |
|Le bouton C est pressé|Le bouton D est pressé|
| ![Img](./media/2013.png)    |     ![Img](./media/2014.png)   |
|Le bouton E est pressé|Le bouton F est pressé|

④ Lorsque le mode est réglé sur 1 et que l'intervalle entre le temps actuel et le temps du mode précédent dépasse MODE1Delay, mettez d'abord à jour l'horodatage du mode, et affichez les lumières en fonction des différentes valeurs de model_step (0–4) dans l'ordre : rouge, vert, bleu, jaune et violet. Après avoir actualisé l'affichage, réinitialisez la boucle de model_step par une opération modulo pour changer régulièrement ces cinq couleurs.

![Img](./media/2015.png)

⑤ Lorsque le mode est 2 et que l'intervalle entre le temps actuel et le temps du mode précédent dépasse MODE2_DELAY, mettez d'abord à jour l'horodatage du mode, et incrémentez la valeur de couleur (teinte) de manière cyclique par modulo (plage 0–359). Ensuite, effacez la lumière et affichez la teinte correspondante avec une saturation élevée (99) et une faible luminosité (20), et les couleurs en dégradé changeront en douceur. (Les valeurs de luminosité et de saturation dans les codes peuvent être ajustées selon les besoins.)

![Img](./media/2016.png)

⑥ Lorsque le mode est 3 et que l'intervalle entre le temps actuel et le temps du mode précédent dépasse MODE3_DELAY, mettez d'abord à jour l'horodatage du mode et décalez tous les pixels de la bande lumineuse d'un cran, assignez une teinte aléatoire (0–359), une saturation élevée (99) et une faible luminosité (20) au pixel 0. Actualisez l'affichage et vous verrez un effet d'eau courante : les lumières se déplacent séquentiellement et changent de couleur de façon aléatoire. (Les valeurs de luminosité et de saturation dans le code peuvent être ajustées selon les besoins.)

![Img](./media/2017.png)

⑦ Lorsque le mode est 4 et que l'intervalle entre le temps actuel et le temps du mode précédent dépasse MODE4_DELAY, mettez d'abord à jour l'horodatage du mode et effacez la bande lumineuse, assignez une teinte aléatoire (0–359), une saturation élevée (99) et une faible luminosité (20) aux pixels correspondant à model_step, et actualisez l'affichage. Enfin, faites cycler model_step dans 0–3 via modulo, et vous verrez un seul LED s'allumer séquentiellement dans des couleurs aléatoires. (Les valeurs de luminosité et de saturation dans le code peuvent être ajustées selon les besoins.)

![Img](./media/2018.png)

#### 4.2.2.6 Résultat du test

![Img](./media/4top.png)

Après avoir téléversé le code, insérez la carte micro:bit dans la fente du gamepad (**piles installées**), et basculez l'interrupteur sur “ON”.

Appuyez sur **C** : les lumières alternent parmi **rouge-vert-bleu-jaune-violet** dans l'ordre.

Appuyez sur **D** : la teinte des lumières augmentera, et finalement les couleurs en dégradé changeront en douceur.

Appuyez sur **E** : les lumières génèrent une couleur aléatoire à partir du pixel 0, et déplacent la couleur d'un pixel séquentiellement, vous voyez donc un effet d'eau courante.

Appuyez sur **F** : chaque pixel s'allume séquentiellement avec des couleurs aléatoires.

![Img](./media/2019.gif)

<span style="color: rgb(0, 209, 0);">**Astuce :** Si la carte ne répond pas, veuillez appuyer sur le bouton de réinitialisation à l'arrière de la carte micro:bit.</span>

![Img](./media/4bottom.png)