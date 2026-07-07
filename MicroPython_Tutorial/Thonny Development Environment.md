## 5.1 Thonny Ontwikkelomgeving

**Voordat u begint met programmeren, zijn er enkele belangrijke voorbereidingen nodig.**

### 5.1.1 Thonny installeren

Thonny is een gratis en open-source softwareplatform met een klein formaat, eenvoudige interface, gemakkelijke bediening en rijke functionaliteit. Het is een Python IDE die geschikt is voor beginners. In deze tutorial gebruiken we deze IDE om een ESP32 te ontwikkelen. Thonny ondersteunt meerdere besturingssystemen, waaronder Windows, Mac OS en Linux.

**1. Thonny downloaden**

(1) Ga naar de website: [https://thonny.org](https://thonny.org) om de nieuwste versie van Thonny te downloaden. Andere versies zijn mogelijk niet compatibel met microbit-functies.
(2) Thonny open-source codebibliotheek: [https://github.com/thonny/thonny](https://github.com/thonny/thonny).

Download de versie die geschikt is voor uw besturingssysteem.

| OS | Download |
| :-- | :-- |
| MAC OS： | https://github.com/thonny/thonny/releases/download/v4.1.7/thonny-4.1.7.pkg|
| Windows： | https://github.com/thonny/thonny/releases/download/v4.1.7/thonny-4.1.7.exe|

| OS | Methode          | Commando |
| :-- |---------|--------------|
| Linux | Binair pakket | `bash <(wget -O - https://thonny.org/installer-for-linux)` |
|       | Met pip | `pip3 install thonny` |
|       | Distro pakketten | Debian/Ubuntu：`sudo apt install thonny`<br>Fedora：`sudo dnf install thonny` |

![Img](./media/t001.png)

**2. Windows Systeem**

A. Het gedownloade Thonny-pictogram ziet er als volgt uit:

![Img](./media/t002.png)

B. Dubbelklik op “thonny-4.1.7.exe” en selecteer de installatiemodus. Hier kiezen we voor “Install for all users”.

![Img](./media/t003.png)

C. U kunt ook blijven klikken op “Next” om de installatie te voltooien.

![Img](./media/t004.png)

![Img](./media/t005.png)


D. Als u de installatielocatie van Thonny wilt wijzigen, klikt u op “Browse...” om een nieuwe locatie te selecteren. Zo niet, dan blijft u gewoon op “Next” klikken.

![Img](./media/t006.png)

![Img](./media/t007.png)

E. Vink “Create desktop icon” aan, dan ziet u Thonny op uw bureaublad.

![Img](./media/t008.png)

F. “Installeren”.

![Img](./media/t009.png)

G. Wacht even, maar klik niet op “Cancel”.

![Img](./media/t010.png)

H. Wanneer u het succesvolle installatiescherm ziet, klikt u op “Finish”.

![Img](./media/t011.png)

I. U ziet het pictogram op uw bureaublad als u “Create desktop icon” hebt aangevinkt:

![Img](./media/t011.png)                    

### 5.1.2 Thonny Basisinstellingen

A. Dubbelklik op Thonny, kies de taal en de initiële instellingen en klik op “Let’s go!”.

![Img](./media/t013.png)

![Img](./media/t014.png)

![Img](./media/t015.png)

B. Klik op “**View**”→“**File**” en “**Shell**”.

![Img](./media/t016.png)

![Img](./media/t017.png)

![Img](./media/t018.png)

### 5.1.3 MicroPython Firmware branden (Belangrijk)

Om een Python-programma op het Micro:bit-bord uit te voeren, moeten we eerst de firmware erop branden.

**De MicroPython firmware branden:**

Verbind de Micro:bit met uw pc met een USB-kabel.

![Img](./media/A800.png)

Zorg ervoor dat het stuurprogramma succesvol is geïnstalleerd en dat de COM-poort correct kan worden geïdentificeerd. Open “**Apparaatbeheer**” en vouw “**Poorten**” uit.

![Img](./media/t019.png)

Het COM-poortnummer kan per computer verschillen.

Open Thonny, klik op “**run**” en “**Configure interpreter...**”

![Img](./media/t020.png)

Selecteer “Micropython (BBC micro:bit)” en “mbeb Serial Port @ COM16” in de interpreter, en klik op “Install or update firmware”.

![Img](./media/t021.png)

En u ziet het volgende. Stel “Target volume” in op “MICROBIT”, “MicroPython family” op “nRF52”, “variant” op “BBC micro:bit v2 (original simplifiled API)”, “version” op “2.1.2”, en vervolgens “Install”. 

Als de firmware niet kan worden geïnstalleerd, drukt u op de resetknop op de Micro:bit en klikt u op “Install”.

![Img](./media/t022.png)

Klik daarna op “Close” en “OK”.

![Img](./media/t023.png)

Sluit alle vensters en ga naar de hoofdpagina en klik op het “STOP”-pictogram:

![Img](./media/t024.png)

### 5.1.4 Code uploaden

**De testcode uitvoeren (online)**

De Micro:bit voert de code online uit wanneer deze met de computer moet worden verbonden. Gebruikers kunnen programma's programmeren en debuggen met Thonny.

Open Thonny en klik op "**Open**".

![Img](./media/t025.png)

Wanneer een nieuw venster verschijnt, opent u ".\MicroPython_Resource\Codes\Heart beat", selecteert u “heartbeat&ZeroWidthSpace;.py”, en klikt u op “Run current script” (als er een foutmelding verschijnt, klikt u eerst op ![Img](./media/t027.png) en vervolgens op “Run current script”), en u ziet een kloppend hart op de Micro:bit.

![Img](./media/t026.png)

Opmerking: Wanneer u het online uitvoert, wordt de code niet opnieuw uitgevoerd als u op de resetknop drukt. Als u wilt dat het na het resetten wordt uitgevoerd, raadpleegt u de onderstaande instructies voor offline uitvoeren.

**De testcode uitvoeren (offline)**

Na het resetten van de Micro:bit, voert u eerst het bestand main.py uit in de hoofdmap. 

Daarom moet de bestandsnaam die we uploaden naar de Micro:bit worden gewijzigd in main.py als we willen dat deze de code na het resetten uitvoert. Upload vervolgens het bestand, druk op de resetknop en de code wordt nog steeds uitgevoerd.

Hier nemen we heartbeat.py als voorbeeld. Selecteer **heartbeat&ZeroWidthSpace;.py** om het te "**hernoemen**" naar main.py, en klik op "**OK**". Nu kunt u kiezen om te “**Upload to micro:bit**”.

![Img](./media/t028.png)

![Img](./media/t029.png)

![Img](./media/t030.png)

Druk op de Reset-knop en u ziet het hart kloppen op de Micro:bit.

Als u andere code (geen bibliotheken) wilt uitvoeren, moet u eerst de naam wijzigen in main&ZeroWidthSpace;.py voordat u uploadt. 

Wat betreft bibliotheken, klik met de rechtermuisknop om direct “Upload to micro:bit” (Soms kan het uploaden mislukken vanwege een te grote bibliotheek. U moet deze dan vereenvoudigen of ongebruikte bibliotheken verwijderen).

### 5.1.5 Andere veelvoorkomende bewerkingen

**Bestand verwijderen onder Micro:bit**

In “micro:bit” selecteert u “main&ZeroWidthSpace;.py” om te “Delete”, en het wordt verwijderd.

![Img](./media/t031.png)

Dezelfde procedure is van toepassing bij het verwijderen van andere bestanden.
