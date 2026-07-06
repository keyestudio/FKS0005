## 5.1 Thonny Development Environment

**Avant de programmer, vous devez effectuer quelques préparatifs importants.**

### 5.1.1 Install Thonny

Thonny est un logiciel libre et open source de petite taille, avec une interface simple, une utilisation facile et des fonctionnalités riches. C'est un IDE Python adapté aux débutants. Dans ce tutoriel, nous utilisons cet IDE pour développer un ESP32. Thonny prend en charge plusieurs systèmes d'exploitation, y compris Windows, Mac OS, Linux.

**1. Download Thonny**

(1)  Rendez-vous sur le site : [https://thonny.org](https://thonny.org) pour télécharger la dernière version de Thonny. D'autres versions peuvent ne pas être compatibles avec les fonctions micro:bit.  
(2)  Bibliothèque de code open-source de Thonny : [https://github.com/thonny/thonny](https://github.com/thonny/thonny).

Veuillez télécharger la version correspondant à votre système d'exploitation.

| OS | Download |
| :-- | :-- |
| MAC OS： | https://github.com/thonny/thonny/releases/download/v4.1.7/thonny-4.1.7.pkg|
| Windows： | https://github.com/thonny/thonny/releases/download/v4.1.7/thonny-4.1.7.exe|

| OS | Method          | Command |
| :-- |---------|--------------|
| Linux | Binary bundle | `bash <(wget -O - https://thonny.org/installer-for-linux)` |
|       | With pip | `pip3 install thonny` |
|       | Distro packages | Debian/Ubuntu：`sudo apt install thonny`<br>Fedora：`sudo dnf install thonny` |

![Img](./media/t001.png)

**2. Windows System**

A. L'icône Thonny téléchargée est la suivante :

![Img](./media/t002.png)

B. Double-cliquez sur “thonny-4.1.7.exe” et choisissez le mode d'installation. Ici nous choisissons «Install for all users».

![Img](./media/t003.png)

C. Vous pouvez aussi continuer à cliquer sur «Next» pour terminer l'installation.

![Img](./media/t004.png)

![Img](./media/t005.png)


D. Si vous souhaitez changer le chemin d'installation de Thonny, cliquez sur «Browse...» pour sélectionner un nouveau chemin. Sinon, continuez à cliquer sur «Next».

![Img](./media/t006.png)

![Img](./media/t007.png)

E. Cochez «Create desktop icon», vous verrez Thonny sur votre bureau.

![Img](./media/t008.png)

F. «Install».

![Img](./media/t009.png)

G. Patientez un moment et ne cliquez pas sur «Cancel».

![Img](./media/t010.png)

H. Lorsque vous voyez l'interface de succès, cliquez sur «Finish».

![Img](./media/t011.png)

I. Vous pouvez voir l'icône sur votre bureau si vous avez coché «Create desktop icon» :

![Img](./media/t011.png)                    

### 5.1.2 Thonny Basic Settings

A. Double-cliquez sur Thonny, choisissez la langue et les paramètres initiaux puis cliquez sur «Let’s go!».

![Img](./media/t013.png)

![Img](./media/t014.png)

![Img](./media/t015.png)

B. Cliquez sur “**View**” → “**File**” et “**Shell**”.

![Img](./media/t016.png)

![Img](./media/t017.png)

![Img](./media/t018.png)

### 5.1.3 Burn Micropython Firmware(Important)

Pour exécuter un programme Python sur la carte Micro:bit, il faut d'abord y flasher le micrologiciel.

**Flasher le micrologiciel MicroPython :**

Connectez le Micro:bit à votre PC avec un câble USB.

![Img](./media/A800.png)

Assurez-vous que le pilote est installé correctement et que le port COM est bien reconnu. Ouvrez le «**Device Manager**» et développez «**Ports**».

![Img](./media/t019.png)

Le numéro du port COM peut varier selon les ordinateurs.

Ouvrez Thonny, cliquez sur «**run**» et «**Configure interpreter...**»

![Img](./media/t020.png)

Sélectionnez “Micropython (BBC micro:bit)” et “mbeb Serial Port @ COM16” dans son interpréteur, puis cliquez sur «Install or update firmware».

![Img](./media/t021.png)

Et vous verrez les éléments suivants. Définissez “Target volume” sur “MICROBIT”, “MicroPython family” sur “nRF52”, “variant” sur “BBC micro:bit v2 (original simplifiled API)”, “version” sur “2.1.2”, puis cliquez sur «Install».

Si l'installation du micrologiciel échoue, appuyez sur le bouton de réinitialisation du Micro:bit, puis cliquez sur «Install».

![Img](./media/t022.png)

Après cela, cliquez sur «Close» puis sur «OK».

![Img](./media/t023.png)

Fermez toutes les fenêtres et retournez à la page principale puis cliquez sur l'icône «STOP» :

![Img](./media/t024.png)

### 5.1.4 Upload Code

**Run the test code(online)**

Le Micro:bit exécute le code en ligne lorsqu'il est connecté à l'ordinateur. Les utilisateurs peuvent programmer et déboguer les programmes avec Thonny.

Ouvrez Thonny et cliquez sur "**Open**".

![Img](./media/t025.png)

Lorsque une nouvelle fenêtre apparaît, ouvrez ".\MicroPython_Resource\Codes\Heart beat", sélectionnez “heartbeat&ZeroWidthSpace;.py”, et cliquez sur «Run current script» (si une erreur apparaît, cliquez d'abord sur ![Img](./media/t027.png) puis sur «Run current script»), et vous verrez un cœur battre sur le Micro:bit.

![Img](./media/t026.png)

Note : Lors de l'exécution en ligne, si vous appuyez sur le bouton de réinitialisation, le code ne sera pas exécuté de nouveau. Si vous souhaitez qu'il s'exécute après une réinitialisation, veuillez vous référer aux instructions d'exécution hors ligne ci-dessous.

**Run the test code(offline)**

Après avoir réinitialisé le Micro:bit, exécutez d'abord le fichier main.py à la racine.

Par conséquent, le nom de fichier que nous téléversons sur le Micro:bit doit être changé en main.py si nous voulons qu'il s'exécute après la réinitialisation. Ensuite, téléversez le fichier, appuyez sur le bouton de réinitialisation, et le code sera toujours exécuté.

Ici nous prenons heartbeat.py comme exemple. Sélectionnez **heartbeat&ZeroWidthSpace;.py** pour le «rename» en main.py, puis cliquez sur «OK». Maintenant vous pouvez choisir de «Upload to micro:bit».

![Img](./media/t028.png)

![Img](./media/t029.png)

![Img](./media/t030.png)

Appuyez sur le bouton de réinitialisation et vous verrez le cœur battre sur le Micro:bit.

Si vous souhaitez exécuter un autre code (pas des bibliothèques), vous devez d'abord renommer son fichier en main&ZeroWidthSpace;.py avant de le téléverser.

Pour les bibliothèques, faites un clic droit et sélectionnez directement «Upload to micro:bit» (Parfois le téléversement peut échouer en raison d'une taille trop importante de la bibliothèque. Dans ce cas, vous devez la simplifier ou supprimer les éléments inutiles).

### 5.1.5 Other Common Operations

**Delete file under Micro:bit**

Dans «micro:bit», sélectionnez «main&ZeroWidthSpace;.py» puis «Delete», et il sera supprimé.

![Img](./media/t031.png)

La même procédure s'applique pour la suppression d'autres fichiers.