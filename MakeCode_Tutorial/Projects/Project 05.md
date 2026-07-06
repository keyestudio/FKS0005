### 4.2.5 Ziegelsteinen ausweichen

#### 4.2.5.1 Übersicht

![Img](./media/top1.png)

In diesem Projekt spielen wir ein Ziegelstein-Ausweichspiel, bei dem die Spieler ein Micro:bit Gamepad verwenden, um ihren LED-Indikator nach links und rechts zu bewegen, während sie von oben fallenden Ziegelsteinen ausweichen. Es gibt drei Zustände: a) ein dynamisches Symbol beim Start, b) Echtzeit-Ausweichaktionen während des Spiels und c) eine Endpunktzahl nach Kollisionen.

Spieler erhalten 1 Punkt nach jedem Ausweichen (wenn der Ziegelstein den Boden erreicht), und das Spiel ist beendet, wenn sie mit einem Ziegelstein kollidieren; die Endpunktzahl wird mit einem Scrolleffekt angezeigt.

Das Spiel kann durch Drücken von A+B gestartet oder zurückgesetzt werden. Dieser unkomplizierte Spielmechanismus kombiniert Echtzeit-Reaktionsfähigkeit mit strategischer Antizipation.

![Img](./media/bottom1.png)

#### 4.2.5.2 Benötigte Teile

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 board** (selbst mitzubringen) ×1 | **micro:bit Smart Gamepad** (montiert) ×1 |**AAA battery** (selbst mitzubringen) ×4 |

#### 4.2.5.3 Code-Ablauf

![Img](./media/5001.png)

#### 4.2.5.4 Testcode

⚠️ **Beachten Sie, dass der anfängliche Schwellenwert 300 im Code je nach Ihren Bedürfnissen geändert werden kann. Je höher der Wert ist, desto langsamer fällt der Ziegelstein.**

**Vollständiger Code:**

![Img](./media/5002.png)

![Img](./media/line1.png)

**Kurze Erklärung:**

① Initialisieren Sie die zugehörigen Variablen, einschließlich der anfänglichen Spalte, Zeile und Geschwindigkeit des Ziegelsteins des Spielers, und setzen Sie die Position des Spielers auf die anfängliche Spalte.

Rufen Sie eine on_start-Funktion auf.

![Img](./media/5003.png)

② Bei dieser Funktion erscheint der Ziegelstein zu Beginn des Spiels in einer zufälligen Spalte von 0~4.

![Img](./media/5004.png)

③ Ermitteln Sie, ob „A+B gedrückt und das Spiel nicht gestartet“ ist. Wenn ja und der Start als Anfangszustand markiert ist, markieren Sie zuerst den Startzustand und bestätigen Sie nach einer kurzen Verzögerung erneut, ob die Tasten noch gedrückt sind. Wenn ja, setzen Sie das Spiel zurück (rufen Sie die reset_game-Funktion auf) und zeichnen Sie die Zeit auf. Andernfalls brechen Sie die Startmarkierung ab.

![Img](./media/5005.png)

④ Die folgende Funktion setzt das Spiel in den Anfangszustand zurück. Sie setzt den Zustand auf „Gaming“ (game_state=1) und platziert den Spieler in die Ausgangsposition. Und der Ziegelstein erscheint in einer zufälligen Spalte (0~4) und der 0. Zeile, und die Punktzahlen werden auf Null gesetzt. Zuletzt wird das Drücken von A/B als nicht ausgelöst markiert, und die Matrix wird dann gelöscht.

![Img](./media/5006.png)

⑤ Wenn der Spielzustand **0-Anfangszustand** ist (nicht spielend nach dem Einschalten), blinkt das angezeigte Symbol.

![Img](./media/5007.png)

⑥ Wenn es **2-Spiel vorbei** ist, wird die Punktzahl entsprechend der Blinkanzahl (flash_count) gesteuert. Wenn die Anzahl <3 ist, wiederholt sich „Punktzahl anzeigen → kurze Verzögerung → Anzeige löschen → kurze Verzögerung → Anzahl+1“; wenn die Anzahl 3 erreicht, wird immer die Punktzahl angezeigt und die Verzögerung verlängert.

![Img](./media/5008.png)

⑦ Im Zustand **1-Gaming**, wenn Sie C drücken, ohne die Druckmarkierung auszulösen und die Spielerspalte > 0 ist, wird die Spielerspalte -1 und die Taste C als ausgelöst markiert (mit Verzögerung zur Entprellung); drücken Sie E, ohne auszulösen, und wenn die Spielerspalte < 4 ist, und die Spalte +1, wobei E ausgelöst wird (Verzögerung); wenn keine Aktion ausgeführt wird, wird die Auslösemarkierung der entsprechenden Tasten zurückgesetzt.

![Img](./media/5009.png)

⑧ Berechnen Sie die Differenz zwischen der aktuellen Zeit und der letzten Ziegelsteinbewegungszeit. Wenn diese Differenz den Schwellenwert der Ziegelsteingeschwindigkeit überschreitet, aktualisieren Sie die Ziegelsteinbewegungszeit und die Ziegelsteinzeile +1. Wenn die Zeile > 4 ist (Grenze erreicht), setzen Sie den Ziegelstein auf eine zufällige Spalte mit Zeile=Null zurück und Punktzahl+1.

Rufen Sie die Kollisionserkennungs- und Spielgrafik-Rendering-Funktionen auf, um Ziegelsteine fallen zu lassen, nach Erreichen der Grenze zurückzusetzen, Punkte zu sammeln und den Spielzustand in Echtzeit zu aktualisieren.

Die Kollisionserkennungs- und Spielgrafik-Rendering-Funktionen werden aufgerufen, um den automatischen Ziegelsteinfortschritt, das Zurücksetzen der Grenze, die Punktesammlung und die Echtzeit-Aktualisierung des Spielzustands zu erreichen.

![Img](./media/5010.png)

⑨ Ermitteln Sie, ob das Spiel vorbei ist: Es wird zuerst geprüft, ob „die Ziegelsteinspalte mit der des Spielers übereinstimmt“ und „ob die Ziegelsteinzeile mit der des Spielers übereinstimmt“. Wenn beide Bedingungen erfüllt sind (d.h. die Ziegelsteine überlappen sich mit dem Spieler), wird das Spiel auf Zustand 2 (Spiel vorbei) gesetzt, die Anzeige gelöscht und die Blinkanzahl zurückgesetzt.

„Spiel vorbei bei Kollision.“

![Img](./media/5011.png)

⑩ Rendern Sie die Spielgrafik: Zuerst wird die Anzeige gelöscht, und dann werden Punkte mit einer Helligkeit von 255 (Spieler) an der festen Zeile und den aktuellen Spaltenpositionen des Spielers gezeichnet; wenn das Spiel gestartet ist (game_state=1), werden Punkte mit einer Helligkeit von 85 (Ziegelstein) an der Zeile und Spalte des Ziegelsteins gezeichnet. So können wir Ziegelsteine vom Spieler anhand ihrer Helligkeit unterscheiden.

![Img](./media/5012.png)

#### 4.2.5.5 Testergebnis

![Img](./media/4top.png)

Nach dem Brennen des Codes stecken Sie das micro:bit board in den Steckplatz des Gamepads (**Batterien eingelegt**) und schalten Sie es auf „ON“.

Es befindet sich nach dem Einschalten im **0-Anfangszustand** und die Matrix blinkt zwei quadratische Symbole.

Drücken Sie A und B (für mindestens 1 Sekunde), um das Spiel zu starten (im **1-Gaming**-Zustand), und ein Ziegelstein fällt in eine zufällige Spalte. Jetzt können Sie sich durch Drücken von C/E nach links/rechts bewegen. Jedes Mal, wenn Sie einem Ziegelstein ausweichen, erhöht sich die Punktzahl um 1.

Spiel vorbei bei Kollision (**2-Spiel vorbei**), und die Endpunktzahl wird auf der Matrix angezeigt. Wenn Sie eine weitere Runde spielen möchten, drücken Sie A und B erneut. Schalten Sie das Gerät aus, um das Spiel zu beenden (schalten Sie den DIP-Schalter auf „OFF“).

![Img](./media/5000.gif)

<span style="color: rgb(0, 209, 0);">**Tipp:** Wenn das Board nicht reagiert, drücken Sie bitte die Reset-Taste auf der Rückseite des micro:bit board.</span>

![Img](./media/4bottom.png)
