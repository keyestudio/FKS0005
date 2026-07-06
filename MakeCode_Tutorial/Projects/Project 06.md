### 4.2.6 Steen-Papier-Schaar

#### 4.2.6.1 Overzicht

![Img](./media/top1.png)

Hierin spelen we steen-papier-schaar via draadloze communicatie van de micro:bit. Spelers kiezen hun zet (steen, papier of schaar) via de knoppen, met gegevensuitwisseling tussen apparaten. Het spel volgt een best-of-three; als alle drie de rondes eindigen in een gelijkspel of winst-verlies-gelijkspel, wordt een vierde wedstrijd geactiveerd.

Elke uitkomst wordt weergegeven op de micro:bit matrix (W voor winst, L voor verlies, = voor gelijkspel) en onthuld door de RGB-lampjes (groen voor winst, rood voor verlies, geel voor gelijkspel) op pin P8. Na voltooiing van een ronde resetten de twee apparaten alle gegevens en lampjes, ter voorbereiding op de volgende wedstrijd.

De gameplay integreert naadloos draadloze interactie met de meer-ronde gevechten.

![Img](./media/bottom1.png)

#### 4.2.6.2 Component Kennis

![Img](./media/2top.png)

**Microbit draadloze communicatie**

![Img](./media/6001.png)

Het micro:bit board integreert twee handige draadloze communicatiemogelijkheden: **2.4GHz radio** en **low-power Bluetooth (BLE)**. Ze kunnen echter niet gelijktijdig worden gebruikt.

De eerste vereist geen koppeling en ondersteunt tot 255 onafhankelijke pakketten om interferentie te minimaliseren, met een communicatiebereik van 10-30 meter, waardoor snelle overdracht van digitale gegevens en strings mogelijk is. De laatste wordt voornamelijk gebruikt voor koppeling met smartphones, tablets en andere slimme apparaten voor IoT-toepassingen zoals het uploaden van sensorgegevens en afstandsbediening via mobiele apps.

Ze breiden de creatieve ontwikkelingsmogelijkheden van de micro:bit uit.

#### 4.2.6.3 Benodigde Onderdelen

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 board** (zelf meegeleverd) ×2 | **micro:bit Smart Gamepad** (gemonteerd) ×2 |**AAA batterij** (zelf meegeleverd) ×8 |

#### 4.2.6.4 Code Stroom

![Img](./media/6002.png)

#### 4.2.6.5 Test Code

**Volledige code:**

![Img](./media/6003.png)

![Img](./media/line1.png)

**Korte uitleg:**

① Initialiseer de radio en stel de groep in op \'1\'; stel het aantal rondes, status, tegenstander en de steen-papier-schaar resultaten van de spelers in; verbind de vier RGB-lampjes met pin P8 en ververs het display, stel de matrix in om ![Img](./media/6004.png) te tonen.

![Img](./media/6005.png)

② Bepaal de uitkomst van de huidige ronde: als uw keuze overeenkomt met die van de tegenstander (**1/2/3 voor schaar/steen/papier**), is het een gelijkspel; anders, selecteer een winnaar (schaar tegen papier tegen steen tegen schaar), ronde waarde +1 en sla het resultaat op.

![Img](./media/6006.png)

③ Sla de resultaten op in een array en toon de corresponderende string. Als dit het derde spel is, bepaal dan of een vierde spel nodig is (bij een volledig gelijkspel of winst-verlies-gelijkspel). Zo ja, toon "FINAL" en wacht 1 seconde voordat de steen-papier-schaar selectie wordt gewist.

![Img](./media/6007.png)

Anders, toon "WINNER" voor overwinning, "LOSER" voor nederlaag, en "TIE" voor een gelijkspel. Na een vertraging van 3 seconden, roep de resetGame functie aan om alle spelvariabelen te wissen.

Als de wedstrijd uit vier spellen bestaat, toon dan "GAME OVER" en roep de resetGame functie opnieuw aan na een vertraging van 3 seconden om alle spelvariabelen te resetten.

![Img](./media/6008.png)

Als het spel niet voorbij is, toont het ![Img](./media/6004.png) en wist het de keuzes van beide.

![Img](./media/6009.png)

④ Druk op C en het board stuurt "1" als schaar, en de matrix toont ![Img](./media/6011.png); druk op D en het board stuurt "3" als papier, en de matrix toont ![Img](./media/6012.png); Druk op E en het stuurt "2" als steen en toont ![Img](./media/6013.png).

![Img](./media/6010.png)

⑤ Ontvang radio gegevens (keuze van de tegenstander).

![Img](./media/6014.png)

⑥ Bepaal of een vierde ronde nodig is. Als alle drie de spellen eindigen in een volledig gelijkspel of winst-verlies-gelijkspel, is een vierde spel noodzakelijk; anders is het niet nodig.

![Img](./media/6015.png)

⑦ De RGB-lampjes tonen de corresponderende kleuren op basis van de uitkomst: groen voor overwinning, rood voor nederlaag, en geel voor een gelijkspel.

![Img](./media/6016.png)

⑧ Wanneer het spel eindigt, wis dan de weergave van de vier RGB-lampjes.

![Img](./media/6017.png)

⑨ Reset de spelstatus, wis alle spelvariabele waarden, reset de RGB-lampjes, en toon ![Img](./media/6004.png).

![Img](./media/6018.png)

#### 4.2.6.6 Test Resultaat

![Img](./media/4top.png)

Na het branden van de code, plaatst u het micro:bit board in de sleuf van de gamepad (**batterijen geïnstalleerd**), en zet u de schakelaar op "ON".

De matrix toont aanvankelijk ![Img](./media/6004.png). Spelers drukken op knoppen om hun zet te kiezen (E voor steen, D voor papier, of C voor schaar), met uitwisseling van wedstrijdgegevens tussen de twee apparaten. Ze bepalen de uitkomst van de huidige ronde: een overwinning wordt aangegeven door de "W" met groen RGB-licht, een gelijkspel door de "=" met geel licht, en een verlies door de "L" met rood (het eerste RGB-licht gaat aan na de eerste ronde, enzovoort). De volgende ronde volgt als het spel nog niet voorbij is.

Het spel hanteert een best-of-three: als alle drie de rondes eindigen in een volledig gelijkspel of winst-verlies-gelijkspel, wordt een vierde wedstrijd geactiveerd.

Als er na drie rondes een winnaar is, wordt "WINNER" weergegeven voor overwinning en "LOSER" voor nederlaag. Zodra het resultaat wordt getoond, verschijnt "GAME OVER" om het spel te resetten. Als de vierde ronde onbeslist blijft, is het spel ook voorbij.

![Img](./media/6000.gif)

<span style="color: rgb(0, 209, 0);">**Tip:** Wacht tot het hartpictogram verschijnt voordat u doorgaat met de volgende ronde. Als er geen reactie is op het board, druk dan op de resetknop aan de achterkant van het micro:bit board.</span>

![Img](./media/4bottom.png)
