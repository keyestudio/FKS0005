## Dépannage

1\. Après le téléversement du code, la matrice 5x5 du micro:bit affiche un visage en pleurs, et elle affichera des messages d'erreur en défilement.

2\. Si le code téléversé a des caractères ajoutés ou supprimés par erreur, vous pouvez le vérifier selon les invites dans le shell.

![Img](./media/g002.png)

3\. Si le code téléversé contient des fichiers de bibliothèques tierces, vérifiez d'abord si les bibliothèques correspondantes ont été téléversées sur la carte micro:bit. Pour savoir comment importer une bibliothèque, veuillez vous référer à “**5.1.4 Téléverser le code**”. 

4\. Après le téléversement du code, aucune donnée n'est imprimée. Vous devez d'abord cliquer sur "![Img](./media/t027.png)", puis appuyer sur le bouton de réinitialisation à l'arrière de la carte Micro:bit, après quoi les données s'imprimeront normalement.

![Img](./media/g001.png)

5\.  Le micrologiciel micropython sera perdu après la gravure du code Makecode, et le shell affichera des messages d'erreur :

![Img](./media/g000.png)

À ce moment, vous devez regraver le micrologiciel en vous référant à **5.2.3 Graver le micrologiciel Micropython (Important)**.