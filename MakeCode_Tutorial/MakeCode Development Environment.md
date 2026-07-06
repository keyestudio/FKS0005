## 4.1.1 Over MakeCode

⚠️ **De volgende stappen worden uitgevoerd op het Windows-besturingssysteem. Als u een ander besturingssysteem gebruikt, kunt u deze als referentie nemen. Hier worden ze gedemonstreerd op Google Chrome / Microsoft Edge.**

**MakeCode Programmeeromgeving:**

Open de [online versie van de MakeCode-editor](https://makecode.microbit.org/#editor).

Hoofdinterface van MakeCode:

![Img](./media/A637.png)

Er zijn blokken "**on start**" en "**forever**" in het codebewerkingsgebied. Wanneer de stroom wordt aangesloten of gereset, betekent "on start" dat de code in het blok slechts één keer wordt uitgevoerd, terwijl "forever" impliceert dat de code cyclisch wordt uitgevoerd.

Klik op "**JS JavaScript**" om de JavaScript-code te zien:

![Img](./media/A754.png)

Of klik op "**Python**" om over te schakelen naar Python-code:

![Img](./media/A814.png)

**Taalinstellingen:**

![Img](./media/Animation-3.gif)

Stappen:

Stap 1: Klik op de instellingenknop ![Img](./media/A806.png).

![Img](./media/A301.png)

Stap 2: Klik op "Language".

![Img](./media/A302.png)

Stap 3: Selecteer de gewenste taal. Hier stellen we deze in op "English".

![Img](./media/A303.png)

## 4.1.2 Makecode Uitbreidingsbibliotheek

### 4.1.2.1 Bibliotheek Toevoegen

⚠️ **Wij leveren codebestanden (.hex) voor elk project, zodat u deze direct kunt laden in de MakeCode-editor. Of als u wilt, kunt u ook zelf codeblokken bouwen. Houd er rekening mee dat bibliotheken vereist zijn wanneer u ze handmatig bouwt.**

⚠️ **<span style="color: rgb(255, 76, 65);">Opmerking:</span>** Kopieer en plak de link in het zoekvak: `https://github.com/keyestudio2019/pxt-creative-inventors-kit-master.git`.

![Img](./media/Animation-4.gif)

Stappen:

1\. Klik op ![Img](./media/A806.png) om "**Extensions**" te selecteren.

![Img](./media/A842.png)

Of klik op de "**Extensions**" boven de **Advanced** blokken.

![Img](./media/A900.png)

2\. Zoek trefwoorden of plak de GitHub-link.

![Img](./media/A909.png)

3\. Hier voeren we de URL: `https://github.com/keyestudio2019/KEYES-Smart-Gamepad-master.git` in het zoekvak in en klikken op ![Img](./media/A3257.png), en laden de extensie van "**Smart-Gamepad**".

![Img](./media/A306.png)

4\. Laden:

![Img](./media/A3316.png)

5\. Geladen:

![Img](./media/A335.png)

### 4.1.2.2 Bibliotheek Bijwerken/Verwijderen

⚠️ **Over het algemeen is het niet nodig om bibliotheken te verwijderen, tenzij ze niet langer nodig zijn.**

![Img](./media/Animation-4.gif)

Stappen:

1\. Klik op "**JavaScript**" om over te schakelen naar tekstcodes.

![Img](./media/A724.png)

2\. Klik op "**Explorer**".

![Img](./media/A749.png)

3\. Zoek de "**Smart-Gamepad**" en klik op de prullenbak ![Img](./media/A813.png) om deze te verwijderen.

![Img](./media/A824.png)

4\. "**Remove it**".

![Img](./media/A727.png)

## 4.1.3 MakeCode Programma

### 4.1.3.1 Programma Importeren in MakeCode

We nemen het project "**heartbeat**" als voorbeeld.

![Img](./media/Animation-2.gif)

Stappen:

1\. Verbind het micro:bit-bord met uw computer via een micro USB-kabel.

![Img](./media/A800.png)

Wanneer de micro:bit wordt ingeschakeld, zal de rode LED-indicator aan de achterkant oplichten.

Op het micro:bit-bord bevindt zich een gele LED-indicator die knippert wanneer het bord communiceert met uw computer via micro USB.

Open Finder(Mac) / Apparaten en schijven(Windows), en u ziet een USB-station genaamd "MICROBIT". Let wel op dat het geen gewone schijf is!

![Img](./media/A849.png)

2\. Klik op "**Import**":

![Img](./media/A956.png)

3\. En selecteer "**Import File...**".

![Img](./media/A042.png)

4\. "**Choose File**" om het bestand te openen dat u nodig heeft.

![Img](./media/A06.png)

5\. Hier kiezen we "**heartbeat.hex**".

![Img](./media/A28.png)

6\. "**Go ahead √**".

![Img](./media/A149.png)

Of u kunt het hex-bestand direct naar de hoofdinterface van Makecode slepen:

![Img](./media/A202.png)

7\. Geïmporteerd:

![Img](./media/A217.png)

### 4.1.3.2 Code Downloaden (WebUSB)

Voor browsers zoals **Google Chrome/Microsoft Edge** maakt hun WebUSB directe toegang tot het micro USB-hardwareapparaat mogelijk via een online webpagina. Klik op "Connect Device" om het apparaat te koppelen. Klik daarna op "**Download**" om de code naar het micro:bit-bord te laden.

![Img](./media/Animation.gif)

Stappen:

#### 4.1.3.2.1 Apparaat Koppelen

1\. Verbind het micro:bit-bord met uw computer via een micro USB-kabel.

![Img](./media/A951.png)

2\. Klik op de drie puntjes "**...**" achter de "**Download**" en selecteer "**Connect device**".

![Img](./media/A028.png)

3\. "**Next**".

![Img](./media/A046.png)

4\. "**Pair**".

![Img](./media/A104.png)

5\. Verbind met een "**Device**" en "**Connect**".

![Img](./media/A127.png)

6\. "**Done**" en verbonden.

![Img](./media/A144.png)

#### 4.1.3.2.2 Code Downloaden

Na het verbinden klikt u op "**Download**" en de code wordt gedownload naar het micro:bit-bord, en ![Img](./media/A212.png) wordt ![Img](./media/A220.png).

![Img](./media/A232.png)

⚠️ **Tips**

Als er geen apparaat is om te koppelen in de interface, raadpleeg dan de [device-webusb-troubleshoot](https://makecode.microbit.org/device/usb/webusb/troubleshoot).

Als de micro:bit-firmware een update vereist, raadpleeg dan [how-to-update-the-firmware](https://microbit.org/guide/firmware/).

### 4.1.3.3 Code Downloaden (geen WebUSB)

1\. Verbind het micro:bit-bord met uw computer via een micro USB-kabel.

![Img](./media/A800.png)

Wanneer de micro:bit wordt ingeschakeld, zal de rode LED-indicator aan de achterkant oplichten.

Op het micro:bit-bord bevindt zich een gele LED-indicator die knippert wanneer het bord communiceert met uw computer via micro USB.

Open Finder(Mac) / Apparaten en schijven(Windows), en u ziet een USB-station genaamd "MICROBIT". Let wel op dat het geen gewone schijf is!

![Img](./media/A849.png)

2\. Voor browsers, laad de code naar het micro:bit-bord als volgt:

![Img](./media/Animations-1.gif)

Stappen:

① Klik op de "**Download**"-knop en een ".hex"-bestand wordt gedownload, dat kan worden gelezen door het micro:bit-bord. Kopieer en plak het daarna naar het bord.

Voor Windows kunt u "**Send to→MICROBIT**" en de ".hex" naar het micro:bit-bord laden. Tijdens dit proces knippert de gele indicator aan de achterkant van het bord. Wanneer het laden is voltooid, blijft de indicator branden.

![Img](./media/A319.png)

![Img](./media/A449.png)

Of u kunt het ".hex"-bestand direct naar de MICROBIT slepen:

![Img](./media/A341.png)

![Img](./media/A345.png)

② Daarna, verbind het micro:bit-bord met de computer via een micro USB-kabel en schakel het in, en u ziet de ingebouwde 5 x 5 LED-matrix herhaaldelijk ![Img](./media/A903.png) en ![Img](./media/A910.png) tonen.

![Img](./media/A22.png)



⚠️ Tijdens elke programmering zal de MICROBIT-schijf automatisch uitwerpen en terugkeren, en de **.hex**-bestanden die u ernaartoe hebt gekopieerd, worden niet weergegeven. Dat komt omdat het micro:bit-bord alleen het laatst geüploade programma ontvangt en uitvoert, in plaats van ze op te slaan.
