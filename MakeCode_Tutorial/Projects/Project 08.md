### 4.2.8 Indovina il Numero

#### 4.2.8.1 Panoramica

![Img](./media/top1.png)

In questo progetto, giochiamo a un gioco di indovinazione del numero con una scheda Micro:bit, una scheda di controllo gamepad e un display OLED. Quando il numero corretto viene indovinato, l'OLED visualizza "Great!!!"; se l'ipotesi è troppo alta o troppo bassa, mostra rispettivamente "To High!"/"To Low!", insieme all'intervallo corrispondente di numeri possibili.

![Img](./media/bottom1.png)

#### 4.2.8.2 Conoscenza dei Componenti

Questo progetto utilizza lo stesso display OLED del Progetto 07. Si prega di fare riferimento alla sezione 4.2.7.2 per la conoscenza dei suoi componenti.

#### 4.2.8.3 Parti Richieste

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **Scheda micro:bit V2** (auto-fornita) ×1 | **Smart Gamepad micro:bit** (assemblato) ×1 | **Batteria AAA** (auto-fornita) ×4 |
|![Img](./media/OLED.png)|![Img](./media/7008.png)||
|**Display OLED** (auto-fornito)×1 |**Cavo DuPont F-F**(auto-fornito) x4||

#### 4.2.8.4 Schema di Cablaggio

![Img](./media/jiexian8.png)

**Dopo aver cablato come mostrato sopra, inserisci la micro:bit nello slot sulla scheda di controllo del gamepad.**

| Display OLED | Scheda di controllo gamepad micro:bit | Pin scheda micro:bit |
| :--: | :--: | :--: |
| GND | GND | GND |
| VCC | 3V | 3V |
| SDA | SDA | P20 |
| SCL | SCL | P19 |

#### 4.2.8.5 Flusso del Codice

![Img](./media/8001.png)

#### 4.2.8.6 Codice di Test

⚠️ **Nota che qui è inclusa la libreria OLED, quindi dobbiamo importare: https://github.com/keyestudio/pxt-environment-kit-master**.

**Codice completo:**

![Img](./media/8002.png)

![Img](./media/line1.png)

**Breve spiegazione:**

① Inizializza il bit flag di aggiornamento dello schermo, imposta la variabile mode a 0 (0-prontezza di gioco, 1-gioco in corso) e inizializza la visualizzazione dello schermo OLED.

![Img](./media/8003.png)

② Durante la preparazione del gioco, imposta l'intervallo di ipotesi, il valore di ipotesi iniziale, il valore target e l'ipotesi.

![Img](./media/8004.png)

③ Aggiorna l'intervallo di valori e il valore di ipotesi sull'OLED. Visualizza i prompt corrispondenti quando il bit flag dello stato del risultato cambia: "To High!" quando state=1; "To Low!" quando state=2; e "Great!!!" quando state=3.

E imposta la modalità sulla prontezza di gioco e attendi 1000 millisecondi (1s).

![Img](./media/8005.png)

④ Premi C e il valore di ipotesi temp+1; se il valore di ipotesi supera il massimo, impostalo come nuovo massimo.

Premi E e il valore di ipotesi temp-1; se il valore di ipotesi è inferiore al minimo, impostalo come nuovo minimo.

![Img](./media/8006.png)

⑤ Premi D per confrontare il valore di ipotesi con il valore target. Se temp è maggiore, registra il nuovo massimo max2 e inserisci lo Stato 1; se temp è minore, registra il nuovo minimo min2 e inserisci lo Stato 2; se entrambi i valori sono uguali, vai allo Stato 3.

Infine, aggiorna il display con un ritardo di 1000 millisecondi.

![Img](./media/8007.png)

#### 4.2.8.7 Risultato del Test

![Img](./media/4top.png)

Dopo aver caricato il codice, inserisci la scheda micro:bit nello slot del gamepad (**batterie installate**) e sposta l'interruttore su “ON”.

Dopo aver caricato il codice, l'OLED si inizializza e mostra l'intervallo di valori di “num: 1 ~ 100” e l'ipotesi iniziale di 50. Puoi premere C per temp+1 (max di 100) o E per temp-1 (min di 1) per cambiare il tuo valore di ipotesi sull'OLED.

Premi D per inviare il tuo valore, e temp verrà confrontato con il valore target casuale. Se temp>value, mostra “To High!” e assegna temp a max2; se temp<value, mostra “To Low!” e assegnalo a min2. Se sei troppo fortunato che temp=value, vedrai “Great!!!” per 1s.

Dopo di che, il gioco verrà resettato e verrà impostato un nuovo valore target. Giochiamo un altro round!

![Img](./media/8000.gif)

⚠️ **Il blocco di costruzione nel Risultato del Test non è incluso in questo kit di prodotti.**

<span style="color: rgb(0, 209, 0);">**Suggerimento:** Se non c'è risposta sulla scheda, premi il pulsante di reset sul retro della scheda micro:bit.</span>

![Img](./media/4bottom.png)
