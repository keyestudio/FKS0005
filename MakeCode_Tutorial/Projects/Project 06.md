### 4.2.6 Rock-Paper-Scissors

#### 4.2.6.1 Aperçu

![Img](./media/top1.png)

Ici, jouons à pierre-feuille-ciseaux par communication sans fil entre micro:bit. Les joueurs sélectionnent leur coup (pierre, feuille ou ciseaux) via les boutons, avec échange de données entre les appareils. Le jeu se joue au meilleur des trois ; si les trois manches se terminent toutes par des égalités ou par une combinaison victoire-défaite-égalité, une quatrième partie est déclenchée.

Chaque résultat est affiché sur la matrice du micro:bit (W pour victoire, L pour défaite, = pour égalité) et révélé par les lumières RGB (vert pour victoire, rouge pour défaite, jaune pour égalité) sur la broche P8. À la fin d'une manche, les deux appareils réinitialisent toutes les données et les lumières, se préparant pour la manche suivante.

Le gameplay intègre de manière fluide l'interaction sans fil avec le combat en plusieurs manches.

![Img](./media/bottom1.png)

#### 4.2.6.2 Connaissances composants

![Img](./media/2top.png)

**Microbit wireless communication**

![Img](./media/6001.png)

La carte micro:bit intègre deux capacités pratiques de communication sans fil : **radio 2.4GHz** et **Bluetooth basse consommation (BLE)**. Cependant elles ne peuvent pas être utilisées simultanément.

La première ne nécessite pas d'appariement et prend en charge jusqu'à 255 paquets indépendants pour minimiser les interférences, avec une portée de communication de 10–30 mètres, permettant une transmission rapide de données numériques et de chaînes. Tandis que la seconde est principalement utilisée pour l'appariement avec les smartphones, tablettes et autres appareils intelligents pour des applications IoT telles que le téléversement de données de capteurs et le contrôle à distance via une application mobile.

Elles élargissent les possibilités de développement créatif du micro:bit.

#### 4.2.6.3 Pièces requises

| ![Img](./media/microbitV2.png)|  ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 board** (fournie) ×2 | **micro:bit Smart Gamepad** (assemblé) ×2 |**AAA battery** (fournies) ×8 |

#### 4.2.6.4 Flux du code

![Img](./media/6002.png)

#### 4.2.6.5 Code de test

**Code complet:**

![Img](./media/6003.png)

![Img](./media/line1.png)

**Brève explication:**

① Initialiser la radio et définir le groupe sur '1' ; définir le nombre de manches, le statut, l'adversaire, et le résultat pierre-feuille-ciseaux des joueurs ; connecter les quatre lumières RGB à la broche P8 et rafraîchir l'affichage, définir la matrice pour afficher ![Img](./media/6004.png).

![Img](./media/6005.png)

② Déterminer l'issue de la manche en cours : si votre choix correspond à celui de l'adversaire (**1/2/3 pour ciseaux/pierre/papier**), c'est une égalité ; sinon, sélectionner un gagnant (ciseaux battent feuille, feuille bat pierre, pierre bat ciseaux), incrémenter la valeur de la manche de +1 et stocker le résultat.

![Img](./media/6006.png)

③ Stocker les résultats dans un tableau et afficher la chaîne correspondante. Si c'est la troisième partie, déterminer si une quatrième partie est nécessaire (si les trois parties sont toutes des égalités ou forment victoire-défaite-égalité). Si oui, afficher "FINAL" et attendre 1 seconde avant d'effacer la sélection pierre-feuille-ciseaux.

![Img](./media/6007.png)

Sinon, afficher "GAGNANT" pour la victoire, "PERDANT" pour la défaite, et "ÉGALITÉ" pour une égalité. Après un délai de 3 secondes, appeler la fonction resetGame pour effacer toutes les variables du jeu.

Si le match comporte quatre parties, afficher "FIN DU JEU" et appeler à nouveau la fonction resetGame après un délai de 3 secondes pour réinitialiser toutes les variables du jeu.

![Img](./media/6008.png)

Si le jeu n'est pas terminé, il affiche ![Img](./media/6004.png) et efface les choix des deux joueurs.

![Img](./media/6009.png)

④ Appuyez sur C et la carte envoie "1" pour ciseaux, et la matrice affiche ![Img](./media/6011.png) ; appuyez sur D et la carte envoie "3" pour papier, et la matrice affiche ![Img](./media/6012.png) ; appuyez sur E et elle envoie "2" pour pierre et affiche ![Img](./media/6013.png).

![Img](./media/6010.png)

⑤ Recevoir les données radio (le choix de l'adversaire).

![Img](./media/6014.png)

⑥ Déterminer si une quatrième manche est requise. Si les trois jeux se terminent tous par des égalités ou par une combinaison victoire-défaite-égalité, une quatrième manche est nécessaire ; sinon, elle n'est pas nécessaire.

![Img](./media/6015.png)

⑦ Les lumières RGB affichent les couleurs correspondantes en fonction du résultat : vert pour victoire, rouge pour défaite, et jaune pour égalité.

![Img](./media/6016.png)

⑧ Lorsque le jeu se termine, effacer l'affichage des quatre lumières RGB.

![Img](./media/6017.png)

⑨ Réinitialiser l'état du jeu, effacer toutes les valeurs des variables du jeu, réinitialiser les lumières RGB, et afficher ![Img](./media/6004.png).

![Img](./media/6018.png)


#### 4.2.6.6 Résultat du test

![Img](./media/4top.png)

Après avoir transféré le code, insérez la carte micro:bit dans l'emplacement du gamepad (**piles installées**), et basculez l'interrupteur dessus sur “ON”.

La matrice affiche initialement ![Img](./media/6004.png). Les joueurs appuient sur des boutons pour sélectionner leur coup (E pour pierre, D pour papier, ou C pour ciseaux), avec échange de données de match entre les deux appareils. Ils déterminent l'issue de la manche en cours : une victoire est indiquée par le "W" avec la lumière RGB devenant verte, une égalité par le "=" avec la lumière jaune, et une défaite par le "L" avec la lumière rouge (la première lumière RGB s'allume après la première manche, et ainsi de suite). La manche suivante aura lieu si le jeu n'est pas terminé.

Le jeu adopte le meilleur des trois : si les trois manches se terminent toutes par des égalités ou par une combinaison victoire-défaite-égalité, une quatrième partie est déclenchée.

S'il y a un gagnant après trois manches, il affichera "GAGNANT" pour la victoire et "PERDANT" pour la défaite. Une fois le résultat affiché, "FIN DU JEU" apparaîtra pour réinitialiser le jeu. Si la quatrième manche reste indécise, le jeu se terminera également.

![Img](./media/6000.gif)

<span style="color: rgb(0, 209, 0);">**Astuce :** Attendez que l'icône du cœur apparaisse avant de continuer la manche suivante. Si la carte ne répond pas, veuillez appuyer sur le bouton de réinitialisation à l'arrière de la carte micro:bit.</span>

![Img](./media/4bottom.png)