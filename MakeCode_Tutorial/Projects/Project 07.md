### 4.2.7 Temperatur- und Feuchtigkeitsmesser

#### 4.2.7.1 Übersicht

![Img](./media/top1.png)

In diesem Projekt bauen wir ein Temperatur- und Feuchtigkeitsüberwachungssystem mit einem Micro:bit board, einem Gamepad, einem XHT11 Temperatur- und Feuchtigkeitssensor und einem OLED display. Der XHT11 Sensor misst die Umgebungstemperatur und -feuchtigkeit, während das OLED display die Messwerte in Echtzeit aktualisiert. Die Steuerplatine des Gamepads erleichtert die Schaltungserweiterung und stabile Verbindungen, wodurch das System als einfaches Thermometer fungieren kann.

![Img](./media/bottom1.png)

#### 4.2.7.2 Komponentenwissen

![Img](./media/2top.png)

**XHT11 Temperatur- und Feuchtigkeitssensor**

![Img](./media/XHT11.png)

Der XHT11 Temperatur- und Feuchtigkeitssensor gibt digitale Signale aus und verwendet spezielle analoge Signalakquisition und -umwandlung sowie fortschrittliche Temperatur- und Feuchtigkeitssensor-Techniken, um eine ausgezeichnete Langzeitstabilität und hohe Zuverlässigkeit zu gewährleisten.

Er enthält hochpräzise resistive Feuchtigkeits- und Thermistor-Temperatursensoren, integriert mit einem 8-Bit-Hochleistungs-Mikrocontroller.

**XHT11 Kommunikationsmodus:**

Er verwendet eine vereinfachte Single-Bus-Kommunikation. Der Single-Bus besteht aus einer einzigen Datenleitung, über die der gesamte Datenaustausch und die Steueroperationen innerhalb des Systems durchgeführt werden.

- Single-Bus Übertragungsdatenbit:

  - Single-Bus Datenformat: Überträgt 40 Bit Daten auf einmal, höchstes Bit zuerst.

  - 8-Bit Integer Feuchtigkeitsdaten + 8-Bit Dezimal Feuchtigkeitsdaten + 8-Bit Integer Temperaturdaten + 8-Bit Dezimal Temperaturdaten + 8-Bit Paritätsbit.

    **Hinweis: Der Dezimalteil der Feuchtigkeit ist 0**.

- Paritätsbit:

  - 8-Bit Integer Feuchtigkeitsdaten + 8-Bit Dezimal Feuchtigkeitsdaten + 8-Bit Integer Temperaturdaten + 8-Bit Dezimal Temperaturdaten

    Das 8-Bit Paritätsbit ist das letzte 8 Bit des Ergebnisses.

![Img](./media/7001.png)

Datensequenzdiagramm des XH11 Temperatur- und Feuchtigkeitssensors:

Nachdem der Benutzer-Host (MCU) ein Startsignal gesendet hat, wechselt der XHT11 vom Low-Power-Modus in den High-Speed-Modus, und nachdem dieses Signal endet, sendet der XHT11 ein Antwortsignal und 40-Bit-Daten und löst eine Signalakquisition aus.

Das Signal wird wie in der Abbildung gezeigt gesendet:

![Img](./media/7002.png)

⚠️ **Tipp:** Die vom Host vom XHT11 Sensor gelesenen Temperatur- und Feuchtigkeitsdaten sind immer die Werte der vorherigen Messung. Wenn zwischen zwei Messungen ein langer Intervall liegt, nehmen Sie bitte zwei aufeinanderfolgende Messungen vor; der Wert beim zweiten Mal ist der tatsächliche.

**Schaltplan:**

![Img](./media/cou73-2.png)

**Parameter:**

- Betriebsspannung: DC 3V~5V
- Betriebsstrom: (Max)2.5mA
- Maximale Leistung: 0.0125W
- Temperaturbereich: -25 ~ +60°C (±2℃)
- Feuchtigkeitsbereich: 5 ~ 95%RH (Genauigkeit um 25C° beträgt ±5%RH)
- Ausgangssignal: digital bidirektionaler Single-Bus

**OLED display**

![Img](./media/A636.png)

OLED bietet außergewöhnliche Vorteile wie reiche Farbwiedergabe, hohen Kontrast und weite Betrachtungswinkel. Bilder darauf sind klar und lebendig, mit besonders herausragendem Schwarz. Jedes Pixel ist selbstleuchtend und benötigt keine Hintergrundbeleuchtung, was zu einem relativ geringen Stromverbrauch führt. Der 0.9-inch OLED Bildschirm ist mit seiner kompakten Größe, hohen Auflösung (128×64 Pixel) und geringem Stromverbrauch ideal für Anwendungen in eingebetteten Systemen und tragbaren Geräten.

⚠️ **Hinweis**: Für dieses OLED display ist die SDA Schnittstelle mit Pin P20 auf dem Micro:bit board verbunden, während die SCL mit Pin P19 verbunden ist.

**Parameter:**

- Betriebsspannung: DC 3V - 5V
- Betriebsstrom: 30mA
- Schnittstelle: Pin mit einem Abstand von 2.54mm
- Kommunikationsmodus: I2C communication
- Interner Treiberchip: SSD1306
- Auflösung: 128×64
- Betrachtungswinkel: Größer als 150°

#### 4.2.7.3 Benötigte Teile

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 board** (selbst mitzubringen) ×1 | **micro:bit Smart Gamepad** (montiert) ×1 |**AAA battery** (selbst mitzubringen) ×4 |
|![Img](./media/XHT11.png)|![Img](./media/OLED.png)|![Img](./media/7008.png)|
|**XHT11 temperature and humidity sensor** (selbst mitzubringen)×1|**OLED display** (selbst mitzubringen)×1 |**F-F DuPont wire**(selbst mitzubringen) x7|

#### 4.2.7.4 Schaltplan

![Img](./media/jiexian.png)

**Nachdem die Verkabelung wie oben gezeigt abgeschlossen ist, stecken Sie das micro:bit in den Steckplatz auf der Gamepad-Steuerplatine.**

| OLED display | micro:bit gamepad control board |micro:bit board pin |
| :--: | :--: | :--: |
| GND | GND | GND |
| VCC | 3V | 3V |
| SDA | SDA | P20 |
| SCL | SCL | P19 |

| XHT11 temperature and humidity sensor | micro:bit gamepad control board | micro:bit board pin |
| :--: | :--: | :--: |
| G | GND | GND |
| V | 3V | 3V |
| S | 12 | P12 |

#### 4.2.7.5 Code-Ablauf

![Img](./media/7003.png)

#### 4.2.7.6 Testcode
⚠️ **Beachten Sie, dass hier OLED und DHT11 libraries enthalten sind, daher müssen wir importieren: https://github.com/keyestudio/pxt-environment-kit-master**.

**Vollständiger Code:**

![Img](./media/7004.png)

![Img](./media/line1.png)

**Kurze Erklärung:**

① Initialisieren Sie die Pixel des OLED und löschen Sie es, setzen Sie die 5×5LED matrix so, dass ![Img](./media/1006.png) angezeigt wird, und definieren Sie die Werte für Temperatur und Feuchtigkeit auf 0.

![Img](./media/7005.png)

② Weisen Sie die entsprechenden Messwerte des XHT11 sensors den Variablen temperature und humidity zu.

![Img](./media/7006.png)

③ Das OLED zeigt die Messwerte des XHT11 sensors an.

![Img](./media/7007.png)

④ Verzögerung 500ms (0.5s).

![Img](./media/cou28.png)

#### 4.2.7.7 Testergebnis

![Img](./media/4top.png)

Nach dem Brennen des Codes stecken Sie das micro:bit board in den Steckplatz des Gamepads (**Batterien eingelegt**) und schalten Sie es auf „ON“.

Nach dem Hochladen des Codes auf das micro:bit board zeigt das OLED die vom XHT11 sensor gelesene Temperatur und Feuchtigkeit in Echtzeit an.

![Img](./media/7000.gif)

<span style="color: rgb(0, 209, 0);">**Tipp:** Wenn das Board nicht reagiert, drücken Sie bitte die Reset-Taste auf der Rückseite des micro:bit board.</span>

![Img](./media/4bottom.png)
