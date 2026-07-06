## Risoluzione dei Problemi
### 4.3.1 Installazione del Driver USB (Opzionale)

**Micro:bit non richiede l'installazione di driver. Tuttavia, nel caso in cui il computer non riconosca la scheda principale, è possibile installare il driver.**


#### 4.3.1.1 Download del Driver USB

Clicca per scaricare il [driver USB](./USB_driver.7z).

#### 4.3.1.2 Installazione del Driver USB

⚠️ Nota che qui dimostriamo come installare il driver su Windows, che può essere preso come riferimento per gli utenti MacOS.

1\. Collega la scheda principale micro:bit al computer tramite cavo USB.

![Img](./media/A800.png)

2\. Trova il file del driver e cliccalo per **Installare**.

![Img](./media/A323.png)

![Img](./media/A327.png)

3\. Clicca “**Install**” e “**Next**”.

![Img](./media/A347.png)

4\. Clicca “**Install**” e “**Finish**”.

![Img](./media/A408.png)

![Img](./media/A349.png)

5\. Clicca “**Computer**” → “**Properties**” → “**Device manager**” e vedrai:

![Img](./media/A427.png)

### 4.3.2 FAQ
Soluzioni per il problema in cui Microbit non riesce a scaricare i programmi e visualizza MAINTENANCE.

#### 4.3.2.1 Problemi

Molti nuovi utenti hanno recentemente riscontrato questo problema: quando collegano la scheda Micro:bit al computer tramite un cavo Micro USB e cliccano su “**Download**”, il codice non viene scaricato e la scheda non mostra alcuna risposta.

Se si teneva accidentalmente premuto il pulsante di reset sul retro della scheda Micro:bit nel momento in cui si copiava il programma su di essa, questo avrebbe messo la scheda in modalità di manutenzione. O forse a causa di alcuni errori propri, il firmware sulla scheda è andato perso.

Di conseguenza, una nuova unità “**MAINTENANCE**” apparirà nel tuo file manager, quindi la micro:bit non accetterà il tuo codice utente.

L'unità MAINTENANCE apparirà così, a seconda del tuo computer:

![Img](./media/158.png)

 #### 4.3.2.2 Soluzioni

(1) Scarica il file <span style="color: rgb(255, 76, 65);">.hex</span> appropriato per la tua versione di micro:bit da questa pagina al tuo computer.

Scarica [l'ultimo firmware Micro:bit -0255 .hex file](https://www.microbit.org/get-started/user-guide/firmware/), che abbiamo anche fornito nella cartella.

(2) Trascina e rilascia il file .hex scaricato da questa pagina sull'unità **MAINTENANCE**. <span style="color: rgb(255, 76, 65);">Nota che il firmware varia dal modello della scheda Micro:bit V2. Qui è il Firmware per V2.20_V2.21.</span> Quando l'aggiornamento è completato, la micro:bit si resetterà, espellendosi dal computer e riapparirà in modalità unità **MICROBIT** normale.

![Img](./media/326.png)

![Img](./media/331.png)

#### 4.3.2.3 Evitare la Modalità “MAINTENANCE”

(1) Non premere il pulsante di reset sul retro della scheda Micro:bit quando è collegata a un cavo Micro USB.

Se il pulsante di reset viene premuto durante l'accensione, la micro:bit entrerà in modalità di manutenzione. (**<span style="color: rgb(255, 76, 65);">Errori comuni commessi dai principianti</span>**)

![Img](./media/228.png)

(2) Non scollegarla improvvisamente durante il download del programma. Altrimenti il firmware potrebbe andare perso e la micro:bit entrerà in modalità MAINTENANCE.

(3) Durante l'esperimento, un cablaggio errato causerà anche un cortocircuito, quindi il firmware della micro:bit potrebbe andare perso. I principianti devono prestare attenzione durante l'operazione.

#### 4.3.2.4 Download con WebUSB

La tua micro:bit sembra aver sviluppato un difetto con WebUSB (/ device/ usb/ webusb)? Cerchiamo di capire il motivo.

**Passaggio 1: Test sul cavo micro USB**

Collega la micro:bit al computer con un cavo micro USB. Dovrebbe apparire come un'unità MICROBIT.

![Img](./media/321.png)

Se MICROBIT appare come un'unità sotto Dispositivi e unità, vai al Passaggio 2.

In caso contrario, prova: (a) un altro cavo; (b) un'altra porta USB sul tuo computer; (c) collegare la micro:bit a un altro computer.

Alcuni cavi micro USB potrebbero offrire solo una connessione di alimentazione e non trasmettere dati, e alcuni computer potrebbero disattivare le loro porte USB per qualche motivo.

Non riesci ancora a vedere l'unità MICROBIT? Hmm, potrebbe esserci un problema con la tua scheda micro:bit. Consulta l'articolo sulla [risoluzione dei problemi](https://support.microbit.org/solution/articles/19000024000-fault-finding-with-a-micro-bit) con microbit.org o apri un [ticket di supporto](https://support.microbit.org/support/tickets/new) per notificare il problema alla Micro:bit Foundation. E, salta tutti i passaggi seguenti.

**Passaggio 2: Verifica della versione del firmware**

Per scoprire quale versione del firmware hai sulla tua micro:bit:

① Collegala a un computer usando il cavo USB e apri l'unità **MICROBIT**.

![Img](./media/A8491.png)

② Apri il file **DETAILS.TXT**.

![Img](./media/0452.png)

③ Cerca il numero sulla riga che inizia con “Interface/Bootloader Version”.

![Img](./media/501.png)

Se è 0234/0241/0243, devi aggiornare il firmware sulla tua scheda micro:bit V2. Vai al Passaggio 3 per l'aggiornamento.

Se è 0249/0257 o superiore, vai al Passaggio 4.

**Passaggio 3: Come aggiornare il firmware**

Se devi aggiornare il firmware per accedere a una nuova funzionalità o risolvere un problema, ecco come fare:

① Scollega il cavo USB e il pacco batterie dalla micro:bit.

② Tieni premuto il pulsante di reset sul retro della micro:bit e collega il cavo USB alla micro:bit e al tuo computer. Dovresti vedere un'unità apparire nel tuo file manager chiamata **MAINTENANCE** (invece di MICROBIT) e l'indicatore LED giallo sul retro dovrebbe accendersi.

![Img](./media/551.png)

![Img](./media/AAC1.webp)

③ Scarica il [file .hex del firmware](https://microbit.org/guide/firmware/) appropriato per la tua versione di micro:bit. <span style="color: rgb(255, 76, 65);">Qui è il Firmware per V2.20_V2.21.</span>

![Img](./media/0629.png)

④ Trascina e rilascia il firmware <span style="color: rgb(255, 76, 65);">.hex</span> sull'unità **MAINTENANCE**.

![Img](./media/331.png)

⑤ Attendi che il LED giallo sul retro del dispositivo smetta di lampeggiare. Dopo la copia, il LED si spegnerà e la micro:bit si resetterà. MAINTENANCE tornerà a MICROBIT.

⑥ Infine, controlla il file <span style="color: rgb(255, 76, 65);">DETAILS.TXT</span> che si trova sull'unità **MICROBIT** e assicurati che abbia lo stesso numero di versione del firmware .hex.

Per qualsiasi problema relativo alla scheda, alla modalità di manutenzione e agli aggiornamenti del firmware, consulta la [Guida al Firmware](https://microbit.org/guide/firmware/).

**Passaggio 4: Verifica della versione del browser**

WebUSB è una funzione relativamente nuova che potresti dover aggiornare il tuo browser. Controlla se il tuo browser è: (a) compatibile con Android, Chrome OS; (b) Microsoft Edge; (c) Chrome 65+ di Linux, macOS e Windows 10.

**Passaggio 5: Connessione di un dispositivo**

Apri Google Chrome / Microsoft Edge per andare all'editor MakeCode e clicca su “**Connect Device**”. Per come accoppiare un dispositivo, consulta [WebUSB (/ device/ usb/ webusb)](https://microbit.org/get-started/user-guide/web-usb/).

Goditi il download rapido!
