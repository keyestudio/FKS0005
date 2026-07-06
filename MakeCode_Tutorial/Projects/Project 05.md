### 4.2.5 Evita i Mattoni

#### 4.2.5.1 Panoramica

![Img](./media/top1.png)

In questo progetto, giochiamo a un gioco di evitamento dei mattoni in cui i giocatori usano un gamepad Micro:bit per muovere il loro indicatore LED a sinistra e a destra mentre evitano i mattoni che cadono dall'alto. Ci sono tre stati: a) un'icona dinamica all'avvio, b) azioni di evitamento in tempo reale durante il gioco, e c) un punteggio finale dopo le collisioni.

I giocatori guadagnano 1 punto dopo ogni evitamento (quando il mattone raggiunge il fondo), e il gioco finisce quando si scontrano con un mattone; il punteggio finale viene visualizzato con un effetto di scorrimento.

Il gioco può essere avviato o resettato premendo entrambi i pulsanti A+B. Questo meccanismo di gioco semplice combina la reattività in tempo reale con l'anticipazione strategica.

![Img](./media/bottom1.png)

#### 4.2.5.2 Parti Richieste

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **Scheda micro:bit V2** (auto-fornita) ×1 | **Smart Gamepad micro:bit** (assemblato) ×1 | **Batteria AAA** (auto-fornita) ×4 |

#### 4.2.5.3 Flusso del Codice

![Img](./media/5001.png)

#### 4.2.5.4 Codice di Test

⚠️ **Nota che la soglia iniziale 300 nel codice può essere modificata in base alle proprie esigenze. Più alto è il valore, più lentamente cadrà il mattone.**

**Codice completo:**

![Img](./media/5002.png)

![Img](./media/line1.png)

**Breve spiegazione:**

① Inizializza le variabili correlate, inclusa la colonna iniziale del giocatore, la riga e la velocità del mattone, e imposta la posizione del giocatore sulla colonna iniziale.

Chiama una funzione on_start.

![Img](./media/5003.png)

② Per quanto riguarda questa funzione, fa apparire il mattone in una colonna casuale da 0 a 4 all'inizio del gioco.

![Img](./media/5004.png)

③ Determina se “A+B è premuto e il gioco non è iniziato”. Se sì e l'avvio è contrassegnato come stato iniziale, contrassegna prima lo stato di avvio e conferma di nuovo se i pulsanti sono ancora premuti dopo un breve ritardo. Se lo sono, resetta il gioco (chiama la funzione reset_game) e registra il tempo. Altrimenti, annulla il contrassegno di avvio.

![Img](./media/5005.png)

④ La seguente funzione resetta il gioco allo stato iniziale. Imposta lo stato su “gaming” (game_state=1) e posiziona il giocatore nella posizione iniziale. E il mattone apparirà in una colonna casuale (0~4) e nella riga 0, e i punteggi si azzereranno. Infine, la pressione di A/B è contrassegnata come non attivata, e la matrice viene quindi cancellata.

![Img](./media/5006.png)

⑤ Quando lo stato del gioco è **0-stato iniziale** (non in gioco dopo l'accensione), l'icona visualizzata lampeggerà.

![Img](./media/5007.png)

⑥ Quando è **2-game over**, il punteggio sarà controllato in base al conteggio dei lampeggi (flash_count). Se il conteggio <3, ripete “mostra punteggio → breve ritardo → cancella display → breve ritardo → conteggio+1”; quando il conteggio raggiunge 3, mostra sempre il punteggio ed estende il ritardo.

![Img](./media/5008.png)

⑦ Nello stato **1-gaming**, quando si preme C senza attivare il contrassegno di pressione e la colonna del giocatore > 0, la colonna del giocatore -1 e contrassegna il pulsante C come attivato (con ritardo per anti-jitter); premere E senza attivare e quando la colonna del giocatore < 4, e la colonna +1 con E attivato (ritardo); se non viene eseguita alcuna azione, il contrassegno di attivazione dei pulsanti corrispondenti viene resettato.

![Img](./media/5009.png)

⑧ Calcola la differenza tra il tempo corrente e l'ultimo tempo di movimento del mattone. Se questa differenza supera la soglia di velocità del mattone, aggiorna il tempo di movimento del mattone e la riga del mattone +1. Se la riga > 4 (raggiungendo il bordo), resetta il mattone a una colonna casuale con la sua riga=zero, e punteggio+1.

Chiama le funzioni di rilevamento delle collisioni e di rendering della grafica del gioco per far cadere i mattoni, resettare dopo aver raggiunto il bordo, accumulare il punteggio e aggiornare lo stato del gioco in tempo reale.

Invoca le funzioni di rilevamento delle collisioni e di rendering della grafica del gioco per ottenere l'avanzamento automatico dei mattoni, il reset del bordo, l'accumulo del punteggio e gli aggiornamenti dello stato del gioco in tempo reale.

![Img](./media/5010.png)

⑨ Determina se il gioco è finito: prima controlla se “la colonna del mattone corrisponde a quella del giocatore” e “se la riga del mattone corrisponde a quella del giocatore”. Se entrambe le condizioni sono soddisfatte (cioè, i mattoni si sovrappongono al giocatore), imposta il gioco allo stato 2 (game over), cancella il display e resetta il conteggio dei lampeggi.

“Game over in caso di collisione.”

![Img](./media/5011.png)

⑩ Renderizza gli elementi visivi del gioco: prima cancella il display, e poi traccia i punti con una luminosità di 255 (Giocatore) alle posizioni fisse della riga e della colonna corrente del giocatore; se il gioco è iniziato (game_state=1), traccia i punti con una luminosità di 85 (mattone) alla riga e alla colonna del mattone. Così possiamo distinguere i mattoni dal giocatore in base alla loro luminosità.

![Img](./media/5012.png)

#### 4.2.5.5 Risultato del Test

![Img](./media/4top.png)

Dopo aver caricato il codice, inserisci la scheda micro:bit nello slot del gamepad (**batterie installate**) e sposta l'interruttore su “ON”.

È nello **stato iniziale 0** dopo l'accensione e la matrice lampeggia due icone quadrate.

Premi A e B (per almeno 1 secondo) per avviare il gioco (nello **stato 1-gaming**), e un mattone cadrà in una colonna casuale. Ora puoi muoverti a sinistra/destra premendo C/E. Ogni volta che eviti un mattone, il punteggio +1.

Game over in caso di collisione (**2-game over**), e il punteggio finale verrà visualizzato sulla matrice. Se vuoi giocare un altro round, premi di nuovo A e B. Spegni per uscire dal gioco (sposta l'interruttore DIP su “OFF”).

![Img](./media/5000.gif)

<span style="color: rgb(0, 209, 0);">**Suggerimento:** Se non c'è risposta sulla scheda, premi il pulsante di reset sul retro della scheda micro:bit.</span>

![Img](./media/4bottom.png)
