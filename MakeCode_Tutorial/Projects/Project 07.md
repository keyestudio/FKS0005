### 4.2.7 Misuratore di Temperatura e Umidità

#### 4.2.7.1 Panoramica

![Img](./media/top1.png)

In questo progetto, costruiamo un sistema di monitoraggio della temperatura e dell'umidità con una scheda Micro:bit, un gamepad, un sensore di temperatura e umidità XHT11 e un display OLED. Il sensore XHT11 misura la temperatura e l'umidità ambiente, mentre il display OLED aggiorna le letture in tempo reale. La scheda di controllo del gamepad facilita l'espansione del circuito e le connessioni stabili, consentendo al sistema di funzionare come un semplice termometro.

![Img](./media/bottom1.png)

#### 4.2.7.2 Conoscenza dei Componenti

![Img](./media/2top.png)

**Sensore di temperatura e umidità XHT11**

![Img](./media/XHT11.png)

Il sensore di temperatura e umidità XHT11 emette segnali digitali e impiega un'acquisizione e conversione del segnale analogico specializzata, tecniche avanzate di rilevamento della temperatura e dell'umidità per garantire un'eccellente stabilità a lungo termine e un'elevata affidabilità.

Incorpora sensori di umidità resistivi e termistori di temperatura ad alta precisione, integrati con un microcontrollore a 8 bit ad alte prestazioni.

**Modalità di comunicazione XHT11:**

Impiega una comunicazione single-bus semplificata. Il single-bus è costituito da una singola linea dati, attraverso la quale vengono eseguite tutte le operazioni di scambio dati e controllo all'interno del sistema.

- Bit di dati di trasmissione single-bus:

  - Formato dati single-bus: Trasmette 40 bit di dati alla volta, bit più significativo per primo.

  - 8 bit di dati di umidità interi + 8 bit di dati di umidità decimali + 8 bit di dati di temperatura interi + 8 bit di dati di temperatura decimali + 8 bit di parità.

    **Nota: La parte decimale dell'umidità è 0**.

- Bit di parità:
  
  - 8 bit di dati di umidità interi + 8 bit di dati di umidità decimali + 8 bit di dati di temperatura interi + 8 bit di dati di temperatura decimali
  
    Il bit di parità a 8 bit è l'ultimo 8 bit del risultato.

![Img](./media/7001.png)

Diagramma della sequenza dati del sensore di temperatura e umidità XH11:

Dopo che l'host utente (MCU) invia un segnale di avvio, l'XHT11 passa dalla modalità a basso consumo alla modalità ad alta velocità, e dopo la fine di questo segnale, l'XHT11 invia un segnale di risposta e 40 bit di dati, e attiva un'acquisizione del segnale.

Il segnale viene inviato come mostrato nella figura:

![Img](./media/7002.png)

⚠️ **Suggerimento:** I dati di temperatura e umidità letti dall'host dal sensore XHT11 sono sempre i valori della misurazione precedente. Se c'è un lungo intervallo tra due misurazioni, si prega di effettuare due letture consecutive; il valore della seconda volta sarà quello effettivo.

**Schema schematico:**

![Img](./media/cou73-2.png)

**Parametri:**

- Tensione operativa: DC 3V~5V
- Corrente operativa: (Max)2.5mA
- Potenza massima: 0.0125W
- Intervallo di temperatura: -25 ~ +60°C (±2℃)
- Intervallo di umidità: 5 ~ 95%RH (Precisione intorno a 25°C è ±5%RH)
- Segnale di uscita: single-bus digitale bidirezionale

**Display OLED**

![Img](./media/A636.png)

L'OLED offre vantaggi eccezionali come una ricca riproduzione dei colori, un contrasto elevato e ampi angoli di visione. Le immagini su di esso sono chiare e vivide, con un nero particolarmente eccezionale. Ogni pixel è auto-emissivo senza bisogno di retroilluminazione, con conseguente consumo energetico relativamente basso. Lo schermo OLED da 0,9 pollici, con le sue dimensioni compatte, l'alta risoluzione (128×64 pixel) e il basso consumo energetico, è ideale per applicazioni in sistemi embedded e dispositivi indossabili.

⚠️ **Nota**: Per questo display OLED, l'interfaccia SDA è collegata al pin P20 sulla scheda Micro:bit, mentre l'SCL è collegata al pin P19.

**Parametri:**

- Tensione operativa: DC 3V - 5V
- Corrente operativa: 30mA
- Interfaccia: Pin con spaziatura di 2.54mm
- Modalità di comunicazione: comunicazione I2C
- Chip di pilotaggio interno: SSD1306
- Risoluzione: 128×64
- Angolo di visione: Maggiore di 150°

#### 4.2.7.3 Parti Richieste

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **Scheda micro:bit V2** (auto-fornita) ×1 | **Smart Gamepad micro:bit** (assemblato) ×1 | **Batteria AAA** (auto-fornita) ×4 |
|![Img](./media/XHT11.png)|![Img](./media/OLED.png)|![Img](./media/7008.png)|
|**Sensore di temperatura e umidità XHT11** (auto-fornito)×1|**Display OLED** (auto-fornito)×1 |**Cavo DuPont F-F**(auto-fornito) x7|


#### 4.2.7.4 Schema di Cablaggio

![Img](./media/jiexian.png)

**Dopo aver cablato come mostrato sopra, inserisci la micro:bit nello slot sulla scheda di controllo del gamepad.**

| Display OLED | Scheda di controllo gamepad micro:bit | Pin scheda micro:bit |
| :--: | :--: | :--: |
| GND | GND | GND |
| VCC | 3V | 3V |
| SDA | SDA | P20 |
| SCL | SCL | P19 |

| Sensore di temperatura e umidità XHT11 | Scheda di controllo gamepad micro:bit | Pin scheda micro:bit |
| :--: | :--: | :--: |
| G | GND | GND |
| V | 3V | 3V |
| S | 12 | P12 |


#### 4.2.7.5 Flusso del Codice

![Img](./media/7003.png)

#### 4.2.7.6 Codice di Test
⚠️ **Nota che qui sono incluse le librerie OLED e DHT11, quindi dobbiamo importare: https://github.com/keyestudio/pxt-environment-kit-master**.

**Codice completo:**

![Img](./media/7004.png)

![Img](./media/line1.png)

**Breve spiegazione:**

① Inizializza i pixel dell'OLED e cancellalo, imposta la matrice 5×5LED per mostrare ![Img](./media/1006.png), e definisci i valori di temperatura e umidità a 0.

![Img](./media/7005.png)

② Assegna le letture corrispondenti del sensore XHT11 alle variabili temperatura e umidità.

![Img](./media/7006.png)

③ L'OLED mostra le letture del sensore XHT11.

![Img](./media/7007.png)

④ Ritardo 500ms (0.5s).

![Img](./media/cou28.png)

#### 4.2.7.7 Risultato del Test

![Img](./media/4top.png)

Dopo aver caricato il codice, inserisci la scheda micro:bit nello slot del gamepad (**batterie installate**) e sposta l'interruttore su “ON”.

Dopo aver caricato il codice sulla scheda micro:bit, l'OLED mostra in tempo reale la temperatura e l'umidità lette dal sensore XHT11.

![Img](./media/7000.gif)

<span style="color: rgb(0, 209, 0);">**Suggerimento:** Se non c'è risposta sulla scheda, premi il pulsante di reset sul retro della scheda micro:bit.</span>

![Img](./media/4bottom.png)
