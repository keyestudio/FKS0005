### 5.2.2 Lumières colorées

#### 5.2.2.1 Aperçu

![Img](./media/top1.png)

Les RGB LEDs sont un type de source lumineuse LED qui crée des images en mélangeant la lumière des trois couleurs primaires : rouge, vert et bleu, dont l'intersection produit différentes teintes. Les méthodes courantes incluent le mélange direct des couleurs primaires, l'utilisation d'une LED bleue combinée à un phosphore jaune, ou l'emploi d'une LED ultraviolet avec un phosphore RGB. Par rapport aux LED qui émettent de la lumière blanche directement, les RGB LEDs offrent une gamme plus large de possibilités de mélange de couleurs car les trois couleurs primaires peuvent être contrôlées indépendamment.

Dans ce projet, chaque bouton correspond à un mode différent des RGB LEDs. Lorsque le bouton C est pressé, les lumières clignotent alternativement dans l'ordre « rouge, vert, bleu, jaune et violet » ; appuyez sur D pour passer aux lumières en respiration ; appuyez sur E pour l'effet d'eau courante ; appuyez sur F pour l'effet de défilement (marquee).

Guirlandes lumineuses colorées pour décorations de fête, guirlandes de sapin de Noël, bandes RGB pour ambiance quotidienne, éclairages décoratifs à LED dans les parcs d'attractions et les centres commerciaux... Ce sont tous des exemples courants d'éclairages multi-modes dans notre vie quotidienne.

![Img](./media/bottom1.png)

#### 5.2.2.2 Connaissances sur les composants

![Img](./media/2top.png)

**SK6812 RGB LED**

| ![Img](./media//2001.png)| ![Img](./media//2002.png)|
| :--: | :--: |
|       Produit réel        |     Schéma     |

La SK6812 est une source lumineuse LED à contrôle externe qui intègre les circuits de commande et d'éclairage. Sa partie principale est constituée de billes LED à éclairage de surface de 5x5 mm, chacune fonctionnant comme un pixel indépendant qui intègre plusieurs circuits principaux : un circuit de verrouillage de données d'interface numérique intelligente, un circuit de mise en forme et d'amplification du signal, un circuit de régulation d'alimentation, un circuit de courant constant intégré et un oscillateur RC haute précision.

Sa communication utilise un protocole de codage unipolaire à retour à zéro. Au démarrage après mise sous tension, chaque pixel reçoit les données du contrôleur via le port DIN. Les 24 premiers bits de données sont extraits par le pixel initial et stockés dans le verrouillage de données interne, tandis que les bits restants sont mis en forme et amplifiés en interne avant d'être transmis via le port DOUT aux pixels suivants. À chaque pixel traité, la taille du signal transmis diminue de 24 bits.

Sur la manette, il y a quatre lumières SK6812 RGB. Elles supportent toutes un réglage de luminosité sur 256 niveaux sur leurs canaux rouge, vert et bleu, permettant des combinaisons de couleurs 256×256×256. Grâce à cela, elles offrent divers effets d'éclairage tels que des clignotements alternés, des dégradés en respiration et des animations défilantes, fournissant des interactions plus intuitives et plus vivantes.

**Bouton**

| ![Img](./media//2003.png)| ![Img](./media//2004.png)|
| :--: | :--: |
|       Produit réel        |     Schéma     |

Le bouton, apparu pour la première fois au Japon, était appelé interrupteur sensible. Lors de son utilisation, on appuie sur l'interrupteur pour exercer une force et fermer le circuit. Lors du relâchement de la pression, l'interrupteur s'ouvre. Sa lame ressort métallique interne change son état de connexion/déconnexion en réponse à la force appliquée.

Il y a quatre boutons, chacun connecté indépendamment à une broche de la carte micro:bit. Lorsqu'un bouton est pressé, le circuit génère un signal bas correspondant, permettant au micro:bit de répondre rapidement aux commandes et améliorant considérablement la commodité et la précision de l'interaction.

![Img](./media/2bottom.png)

#### 5.2.2.3 Pièces requises

| ![Img](./media/microbitV2.png)|  ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 board** (à fournir) ×1 | **micro:bit Smart Gamepad** (assemblé) ×1 | **Pile AAA** (à fournir) ×4 |


#### 5.2.2.4 Flux du code

![Img](./media/2006.png)

#### 5.2.2.5 Code de test

⚠️ **Remarque : le temps de délai de MODE\*_DELAY dans les codes peut être modifié selon vos besoins.**

**Complete code:**

```python
# import related libraries
from microbit import *
import neopixel, random, utime

# ==================== Configuration & Initialization ====================
BRIGHTNESS = 0.3        # Global brightness factor (0.0 to 0.9)
NP_NUM = 4              # Number of LEDs in the strip
strip = neopixel.NeoPixel(pin8, NP_NUM)

# Button Pins: Mapping JoyBit buttons to Pins
# C_KEY: Left, D_KEY: Right, E_KEY: Up, F_KEY: Down
KEYS = [pin15, pin16, pin13, pin14] 
for p in KEYS: 
    p.set_pull(p.PULL_UP)

# Global State Variables
mode = 0                # Current active mode (0-4)
last_btn_time = 0       # Global timestamp for button debouncing
# Shared state dictionary to handle indices and timing across modes
mode_data = {"idx": 0, "last_t": 0, "val": 0} 

# ==================== Utility Functions ====================
def get_rgb(h, s=99, l=15):
    """ Converts HSL to RGB and applies global brightness scaling """
    h %= 360
    s, l = s/100.0, l/100.0
    c = (1 - abs(2 * l - 1)) * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = l - c / 2
    # Determine RGB sector based on Hue
    res = [(c,x,0), (x,c,0), (0,c,x), (0,x,c), (x,0,c), (c,0,x)][int(h/60)]
    return tuple(int((i + m) * 255 * BRIGHTNESS) for i in res)

def update_mode(new_mode):
    """ Resets mode states and clears the strip when switching modes """
    global mode
    mode = new_mode
    mode_data["idx"], mode_data["val"] = 0, 0
    mode_data["last_t"] = utime.ticks_ms()
    strip.fill((0, 0, 0))
    strip.show()

# ==================== Mode Behavior Definitions ====================
def run_m1(): # Mode 1: Solid Color Cycling
    colors = [(255,0,0), (0,255,0), (0,0,255), (255,255,0), (128,0,128)]
    rgb = tuple(int(i * BRIGHTNESS) for i in colors[mode_data["idx"]])
    strip.fill(rgb)
    mode_data["idx"] = (mode_data["idx"] + 1) % len(colors)

def run_m2(): # Mode 2: Smooth Rainbow Gradient (HSL)
    mode_data["val"] = (mode_data["val"] + 1) % 360
    strip.fill(get_rgb(mode_data["val"]))

def run_m3(): # Mode 3: Pixel Shifting with Random Colors
    # Shift existing pixels to the right
    for i in range(NP_NUM - 1, 0, -1): 
        strip[i] = strip[i-1]
    # Inject a new random color at the start
    strip[0] = get_rgb(random.randint(0, 360))

def run_m4(): # Mode 4: Chasing Single Pixel
    strip.fill((0,0,0)) # Clear all
    strip[mode_data["idx"]] = get_rgb(random.randint(0, 360), l=18)
    mode_data["idx"] = (mode_data["idx"] + 1) % NP_NUM

# Mode Map: Mode ID -> (Function to execute, delay in milliseconds)
MODES = {
    1: (run_m1, 500), 2: (run_m2, 5), 
    3: (run_m3, 200), 4: (run_m4, 200)
}

# ==================== Main Loop (Non-Blocking) ====================
while True:
    curr_t = utime.ticks_ms()
    
    # 1. Scan Buttons (Non-blocking debounce)
    for i, pin in enumerate(KEYS):
        if pin.read_digital() == 0 and utime.ticks_diff(curr_t, last_btn_time) > 200:
            last_btn_time = curr_t
            update_mode(i + 1) # i+1 maps 0-3 to modes 1-4
            break 

    # 2. Execute Mode Logic based on Timer
    if mode in MODES:
        func, delay = MODES[mode]
        if utime.ticks_diff(curr_t, mode_data["last_t"]) > delay:
            mode_data["last_t"] = curr_t
            func()
            strip.show()
    elif mode == 0:
        # Standby: Keep strip off and save CPU cycles
        strip.fill((0,0,0))
        strip.show()
        utime.sleep_ms(20)

```
**Brève explication :**

① Importer les bibliothèques, configurer les constantes, initialiser les bandes NeoPixel et les broches des boutons.

Le script importe d'abord la bibliothèque principale `microbit` requise pour MicroPython, `neopixel` pour contrôler les LED NeoPixel, `random` pour générer des nombres aléatoires, et `utime` pour les opérations liées au temps (comme obtenir l'horodatage courant et effectuer des temporisations).

Ensuite, plusieurs constantes de configuration clés sont définies : `BRIGHTNESS` contrôle la luminosité globale des LED (0.0~0.9), `NP_NUM` spécifie le nombre de LED sur la bande NeoPixel (ici 4), et l'objet `strip` est initialisé, connecté à `pin8` et contient `NP_NUM` LED.

La liste `KEYS` spécifie les broches Micro:bit correspondant aux quatre boutons connectés à la carte d'extension JoyBit. En appliquant des résistances de pull-up (`p.PULL_UP`) à ces broches dans une boucle, les broches restent à un niveau haut lorsque les boutons ne sont pas pressés et à un niveau bas lorsqu'ils le sont (pour une détection aisée).

Enfin, les variables d'état globales suivantes sont définies : `mode` suit le mode d'éclairage actuellement actif (0 pour veille ; 1–4 sont différents effets d'éclairage), `last_btn_time` stocke l'horodatage pour l'anti-rebond logiciel des boutons, et `mode_data` est un dictionnaire qui contient les informations d'état partagées ou maintenues entre les modes (par ex. index, dernière mise à jour, valeur).

```python
# import related libraries
from microbit import *
import neopixel, random, utime

# ==================== Configuration & Initialization ====================
BRIGHTNESS = 0.3        # Global brightness factor (0.0 to 0.9)
NP_NUM = 4              # Number of LEDs in the strip
strip = neopixel.NeoPixel(pin8, NP_NUM)

# Button Pins: Mapping JoyBit buttons to Pins
# C_KEY: Left, D_KEY: Right, E_KEY: Up, F_KEY: Down
KEYS = [pin15, pin16, pin13, pin14] 
for p in KEYS: 
    p.set_pull(p.PULL_UP)

# Global State Variables
mode = 0                # Current active mode (0-4)
last_btn_time = 0       # Global timestamp for button debouncing
# Shared state dictionary to handle indices and timing across modes
mode_data = {"idx": 0, "last_t": 0, "val": 0} 
```

② Fonctions utilitaires : conversion HSL→RGB et gestion du changement de mode.

Cette partie définit deux fonctions utilitaires :

*   `get_rgb(h, s, l)` : conversion de couleurs. Elle accepte des valeurs HSL (Teinte, Saturation, Luminosité) et les convertit en format RGB. Elle applique aussi le facteur de luminosité global `BRIGHTNESS`, garantissant que toutes les couleurs sont ajustées selon la limite de luminosité. Cette fonction facilite la génération d'effets lumineux de diverses couleurs.
*   `update_mode(new_mode)` : permet un changement sécurisé entre les modes d'éclairage. Appelez-la pour passer à un nouveau mode ; elle mettra à jour la variable globale `mode`, remettra à zéro `idx` et `val` dans le dictionnaire `mode_data`, et définira `last_t` sur l'heure actuelle pour que le nouveau mode puisse démarrer son chronométrage. De plus, elle efface la bande NeoPixel pour éviter des résidus d'effets précédents lors du changement de mode.

```python
# ==================== Utility Functions ====================
def get_rgb(h, s=99, l=15):
    """ Converts HSL to RGB and applies global brightness scaling """
    h %= 360
    s, l = s/100.0, l/100.0
    c = (1 - abs(2 * l - 1)) * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = l - c / 2
    # Determine RGB sector based on Hue
    res = [(c,x,0), (x,c,0), (0,c,x), (0,x,c), (x,0,c), (c,0,x)][int(h/60)]
    return tuple(int((i + m) * 255 * BRIGHTNESS) for i in res)

def update_mode(new_mode):
    """ Resets mode states and clears the strip when switching modes """
    global mode
    mode = new_mode
    mode_data["idx"], mode_data["val"] = 0, 0
    mode_data["last_t"] = utime.ticks_ms()
    strip.fill((0, 0, 0))
    strip.show()
```

③ Définition des comportements lumineux et mappage des modes.

Quatre fonctions de mode d'éclairage différentes sont définies, chacune implémentant un effet lumineux unique :

*   `run_m1()` (Mode 1 : Cycle de couleurs unies) : la bande affiche régulièrement une série de couleurs unies prédéfinies (rouge, vert, bleu, jaune, violet), changeant d'une couleur à l'autre.
*   `run_m2()` (Mode 2 : Dégradé arc-en-ciel fluide) : la bande affiche un dégradé arc-en-ciel fluide en changeant constamment la teinte (`mode_data["val"]`).
*   `run_m3()` (Mode 3 : Décalage de pixels avec couleurs aléatoires) : les pixels de la bande se déplacent vers la droite, et le pixel le plus à gauche est rempli d'une nouvelle couleur aléatoire, comme un flux.
*   `run_m4()` (Mode 4 : Pixel unique en poursuite) : un seul pixel de la bande s'allume et se déplace le long de la bande, avec une couleur aléatoire à chaque fois.

Enfin, le dictionnaire `MODES` associe chaque identifiant de mode (1–4) à la fonction d'exécution correspondante et au délai de mise à jour (en millisecondes), de sorte que la boucle principale puisse appeler facilement la fonction appropriée selon le mode courant et contrôler sa fréquence de mise à jour.

```python
# ==================== Mode Behavior Definitions ====================
def run_m1(): # Mode 1: Solid Color Cycling
    colors = [(255,0,0), (0,255,0), (0,0,255), (255,255,0), (128,0,128)]
    rgb = tuple(int(i * BRIGHTNESS) for i in colors[mode_data["idx"]])
    strip.fill(rgb)
    mode_data["idx"] = (mode_data["idx"] + 1) % len(colors)

def run_m2(): # Mode 2: Smooth Rainbow Gradient (HSL)
    mode_data["val"] = (mode_data["val"] + 1) % 360
    strip.fill(get_rgb(mode_data["val"]))

def run_m3(): # Mode 3: Pixel Shifting with Random Colors
    # Shift existing pixels to the right
    for i in range(NP_NUM - 1, 0, -1): 
        strip[i] = strip[i-1]
    # Inject a new random color at the start
    strip[0] = get_rgb(random.randint(0, 360))

def run_m4(): # Mode 4: Chasing Single Pixel
    strip.fill((0,0,0)) # Clear all
    strip[mode_data["idx"]] = get_rgb(random.randint(0, 360), l=18)
    mode_data["idx"] = (mode_data["idx"] + 1) % NP_NUM

# Mode Map: Mode ID -> (Function to execute, delay in milliseconds)
MODES = {
    1: (run_m1, 500), 2: (run_m2, 5), 
    3: (run_m3, 200), 4: (run_m4, 200)
}
```

④ Boucle principale : balayage des boutons, exécution des modes et gestion de la veille.
1.  Balayage des boutons : elle parcourt chaque broche de bouton dans la liste `KEYS` pour détecter si un bouton est pressé (lecture de la broche égale à `0`). Pour éviter les déclenchements multiples causés par les rebonds, un mécanisme anti-rebond logiciel est employé : une nouvelle pression n'est prise en compte que si plus de 200 millisecondes se sont écoulées depuis l'opération précédente. Lorsqu'une pression valide est détectée, elle appelle `update_mode()` pour le mode d'éclairage correspondant (l'identifiant du mode est obtenu en ajoutant 1 à l'index du bouton `i`) et met à jour `last_btn_time`.
2.  Exécution du mode : si le `mode` courant figure dans le dictionnaire `MODES` (c.-à-d. qu'il ne s'agit pas du mode veille), il récupère la fonction d'exécution correspondante et le délai de mise à jour. Il vérifie ensuite si la période de délai spécifiée est écoulée depuis la dernière mise à jour de ce mode. Le cas échéant, il met à jour `mode_data["last_t"]`, appelle la fonction `func()` du mode pour actualiser les données de couleur, et envoie les mises à jour à la bande lumineuse via `strip.show()`.
3.  Traitement en veille : si `mode` = `0` (veille), il efface la bande lumineuse (`strip.fill((0,0,0))`), affiche un état éteint, avec un bref délai via `utime.sleep_ms(20)` pour économiser les ressources CPU.

```python
# ==================== Main Loop (Non-Blocking) ====================
while True:
    curr_t = utime.ticks_ms()
    
    # 1. Scan Buttons (Non-blocking debounce)
    for i, pin in enumerate(KEYS):
        if pin.read_digital() == 0 and utime.ticks_diff(curr_t, last_btn_time) > 200:
            last_btn_time = curr_t
            update_mode(i + 1) # i+1 maps 0-3 to modes 1-4
            break 

    # 2. Execute Mode Logic based on Timer
    if mode in MODES:
        func, delay = MODES[mode]
        if utime.ticks_diff(curr_t, mode_data["last_t"]) > delay:
            mode_data["last_t"] = curr_t
            func()
            strip.show()
    elif mode == 0:
        # Standby: Keep strip off and save CPU cycles
        strip.fill((0,0,0))
        strip.show()
        utime.sleep_ms(20)
```

#### 5.2.2.6 Résultat du test

![Img](./media/4top.png)

Après avoir flashé le code, insérez la carte micro:bit dans la fente de la manette (**piles installées**), et mettez l'interrupteur sur « ON ».

Appuyez sur **C** : les lumières alternent entre **rouge-vert-bleu-jaune-violet** dans l'ordre.

Appuyez sur **D** : la teinte des couleurs des lumières augmentera, et les dégradés changeront progressivement.

Appuyez sur **E** : les LED génèrent une couleur aléatoire à partir du pixel 0, et la couleur se décale d’un pixel à la fois, on observe ainsi un effet d'eau courante.

Appuyez sur **F** : chaque pixel s'allume successivement avec des couleurs aléatoires.

![Img](./media/2019.gif)

<span style="color: rgb(0, 209, 0);">**Astuce :** Si la carte ne répond pas, veuillez appuyer sur le bouton de réinitialisation au dos de la carte micro:bit.</span>

![Img](./media/4bottom.png)