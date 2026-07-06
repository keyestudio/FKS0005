### 4.2.4 Muziekspeler

#### 4.2.4.1 Overzicht

![Img](./media/top1.png)

Hier bouwen we een muziekspeler die geluid genereert via de ingebouwde buzzer op het micro:bit-bord (speelt geen vocale muziek). Het beschikt over een bibliotheek van 20 korte nummers en ondersteunt zowel sequentiële als willekeurige weergave.

In de sequentiële modus schakelt het indrukken van knop C (Vorig nummer) of E (Volgend nummer) nummers volgens een vooraf ingestelde volgorde totdat het einde van de lijst is bereikt; terwijl in de willekeurige modus elke druk een nummer willekeurig selecteert uit de 20 geluiden met knipperende kleurenlichten, en wanneer een nummer is afgelopen, stopt het onmiddellijk.

Ondertussen toont de micro:bit LED-matrix de huidige afspeelmodus in realtime.

![Img](./media/bottom1.png)

#### 4.2.4.2 Benodigde onderdelen

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2-bord** (zelf meegebracht) ×1 | **micro:bit Smart Gamepad** (gemonteerd) ×1 |**AAA-batterij** (zelf meegebracht) ×4 |

#### 4.2.4.3 Codestroom

![Img](./media/4001.png)

#### 4.2.4.4 Testcode

**Volledige code:**

![Img](./media/4002.png)

![Img](./media/line1.png)

**Korte uitleg:**

① Initialiseer de LED-matrix en het geluidsvolume, verbind de RGB-pin met P8 en stel het aantal RGB in op 4.

![Img](./media/4003.png)

② Initialiseer de array van melodieën op 20 en voeg hun gedetailleerde nummers toe, en stel het initiële volume in.

![Img](./media/4004.png)

③ Bepaal of knop D of F is ingedrukt. Druk op D voor '0-sequentiële weergave', F voor '1-willekeurige weergave'.

![Img](./media/4005.png)

④ In de sequentiële modus, druk op C om het vorige nummer af te spelen, E om naar het volgende nummer te gaan.

![Img](./media/4006.png)

Aangezien er slechts 20 nummers in de array zijn, kan alleen muziek van N.O. 0-19 worden afgespeeld. Daarom voegen we een if-conditie toe om overschrijdingen en onderschrijdingen van de array te voorkomen.

![Img](./media/4007.png)

Echter, in de willekeurige modus, druk op C/E om al deze 20 nummers te schudden.

![Img](./media/4008.png)

⑤ Bepaal of het vorige nummer inconsistent is met het huidige. Zo ja, stop dan eerst het huidige en speel dan dat nummer af.

![Img](./media/4009.png)

⑥ Controleer of de modus '0-sequentiële weergave' is, met '![Img](./media/4010.png)', of '1-willekeurige weergave', met '![Img](./media/4011.png)', met een vertraging van 100ms.

![Img](./media/4012.png)

⑦ Laat de RGB-lampjes op de achtergrond ademen.

![Img](./media/4013.png)

⑧ Druk op A om het volume te verhogen (+10); druk op B om het te verlagen (-10). Het volume van de micro:bit-buzzer wordt bepaald door de uitgangsspanning van de intern aangesloten pin. We kunnen het volume regelen door digitale waarden 0~255 om te zetten in analoge waarden via DAC.

![Img](./media/4014.png)

#### 4.2.4.5 Testresultaat

![Img](./media/4top.png)

Na het branden van de code, plaatst u het micro:bit-bord in de sleuf van de gamepad (**batterijen geïnstalleerd**), en zet u de schakelaar op "ON".

Na het inschakelen bevindt het zich standaard in de sequentiële modus en speelt het het nummer op N.O. "0" af. Wanneer het is afgelopen, kunt u op C drukken voor het vorige nummer of op E voor het volgende.

Druk op F om over te schakelen naar de willekeurige modus. En u kunt op D drukken om terug te gaan naar de sequentiële modus. In de F-modus wordt een willekeurig nummer van deze 20 afgespeeld als u op C/E drukt. Na afloop stopt het.

De RGB-lampjes ademen altijd vanaf het moment van inschakelen. Ondertussen toont de micro:bit LED-matrix “![Img](./media/4010.png)” in de sequentiële modus en “![Img](./media/4011.png)” in de willekeurige modus.

Voor het volume, druk op A om te verhogen en B om te verlagen.

![Img](./media/4015.gif)

<span style="color: rgb(0, 209, 0);">**Tip:** Als er geen reactie is op het bord, druk dan op de resetknop aan de achterkant van het micro:bit-bord.</span>

![Img](./media/4bottom.png)
