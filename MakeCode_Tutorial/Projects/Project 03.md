### 4.2.3 Eenvoudige Elektronische Piano

#### 4.2.3.1 Overzicht

![Img](./media/top1.png)

In dit project besturen we de micro:bit-luidspreker om verschillende tonen af te spelen door de joystick te bewegen en op de knoppen te drukken. Ondertussen zal de ingebouwde LED-matrix overeenkomstige nummers tonen.

De joystick naar rechts draaien produceert "Do (Toon Centrale C)" met de weergave "1"; naar links draaien produceert "Re (Toon D)" met "2"; naar boven draaien produceert "Mi (Toon E)" met "3"; naar beneden draaien produceert "Fa (Toon F)" met "4". Op knop C drukken produceert "Sol (Toon G)" met "5", op D drukken produceert "La (Toon A)" met "6", E produceert "Si (Toon B)" met "7", en op F drukken produceert een hogere "Do(Sharp)" terwijl de weergave terugkeert naar "1". Er is een mooie synchronisatie van de joystick, knoppen, tonen en weergave.

![Img](./media/bottom1.png)

#### 4.2.3.2 Componentkennis

![Img](./media/2top.png)

**Microbit luidspreker**

![Img](./media/j901.png)

Het micro:bit-bord beschikt over een ingebouwde luidspreker voor het maken van geluid, zoals gegiechel, begroetingen, geeuwen of uitingen van verdriet, of zelfs het componeren van een lied. Door te programmeren kan het zelfs individuele noten, melodieën en ritmes genereren, of zelfs muzikale composities, zoals het lied *Twinkle Twinkle Little Star*.

![Img](./media/2bottom.png)

#### 4.2.3.3 Benodigde onderdelen

| **micro:bit V2-bord** (zelf meegebracht) ×1 | **micro:bit Smart Gamepad** (gemonteerd) ×1 |**AAA-batterij** (zelf meegebracht) ×4 |
| :--: | :--: | :--: |
| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |

#### 4.2.3.4 Codestroom

![Img](./media/3009.png)

#### 4.2.3.5 Testcode

⚠️ **Let op dat de gevoeligheid van de joystick naar behoefte kan worden aangepast.**

**Volledige code:**

![Img](./media/3008.png)

![Img](./media/line1.png)

**Korte uitleg:**

① Initialiseer de micro:bit LED-matrix om ![Img](./media/3004.png) te tonen.

![Img](./media/3005.png)

② Bepaal de richting van de joystickbeweging; speel de overeenkomstige tonen een halve tel op de achtergrond, en de LED-matrix toont het overeenkomstige nummer.

![Img](./media/3006.png)

③ Controleer of een knop is ingedrukt, en speel de overeenkomstige toon een halve tel op de achtergrond, en de LED-matrix toont het overeenkomstige nummer.

![Img](./media/3007.png)


#### 4.2.3.6 Testresultaat

![Img](./media/4top.png)

Na het branden van de code, plaatst u het micro:bit-bord in de sleuf van de gamepad (**batterijen geïnstalleerd**), en zet u de schakelaar op "ON". De LED-matrix toont eerst “![Img](./media/3004.png)”.

De joystick naar rechts draaien produceert "Do (Toon Centrale C)" met de weergave "1"; naar links draaien produceert "Re (Toon D)" met "2"; naar boven draaien produceert "Mi (Toon E)" met "3"; naar beneden draaien produceert "Fa (Toon F)" met "4". Op knop C drukken produceert "Sol (Toon G)" met "5", op D drukken produceert "La (Toon A)" met "6", E produceert "Si (Toon B)" met "7", en op F drukken produceert een hogere "Do(Sharp)" terwijl de weergave terugkeert naar "1".

U hebt de eenvoudige elektronische piano gebouwd!

![Img](./media/3010.gif)

<span style="color: rgb(0, 209, 0);">**Tip:** Als er geen reactie is op het bord, druk dan op de resetknop aan de achterkant van het micro:bit-bord.</span>

![Img](./media/4bottom.png)
