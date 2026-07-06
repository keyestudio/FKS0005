### 4.2.9 Micro:bit Gamepad Bestuurde 4WD Mecanum Robot Auto

#### 4.2.9.1 Overzicht

![Img](./media/top1.png)
In dit project besturen we een 4WD Mecanum Robot Auto met een gamepad-besturingsbord en een Micro:bit board. De joystick stelt de auto in staat om vooruit, achteruit, links en rechts te draaien; de C-knop beweegt de auto zijdelings naar links, de D naar zijdelings naar rechts, de E versnelt, en de F-toets vertraagt (met een snelheidsbereik van 20–95). Wanneer er geen handeling wordt uitgevoerd, blijft de auto stilstaan.

![Img](./media/bottom1.png)

#### 4.2.9.2 Benodigde Onderdelen

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 board** (zelf meegeleverd) ×1 | **micro:bit Smart Gamepad** (gemonteerd) ×1 |**AAA batterij** (zelf meegeleverd) ×4 |
| ![Img](./media/che.png) | ![Img](./media/18650.png) ||
| **KS4034 kit**(zelf meegeleverd) ×1 | **18650 batterij**(zelf meegeleverd) ×2 ||

Voor gedetailleerde informatie over de 4WD Mecanum Robot Auto**(KS4034)**, bezoek [hier](https://docs.keyestudio.com/projects/KS4034/en/latest/).
#### 4.2.9.3 Bedradingsschema

Raadpleeg de bedradingsinstructies in de KS4034-documentatie voor het aansluiten van de 4WD Mecanum Robot Auto en de gamepad via radiocommunicatie. Er is geen fysieke bedrading tussen de twee vereist; beide apparaten communiceren draadloos.

#### 4.2.9.4 Code Stroom
⚠️ **Let op dat de volgende bibliotheek moet worden geïmporteerd bij het programmeren van codes van de auto: https://github.com/keyestudio2019/mecanum_robot_v2**.

**Code stroom van de gamepad:**

![Img](./media/9001.png)

**Code stroom van de auto:**

![Img](./media/9002.png)

#### 4.2.9.5 Test Code

**Volledige code van de gamepad:**

![Img](./media/9003.png)

![Img](./media/line1.png)

**Korte uitleg:**

① Initialiseer de radiogroep op 1 met een signaaloverdrachtsterkte van 7; toon een hartpictogram en stel de variabelen SEND_INTERCAL in op 100 en BTN_DEBOUNCE_TIME op 20.

![Img](./media/9004.png)

② Stel de variabele currentCmd (instructie-inhoudvariabele) in op teken \'0\', en wijs de X- en Y-waarden van de joystick toe aan respectievelijk de variabelen rockerX en rockerY.

![Img](./media/9005.png)

③ Controleer of de joystick of knop een corresponderende handeling heeft. Als er een handeling plaatsvindt, stel de variabele currentCmd (instructie-inhoudvariabele) in op het corresponderende teken (R/U/L/D/A/B/Z/X); anders, laat het ongewijzigd.

![Img](./media/9006.png)

④ Controleer of currentCmd (instructie-inhoudvariabele) verschilt van lastCmd (slaat de vorige instructie-inhoud op). Als ja, verzend currentCmd, stel lastCmd in op currentCmd, en wacht een gespecificeerde vertraging.

![Img](./media/9007.png)

**Volledige code van de auto:**

![Img](./media/9008.png)

![Img](./media/line1.png)

**Korte uitleg:**

① Initialiseer de radiogroep op 1 met een signaaloverdrachtsterkte van 7; toon een hartpictogram en stel de variabelen SPEED in op 50, MIN_SPEED op 20 en MAX_speed op 95.

![Img](./media/9009.png)

② Ontvang de commandowaarde verzonden door de radio en sla het commando op in de variabele item.

![Img](./media/9010.png)

③ Op basis van de karaktercommando\'s (U/L/D/R/A/B) ontvangen door item, roep de corresponderende functies aan om de auto te besturen om vooruit, achteruit, links, rechts te draaien, en links en rechts te verschuiven.

![Img](./media/9011.png)

④ Op basis van het karaktercommando (Z/X) ontvangen door item, wordt de auto dienovereenkomstig versneld of vertraagd.

Tijdens acceleratie wordt de snelheid ingesteld op het minimum van SPEED+5 en MAX_speed (om overschrijding van MAX_speed te voorkomen); tijdens deceleratie wordt de snelheid ingesteld op het maximum van SPEED-5 en MIN_speed (om onder MIN_speed te voorkomen).

![Img](./media/9012.png)

⑤ Zes functies voor voertuigbewegingscontrole zijn hier gedefinieerd:

- car_back bestuurt alle vier de motoren om achteruit te draaien voor achteruitrijden;
- car_forward bestuurt alle vier de motoren om vooruit te draaien voor vooruitrijden;
- car_left realiseert het linksaf slaan van de auto door de linker motoren achteruit en de rechter motoren vooruit te zetten;
- car_right realiseert het rechtsaf slaan door de rechter motoren achteruit en de linker motoren vooruit te zetten;
- car_left_move en car_right_move maken links en rechts verschuiven mogelijk door gecoördineerde rotatie van de diagonale motoren.

Alle functies nemen de variabele SPEED als de motorparametersnelheid.

![Img](./media/9013.png)

#### 4.2.9.6 Test Resultaat

![Img](./media/4top.png)

Na het branden van de code, plaatst u het micro:bit board in de sleuf van de gamepad (**batterijen geïnstalleerd**), en zet u de schakelaar op "ON".

Upload deze codes naar respectievelijk twee Micro:bit boards van de gamepad en van de auto, en zorg ervoor dat de batterijen voldoende zijn opgeladen. Plaats de corresponderende Micro:bit in de gamepad en de auto en zet de schakelaars op beide op "ON".

Nu kunt u de auto besturen met de gamepad: duw de joystick omhoog en de auto beweegt vooruit, duw hem omlaag om achteruit te bewegen, links draait hem naar links, en rechts draait hem naar rechts. We kunnen de auto ook versnellen (druk op knop E)/vertragen (druk op knop F), links verschuiven (C) en rechts verschuiven (D). Let op dat het snelheidsbereik 20–95 is.

![Img](./media/9000.gif)

<span style="color: rgb(0, 209, 0);">**Tip:** Als er geen reactie is op het board, druk dan op de resetknop aan de achterkant van het micro:bit board.</span>

![Img](./media/4bottom.png)
