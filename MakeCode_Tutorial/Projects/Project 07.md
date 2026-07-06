### 4.2.7 Thermomètre et Hygromètre

#### 4.2.7.1 Aperçu

![Img](./media/top1.png)

Dans ce projet, nous construisons un système de surveillance de la température et de l'humidité à l'aide d'une carte micro:bit, d'un gamepad, d'un capteur de température et d'humidité XHT11 et d'un écran OLED. Le capteur XHT11 mesure la température ambiante et l'humidité, tandis que l'écran OLED met à jour les lectures en temps réel. La carte contrôleur du gamepad facilite l'extension du circuit et les connexions stables, permettant au système de fonctionner comme un simple thermomètre.

![Img](./media/bottom1.png)

#### 4.2.7.2 Connaissances sur les composants

![Img](./media/2top.png)

**Capteur de température et d'humidité XHT11**

![Img](./media/XHT11.png)

Le capteur XHT11 fournit des signaux numériques et utilise une acquisition et une conversion de signal analogique spécialisées, ainsi que des techniques avancées de détection de la température et de l'humidité pour garantir une excellente stabilité à long terme et une grande fiabilité.

Il intègre des capteurs d'humidité résistifs haute précision et des thermistances de température, intégrés à un microcontrôleur 8 bits haute performance.

**Mode de communication du XHT11 :**

Il utilise une communication par bus unique simplifiée. Le bus unique se compose d'une seule ligne de données, via laquelle tous les échanges de données et opérations de contrôle au sein du système sont effectués.

- Bits de transmission sur le bus unique :

  - Format de données du bus unique : Transmet 40 bits de données à la fois, bit de poids fort en premier.

  - 8 bits de partie entière de l'humidité + 8 bits de partie décimale de l'humidité + 8 bits de partie entière de la température + 8 bits de partie décimale de la température + 8 bits de parité.

    **Note : La partie décimale de l'humidité est 0**.

- Bit de parité :

  - 8 bits de partie entière de l'humidité + 8 bits de partie décimale de l'humidité + 8 bits de partie entière de la température + 8 bits de partie décimale de la température

    Le bit de parité de 8 bits est les 8 derniers bits du résultat.

![Img](./media/7001.png)

Diagramme de séquence des données du capteur de température et d'humidité XH11 :

Après que l'hôte utilisateur (MCU) envoie un signal de démarrage, le XHT11 passe du mode basse consommation au mode haute vitesse, et après la fin de ce signal, le XHT11 envoie un signal de réponse et 40 bits de données, et déclenche une acquisition de signal.

Le signal est envoyé comme illustré dans la figure :

![Img](./media/7002.png)

⚠️ **Astuce :** Les données de température et d'humidité lues par l'hôte à partir du capteur XHT11 sont toujours les valeurs de la mesure précédente. S'il y a un long intervalle entre deux mesures, veuillez effectuer deux lectures consécutives ; la valeur lors de la deuxième lecture sera la valeur réelle.

**Schéma :**

![Img](./media/cou73-2.png)

**Paramètres :**

- Tension de fonctionnement : DC 3V~5V
- Courant de fonctionnement : (Max)2.5mA
- Puissance maximale : 0.0125W
- Plage de température : -25 ~ +60°C (±2℃)
- Plage d'humidité : 5 ~ 95%RH(Précision autour de 25°C ±5%RH)
- Signal de sortie : bus unique numérique bidirectionnel

**Écran OLED**

![Img](./media/A636.png)

L'OLED offre des avantages exceptionnels tels que la richesse des couleurs, un fort contraste et de larges angles de vue. Les images sont nettes et vives, avec un noir particulièrement remarquable. Chaque pixel est auto-émissif sans besoin de rétroéclairage, ce qui entraîne une consommation d'énergie relativement faible. L'écran OLED de 0,9 pouce, avec sa taille compacte, sa haute résolution (128×64 pixels) et sa faible consommation d'énergie, est idéal pour les applications dans les systèmes embarqués et les dispositifs portables.

⚠️ **Remarque** : Pour cet écran OLED, l'interface SDA est connectée à la broche P20 sur la carte micro:bit, tandis que le SCL est connecté à la broche P19.

**Paramètres :**

- Tension de fonctionnement : DC 3V - 5V
- Courant de fonctionnement : 30mA
- Interface : broches avec un espacement de 2,54mm
- Mode de communication : communication I2C
- Puce de pilotage interne : SSD1306
- Résolution : 128×64
- Angle de vue : supérieur à 150°

#### 4.2.7.3 Pièces requises

| ![Img](./media/microbitV2.png)|  ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 board** (apporté par l'utilisateur) ×1 | **micro:bit Smart Gamepad** (assemblé) ×1 |**Pile AAA** (apportées par l'utilisateur) ×4 |
|![Img](./media/XHT11.png)|![Img](./media/OLED.png)|![Img](./media/7008.png)|
|**Capteur de température et d'humidité XHT11** (apporté par l'utilisateur)×1|**Écran OLED** (apporté par l'utilisateur)×1 |**Fil Dupont F-F**(apporté par l'utilisateur) x7|

#### 4.2.7.4 Schéma de câblage

![Img](./media/jiexian.png)

**Après avoir câblé comme indiqué ci-dessus, insérez la micro:bit dans la fente de la carte de contrôle du gamepad.**

| OLED display | micro:bit gamepad control board |micro:bit board pin |
| :--: | :--: | :--: |
| GND |  GND | GND |
| VCC |  3V | 3V |
| SDA |  SDA | P20 |
| SCL |  SCL | P19 |

| XHT11 temperature and humidity sensor | micro:bit gamepad control board | micro:bit board pin |
| :--: | :--: | :--: |
| G | GND | GND |
| V |  3V | 3V |
| S |  12 | P12 |

#### 4.2.7.5 Flux du code

![Img](./media/7003.png)

#### 4.2.7.6 Code de test
⚠️ **Remarque :** ici les bibliothèques OLED et DHT11 sont incluses, donc nous devons importer : https://github.com/keyestudio/pxt-environment-kit-master.

**Code complet :**

![Img](./media/7004.png)

![Img](./media/line1.png)

**Brève explication :**

① Initialiser les pixels de l'OLED et le nettoyer, afficher ![Img](./media/1006.png) sur la matrice 5×5 LED, et définir les valeurs des variables temperature et humidity à 0.

![Img](./media/7005.png)

② Attribuer les mesures correspondantes du capteur XHT11 aux variables temperature et humidity.

![Img](./media/7006.png)

③ L'OLED affiche les relevés du capteur XHT11.

![Img](./media/7007.png)

④ Pause de 500 ms (0,5 s).

![Img](./media/cou28.png)

#### 4.2.7.7 Résultat du test

![Img](./media/4top.png)

Après avoir transféré le code, insérez la carte micro:bit dans la fente du gamepad (**piles installées**), et basculez l'interrupteur sur « ON ».

Après avoir téléversé le code sur la carte micro:bit, l'OLED affiche en temps réel la température et l'humidité lues par le capteur XHT11.

![Img](./media/7000.gif)

<span style="color: rgb(0, 209, 0);">**Astuce :** Si la carte ne répond pas, veuillez appuyer sur le bouton de réinitialisation au dos de la carte micro:bit.</span>

![Img](./media/4bottom.png)