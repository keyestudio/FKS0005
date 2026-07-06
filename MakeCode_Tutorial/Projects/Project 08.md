### 4.2.8 Raad het Getal

#### 4.2.8.1 Overzicht

![Img](./media/top1.png)

In dit project spelen we een raadspel met een Micro:bit board, een gamepad-besturingsbord en een OLED-display. Wanneer het juiste getal is geraden, toont de OLED "Great!!!"; als de gok te hoog of te laag is, toont het respectievelijk "To High!"/"To Low!", samen met het corresponderende bereik van mogelijke getallen.

![Img](./media/bottom1.png)

#### 4.2.8.2 Component Kennis

Dit project gebruikt hetzelfde OLED-display als Project 07. Raadpleeg sectie 4.2.7.2 voor de componentkennis.

#### 4.2.8.3 Benodigde Onderdelen

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 board** (zelf meegeleverd) ×1 | **micro:bit Smart Gamepad** (gemonteerd) ×1 |**AAA batterij** (zelf meegeleverd) ×4 |
|![Img](./media/OLED.png)|![Img](./media/7008.png)|||
|**OLED display** (zelf meegeleverd)×1 |**F-F DuPont draad**(zelf meegeleverd) x4||

#### 4.2.8.4 Bedradingsschema

![Img](./media/jiexian8.png)

**Na de bedrading zoals hierboven weergegeven, plaatst u de micro:bit in de sleuf op het gamepad-besturingsbord.**

| OLED-display | micro:bit gamepad-besturingsbord | micro:bit board pin |
| :--: | :--: | :--: |
| GND | GND | GND |
| VCC | 3V | 3V |
| SDA | SDA | P20 |
| SCL | SCL | P19 |

#### 4.2.8.5 Code Stroom

![Img](./media/8001.png)

#### 4.2.8.6 Test Code

⚠️ **Let op dat hier de OLED-bibliotheek is opgenomen, dus we moeten importeren: https://github.com/keyestudio/pxt-environment-kit-master**.

**Volledige code:**

![Img](./media/8002.png)

![Img](./media/line1.png)

**Korte uitleg:**

① Initialiseer de schermupdate-vlagbit, stel de modusvariabele in op 0 (0-spel klaar, 1-spel actief), en initialiseer de OLED-schermweergave.

![Img](./media/8003.png)

② Tijdens de spelvoorbereiding, stel het gokbereik, de initiële gokwaarde, de doelwaarde en de gok in.

![Img](./media/8004.png)

③ Werk het waardebereik en de gokwaarde op de OLED bij. Toon corresponderende prompts wanneer de statusvlagbit van het resultaat verandert: "To High!" wanneer state=1; "To Low!" wanneer state=2; en "Great!!!" wanneer state=3.

En stel de modus in op spel klaar en wacht 1000 milliseconden (1s).

![Img](./media/8005.png)

④ Druk op C en de gokwaarde temp+1; als de gokwaarde het maximum overschrijdt, stel deze dan in als het nieuwe maximum.

Druk op E en de gokwaarde temp-1; als de gokwaarde kleiner is dan het minimum, stel deze dan in als het nieuwe minimum.

![Img](./media/8006.png)

⑤ Druk op D om de gokwaarde te vergelijken met de doelwaarde. Als temp groter is, registreer dan het nieuwe maximum max2 en ga naar Staat 1; als temp kleiner is, registreer dan het nieuwe minimum min2 en ga naar Staat 2; als beide waarden gelijk zijn, ga dan naar Staat 3.

Werk ten slotte het display bij met een vertraging van 1000 milliseconden.

![Img](./media/8007.png)

#### 4.2.8.7 Test Resultaat

![Img](./media/4top.png)

Na het branden van de code, plaatst u het micro:bit board in de sleuf van de gamepad (**batterijen geïnstalleerd**), en zet u de schakelaar op "ON".

Na het uploaden van de code, initialiseert de OLED en toont het waardebereik van "num: 1 ~ 100" en de initiële gok van 50. U kunt op C drukken om temp+1 (max van 100) of op E om temp-1 (min van 1) te wijzigen om uw gokwaarde op de OLED te veranderen.

Druk op D om uw waarde in te dienen, en temp zal worden vergeleken met de willekeurige doelwaarde. Als temp>value, toon "To High!" en wijs temp toe aan max2; als temp<value, toon "To Low!" en wijs het toe aan min2. Als u geluk heeft dat temp=value, ziet u "Great!!!" gedurende 1s.

Daarna wordt het spel gereset en wordt een nieuwe doelwaarde ingesteld. Laten we nog een ronde spelen!

![Img](./media/8000.gif)

⚠️ **De bouwsteen in Test Resultaat is niet inbegrepen in deze productkit.**

<span style="color: rgb(0, 209, 0);">**Tip:** Als er geen reactie is op het board, druk dan op de resetknop aan de achterkant van het micro:bit board.</span>

![Img](./media/4bottom.png)
