### 4.2.2 Kleurrijke Lichten

#### 4.2.2.1 Overzicht

![Img](./media/top1.png)

RGB LED's zijn een type LED-lichtbron dat beelden creëert door licht te mengen van de drie primaire kleuren: rood, groen en blauw, waarvan de intersectie verschillende tinten produceert. Gangbare methoden omvatten directe menging van de primaire kleuren, het gebruik van een blauwe LED gecombineerd met gele fosfor, of het gebruik van een ultraviolette LED samen met RGB-fosfor. Vergeleken met LED's die direct wit licht uitstralen, bieden RGB LED's een breder scala aan kleurmengmogelijkheden omdat de drie primaire kleuren onafhankelijk kunnen worden geregeld.

In dit project komt elke knop overeen met een andere modus van de RGB LED's. Wanneer knop C wordt ingedrukt, knipperen de lichten afwisselend in de volgorde van "rood, groen, blauw, geel en paars"; Druk op D om over te schakelen naar ademende lichten; Druk op E voor waterstromende lichten; Druk op F voor markeerlichten.

Kleurrijke lichtslingers voor festivaldecoraties, kerstboomverlichting, RGB-strips voor dagelijkse sfeer, LED-decoratieve verlichting in pretparken en winkelcentra... Dit zijn allemaal veelvoorkomende voorbeelden van multi-mode verlichting in ons dagelijks leven.

![Img](./media/bottom1.png)

#### 4.2.2.2 Componentkennis

![Img](./media/2top.png)

**SK6812 RGB LED**

| ![Img](./media//2001.png)| ![Img](./media//2002.png)|
| :--: | :--: |
| Werkelijk product | Schematisch diagram |

De SK6812 is een extern gestuurde LED-lichtbron die besturings- en verlichtingscircuits integreert. Het belangrijkste onderdeel zijn 5x5mm oppervlakte-verlichte LED-kralen, elk functionerend als een onafhankelijke pixel die meerdere kerncircuits omvat: een slim digitaal interface-datalatchcircuit, signaalvormings- en versterkingsaandrijfcircuit, stroomregelcircuit, ingebouwd constant-stroomcircuit en een zeer nauwkeurige RC-oscillator.

De communicatie maakt gebruik van een enkelpolig nul-retourcode-protocol. Bij inschakelen/reset ontvangt elke pixel gegevens van de controller via de DIN-poort. De eerste 24 bits aan gegevens worden door de initiële pixel geëxtraheerd en opgeslagen in de interne datalatch, terwijl de resterende bits intern worden gevormd en versterkt voordat ze via de DOUT-poort naar volgende pixels worden verzonden. Met elke verwerkte pixel neemt de grootte van het verzonden signaal met 24 bits af.

Op de gamepad bevinden zich vier SK6812 RGB-lampjes. Deze ondersteunen allemaal 256-niveau helderheidsaanpassing over hun rode, groene en blauwe kanalen, waardoor 256×256×256 kleurencombinaties mogelijk zijn. Hierdoor levert het diverse lichteffecten zoals afwisselende flitsen, ademende gradiënten en scrollende animaties, wat intuïtievere en levendigere interacties biedt.

**Knop**

| ![Img](./media//2003.png)| ![Img](./media//2004.png)|
| :--: | :--: |
| Werkelijk product | Schematisch diagram |

De knop, voor het eerst verschenen in Japan, werd aangeduid als een gevoelige schakelaar. Tijdens de bediening drukt men op de schakelaar om kracht uit te oefenen om het circuit te sluiten. Bij het loslaten van de druk opent de schakelaar. De interne metalen veer verandert van staat (verbonden/losgekoppeld) als reactie op de uitgeoefende kracht.

Er zijn vier knoppen, elk onafhankelijk verbonden met een pin op het micro:bit-bord. Wanneer een knop wordt ingedrukt, genereert het circuit een overeenkomstig laag niveau signaal, waardoor de micro:bit snel kan reageren op commando's en het interactiegemak en de nauwkeurigheid aanzienlijk worden verbeterd.

![Img](./media/2bottom.png)

#### 4.2.2.3 Benodigde onderdelen

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2-bord** (zelf meegebracht) ×1 | **micro:bit Smart Gamepad** (gemonteerd) ×1 |**AAA-batterij** (zelf meegebracht) ×4 |

#### 4.2.2.4 Codestroom

![Img](./media/2006.png)

#### 4.2.2.5 Testcode

⚠️ **Let op dat de vertragingstijd van de MODE\*_DELAY in de codes kan worden aangepast aan uw behoeften.**

**Volledige code:**

![Img](./media/2005.png)

![Img](./media/line1.png)

**Korte uitleg:**

① Schakel in het begin de functie van de LED's uit (zet led enable op false).

En definieer 4 LED-vertragingen (zeg, zet 5 in modus 2, zet 500 in modus 1...), stel knop debounce in op 20. Initialiseer vier RGB LED's op pin P8 op geen kleur (zet alle waarden op 0), d.w.z. zet ze uit.

![Img](./media/2009.png)

② Tijdens de lus wordt een anti-jitter-bewerking geïmplementeerd door te controleren of het verschil tussen de huidige uitvoeringstijd en de vorige druktijd de vooraf ingestelde anti-jitter-drempel (BTN_DEBOUNCE) overschrijdt, waardoor herhaalde drukken veroorzaakt door fysieke jitter worden voorkomen.


![Img](./media/2010.png)


③ Wanneer de C(/D/E/F) wordt ingedrukt, wordt de modus ingesteld op 1(2/3/4), terwijl de animatiestappen en timingstartpunten voor de overeenkomstige modus worden gereset, de lichten worden gewist en de knop-tijdstempel wordt bijgewerkt. Dit maakt nauwkeurig schakelen en initiële bediening van verschillende LED-modi mogelijk.


| ![Img](./media/2011.png)|![Img](./media/2012.png)|
| :--: | :--: |
|Knop C is ingedrukt|Knop D is ingedrukt|
| ![Img](./media/2013.png) | ![Img](./media/2014.png) |
|Knop E is ingedrukt|Knop F is ingedrukt|

④ Wanneer de modus is ingesteld op 1 en het interval tussen de huidige tijd en de vorige modustijd MODE1Delay overschrijdt, werk dan eerst de modustijdstempel bij en toon de lichten op basis van de verschillende waarden van model_step (0–4) in volgorde: rood, groen, blauw, geel en paars. Na het vernieuwen van de weergave, reset de model_step-lus door een modulo-bewerking om deze vijf kleuren regelmatig te veranderen.

![Img](./media/2015.png)

⑤ Wanneer de modus 2 is en het interval tussen de huidige tijd en de vorige modustijd MODE2_DELAY overschrijdt, werk dan eerst de modustijdstempel bij en verhoog de kleurwaarde (tint) cyclisch met modulo (bereik 0–359). Wis vervolgens het licht en toon de overeenkomstige tint met hoge verzadiging (99) en lage helderheid (20), en de gradiëntkleuren zullen vloeiend veranderen. (De helderheids- en verzadigingswaarden in de codes kunnen naar behoefte worden aangepast.)

![Img](./media/2016.png)

⑥ Wanneer de modus 3 is en het interval tussen de huidige tijd en de vorige modustijd MODE3_DELAY overschrijdt, werk dan eerst de modustijdstempel bij en verschuif alle pixels van de lichtstrip met 1 bit, wijs een willekeurige tint (0–359), hoge verzadiging (99) en lage helderheid (20) toe aan de 0e pixel. Vernieuw de weergave en u ziet een stromend licht: Lichten bewegen sequentieel en veranderen willekeurig van kleur. (De helderheids- en verzadigingswaarden in de code kunnen naar behoefte worden aangepast.)

![Img](./media/2017.png)

⑦ Wanneer de modus 4 is en het interval tussen de huidige tijd en de vorige modustijd MODE4_DELAY overschrijdt, werk dan eerst de modustijdstempel bij en wis de lichtstrip, wijs een willekeurige tint (0–359), hoge verzadiging (99) en lage helderheid (20) toe aan de pixels die overeenkomen met model_step, en vernieuw de weergave. Tenslotte, doorloop model_step binnen 0-3 via modulo, en u zult zien dat enkele LED's sequentieel in willekeurige kleuren aangaan. (De helderheids- en verzadigingswaarden in de code kunnen naar behoefte worden aangepast.)

![Img](./media/2018.png)

#### 4.2.2.6 Testresultaat

![Img](./media/4top.png)

Na het branden van de code, plaatst u het micro:bit-bord in de sleuf van de gamepad (**batterijen geïnstalleerd**), en zet u de schakelaar op "ON".

Druk op **C**: de lichten wisselen af tussen **rood-groen-blauw-geel-paars** in volgorde.

Druk op **D**: de kleurtint van de lichten zal toenemen, en uiteindelijk zullen de gradiëntkleuren vloeiend veranderen.

Druk op **E**: de lichten genereren een willekeurige kleur beginnend bij de 0e pixel, en verschuiven de kleur sequentieel één pixel, zodat u een waterstromend licht ziet.

Druk op **F**: elke pixel licht sequentieel op in willekeurige kleuren.

![Img](./media/2019.gif)

<span style="color: rgb(0, 209, 0);">**Tip:** Als er geen reactie is op het bord, druk dan op de resetknop aan de achterkant van het micro:bit-bord.</span>

![Img](./media/4bottom.png)
