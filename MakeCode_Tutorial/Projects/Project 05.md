### 4.2.5 Vermijd Bakstenen

#### 4.2.5.1 Overzicht

![Img](./media/top1.png)

In dit project spelen we een baksteen-vermijdingsspel waarbij spelers een Micro:bit gamepad gebruiken om hun LED-indicator naar links en rechts te bewegen terwijl ze vallende bakstenen ontwijken. Er zijn drie staten: a) een dynamisch pictogram bij het opstarten, b) real-time vermijdingsacties tijdens het spelen, en c) een eindscore na botsingen.

Spelers verdienen 1 punt na elke ontwijking (wanneer de baksteen de onderkant bereikt), en het spel is voorbij wanneer ze botsen met een baksteen; de eindscore wordt weergegeven met een scrolleffect.

Het spel kan worden gestart of gereset door zowel A+B in te drukken. Dit eenvoudige gameplay-mechanisme combineert real-time responsiviteit met strategische anticipatie.

![Img](./media/bottom1.png)

#### 4.2.5.2 Benodigde Onderdelen

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 board** (zelf meegeleverd) ×1 | **micro:bit Smart Gamepad** (gemonteerd) ×1 |**AAA batterij** (zelf meegeleverd) ×4 |

#### 4.2.5.3 Code Stroom

![Img](./media/5001.png)

#### 4.2.5.4 Test Code

⚠️ **Let op: de initiële drempelwaarde 300 in de code kan naar behoefte worden aangepast. Hoe hoger de waarde, hoe langzamer de baksteen zal vallen.**

**Volledige code:**

![Img](./media/5002.png)

![Img](./media/line1.png)

**Korte uitleg:**

① Initialiseer gerelateerde variabelen, inclusief de initiële kolom, rij en snelheid van de baksteen van de speler, en stel de positie van de speler in op de initiële kolom.

Roep een on_start functie aan.

![Img](./media/5003.png)

② Wat deze functie betreft, deze zorgt ervoor dat de baksteen aan het begin van het spel in een willekeurige kolom van 0~4 verschijnt.

![Img](./media/5004.png)

③ Bepaal of "A+B is ingedrukt en het spel niet is gestart". Zo ja, en het opstarten is gemarkeerd als een initiële staat, markeer dan eerst de opstartstaat en bevestig opnieuw of de knoppen na een korte vertraging nog steeds zijn ingedrukt. Zo ja, reset het spel (roep de reset_game functie aan) en registreer de tijd. Anders, annuleer de opstartmarkering.

![Img](./media/5005.png)

④ De volgende functie reset het spel naar de initiële staat. Het stelt de staat in op "gaming" (game_state=1) en plaatst de speler op de initiële positie. En de baksteen verschijnt in een willekeurige kolom (0~4) en de 0e rij, en de scores worden nul. Ten slotte wordt het indrukken van A/B gemarkeerd als niet geactiveerd, en de matrix wordt vervolgens gewist.

![Img](./media/5006.png)

⑤ Wanneer de spelstatus **0-initiële staat** is (niet aan het spelen na het inschakelen), zal het weergegeven pictogram knipperen.

![Img](./media/5007.png)

⑥ Wanneer het **2-game over** is, wordt de score gecontroleerd volgens het knipperen (flash_count). Als de telling <3 is, herhaalt het "toon score → korte vertraging → wis display → korte vertraging → telling+1"; wanneer de telling 3 bereikt, toont het altijd de score en verlengt het de vertraging.

![Img](./media/5008.png)

⑦ In de **1-gaming** staat, wanneer u C indrukt zonder de drukmarkering te activeren en de spelerskolom > 0 is, wordt de spelerskolom -1 en wordt knop C gemarkeerd als geactiveerd (met vertraging om jitter te voorkomen); druk op E zonder te activeren en wanneer de spelerskolom < 4 is, en de kolom +1 met E wordt geactiveerd (vertaging); als er geen actie wordt uitgevoerd, wordt de activeringsmarkering van de corresponderende knoppen gereset.

![Img](./media/5009.png)

⑧ Bereken het verschil tussen de huidige tijd en de tijd van de laatste baksteenbeweging. Als dit verschil de drempelwaarde voor de baksteensnelheid overschrijdt, werk dan de baksteenbewegingstijd en de baksteenrij +1 bij. Als de rij > 4 is (de grens bereikt), reset de baksteen dan naar een willekeurige kolom met zijn rij=nul, en score+1.

Roep de botsingsdetectie- en spelgrafische weergavefuncties aan om bakstenen te laten vallen, te resetten na het bereiken van de grens, score te verzamelen en de spelstatus in real-time bij te werken.

Roep de botsingsdetectie- en spelgrafische weergavefuncties aan om automatische baksteenbeweging, grensreset, scoreaccumulatie en real-time spelstatusupdates te realiseren.

![Img](./media/5010.png)

⑨ Bepaal of het spel voorbij is: het controleert eerst of "de baksteenkolom overeenkomt met die van de speler" en "of de baksteenrij overeenkomt met die van de speler". Als aan beide voorwaarden is voldaan (d.w.z. de bakstenen overlappen met de speler), stel het spel dan in op staat 2 (game over), wis het display en reset de knipperteller.

"Game over bij botsing."

![Img](./media/5011.png)

⑩ Render spelvisuals: het wist eerst het display en tekent vervolgens punten met een helderheid van 255 (Speler) op de vaste rij en huidige kolomposities van de speler; als het spel is gestart (game_state=1), tekent het punten met een helderheid van 85 (baksteen) op de rij en kolom van de baksteen. Zo kunnen we bakstenen van de speler onderscheiden op basis van hun helderheid.

![Img](./media/5012.png)

#### 4.2.5.5 Test Resultaat

![Img](./media/4top.png)

Na het branden van de code, plaatst u het micro:bit board in de sleuf van de gamepad (**batterijen geïnstalleerd**), en zet u de schakelaar op "ON".

Het bevindt zich in **0-initiële staat** na het inschakelen en de matrix knippert twee vierkante pictogrammen.

Druk op A en B (gedurende ten minste 1 seconde) om het spel te starten (in **1-gaming** staat), en een baksteen zal in een willekeurige kolom vallen. Nu kunt u naar links/rechts bewegen door op C/E te drukken. Elke keer dat u een baksteen ontwijkt, score+1.

Game over bij botsing (**2-game over**), en de eindscore wordt weergegeven op de matrix. Als u nog een ronde wilt spelen, drukt u opnieuw op A en B. Schakel uit om het spel te verlaten (zet de DIP-schakelaar op "OFF").

![Img](./media/5000.gif)

<span style="color: rgb(0, 209, 0);">**Tip:** Als er geen reactie is op het board, druk dan op de resetknop aan de achterkant van het micro:bit board.</span>

![Img](./media/4bottom.png)
