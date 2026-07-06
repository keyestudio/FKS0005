## 4.1.1 Informazioni su MakeCode

⚠️ **I seguenti passaggi sono eseguiti sul sistema operativo Windows. Se si utilizza un altro sistema operativo, possono essere presi come riferimento. Qui sono dimostrati su Google Chrome / Microsoft Edge.**

**Ambiente di Programmazione MakeCode:**

Aprire la [versione online dell'editor MakeCode](https://makecode.microbit.org/#editor).

Interfaccia principale di MakeCode:

![Img](./media/A637.png)

Ci sono blocchi “**all'avvio**” e “**per sempre**” nell'area di modifica del codice. Quando l'alimentazione è collegata o resettata, “all'avvio” significa che il codice nel blocco viene eseguito una sola volta, mentre “per sempre” implica che il codice viene eseguito ciclicamente.

Clicca “**JS JavaScript**” per vedere il codice JavaScript:

![Img](./media/A754.png)

Oppure clicca “**Python**” per passare al codice Python:

![Img](./media/A814.png)

**Impostazioni della lingua:**

![Img](./media/Animation-3.gif)

Passaggi:

Passaggio 1: Clicca il pulsante delle impostazioni ![Img](./media/A806.png).

![Img](./media/A301.png)

Passaggio 2: Clicca “Language”.

![Img](./media/A302.png)

Passaggio 3: Seleziona la lingua desiderata. Qui la impostiamo su “English”.

![Img](./media/A303.png)

## 4.1.2 Libreria di Estensione Makecode

### 4.1.2.1 Aggiungi Libreria

⚠️ **Forniamo file di codice (.hex) per ogni progetto, quindi puoi caricarli direttamente nell'editor MakeCode. Oppure, se lo desideri, puoi anche costruire blocchi di codice da solo. Nota che le librerie sono necessarie quando li costruisci manualmente.**

⚠️ **<span style="color: rgb(255, 76, 65);">Nota:</span>** Copia e incolla il link nella casella di ricerca: `https://github.com/keyestudio2019/pxt-creative-inventors-kit-master.git`.

![Img](./media/Animation-4.gif)

Passaggi:

1\. Clicca ![Img](./media/A806.png) per selezionare “**Extensions**”.

![Img](./media/A842.png)

Oppure clicca “**Extensions**” sopra i blocchi **Advanced**.

![Img](./media/A900.png)

2\. Cerca parole chiave o incolla il link GitHub.

![Img](./media/A909.png)

3\. Qui inseriamo l'URL: `https://github.com/keyestudio2019/KEYES-Smart-Gamepad-master.git` nella casella di ricerca e clicchiamo ![Img](./media/A3257.png), e carichiamo l'estensione di “**Smart-Gamepad**”.

![Img](./media/A306.png)

4\. Caricamento:

![Img](./media/A3316.png)

5\. Caricato:

![Img](./media/A335.png)

### 4.1.2.2 Aggiorna/Elimina Libreria

⚠️ **Generalmente, non è necessario rimuovere le librerie, a meno che non siano più richieste.**

![Img](./media/Animation-4.gif)

Passaggi:

1\. Clicca “**JavaScript**” per passare ai codici testuali.

![Img](./media/A724.png)

2\. Clicca “**Explorer**”.

![Img](./media/A749.png)

3\. Trova “**Smart-Gamepad**” e clicca l'icona del cestino ![Img](./media/A813.png) per rimuoverlo.

![Img](./media/A824.png)

4\. “**Remove it**”.

![Img](./media/A727.png)

## 4.1.3 Programma MakeCode

### 4.1.3.1 Importa Programma in MakeCode

Prendiamo come esempio il progetto “**heartbeat**”.

![Img](./media/Animation-2.gif)

Passaggi:

1\. Collega la scheda micro:bit al tuo computer tramite cavo micro USB.

![Img](./media/A800.png)

Quando la micro:bit è accesa, l'indicatore LED rosso sul retro si illuminerà.

Sulla scheda micro:bit, c'è un indicatore LED giallo che lampeggerà quando la scheda comunica con il tuo computer tramite micro USB.

Apri Finder (Mac) / Dispositivi e unità (Windows), e vedrai un'unità USB chiamata "MICROBIT". Nota però che non è un disco comune!

![Img](./media/A849.png)

2\. Clicca “**Import**”:

![Img](./media/A956.png)

3\. E seleziona “**Import File...**”.

![Img](./media/A042.png)

4\. “**Choose File**” per aprire il file di cui hai bisogno.

![Img](./media/A06.png)

5\. Qui scegliamo “**heartbeat.hex**”.

![Img](./media/A28.png)

6\. “**Go ahead √**”.

![Img](./media/A149.png)

Oppure puoi trascinare direttamente il file hex nell'interfaccia principale di Makecode:

![Img](./media/A202.png)

7\. Importato:

![Img](./media/A217.png)

### 4.1.3.2 Scarica Codice (WebUSB)

Per browser come **Google Chrome/Microsoft Edge**, il loro WebUSB consente l'accesso diretto al dispositivo hardware micro USB tramite pagina web online. Clicca “Connect Device” per accoppiare il dispositivo. Dopodiché, clicca “**Download**” per caricare il codice sulla scheda micro:bit.

![Img](./media/Animation.gif)

Passaggi:

#### 4.1.3.2.1 Accoppia dispositivo

1\. Collega la scheda micro:bit al tuo computer tramite cavo micro USB.

![Img](./media/A951.png)

2\. Clicca i tre puntini “**...**” dietro “**Download**” e seleziona “**Connect device**”.

![Img](./media/A028.png)

3\. “**Next**”.

![Img](./media/A046.png)

4\. “**Pair**”.

![Img](./media/A104.png)

5\. Connetti a un “**Device**” e “**Connect**”.

![Img](./media/A127.png)

6\. “**Done**” e connesso.

![Img](./media/A144.png)

#### 4.1.3.2.2 Scarica codice

Dopo la connessione, clicca “**Download**” e il codice verrà scaricato sulla scheda micro:bit, e ![Img](./media/A212.png) diventa ![Img](./media/A220.png).

![Img](./media/A232.png)

⚠️ **Suggerimenti**

Se non c'è nessun dispositivo da accoppiare nell'interfaccia, consulta la [risoluzione dei problemi del dispositivo-webusb](https://makecode.microbit.org/device/usb/webusb/troubleshoot).

Se il firmware della micro:bit richiede un aggiornamento, consulta [come aggiornare il firmware](https://microbit.org/guide/firmware/).

### 4.1.3.3 Scarica Codice (senza WebUSB)

1\. Collega la scheda micro:bit al tuo computer tramite cavo micro USB.

![Img](./media/A800.png)

Quando la micro:bit è accesa, l'indicatore LED rosso sul retro si illuminerà.

Sulla scheda micro:bit, c'è un indicatore LED giallo che lampeggerà quando la scheda comunica con il tuo computer tramite micro USB.

Apri Finder (Mac) / Dispositivi e unità (Windows), e vedrai un'unità USB chiamata "MICROBIT". Nota però che non è un disco comune!

![Img](./media/A849.png)

2\. Per i browser, carica il codice sulla scheda micro:bit come segue:

![Img](./media/Animations-1.gif)

Passaggi:

① Clicca il pulsante “**Download**” e verrà scaricato un file “**.hex**”, che può essere letto dalla scheda micro:bit. Dopodiché, copialo e incollalo sulla scheda.

Per Windows, puoi “**Invia a→MICROBIT**” e caricare il file “**.hex**” sulla scheda micro:bit. Durante questo processo, l'indicatore giallo sul retro della scheda lampeggerà. Una volta completato il caricamento, l'indicatore rimarrà acceso.

![Img](./media/A319.png)

![Img](./media/A449.png)

Oppure puoi trascinare direttamente il file “**.hex**” su MICROBIT:

![Img](./media/A341.png)

![Img](./media/A345.png)

② Dopodiché, collega la scheda micro:bit al computer tramite cavo micro USB e accendila, e vedrai la matrice LED 5x5 a bordo mostrare ripetutamente ![Img](./media/A903.png) e ![Img](./media/A910.png).

![Img](./media/A22.png)

⚠️ Durante ogni programmazione, il disco MICROBIT si espellerà e tornerà automaticamente, e i file **.hex** che hai copiato su di esso non verranno visualizzati. Questo perché la scheda micro:bit riceve ed esegue solo l'ultimo programma caricato anziché memorizzarli.
