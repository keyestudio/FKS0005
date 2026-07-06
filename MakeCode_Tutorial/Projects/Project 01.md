### 4.2.1 Indicatore di Direzione

#### 4.2.1.1 Panoramica

![Img](./media/top1.png)

Quando si muove il joystick, la matrice di punti visualizza frecce nella direzione corrispondente in tempo reale: sinistra, destra, su, giù, fornendo un chiaro riferimento di direzione.

![Img](./media/bottom1.png)

#### 4.2.1.2 Conoscenza dei Componenti

![Img](./media/2top.png)

**Matrice di punti Micro:bit:**

![Img](./media/1001.png)

La matrice di punti LED della scheda micro:bit è composta da un totale di 25 diodi a emissione di luce, un gruppo di 5, corrispondenti agli assi X e Y, formando una matrice 5×5. Ciascuno è posizionato all'intersezione della riga (X) e della colonna (Y). Possiamo controllare uno o alcuni di essi impostando i punti coordinati.

**Joystick:**

| ![Img](./media/1002.png)| ![Img](./media/1003.png) |
| :--: | :--: |
| Prodotto reale | Schema schematico |

La struttura interna di questo joystick è composta da due resistori regolabili (potenziometri) con un valore di resistenza di 10KΩ ciascuno.

Rileva le direzioni (e l'ampiezza) della spinta tramite il pin analogico ADC del microcontrollore per emettere i segnali elettrici analogici della dimensione corrispondente. Durante la lettura effettiva del segnale, quando i valori analogici degli assi X e Y del joystick vengono rilevati nell'intervallo 450~600, si può determinare che il joystick è in uno stato neutro (fermo) senza attivazione attiva.

![Img](./media/2bottom.png)

#### 4.2.1.3 Parti Richieste

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png)|
| :--: | :--: | :--: |
| **Scheda micro:bit V2** (auto-fornita) ×1 | **Smart Gamepad micro:bit** (assemblato) ×1 |**Batteria AAA** (auto-fornita) ×4 |


#### 4.2.1.4 Flusso del Codice

![Img](./media/1008.png)

#### 4.2.1.5 Codice di Test

⚠️ **Nota che i seguenti codici includono le librerie Makecode del Gamepad (il modo per aggiungere le librerie è stato menzionato in precedenza). La sensibilità del joystick può essere regolata in base alle proprie esigenze.**

**Codice completo:**

![Img](./media/1004.png)


![Img](./media/line1.png)

**Breve spiegazione:**

① Inizializza la matrice LED per farla mostrare ![Img](./media/1006.png).


![Img](./media/1005.png)


② Leggi i valori degli assi X e Y per determinare la direzione di movimento. Se viene rilevata, la matrice mostra la freccia corrispondente. In caso contrario, visualizza ![Img](./media/1006.png).

![Img](./media/1007.png)


#### 4.2.1.6 Risultato del Test

![Img](./media/4top.png)

Dopo aver caricato il codice, inserisci la scheda micro:bit nello slot del gamepad (**batterie installate**) e sposta l'interruttore su “ON”.

Quando spingi il joystick del gamepad, puoi vedere le frecce corrispondenti sulla matrice. Se alzi il dito per riportarlo al centro, apparirà un'icona a forma di casa sulla matrice.

![Img](./media/1009.gif)

<span style="color: rgb(0, 209, 0);">**Suggerimento:** Se non c'è risposta sulla scheda, premi il pulsante di reset sul retro della scheda micro:bit.</span>

![Img](./media/4bottom.png)
