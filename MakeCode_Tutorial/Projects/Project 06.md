### 4.2.6 Sasso-Carta-Forbici

#### 4.2.6.1 Panoramica

![Img](./media/top1.png)

Qui, giochiamo a sasso-carta-forbici tramite comunicazione wireless di micro:bit. I giocatori selezionano la loro mossa (sasso, carta o forbici) tramite i pulsanti, con scambio di dati tra i dispositivi. Il gioco segue il meglio di tre; se tutti e tre i round finiscono in parità o vittoria-sconfitta-parità, viene attivata una quarta partita.

Ogni risultato viene visualizzato sulla matrice micro:bit (W per vittoria, L per sconfitta, = per parità) e rivelato dalle luci RGB (verde per vittoria, rosso per sconfitta, giallo per parità) sul pin P8. Al completamento di un round, i due dispositivi resettano tutti i dati e le luci, preparandosi per la partita successiva.

Il gameplay integra perfettamente l'interazione wireless con il combattimento multi-round.

![Img](./media/bottom1.png)

#### 4.2.6.2 Conoscenza dei Componenti

![Img](./media/2top.png)

**Comunicazione wireless Microbit**

![Img](./media/6001.png)

La scheda micro:bit integra due comode capacità di comunicazione wireless: **radio a 2.4GHz** e **Bluetooth a bassa energia (BLE)**. Tuttavia, non possono essere utilizzate contemporaneamente.

La prima non richiede accoppiamento e supporta fino a 255 pacchetti indipendenti per minimizzare le interferenze, con un raggio di comunicazione di 10-30 metri, consentendo una rapida trasmissione di dati digitali e stringhe. Mentre la seconda è utilizzata principalmente per l'accoppiamento con smartphone, tablet e altri dispositivi intelligenti per applicazioni IoT come il caricamento di dati da sensori e il controllo remoto tramite app mobile.

Espandono le possibilità di sviluppo creativo della micro:bit.

#### 4.2.6.3 Parti Richieste

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **Scheda micro:bit V2** (auto-fornita) ×2 | **Smart Gamepad micro:bit** (assemblato) ×2 | **Batteria AAA** (auto-fornita) ×8 |

#### 4.2.6.4 Flusso del Codice

![Img](./media/6002.png)

#### 4.2.6.5 Codice di Test

**Codice completo:**

![Img](./media/6003.png)

![Img](./media/line1.png)

**Breve spiegazione:**

① Inizializza la radio e imposta il gruppo su '1'; imposta il numero di round, lo stato, l'avversario e il risultato di sasso-carta-forbici dei giocatori; collega le quattro luci RGB al pin P8 e aggiorna il display, imposta la matrice per mostrare ![Img](./media/6004.png).

![Img](./media/6005.png)

② Determina l'esito del round corrente: se la tua scelta corrisponde a quella dell'avversario (**1/2/3 per forbici/sasso/carta**), è un pareggio; altrimenti, seleziona un vincitore (forbici contro carta contro sasso contro forbici), il valore del round +1 e memorizza il risultato.

![Img](./media/6006.png)

③ Memorizza i risultati in un array e visualizza la stringa corrispondente. Se questa è la terza partita, determina se è necessaria una quarta partita (in caso di parità o vittoria-sconfitta-parità). In tal caso, visualizza "FINAL" e attendi 1 secondo prima di cancellare la selezione sasso-carta-forbici.

![Img](./media/6007.png)

Altrimenti, mostra "WINNER" per la vittoria, "LOSER" per la sconfitta e "TIE" per un pareggio. Dopo un ritardo di 3 secondi, chiama la funzione resetGame per cancellare tutte le variabili di gioco.

Se la partita consiste in quattro giochi, visualizza "GAME OVER" e chiama di nuovo la funzione resetGame dopo un ritardo di 3 secondi per resettare tutte le variabili di gioco.

![Img](./media/6008.png)

Se il gioco non è finito, mostra ![Img](./media/6004.png) e cancella le scelte di entrambi.

![Img](./media/6009.png)

④ Premi C e la scheda invia "1" come forbici, e la matrice mostra ![Img](./media/6011.png); premi D e la scheda invia "3" come carta, e la matrice mostra ![Img](./media/6012.png); Premi E e invia "2" come sasso e mostra ![Img](./media/6013.png).

![Img](./media/6010.png)

⑤ Ricevi i dati radio (scelta dell'avversario).

![Img](./media/6014.png)

⑥ Determina se è necessario un quarto round. Se tutti e tre i giochi finiscono in parità o vittoria-sconfitta-parità, è necessario un quarto gioco; altrimenti, non è necessario.

![Img](./media/6015.png)

⑦ Le luci RGB visualizzano i colori corrispondenti in base all'esito: verde per la vittoria, rosso per la sconfitta e giallo per un pareggio.

![Img](./media/6016.png)

⑧ Quando il gioco finisce, cancella il display delle quattro luci RGB.

![Img](./media/6017.png)

⑨ Resetta lo stato del gioco, cancella tutti i valori delle variabili di gioco, resetta le luci RGB e mostra ![Img](./media/6004.png).

![Img](./media/6018.png)


#### 4.2.6.6 Risultato del Test

![Img](./media/4top.png)

Dopo aver caricato il codice, inserisci la scheda micro:bit nello slot del gamepad (**batterie installate**) e sposta l'interruttore su “ON”.

La matrice mostra inizialmente ![Img](./media/6004.png). I giocatori premono i pulsanti per selezionare la loro mossa (E per sasso, D per carta o C per forbici), con scambio di dati tra i due dispositivi. Determinano l'esito del round corrente: una vittoria è indicata dalla "W" con la luce RGB che diventa verde, un pareggio dalla "=" con la luce gialla e una sconfitta dalla "L" con la luce rossa (la prima luce RGB si accende dopo il primo round, e così via). Il round successivo seguirà se il gioco non è finito.

Il gioco adotta il meglio di tre: se tutti e tre i round finiscono in parità o vittoria-sconfitta-parità, viene attivata una quarta partita.

Se c'è un vincitore dopo tre round, visualizzerà "WINNER" per la vittoria e "LOSER" per la sconfitta. Una volta mostrato il risultato, apparirà "GAME OVER" per resettare il gioco. Se il quarto round rimane indeciso, anche il gioco sarà finito.

![Img](./media/6000.gif)

<span style="color: rgb(0, 209, 0);">**Suggerimento:** Attendi che l'icona a forma di cuore appaia prima di continuare il round successivo. Se non c'è risposta sulla scheda, premi il pulsante di reset sul retro della scheda micro:bit.</span>

![Img](./media/4bottom.png)
