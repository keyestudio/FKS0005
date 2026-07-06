### 4.2.3 Semplice Pianoforte Elettronico

#### 4.2.3.1 Panoramica

![Img](./media/top1.png)

In questo progetto, controlliamo l'altoparlante micro:bit per riprodurre toni diversi azionando il joystick e premendo i pulsanti. Nel frattempo, la matrice LED a bordo mostrerà i numeri corrispondenti.

Girando il joystick a destra si produce "Do (Tono Do Centrale)" con la visualizzazione che mostra "1"; girandolo a sinistra si produce "Re (Tono Re)" con "2"; girandolo verso l'alto si produce "Mi (Tono Mi)" con "3"; girandolo verso il basso si produce "Fa (Tono Fa)" con "4". Premendo il pulsante C si produce "Sol (Tono Sol)" con "5", premendo D si produce "La (Tono La)" con "6", E produce "Si (Tono Si)" con "7", e premendo F si produce un "Do (Diesis)" più alto mentre la visualizzazione torna a "1". C'è una bella sincronizzazione tra joystick, pulsanti, toni e display.

![Img](./media/bottom1.png)

#### 4.2.3.2 Conoscenza dei Componenti

![Img](./media/2top.png)

**Altoparlante Microbit**

![Img](./media/j901.png)

La scheda micro:bit è dotata di un altoparlante integrato per emettere suoni, come risatine, saluti, sbadigli o espressioni di tristezza, o persino comporre una canzone. Programmando, può persino generare note individuali, melodie e ritmi, o persino composizioni musicali, come la canzone *Twinkle Twinkle Little Star*.

![Img](./media/2bottom.png)

#### 4.2.3.3 Parti Richieste

| **Scheda micro:bit V2** (auto-fornita) ×1 | **Smart Gamepad micro:bit** (assemblato) ×1 |**Batteria AAA** (auto-fornita) ×4 |
| :--: | :--: | :--: |
| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |

#### 4.2.3.4 Flusso del Codice

![Img](./media/3009.png)

#### 4.2.3.5 Codice di Test

⚠️ **Nota che la sensibilità del joystick può essere regolata in base alle proprie esigenze.**

**Codice completo:**

![Img](./media/3008.png)

![Img](./media/line1.png)

**Breve spiegazione:**

① Inizializza la matrice LED micro:bit per mostrare ![Img](./media/3004.png).

![Img](./media/3005.png)

② Determina la direzione del movimento del joystick; riproduci i toni corrispondenti per mezza battuta in sottofondo, e la matrice LED visualizza il numero corrispondente.

![Img](./media/3006.png)

③ Controlla se un pulsante è premuto, e riproduci il tono corrispondente per mezza battuta in sottofondo, e la matrice LED visualizza il numero corrispondente.

![Img](./media/3007.png)


#### 4.2.3.6 Risultato del Test

![Img](./media/4top.png)

Dopo aver caricato il codice, inserisci la scheda micro:bit nello slot del gamepad (**batterie installate**) e sposta l'interruttore su “ON”. La matrice LED mostra “![Img](./media/3004.png)” per prima.

Girando il joystick a destra si produce "Do (Tono Do Centrale)" con la visualizzazione che mostra "1"; girandolo a sinistra si produce "Re (Tono Re)" con "2"; girandolo verso l'alto si produce "Mi (Tono Mi)" con "3"; girandolo verso il basso si produce "Fa (Tono Fa)" con "4". Premendo il pulsante C si produce "Sol (Tono Sol)" con "5", premendo D si produce "La (Tono La)" con "6", E produce "Si (Tono Si)" con "7", e premendo F si produce un "Do (Diesis)" più alto mentre la visualizzazione torna a "1".

Hai costruito il semplice pianoforte elettronico!

![Img](./media/3010.gif)

<span style="color: rgb(0, 209, 0);">**Suggerimento:** Se non c'è risposta sulla scheda, premi il pulsante di reset sul retro della scheda micro:bit.</span>

![Img](./media/4bottom.png)
