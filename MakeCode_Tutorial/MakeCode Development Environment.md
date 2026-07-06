## 4.1.1 À propos de MakeCode

⚠️ **Les étapes suivantes sont effectuées sous le système d'exploitation Windows. Si vous utilisez un autre système d'exploitation, vous pouvez vous en servir comme référence. Les démonstrations ci‑dessous sont effectuées avec Google Chrome / Microsoft Edge.**

**Environnement de programmation MakeCode :**

Ouvrez la [version en ligne de l'éditeur MakeCode](https://makecode.microbit.org/#editor).

MakeCode main interface:

![Img](./media/A637.png)

Il y a des blocs “**on start**” et “**forever**” dans la zone d'édition du code. Lorsque l'alimentation est branchée ou que la carte est réinitialisée, “on start” signifie que le code dans le bloc s'exécute une seule fois, tandis que “forever” implique que le code s'exécute en boucle.

Cliquez sur “**JS JavaScript**” pour voir le code JavaScript:

![Img](./media/A754.png)

Ou cliquez sur “**Python**” pour basculer vers le code Python:

![Img](./media/A814.png)

**Paramètres de langue :**

![Img](./media/Animation-3.gif)

Étapes :

Étape 1 : Cliquez sur le bouton des paramètres ![Img](./media/A806.png).

![Img](./media/A301.png)

Étape 2 : Cliquez sur “Langue”.

![Img](./media/A302.png)

Étape 3 : Sélectionnez la langue souhaitée. Ici nous la réglons sur “Anglais”.

![Img](./media/A303.png)

## 4.1.2 Bibliothèque d'extensions MakeCode

### 4.1.2.1 Ajouter une bibliothèque

⚠️ **Nous fournissons des fichiers de code (.hex) pour chaque projet, vous pouvez donc les charger directement dans l'éditeur MakeCode. Sinon, si vous le souhaitez, vous pouvez aussi construire les blocs de code vous‑même. Notez que des bibliothèques sont nécessaires si vous les construisez manuellement.**

⚠️ **<span style="color: rgb(255, 76, 65);">Remarque :</span>** Copiez-collez le lien dans la zone de recherche : `https://github.com/keyestudio2019/pxt-creative-inventors-kit-master.git`.

![Img](./media/Animation-4.gif)

Étapes :

1\. Cliquez sur ![Img](./media/A806.png) pour sélectionner “**Extensions**”.

![Img](./media/A842.png)

Ou cliquez sur “**Extensions**” au‑dessus des blocs **Avancés**.

![Img](./media/A900.png)

2\. Recherchez des mots‑clés ou collez le lien GitHub.

![Img](./media/A909.png)

3\. Ici nous saisissons l'URL : `https://github.com/keyestudio2019/KEYES-Smart-Gamepad-master.git` dans la zone de recherche et cliquons sur ![Img](./media/A3257.png), puis chargeons l'extension “**Smart-Gamepad**”.

![Img](./media/A306.png)

4\. Chargement :

![Img](./media/A3316.png)

5\. Chargée :

![Img](./media/A335.png)

### 4.1.2.2 Mettre à jour/Supprimer une bibliothèque

⚠️ **En général, il n'est pas nécessaire de supprimer des bibliothèques, sauf si elles ne sont pas requises.**

![Img](./media/Animation-4.gif)

Étapes :

1\. Cliquez sur “**JavaScript**” pour passer au code texte.

![Img](./media/A724.png)

2\. Cliquez sur “**Explorer**”.

![Img](./media/A749.png)

3\. Trouvez “**Smart-Gamepad**” et cliquez sur la corbeille ![Img](./media/A813.png) pour la supprimer.

![Img](./media/A824.png)

4\. « **Supprimer** ».

![Img](./media/A727.png)

## 4.1.3 Programme MakeCode

### 4.1.3.1 Importer un programme dans MakeCode

Nous prenons le projet “**heatbeat**” comme exemple.

![Img](./media/Animation-2.gif)

Étapes :

1\. Connectez la carte micro:bit à votre ordinateur via un câble micro USB.

![Img](./media/A800.png)

Lorsque la micro:bit est sous tension, la LED rouge à l'arrière s'allumera.

Sur la carte micro:bit, une LED jaune clignotera lorsque la carte communiquera avec votre ordinateur via micro USB. 

Ouvrez Finder (Mac) / Devices and drives (Windows), et vous verrez un lecteur USB nommé "MICROBIT". Notez toutefois qu'il ne s'agit pas d'un disque ordinaire !

![Img](./media/A849.png)

2\. Cliquez sur « **Importer** » :

![Img](./media/A956.png)

3\. Puis sélectionnez « **Importer un fichier...** ».

![Img](./media/A042.png)

4\. « **Choisir un fichier** » pour ouvrir le fichier nécessaire.

![Img](./media/A06.png)

5\. Ici nous choisissons « **heartbeat.hex** ».

![Img](./media/A28.png)

6\. « **Continuer √** ».

![Img](./media/A149.png)

Ou vous pouvez glisser directement le fichier hex vers l'interface principale de MakeCode :

![Img](./media/A202.png)

7\. Importé :

![Img](./media/A217.png)

### 4.1.3.2 Télécharger le code (WebUSB)

Pour des navigateurs comme **Google Chrome/Microsoft Edge**, leur WebUSB permet un accès direct au périphérique matériel micro USB via une page web. Cliquez sur « Connecter l'appareil » pour appareiller le périphérique. Ensuite, cliquez sur « **Télécharger** » pour charger le code sur la carte micro:bit.

![Img](./media/Animation.gif)

Étapes :

#### 4.1.3.2.1 Apparier l'appareil

1\. Connectez la carte micro:bit à votre ordinateur via un câble micro USB.

![Img](./media/A951.png)

2\. Cliquez sur les trois points “**...**” derrière « **Télécharger** » et sélectionnez « **Connecter l'appareil** ».

![Img](./media/A028.png)

3\. « **Suivant** ».

![Img](./media/A046.png)

4\. « **Appairer** ».

![Img](./media/A104.png)

5\. Connectez‑vous à un « **Périphérique** » et cliquez sur « **Connecter** ». 

![Img](./media/A127.png)

6\. « **Terminé** » et connecté.

![Img](./media/A144.png)

#### 4.1.3.2.2 Télécharger le code

Après connexion, cliquez sur « **Télécharger** » et le code sera transféré sur la carte micro:bit, et ![Img](./media/A212.png) devient  ![Img](./media/A220.png).

![Img](./media/A232.png)

⚠️ **Conseils**

Si aucun appareil n'apparaît pour l'appairage dans l'interface, veuillez consulter [device-webusb-troubleshoot](https://makecode.microbit.org/device/usb/webusb/troubleshoot).

Si le firmware de la micro:bit nécessite une mise à jour, consultez [how-to-update-the-firmware](https://microbit.org/guide/firmware/).

### 4.1.3.3 Télécharger le code (sans WebUSB)

1\. Connectez la carte micro:bit à votre ordinateur via un câble micro USB.

![Img](./media/A800.png)

Lorsque la micro:bit est sous tension, la LED rouge à l'arrière s'allumera.

Sur la carte micro:bit, une LED jaune clignotera lorsque la carte communiquera avec votre ordinateur via micro USB. 

Ouvrez Finder (Mac) / Devices and drives (Windows), et vous verrez un lecteur USB nommé "MICROBIT". Notez toutefois qu'il ne s'agit pas d'un disque ordinaire !

![Img](./media/A849.png)

2\. Pour les navigateurs, veuillez charger le code sur la carte micro:bit comme suit :

![Img](./media/Animations-1.gif)

Étapes :

① Cliquez sur le bouton « **Télécharger** » et un fichier « **.hex** » sera téléchargé, lisible par la carte micro:bit. Ensuite, copiez‑le et collez‑le sur la carte. 

Pour Windows, vous pouvez « **Envoyer vers→MICROBIT** » et charger le fichier « **.hex** » sur la carte micro:bit. Pendant ce processus, la LED jaune à l'arrière de la carte clignotera. Une fois le chargement terminé, la LED reste allumée.

![Img](./media/A319.png)

![Img](./media/A449.png)

Ou vous pouvez glisser directement le fichier « **.hex** » sur le MICROBIT :

![Img](./media/A341.png)

![Img](./media/A345.png)

② Après cela, connectez la carte micro:bit à l'ordinateur via le câble micro USB et mettez‑la sous tension ; vous verrez la matrice LED 5 x 5 à bord afficher successivement ![Img](./media/A903.png) et ![Img](./media/A910.png).

![Img](./media/A22.png)



⚠️ Lors de chaque programmation, le lecteur MICROBIT s'éjectera automatiquement puis reviendra, et les fichiers **.hex** que vous y avez copiés ne s'afficheront pas. En effet, la carte micro:bit ne reçoit et n'exécute que le dernier programme envoyé et ne les stocke pas.