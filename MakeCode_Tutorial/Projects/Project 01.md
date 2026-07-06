### 4.2.1 Richtingaanwijzer

#### 4.2.1.1 Overzicht

![Img](./media/top1.png)

Wanneer u de joystick beweegt, toont de puntmatrix in realtime pijlen in de overeenkomstige richting: links, rechts, omhoog, omlaag, waardoor u een duidelijke richtingreferentie krijgt.

![Img](./media/bottom1.png)

#### 4.2.1.2 Componentkennis

![Img](./media/2top.png)

**Micro:bit puntmatrix:**

![Img](./media/1001.png)

De LED-puntmatrix van het micro:bit-bord bestaat uit in totaal 25 lichtgevende diodes, een groep van 5, corresponderend met as X en Y, die een 5×5 matrix vormen. Elk is geplaatst op het snijpunt van de rij (X) en de kolom (Y). We kunnen een of enkele ervan bedienen door de coördinatenpunten in te stellen.

**Joystick:**

| ![Img](./media/1002.png)| ![Img](./media/1003.png) |
| :--: | :--: |
| Werkelijk product | Schematisch diagram |

De interne kernstructuur van deze joystick is samengesteld uit twee instelbare weerstanden (potentiometers) met elk een weerstandswaarde van 10KΩ.

Het detecteert richtingen (en amplitude) van de druk via de ADC analoge pin van de microcontroller om de analoge elektrische signalen van de overeenkomstige dimensie uit te voeren. Tijdens het daadwerkelijk uitlezen van signalen, wanneer de analoge waarden van de joystick X- en Y-assen worden gedetecteerd binnen het bereik van 450~600, kan worden vastgesteld dat de joystick zich in een neutrale (stationaire) toestand bevindt zonder actieve beweging.

![Img](./media/2bottom.png)

#### 4.2.1.3 Benodigde onderdelen

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png)|
| :--: | :--: | :--: |
| **micro:bit V2-bord** (zelf meegebracht) ×1 | **micro:bit Smart Gamepad** (gemonteerd) ×1 |**AAA-batterij** (zelf meegebracht) ×4 |


#### 4.2.1.4 Codestroom

![Img](./media/1008.png)

#### 4.2.1.5 Testcode

⚠️ **Let op dat de volgende codes de Makecode-bibliotheken van de Gamepad bevatten (de manier om bibliotheken toe te voegen is eerder vermeld). De gevoeligheid van de joystick kan naar behoefte worden aangepast.**

**Volledige code:**

![Img](./media/1004.png)


![Img](./media/line1.png)

**Korte uitleg:**

① Initialiseer de LED-matrix om ![Img](./media/1006.png) te tonen.


![Img](./media/1005.png)


② Lees de waarden van de X- en Y-as om de bewegingsrichting te bepalen. Indien gedetecteerd, toont de matrix de overeenkomstige pijl. Zo niet, dan wordt ![Img](./media/1006.png) weergegeven.

![Img](./media/1007.png)


#### 4.2.1.6 Testresultaat

![Img](./media/4top.png)

Na het branden van de code, plaatst u het micro:bit-bord in de sleuf van de gamepad (**batterijen geïnstalleerd**), en zet u de schakelaar op "ON".

Wanneer u de joystick van de gamepad beweegt, ziet u de overeenkomstige pijlen op de matrix. Als u uw vinger optilt om deze terug naar het midden te brengen, verschijnt er een huispictogram op de matrix.

![Img](./media/1009.gif)

<span style="color: rgb(0, 209, 0);">**Tip:** Als er geen reactie is op het bord, druk dan op de resetknop aan de achterkant van het micro:bit-bord.</span>

![Img](./media/4bottom.png)
