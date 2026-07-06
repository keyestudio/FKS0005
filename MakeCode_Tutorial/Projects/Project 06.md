### 4.2.6 Schere-Stein-Papier

#### 4.2.6.1 Übersicht

![Img](./media/top1.png)

Hier spielen wir Schere-Stein-Papier mittels drahtloser Kommunikation von micro:bit. Spieler wählen ihren Zug (Stein, Papier oder Schere) über die Tasten, wobei Daten zwischen den Geräten ausgetauscht werden. Das Spiel folgt dem Best-of-Three-Prinzip; wenn alle drei Runden unentschieden oder Sieg-Niederlage-Unentschieden enden, wird ein viertes Spiel ausgelöst.

Jedes Ergebnis wird auf der micro:bit Matrix angezeigt (W für Sieg, L für Niederlage, = für Unentschieden) und durch die RGB-Lichter (grün für Sieg, rot für Niederlage, gelb für Unentschieden) an Pin P8 enthüllt. Nach Abschluss einer Runde setzen die beiden Geräte alle Daten und Lichter zurück und bereiten sich auf das nächste Spiel vor.

Das Gameplay integriert nahtlos drahtlose Interaktion mit dem Mehrrunden-Kampf.

![Img](./media/bottom1.png)

#### 4.2.6.2 Komponentenwissen

![Img](./media/2top.png)

**Microbit drahtlose Kommunikation**

![Img](./media/6001.png)

Das micro:bit board integriert zwei praktische drahtlose Kommunikationsmöglichkeiten: **2.4GHz radio** und **low-power Bluetooth (BLE)**. Sie können jedoch nicht gleichzeitig verwendet werden.

Ersteres erfordert keine Kopplung und unterstützt bis zu 255 unabhängige Pakete, um Interferenzen zu minimieren, mit einer Kommunikationsreichweite von 10–30 Metern, was eine schnelle Übertragung von digitalen Daten und Zeichenketten ermöglicht. Letzteres wird hauptsächlich für die Kopplung mit Smartphones, Tablets und anderen smarten Geräten für IoT-Anwendungen wie Sensor-Daten-Upload und mobile App-Fernsteuerung verwendet.

Sie erweitern die kreativen Entwicklungsmöglichkeiten des micro:bit.

#### 4.2.6.3 Benötigte Teile

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 board** (selbst mitzubringen) ×2 | **micro:bit Smart Gamepad** (montiert) ×2 |**AAA battery** (selbst mitzubringen) ×8 |

#### 4.2.6.4 Code-Ablauf

![Img](./media/6002.png)

#### 4.2.6.5 Testcode

**Vollständiger Code:**

![Img](./media/6003.png)

![Img](./media/line1.png)

**Kurze Erklärung:**

① Initialisieren Sie das radio und setzen Sie die Gruppe auf '1'; setzen Sie die Anzahl der Runden, den Status, den Gegner und das Schere-Stein-Papier-Ergebnis der Spieler; verbinden Sie die vier RGB-Lichter mit Pin P8 und aktualisieren Sie die Anzeige, setzen Sie die Matrix so, dass ![Img](./media/6004.png) angezeigt wird.

![Img](./media/6005.png)

② Bestimmen Sie das Ergebnis der aktuellen Runde: Wenn Ihre Wahl mit der des Gegners übereinstimmt (**1/2/3 für Schere/Stein/Papier**), ist es ein Unentschieden; andernfalls wählen Sie einen Gewinner (Schere gegen Papier gegen Stein gegen Schere), Rundenwert +1 und speichern Sie das Ergebnis.

![Img](./media/6006.png)

③ Speichern Sie die Ergebnisse in einem Array und zeigen Sie die entsprechende Zeichenkette an. Wenn dies das dritte Spiel ist, bestimmen Sie, ob ein viertes Spiel benötigt wird (bei komplettem Unentschieden oder Sieg-Niederlage-Unentschieden). Wenn ja, zeigen Sie „FINAL“ an und warten Sie 1 Sekunde, bevor Sie die Schere-Stein-Papier-Auswahl löschen.

![Img](./media/6007.png)

Andernfalls zeigen Sie „WINNER“ für Sieg, „LOSER“ für Niederlage und „TIE“ für ein Unentschieden an. Nach einer 3-sekündigen Verzögerung rufen Sie die resetGame-Funktion auf, um alle Spielvariablen zu löschen.

Wenn das Spiel aus vier Spielen besteht, zeigen Sie „GAME OVER“ an und rufen Sie die resetGame-Funktion nach einer 3-sekündigen Verzögerung erneut auf, um alle Spielvariablen zurückzusetzen.

![Img](./media/6008.png)

Wenn das Spiel nicht vorbei ist, wird ![Img](./media/6004.png) angezeigt und die Auswahl beider Spieler gelöscht.

![Img](./media/6009.png)

④ Drücken Sie C und das board sendet „1“ als Schere, und die Matrix zeigt ![Img](./media/6011.png); drücken Sie D und das board sendet „3“ als Papier, und die Matrix zeigt ![Img](./media/6012.png); Drücken Sie E und es sendet „2“ als Stein und zeigt ![Img](./media/6013.png).

![Img](./media/6010.png)

⑤ Empfangen Sie radio Daten (Wahl des Gegners).

![Img](./media/6014.png)

⑥ Bestimmen Sie, ob eine vierte Runde erforderlich ist. Wenn alle drei Spiele unentschieden oder Sieg-Niederlage-Unentschieden enden, ist ein viertes Spiel notwendig; andernfalls wird es nicht benötigt.

![Img](./media/6015.png)

⑦ Die RGB-Lichter zeigen die entsprechenden Farben basierend auf dem Ergebnis an: grün für Sieg, rot für Niederlage und gelb für ein Unentschieden.

![Img](./media/6016.png)

⑧ Wenn das Spiel endet, löschen Sie die Anzeige der vier RGB-Lichter.

![Img](./media/6017.png)

⑨ Setzen Sie den Spielzustand zurück, löschen Sie alle Spielvariablenwerte, setzen Sie die RGB-Lichter zurück und zeigen Sie ![Img](./media/6004.png) an.

![Img](./media/6018.png)

#### 4.2.6.6 Testergebnis

![Img](./media/4top.png)

Nach dem Brennen des Codes stecken Sie das micro:bit board in den Steckplatz des Gamepads (**Batterien eingelegt**) und schalten Sie es auf „ON“.

Die Matrix zeigt zunächst ![Img](./media/6004.png) an. Spieler drücken Tasten, um ihren Zug auszuwählen (E für Stein, D für Papier oder C für Schere), wobei die Spieldaten zwischen den beiden Geräten ausgetauscht werden. Sie bestimmen das Ergebnis der aktuellen Runde: Ein Sieg wird durch „W“ mit grün leuchtendem RGB-Licht angezeigt, ein Unentschieden durch „=“ mit gelbem Licht und eine Niederlage durch „L“ mit rotem Licht (das erste RGB-Licht leuchtet nach der ersten Runde auf, und so weiter). Die nächste Runde folgt, wenn das Spiel nicht beendet ist.

Das Spiel wird im Best-of-Three-Modus gespielt: Wenn alle drei Runden unentschieden oder Sieg-Niederlage-Unentschieden enden, wird ein viertes Spiel ausgelöst.

Wenn es nach drei Runden einen Gewinner gibt, wird „WINNER“ für den Sieg und „LOSER“ für die Niederlage angezeigt. Sobald das Ergebnis angezeigt wird, erscheint „GAME OVER“, um das Spiel zurückzusetzen. Wenn die vierte Runde unentschieden bleibt, ist das Spiel ebenfalls beendet.

![Img](./media/6000.gif)

<span style=\"color: rgb(0, 209, 0);\">**Tipp:** Warten Sie, bis das Herzsymbol erscheint, bevor Sie die nächste Runde fortsetzen. Wenn das Board nicht reagiert, drücken Sie bitte die Reset-Taste auf der Rückseite des micro:bit board.</span>

![Img](./media/4bottom.png)
