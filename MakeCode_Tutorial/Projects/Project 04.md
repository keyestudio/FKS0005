### 4.2.4 Lettore Musicale

#### 4.2.4.1 Panoramica

![Img](./media/top1.png)

Qui costruiamo un lettore musicale che genera suoni tramite il buzzer integrato sulla scheda micro:bit (non riproduce musica vocale). Dispone di una libreria di 20 brevi tracce e supporta sia la riproduzione sequenziale che casuale.

In modalità sequenziale, premendo il pulsante C (Canzone precedente) o E (Canzone successiva) si cambiano le tracce secondo una sequenza preimpostata fino a raggiungere la fine dell'elenco; mentre in modalità casuale, ogni pressione seleziona una traccia a caso tra i 20 suoni con le luci colorate che lampeggiano, e quando una canzone finisce si ferma immediatamente.

Nel frattempo, la matrice LED micro:bit visualizza la modalità di riproduzione corrente in tempo reale.

![Img](./media/bottom1.png)

#### 4.2.4.2 Parti Richieste

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **Scheda micro:bit V2** (auto-fornita) ×1 | **Smart Gamepad micro:bit** (assemblato) ×1 | **Batteria AAA** (auto-fornita) ×4 |

#### 4.2.4.3 Flusso del Codice

![Img](./media/4001.png)

#### 4.2.4.4 Codice di Test

**Codice completo:**

![Img](./media/4002.png)

![Img](./media/line1.png)

**Breve spiegazione:**

① Inizializza la matrice LED e il volume del suono, collega il pin RGB a P8 e imposta il numero di RGB a 4.

![Img](./media/4003.png)

② Inizializza l'array della melodia a 20 e aggiungi le loro tracce dettagliate, e imposta il volume iniziale.

![Img](./media/4004.png)

③ Determina se il pulsante D o F è premuto. Premi D per '0-riproduzione sequenziale', F per '1-riproduzione casuale'.

![Img](./media/4005.png)

④ In modalità sequenziale, premi C per riprodurre la canzone precedente, E per passare alla canzone successiva.

![Img](./media/4006.png)

Poiché ci sono solo 20 tracce nell'array, può essere riprodotta solo musica dal N.O. 0-19. Quindi aggiungiamo una condizione if per evitare overflow e underflow dell'array.

![Img](./media/4007.png)

In modalità casuale, invece, premi C/E per mescolare tutte queste 20 canzoni.

![Img](./media/4008.png)

⑤ Determina se la canzone precedente è incoerente con quella attuale. In caso affermativo, ferma prima quella attuale e poi riproduci quella.

![Img](./media/4009.png)

⑥ Controlla se la modalità è '0-riproduzione sequenziale', mostrando '![Img](./media/4010.png)', o '1-riproduzione casuale', mostrando '![Img](./media/4011.png)', con un ritardo di 100ms.

![Img](./media/4012.png)

⑦ Fai respirare le luci RGB in sottofondo.

![Img](./media/4013.png)

⑧ Premi A per aumentare il volume (+10); premi B per diminuirlo (-10). Il volume del buzzer micro:bit è deciso dalla tensione di uscita del pin interno collegato. Possiamo controllare il volume convertendo i valori digitali 0~255 in valori analogici tramite DAC.

![Img](./media/4014.png)

#### 4.2.4.5 Risultato del Test

![Img](./media/4top.png)

Dopo aver caricato il codice, inserisci la scheda micro:bit nello slot del gamepad (**batterie installate**) e sposta l'interruttore su “ON”.

Dopo l'accensione, è in modalità sequenziale per impostazione predefinita e riprodurrà la canzone al N.O. “0”. Una volta terminata, puoi premere C per l'ultima canzone o E per la successiva.

Premi F per passare alla modalità casuale. E puoi premere D per tornare a quella sequenziale. In modalità F, una traccia casuale di queste 20 verrà riprodotta se premi C/E. Dopo aver terminato, si ferma.

Le luci RGB respirano sempre dal momento dell'accensione. Nel frattempo, la matrice LED micro:bit mostra “![Img](./media/4010.png)” in modalità sequenziale e “![Img](./media/4011.png)” in modalità casuale.

Per il volume, premi A per aumentare e B per diminuire.

![Img](./media/4015.gif)

<span style="color: rgb(0, 209, 0);">**Suggerimento:** Se non c'è risposta sulla scheda, premi il pulsante di reset sul retro della scheda micro:bit.</span>

![Img](./media/4bottom.png)
