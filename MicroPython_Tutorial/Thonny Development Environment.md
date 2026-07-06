## 5.1 Ambiente di Sviluppo Thonny

**Prima di programmare, è necessario effettuare alcune importanti preparazioni.**

### 5.1.1 Installa Thonny

Thonny è una piattaforma software gratuita e open source con dimensioni ridotte, interfaccia semplice, funzionamento semplice e funzioni ricche. È un IDE Python adatto ai principianti. In questo tutorial, useremo questo IDE per sviluppare un ESP32. Thonny supporta più sistemi operativi tra cui Windows, Mac OS, Linux.

**1. Scarica Thonny**

(1) Accedi al sito web: [https://thonny.org](https://thonny.org) per scaricare l'ultima versione di Thonny. Altre versioni potrebbero non essere compatibili con le funzioni microbit.
(2) Libreria di codice open-source Thonny: [https://github.com/thonny/thonny](https://github.com/thonny/thonny).

Scarica quella del tuo sistema operativo.

| OS | Download |
| :-- | :-- |
| MAC OS： | https://github.com/thonny/thonny/releases/download/v4.1.7/thonny-4.1.7.pkg|
| Windows： | https://github.com/thonny/thonny/releases/download/v4.1.7/thonny-4.1.7.exe|

| OS | Metodo | Comando |
| :-- |---------|--------------|
| Linux | Pacchetto binario | `bash <(wget -O - https://thonny.org/installer-for-linux)` |
| | Con pip | `pip3 install thonny` |
| | Pacchetti distro | Debian/Ubuntu：`sudo apt install thonny`<br>Fedora：`sudo dnf install thonny` |

![Img](./media/t001.png)

**2. Sistema Windows**

A. L'icona di Thonny scaricata è la seguente:

![Img](./media/t002.png)

B. Fai doppio clic su “thonny-4.1.7.exe” e seleziona la modalità di installazione. Qui scegliamo “Install for all users”.

![Img](./media/t003.png)

C. Puoi anche continuare a selezionare “Next” per completare l'installazione.

![Img](./media/t004.png)

![Img](./media/t005.png)


D. Se desideri modificare il percorso di installazione di Thonny, fai clic su “Browse...” per selezionare un nuovo percorso. In caso contrario, continua a fare clic su “Next”.

![Img](./media/t006.png)

![Img](./media/t007.png)

E. Spunta “Create desktop icon”, vedrai Thonny sul tuo desktop.

![Img](./media/t008.png)

F. “Install”.

![Img](./media/t009.png)

G. Attendi un po' ma non fare clic su “Cancel”.

![Img](./media/t010.png)

H. Quando vedi l'interfaccia di successo, fai clic su “Finish”.

![Img](./media/t011.png)

I. Puoi vedere l'icona sul tuo desktop se hai spuntato “Create desktop icon”:

![Img](./media/t011.png)                    

### 5.1.2 Impostazioni Base di Thonny

A. Fai doppio clic su Thonny, scegli la lingua e le impostazioni iniziali e fai clic su “Let’s go!”.

![Img](./media/t013.png)

![Img](./media/t014.png)

![Img](./media/t015.png)

B. Fai clic su “**View**”→“**File**” e “**Shell**”.

![Img](./media/t016.png)

![Img](./media/t017.png)

![Img](./media/t018.png)

### 5.1.3 Carica Firmware Micropython (Importante)

Per eseguire un programma Python sulla scheda Micro:bit, dobbiamo prima caricarvi il firmware.

**Carica il firmware Micropython:**

Collega il Micro:bit al tuo PC con un cavo USB.

![Img](./media/A800.png)

Assicurati che il driver sia stato installato correttamente e che la porta COM possa essere identificata correttamente. Apri “**Gestione Dispositivi**” ed espandi “**Porte**”.

![Img](./media/t019.png)

Il numero della porta COM può variare a seconda dei computer.

Apri Thonny, fai clic su “**run**” e “**Configure interpreter...**”

![Img](./media/t020.png)

Seleziona “Micropython (BBC micro:bit)” e “mbeb Serial Port @ COM16” nel suo interprete, e fai clic su “Install or update firmware”.

![Img](./media/t021.png)

E vedrai quanto segue. Imposta “Target volume” su “MICROBIT”, “MicroPython family” su “nRF52”, “variant” su “BBC micro:bit v2 (original simplifiled API)”, “version” su “2.1.2”, e poi “Install”.

Se il firmware non si installa, premi il pulsante di reset sul Micro:bit e fai clic su “Install”.

![Img](./media/t022.png)

Dopodiché, fai clic su “Close” e “OK”.

![Img](./media/t023.png)

Chiudi tutte le finestre e torna alla pagina principale e fai clic sull'icona “STOP”:

![Img](./media/t024.png)

### 5.1.4 Carica Codice

**Esegui il codice di test (online)**

Il Micro:bit esegue il codice online quando deve essere collegato al computer. Gli utenti possono programmare e debuggare programmi con Thonny.

Apri Thonny e fai clic su "**Open**".

![Img](./media/t025.png)

Quando si apre una nuova finestra, apri ".\MicroPython_Resource\Codes\Heart beat", seleziona “heartbeat&ZeroWidthSpace;.py”, e fai clic su “Run current script” (se vengono segnalati errori, fai clic prima su ![Img](./media/t027.png) e poi su “Run current script”), e vedrai un cuore che batte sul Micro:bit.

![Img](./media/t026.png)

Nota: Quando lo esegui online, se premi il pulsante di reset, il codice non verrà eseguito di nuovo. Se vuoi che venga eseguito dopo il reset, fai riferimento alle istruzioni di esecuzione offline qui sotto.

**Esegui il codice di test (offline)**

Dopo aver resettato Micro:bit, esegui prima il file main.py nella directory root.

Pertanto, il nome del file che carichiamo sul Micro:bit deve essere cambiato in main.py se vogliamo che esegua il codice dopo il reset. Quindi, carica il file, premi il pulsante di reset, e il codice verrà comunque eseguito.

Qui prendiamo heartbeat.py come esempio. Seleziona **heartbeat&ZeroWidthSpace;.py** per "**rinominarlo**" in main.py, e fai clic su "**OK**". Ora puoi scegliere di “**Upload to micro:bit**”.

![Img](./media/t028.png)

![Img](./media/t029.png)

![Img](./media/t030.png)

Premi il pulsante Reset e vedrai il cuore che batte sul Micro:bit.

Se vuoi eseguire altro codice (non librerie), devi prima cambiare il suo nome in main&ZeroWidthSpace;.py prima di caricarlo.

Per quanto riguarda le librerie, fai clic destro per “Upload to micro:bit” direttamente (a volte il caricamento potrebbe fallire a causa delle dimensioni troppo grandi della libreria. Quindi devi semplificarla o eliminare quelle inutilizzate).

### 5.1.5 Altre Operazioni Comuni

**Elimina file sotto Micro:bit**

In “micro:bit”, seleziona “main&ZeroWidthSpace;.py” per “Delete”, e verrà rimosso.

![Img](./media/t031.png)

La stessa procedura si applica quando si eliminano altri file.
