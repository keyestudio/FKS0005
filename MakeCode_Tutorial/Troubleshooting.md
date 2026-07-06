## Probleemoplossing
### 4.3.1 USB-stuurprogramma Installatie (Optioneel)

**Micro:bit is vrij van stuurprogramma-installatie. Echter, in het geval dat uw computer de hoofdboard niet herkent, kunt u het stuurprogramma ook installeren.**


#### 4.3.1.1 USB-stuurprogramma Downloaden

Klik om het [USB-stuurprogramma](./USB_driver.7z) te downloaden.

#### 4.3.1.2 USB-stuurprogramma Installatie

⚠️ Let op dat we hier demonstreren hoe u het stuurprogramma op Windows installeert, wat als referentie kan dienen voor MacOS-gebruikers.

1\. Verbind de micro:bit hoofdboard met de computer via een USB-kabel.

![Img](./media/A800.png)

2\. Zoek het stuurprogramma-bestand en klik erop om te **Installeren**.

![Img](./media/A323.png)

![Img](./media/A327.png)

3\. Klik op “**Install**” en “**Next**”.

![Img](./media/A347.png)

4\. Klik op “**Install**” en “**Finish**”.

![Img](./media/A408.png)

![Img](./media/A349.png)

5\. Klik op “**Computer**” → “**Properties**” → “**Device manager**” en u zult zien:

![Img](./media/A427.png)

### 4.3.2 Veelgestelde Vragen
Oplossingen voor het probleem waarbij Microbit programma's niet kan downloaden en MAINTENANCE weergeeft.

#### 4.3.2.1 Problemen

Vele nieuwe gebruikers zijn onlangs dit probleem tegengekomen: Wanneer ze de Micro:bit-board via een Micro USB-kabel op de computer aansluiten en op “**Download**” klikken, kan de code niet worden gedownload en reageert de board niet.

Als u per ongeluk de resetknop aan de achterkant van de Micro:bit-board ingedrukt hield op het moment dat u het programma erop kopieerde, zou dit de board in de onderhoudsmodus hebben gezet. Of misschien is door uw eigen fouten de firmware op de board verloren gegaan.

Als gevolg hiervan verschijnt er een nieuwe “**MAINTENANCE**”-schijf in uw bestandsbeheerder, waardoor de micro:bit uw gebruikerscode niet accepteert.

De MAINTENANCE-schijf zal er zo uitzien, afhankelijk van uw computer:

![Img](./media/158.png)

 #### 4.3.2.2 Oplossingen

(1) Download het <span style="color: rgb(255, 76, 65);">.hex</span>-bestand dat geschikt is voor uw versie van de micro:bit van deze pagina naar uw computer.

Download [de nieuwste Micro:bit firmware -0255 .hex-bestand](https://www.microbit.org/get-started/user-guide/firmware/), die we ook in de map hebben geleverd.

(2) Sleep het .hex-bestand dat u van deze pagina hebt gedownload naar de **MAINTENANCE**-schijf. <span style="color: rgb(255, 76, 65);">Let op dat de firmware varieert per model van Micro:bit V2-board. Hier is Firmware voor V2.20_V2.21.</span> Wanneer de upgrade is voltooid, zal de micro:bit resetten, zichzelf uitwerpen van de computer en opnieuw verschijnen in de normale **MICROBIT**-schijfmodus.

![Img](./media/326.png)

![Img](./media/331.png)

#### 4.3.2.3 Vermijd “MAINTENANCE”-modus

(1) Druk niet op de resetknop aan de achterkant van de Micro:bit-board wanneer deze is aangesloten op een Micro USB-kabel.

Als de resetknop wordt ingedrukt tijdens het opstarten, gaat de micro:bit in de onderhoudsmodus. (**<span style="color: rgb(255, 76, 65);">Veelvoorkomende fouten gemaakt door beginners</span>**)

![Img](./media/228.png)

(2) Koppel het niet plotseling los tijdens het downloaden van het programma. Anders kan de firmware verloren gaan en zal de micro:bit in de MAINTENANCE-modus terechtkomen.

(3) Tijdens het experiment zal verkeerde bedrading ook leiden tot kortsluiting, waardoor de micro:bit-firmware verloren kan gaan. Beginners moeten hierop letten bij het bedienen.

#### 4.3.2.4 Downloaden met WebUSB

Lijkt uw micro:bit een storing te hebben ontwikkeld met WebUSB (/ device/ usb/ webusb)? Laten we proberen de reden te achterhalen.

**Stap 1: Test met micro USB-kabel**

Sluit de micro:bit met een micro USB-kabel aan op uw computer. Het zou moeten verschijnen als een MICROBIT-schijf.

![Img](./media/321.png)

Als MICROBIT verschijnt als een schijf onder Apparaten en schijven, ga dan naar Stap 2.

Zo niet, probeer dan: (a) een andere kabel; (b) een andere USB-poort op uw computer; (c) de micro:bit aansluiten op een andere computer.

Sommige micro USB-kabels bieden mogelijk alleen een stroomverbinding en verzenden geen gegevens, en sommige computers kunnen hun USB-poorten om de een of andere reden uitschakelen.

U ziet de MICROBIT-schijf nog steeds niet? Hmm, er is mogelijk een probleem met uw micro:bit-board. Zie het artikel over [probleemoplossing](https://support.microbit.org/solution/articles/19000024000-fault-finding-with-a-micro-bit) met de microbit.org of open een [supportticket](https://support.microbit.org/support/tickets/new) om de Micro:bit Foundation op de hoogte te stellen van het probleem. En, sla alle volgende stappen over.

**Stap 2: Uw firmwareversie controleren**

Om erachter te komen welke versie van de firmware u op uw micro:bit hebt:

① Sluit deze aan op een computer met de USB-kabel en open de **MICROBIT**-schijf.

![Img](./media/A8491.png)

② Open het **DETAILS.TXT**-bestand.

![Img](./media/0452.png)

③ Zoek naar het nummer op de regel die begint met “Interface/Bootloader Version”.

![Img](./media/501.png)

Als het 0234/0241/0243 is, moet u de firmware op uw micro:bit V2-board bijwerken. Ga naar Stap 3 voor de update.

Als het 0249/0257 of hoger is, ga dan naar Stap 4.

**Stap 3: Hoe de firmware bij te werken**

Als u de firmware moet bijwerken om toegang te krijgen tot een nieuwe functie of een probleem op te lossen, kunt u dit als volgt doen:

① Koppel de USB-kabel en het batterijpakket los van de micro:bit.

② Houd de resetknop aan de achterkant van de micro:bit ingedrukt en sluit de USB-kabel aan op de micro:bit en uw computer. U zou een schijf moeten zien verschijnen in uw bestandsbeheerder genaamd **MAINTENANCE** (in plaats van MICROBIT) en de gele LED-indicator aan de achterkant zou moeten oplichten.

![Img](./media/551.png)

![Img](./media/AAC1.webp)

③ Download [firmware .hex-bestand](https://microbit.org/guide/firmware/) dat geschikt is voor uw versie van de micro:bit. <span style="color: rgb(255, 76, 65);">Hier is Firmware voor V2.20_V2.21.</span>

![Img](./media/0629.png)

④ Sleep het <span style="color: rgb(255, 76, 65);">.hex</span> firmware naar de **MAINTENANCE**-schijf.

![Img](./media/331.png)

⑤ Wacht tot de gele LED aan de achterkant van het apparaat stopt met knipperen. Na het kopiëren gaat de LED uit en reset de micro:bit. MAINTENANCE zal terugkeren naar MICROBIT.

⑥ Controleer ten slotte het <span style="color: rgb(255, 76, 65);">DETAILS.TXT</span>-bestand dat zich op de **MICROBIT**-schijf bevindt en zorg ervoor dat het hetzelfde versienummer heeft als de .hex-firmware.

Voor eventuele problemen met de board, onderhoudsmodus en firmware-updates, raadpleeg de [Firmware Gids](https://microbit.org/guide/firmware/).

**Stap 4: Uw browserversie controleren**

WebUSB is een relatief nieuwe functie die u mogelijk uw browser moet bijwerken. Controleer of uw browser: (a) compatibel is met Android, Chrome OS; (b) Microsoft Edge; (c) de Chrome 65+ van Linux, macOS en Windows 10.

**Stap 5: Een apparaat aansluiten**

Open Google Chrome / Microsoft Edge om naar de MakeCode-editor te gaan en klik op de “**Connect Device**”. Voor het koppelen van een apparaat, raadpleeg [WebUSB (/ device/ usb/ webusb)](https://microbit.org/get-started/user-guide/web-usb/).

Geniet van snel downloaden!
