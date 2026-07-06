### 4.2.9 Auto Robot Mecanum 4WD Controllata da Gamepad Micro:bit

#### 4.2.9.1 Panoramica

![Img](./media/top1.png)
In questo progetto, controlliamo un Robot Car Mecanum 4WD con una scheda di controllo gamepad e una scheda Micro:bit. Il joystick consente all'auto di andare avanti, indietro, girare a sinistra e a destra; il pulsante C sposta l'auto lateralmente a sinistra, il D lateralmente a destra, l'E accelera e il tasto F decelera (con un intervallo di velocità di 20–95). Quando non viene eseguita alcuna operazione, l'auto rimane ferma.

![Img](./media/bottom1.png)

#### 4.2.9.2 Parti Richieste

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **Scheda micro:bit V2** (auto-fornita) ×1 | **Smart Gamepad micro:bit** (assemblato) ×1 |**Batteria AAA** (auto-fornita) ×4 |
| ![Img](./media/che.png) | ![Img](./media/18650.png) ||
| **Kit KS4034**(auto-fornito) ×1 | **Batteria 18650**(auto-fornita) ×2 ||

Per informazioni dettagliate sul Robot Car Mecanum 4WD**(KS4034)**, visitare [qui](https://docs.keyestudio.com/projects/KS4034/en/latest/).
#### 4.2.9.3 Schema di Cablaggio

Si prega di fare riferimento alle istruzioni di cablaggio nella documentazione KS4034 per collegare il Robot Car Mecanum 4WD e il gamepad tramite comunicazione radio. Non è richiesto alcun cablaggio fisico tra i due; entrambi i dispositivi comunicano in modalità wireless.

#### 4.2.9.4 Flusso del Codice
⚠️ **Nota che la seguente libreria deve essere importata durante la programmazione dei codici dell'auto: https://github.com/keyestudio2019/mecanum_robot_v2**.

**Flusso del codice del gamepad:**

![Img](./media/9001.png)

**Flusso del codice dell'auto:**

![Img](./media/9002.png)

#### 4.2.9.5 Codice di Test

**Codice completo del gamepad:**

![Img](./media/9003.png)

![Img](./media/line1.png)

**Breve spiegazione:**

① Inizializza il gruppo radio a 1 con una potenza di trasmissione del segnale di 7; visualizza un'icona a forma di cuore e imposta le variabili SEND_INTERCAL a 100 e BTN_DEBOUNCE_TIME a 20.

![Img](./media/9004.png)

② Imposta la variabile currentCmd (variabile del contenuto dell'istruzione) sul carattere '0' e assegna i valori degli assi X e Y del joystick alle variabili rockerX e rockerY, rispettivamente.

![Img](./media/9005.png)

③ Controlla se il joystick o il pulsante hanno un'operazione corrispondente. Se si verifica un'operazione, imposta la variabile currentCmd (variabile del contenuto dell'istruzione) sul carattere corrispondente (R/U/L/D/A/B/Z/X); altrimenti, lasciala invariata.

![Img](./media/9006.png)

④ Controlla se currentCmd (variabile del contenuto dell'istruzione) differisce da lastCmd (memorizza il contenuto dell'istruzione precedente). In caso affermativo, invia currentCmd, imposta lastCmd su currentCmd e attendi un ritardo specificato.

![Img](./media/9007.png)

**Codice completo dell'auto:**

![Img](./media/9008.png)

![Img](./media/line1.png)

**Breve spiegazione:**

① Inizializza il gruppo radio a 1 con una potenza di trasmissione del segnale di 7; visualizza un'icona a forma di cuore e imposta le variabili SPEED a 50, MIN_SPEED a 20 e MAX_speed a 95.

![Img](./media/9009.png)

② Ricevi il valore del comando inviato dalla radio e memorizza il comando nella variabile item.

![Img](./media/9010.png)

③ In base ai comandi dei caratteri (U/L/D/R/A/B) ricevuti da item, chiama le funzioni corrispondenti per controllare l'auto per andare avanti, indietro, girare a sinistra, a destra, e spostarsi a sinistra e a destra.

![Img](./media/9011.png)

④ In base al comando del carattere (Z/X) ricevuto da item, l'auto viene accelerata o decelerata di conseguenza.

Durante l'accelerazione, la velocità è impostata al minimo tra SPEED+5 e MAX_speed (per evitare di superare MAX_speed); durante la decelerazione, la velocità è impostata al massimo tra SPEED-5 e MIN_speed (per evitare di scendere al di sotto di MIN_speed).

![Img](./media/9012.png)

⑤ Qui sono definite sei funzioni di controllo del movimento del veicolo:

- car_back controlla tutti e quattro i motori per ruotare all'indietro per andare indietro;
- car_forward controlla tutti e quattro i motori per ruotare in avanti per avanzare;
- car_left realizza la svolta a sinistra dell'auto impostando i motori laterali sinistri all'indietro e i motori laterali destri in avanti;
- car_right realizza la svolta a destra impostando i motori laterali destri all'indietro e i motori laterali sinistri in avanti;
- car_left_move e car_right_move consentono lo spostamento a sinistra e a destra tramite la rotazione coordinata dei motori diagonali.

Tutte le funzioni prendono la variabile SPEED come parametro di velocità del motore.

![Img](./media/9013.png)

#### 4.2.9.6 Risultato del Test

![Img](./media/4top.png)

Dopo aver caricato il codice, inserisci la scheda micro:bit nello slot del gamepad (**batterie installate**) e sposta l'interruttore su “ON”.

Caricando questi codici su due schede Micro:bit, rispettivamente del gamepad e dell'auto, e assicurati che le batterie siano sufficientemente cariche. Inserisci le Micro:bit corrispondenti nel gamepad e nell'auto e sposta gli interruttori su entrambi su "ON".

Ora puoi controllare l'auto tramite il gamepad: spingi il joystick verso l'alto e l'auto si muove in avanti, spingilo verso il basso per muoversi all'indietro, a sinistra la fa girare a sinistra e a destra la fa girare a destra. Possiamo anche controllare l'accelerazione (premi il pulsante E)/decelerazione (premi il pulsante F), lo spostamento a sinistra (C) e lo spostamento a destra (D) dell'auto. Nota che l'intervallo di velocità è 20–95.

![Img](./media/9000.gif)

<span style="color: rgb(0, 209, 0);">**Suggerimento:** Se non c'è risposta sulla scheda, premi il pulsante di reset sul retro della scheda micro:bit.</span>

![Img](./media/4bottom.png)

