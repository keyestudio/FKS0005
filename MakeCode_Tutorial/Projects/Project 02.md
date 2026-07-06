### 4.2.2 Luci Colorate

#### 4.2.2.1 Panoramica

![Img](./media/top1.png)

I LED RGB sono un tipo di sorgente luminosa a LED che crea immagini mescolando la luce dei tre colori primari: rosso, verde e blu, la cui intersezione produce varie tonalità. I metodi comuni includono la miscelazione diretta dei colori primari, l'utilizzo di un LED blu combinato con fosforo giallo, o l'impiego di un LED ultravioletto insieme a fosforo RGB. Rispetto ai LED che emettono luce bianca direttamente, i LED RGB offrono una gamma più ampia di possibilità di miscelazione dei colori perché i tre colori primari possono essere controllati indipendentemente.

In questo progetto, ogni pulsante corrisponde a una diversa modalità dei LED RGB. Quando si preme il pulsante C, le luci lampeggiano alternativamente nell'ordine di "rosso, verde, blu, giallo e viola"; premere D per passare alle luci a respiro; premere E per le luci a flusso d'acqua; premere F per le luci a scorrimento.

Stringhe di luci colorate per decorazioni festive, luci per alberi di Natale, strisce RGB per l'ambiente quotidiano, luci decorative a LED nei parchi di divertimento e nei centri commerciali... Sono tutti esempi comuni di luci multimodali nella nostra vita quotidiana.

![Img](./media/bottom1.png)

#### 4.2.2.2 Conoscenza dei Componenti

![Img](./media/2top.png)

**LED RGB SK6812**

| ![Img](./media//2001.png)| ![Img](./media//2002.png)|
| :--: | :--: |
| Prodotto reale | Schema schematico |

L'SK6812 è una sorgente luminosa a LED controllata esternamente che integra circuiti di controllo e illuminazione. La sua parte principale è costituita da perle LED illuminate in superficie da 5x5 mm, ciascuna funzionante come un pixel indipendente che incorpora più circuiti centrali: un circuito di latch dati con interfaccia digitale intelligente, un circuito di pilotaggio per la modellazione e l'amplificazione del segnale, un circuito di regolazione dell'alimentazione, un circuito a corrente costante integrato e un oscillatore RC ad alta precisione.

La sua comunicazione impiega un protocollo di codice a ritorno a zero a polarità singola. Al ripristino all'accensione, ogni pixel riceve i dati dal controller tramite la porta DIN. I primi 24 bit di dati vengono estratti dal pixel iniziale e memorizzati nel latch dati interno, mentre i restanti vengono modellati e amplificati internamente prima di essere trasmessi attraverso la porta DOUT ai pixel successivi. Con ogni pixel elaborato, la dimensione del segnale trasmesso diminuisce di 24 bit.

Sul gamepad, ci sono quattro luci RGB SK6812. Queste supportano tutte la regolazione della luminosità a 256 livelli attraverso i loro canali rosso, verde e blu, consentendo combinazioni di colori 256×256×256. Grazie a ciò, offre diversi effetti di illuminazione come lampeggi alternati, gradienti a respiro e animazioni a scorrimento, fornendo interazioni più intuitive e vivide.

**Pulsante**

| ![Img](./media//2003.png)| ![Img](./media//2004.png)|
| :--: | :--: |
| Prodotto reale | Schema schematico |

Il pulsante, apparso per la prima volta in Giappone, era chiamato interruttore sensibile. Durante il funzionamento, premere l'interruttore per applicare forza e chiudere il circuito. Al rilascio della pressione, l'interruttore si apre. La sua lamina metallica interna cambia il suo stato di connessione/disconnessione in risposta alla forza applicata.

Ci sono quattro pulsanti, ciascuno collegato indipendentemente a un pin sulla scheda micro:bit. Quando un pulsante viene premuto, il circuito genera un segnale di basso livello corrispondente, consentendo alla micro:bit di rispondere rapidamente ai comandi e migliorando significativamente la comodità e la precisione dell'interazione.

![Img](./media/2bottom.png)

#### 4.2.2.3 Parti Richieste

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **Scheda micro:bit V2** (auto-fornita) ×1 | **Smart Gamepad micro:bit** (assemblato) ×1 |**Batteria AAA** (auto-fornita) ×4 |

#### 4.2.2.4 Flusso del Codice

![Img](./media/2006.png)

#### 4.2.2.5 Codice di Test

⚠️ **Nota che il tempo di ritardo di MODE\*_DELAY nei codici può essere modificato in base alle proprie esigenze.**

**Codice completo:**

![Img](./media/2005.png)

![Img](./media/line1.png)

**Breve spiegazione:**

① All'inizio, disabilita la funzione dei LED (imposta led enable su false).

E definisci 4 ritardi LED (ad esempio, imposta 5 in modalità 2, imposta 500 in modalità 1...), imposta il debounce del pulsante su 20. Inizializza quattro LED RGB sul pin P8 a nessun colore (imposta tutti i valori a 0), cioè, imposta su spento.

![Img](./media/2009.png)

② Durante il ciclo, l'operazione anti-jitter viene implementata controllando se la differenza tra il tempo di esecuzione corrente e il tempo di pressione precedente supera la soglia anti-jitter preimpostata (BTN_DEBOUNCE), prevenendo così pressioni ripetute causate da jitter fisico.


![Img](./media/2010.png)


③ Quando C(/D/E/F) viene premuto, la modalità viene impostata su 1(2/3/4), mentre i passaggi dell'animazione e i punti di inizio temporizzazione per la modalità corrispondente vengono resettati, le luci vengono cancellate e il timestamp del pulsante viene aggiornato. Ciò consente una commutazione precisa e un funzionamento iniziale di diverse modalità LED.


| ![Img](./media/2011.png)|![Img](./media/2012.png)|
| :--: | :--: |
|Pulsante C premuto|Pulsante D premuto|
| ![Img](./media/2013.png) | ![Img](./media/2014.png) |
|Pulsante E premuto|Pulsante F premuto|

④ Quando la modalità è impostata su 1 e l'intervallo tra il tempo corrente e il tempo della modalità precedente supera MODE1Delay, aggiorna prima il timestamp della modalità e visualizza le luci in base ai diversi valori di model_step (0–4) in sequenza: rosso, verde, blu, giallo e viola. Dopo aver aggiornato la visualizzazione, resetta il ciclo model_step con un'operazione modulo per cambiare regolarmente questi cinque colori.

![Img](./media/2015.png)

⑤ Quando la modalità è 2 e l'intervallo tra il tempo corrente e il tempo della modalità precedente supera MODE2_DELAY, aggiorna prima il timestamp della modalità e incrementa ciclicamente il valore del colore (tonalità) tramite modulo (intervallo 0–359). Quindi, cancella la luce e visualizza la tonalità corrispondente con alta saturazione (99) e bassa luminosità (20), e i colori sfumati cambieranno fluidamente. (I valori di luminosità e saturazione nei codici possono essere regolati secondo necessità.)

![Img](./media/2016.png)

⑥ Quando la modalità è 3 e l'intervallo tra il tempo corrente e il tempo della modalità precedente supera MODE3_DELAY, aggiorna prima il timestamp della modalità e sposta tutti i pixel della striscia luminosa di 1 bit, assegna una tonalità casuale (0–359), alta saturazione (99) e bassa luminosità (20) al pixel 0. Aggiorna la visualizzazione e potrai vedere una luce fluida: le luci si muovono sequenzialmente e cambiano colore casualmente. (I valori di luminosità e saturazione nel codice possono essere regolati secondo necessità.)

![Img](./media/2017.png)

⑦ Quando la modalità è 4 e l'intervallo tra il tempo corrente e il tempo della modalità precedente supera MODE4_DELAY, aggiorna prima il timestamp della modalità e cancella la striscia luminosa, assegna una tonalità casuale (0–359), alta saturazione (99) e bassa luminosità (20) ai pixel corrispondenti a model_step, e aggiorna la visualizzazione. Infine, cicla model_step tra 0-3 tramite modulo, e vedrai un singolo LED accendersi sequenzialmente con colori casuali. (I valori di luminosità e saturazione nel codice possono essere regolati secondo necessità.)

![Img](./media/2018.png)

#### 4.2.2.6 Risultato del Test

![Img](./media/4top.png)

Dopo aver caricato il codice, inserisci la scheda micro:bit nello slot del gamepad (**batterie installate**) e sposta l'interruttore su “ON”.

Premi **C**: le luci si alternano tra **rosso-verde-blu-giallo-viola** in sequenza.

Premi **D**: la tonalità del colore delle luci aumenterà, e alla fine i colori sfumati cambieranno fluidamente.

Premi **E**: le luci generano un colore casuale a partire dal pixel 0, e spostano il colore di un pixel sequenzialmente, in modo da poter vedere una luce a flusso d'acqua.

Premi **F**: ogni pixel si accende con colori casuali in sequenza.

![Img](./media/2019.gif)

<span style="color: rgb(0, 209, 0);">**Suggerimento:** Se non c'è risposta sulla scheda, premi il pulsante di reset sul retro della scheda micro:bit.</span>

![Img](./media/4bottom.png)
