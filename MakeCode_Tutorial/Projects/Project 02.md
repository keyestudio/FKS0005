### 4.2.2 Colorful Lights

#### 4.2.2.1 Übersicht

![Img](./media/top1.png)

RGB-LEDs sind eine Art LED-Lichtquelle, die Bilder durch Mischen von Licht der drei Grundfarben Rot, Grün und Blau erzeugt, deren Überlagerung verschiedene Farbtöne ergibt. Gängige Methoden umfassen das direkte Mischen der Grundfarben, die Verwendung einer blauen LED in Kombination mit gelbem Phosphor oder den Einsatz einer ultravioletten LED zusammen mit RGB-Phosphor. Im Vergleich zu LEDs, die direkt weißes Licht aussenden, bieten RGB-LEDs aufgrund der unabhängigen Regelung der drei Grundfarben ein größeres Farbmischspektrum.

In diesem Projekt entspricht jede Taste einem anderen Modus der RGB-LEDs. Wenn Sie die Taste C drücken, blinken die Lichter abwechselnd in der Reihenfolge „rot, grün, blau, gelb und lila“; drücken Sie D, um auf Atemlicht umzuschalten; drücken Sie E für fließende Lichter; drücken Sie F für Lauflichteffekte.

Bunte Lichterketten für Festdekorationen, Weihnachtsbaumbeleuchtung, RGB-Streifen zur Alltagsatmosphäre, LED-Dekolichter in Vergnügungsparks und Einkaufszentren ... Sie sind alle gängige Beispiele für Mehrfachmodi-Leuchten in unserem Alltag.

![Img](./media/bottom1.png)

#### 4.2.2.2 Komponentenwissen

![Img](./media/2top.png)

**SK6812 RGB LED**

| ![Img](./media//2001.png)| ![Img](./media//2002.png)|
| :--: | :--: |
| Real product | Schematic diagram |

Der SK6812 ist eine extern gesteuerte LED-Lichtquelle, die Steuer- und Beleuchtungsschaltungen integriert. Sein Hauptbestandteil sind 5×5 mm oberflächenbeleuchtete LED-Perlen, jede fungiert als unabhängiges Pixel und beinhaltet mehrere Kernschaltungen: eine digitale Schnittstellen-Datenlatch-Schaltung, Signalformungs- und Verstärkungsantriebs-Schaltung, Spannungsregelungs-Schaltung, integrierte Konstantstromschaltung und einen hochpräzisen RC-Oszillator.

Die Kommunikation verwendet ein einpoliges Null-Rückkehr-Codierungsprotokoll. Nach dem Power-On-Reset empfängt jedes Pixel Daten vom Controller über den DIN-Anschluss. Die ersten 24 Bits werden vom ersten Pixel extrahiert und im internen Datenlatch gespeichert, während die verbleibenden Bits intern geformt und verstärkt werden, bevor sie über den DOUT-Anschluss an nachfolgende Pixel weitergeleitet werden. Mit jeder verarbeiteten Pixel werden die zu übertragenden Daten um 24 Bits reduziert.

Auf dem Gamepad befinden sich vier SK6812 RGB-Leuchten. Diese unterstützen alle eine 256-stufige Helligkeitsregelung über ihre Rot-, Grün- und Blaukanäle, wodurch 256×256×256 Farbkombinationen möglich sind. Daher liefern sie vielfältige Lichteffekte wie abwechselndes Blinken, Atemverläufe und Laufanimationen und bieten eine anschaulichere und lebendigere Interaktion.

**Taste**

| ![Img](./media//2003.png)| ![Img](./media//2004.png)|
| :--: | :--: |
| Real product | Schematic diagram |

Die Taste, die erstmals in Japan auftauchte, wurde als empfindlicher Schalter bezeichnet. Bei Betätigung drücken Sie den Schalter, wodurch der Stromkreis geschlossen wird. Beim Loslassen öffnet sich der Schalter wieder. Sein inneres Metall-Federblatt wechselt bei Krafteinwirkung seinen Verbindungszustand zwischen geschlossen und offen.

Es gibt vier Tasten, die jeweils unabhängig an einen Pin auf der micro:bit-Platine angeschlossen sind. Wenn eine Taste gedrückt wird, erzeugt der Stromkreis ein entsprechendes Signal mit niedrigem Pegel, wodurch die micro:bit schnell auf Befehle reagieren kann und die Bedienung dadurch deutlich komfortabler und genauer wird.

![Img](./media/2bottom.png) 

#### 4.2.2.3 Benötigte Teile

| ![Img](./media/microbitV2.png)|  ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 board** (self-provided) ×1 | **micro:bit Smart Gamepad** (assembled) ×1 |**AAA battery** (self-provided) ×4 |

#### 4.2.2.4 Programmablauf

![Img](./media/2006.png)

#### 4.2.2.5 Testcode

⚠️ **Hinweis: Die Verzögerungszeit der MODE\*_DELAY in den Codes kann nach Ihren Bedürfnissen angepasst werden.**

**Vollständiger Code:**

![Img](./media/2005.png)

![Img](./media/line1.png)

**Kurze Erklärung:**

① Zu Beginn deaktivieren Sie die LED-Funktion (Set led enable to false). Definieren Sie vier LED-Verzögerungen (z. B. MODE2Delay = 5, MODE1Delay = 500 ...), setzen Sie die Entprellzeit der Tasten auf 20. Initialisieren Sie vier RGB-LEDs am Pin P8 auf keine Farbe (setzen Sie alle Werte auf 0), d. h. ausschalten.

![Img](./media/2009.png)

② Innerhalb der Schleife wird die Entprellung implementiert, indem geprüft wird, ob die Differenz zwischen der aktuellen Ausführungszeit und der vorherigen Druckzeit den voreingestellten Entprell-Schwellenwert (BTN_DEBOUNCE) überschreitet. Damit werden Mehrfachauslösungen durch mechanisches Prellen verhindert.

![Img](./media/2010.png)

③ Wenn Sie C(/D/E/F) drücken, wird der Modus auf 1(2/3/4) gesetzt; gleichzeitig werden die Animationsschritte und die zeitlichen Startpunkte des entsprechenden Modus zurückgesetzt, die Lichter gelöscht und der Zeitstempel der Taste aktualisiert. Dadurch ist ein präziser Wechsel und die Initialisierung der verschiedenen LED-Modi gewährleistet.

| ![Img](./media/2011.png)|![Img](./media/2012.png)|
| :--: | :--: |
|Button C is pressed|Button D is pressed|
| ![Img](./media/2013.png)    |     ![Img](./media/2014.png)   |
|Button E is pressed|Button F is pressed|

④ Wenn der Modus auf 1 gesetzt ist und das Intervall zwischen der aktuellen Zeit und der vorherigen Moduszeit MODE1Delay überschreitet, wird zuerst der Modus-Zeitstempel aktualisiert und die Lichter entsprechend den verschiedenen Werten von model_step (0–4) nacheinander angezeigt: Rot, Grün, Blau, Gelb und Lila. Nach der Aktualisierung wird model_step durch eine Modulo-Operation zyklisch zurückgesetzt, sodass diese fünf Farben regelmäßig wechseln.

![Img](./media/2015.png)

⑤ Wenn der Modus 2 aktiv ist und das Intervall zur vorherigen Moduszeit MODE2_DELAY überschreitet, wird zuerst der Modus-Zeitstempel aktualisiert und der Farbwert (Hue) zyklisch um 1 erhöht (Modulobereich 0–359). Dann werden die Lichter gelöscht und der entsprechende Farbton mit hoher Sättigung (99) und niedriger Helligkeit (20) angezeigt, wodurch sich die Farbverläufe sanft ändern. (Helligkeits- und Sättigungswerte im Code können bei Bedarf angepasst werden.)

![Img](./media/2016.png)

⑥ Wenn der Modus 3 aktiv ist und das Intervall zur vorherigen Moduszeit MODE3_DELAY überschreitet, wird zuerst der Modus-Zeitstempel aktualisiert und alle Pixel des Lichtstreifens um eine Position verschoben. Dem Pixel 0 wird ein zufälliger Farbton (0–359), hohe Sättigung (99) und niedrige Helligkeit (20) zugewiesen. Nach Aktualisierung der Anzeige sehen Sie ein fließendes Licht: Die Lichter bewegen sich nacheinander und wechseln zufällig die Farbe. (Helligkeits- und Sättigungswerte im Code können bei Bedarf angepasst werden.)

![Img](./media/2017.png)

⑦ Wenn der Modus 4 aktiv ist und das Intervall zur vorherigen Moduszeit MODE4_DELAY überschreitet, wird zuerst der Modus-Zeitstempel aktualisiert und der Lichtstreifen gelöscht. Den Pixeln entsprechend model_step werden zufällige Farbtöne (0–359) mit hoher Sättigung (99) und niedriger Helligkeit (20) zugewiesen, und die Anzeige wird aktualisiert. Schließlich wird model_step innerhalb von 0–3 per Modulo zyklisch durchlaufen, sodass einzelne LEDs nacheinander in zufälligen Farben aufleuchten. (Helligkeits- und Sättigungswerte im Code können bei Bedarf angepasst werden.)

![Img](./media/2018.png)

#### 4.2.2.6 Testergebnis

![Img](./media/4top.png)

Nachdem Sie den Code aufgespielt haben, stecken Sie die micro:bit-Platine in den Schlitz des Gamepads (**Batterien eingelegt**), und schalten Sie den Schalter darauf auf „ON“.

Drücken Sie **C**: die Lichter wechseln nacheinander zwischen **Rot–Grün–Blau–Gelb–Lila**.

Drücken Sie **D**: der Farbton der Lichter erhöht sich und die Farbverläufe ändern sich schließlich sanft.

Drücken Sie **E**: die Lichter erzeugen von Pixel 0 aus eine zufällige Farbe, die sich dann pixelweise verschiebt, so dass ein fließendes Licht entsteht.

Drücken Sie **F**: jedes Pixel leuchtet nacheinander in zufälligen Farben auf.

![Img](./media/2019.gif)

<span style="color: rgb(0, 209, 0);">**Tipp:** Wenn das Board nicht reagiert, drücken Sie bitte die Reset-Taste auf der Rückseite der micro:bit-Platine.</span>

![Img](./media/4bottom.png)