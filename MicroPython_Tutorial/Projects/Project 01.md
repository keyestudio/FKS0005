### 5.2.1 方向指示器

#### 5.2.1.1 概要

![Img](./media/top1.png)

ジョイスティックを操作すると、ドットマトリックスにリアルタイムで対応する方向（左、右、上、下）の矢印が表示され、明確な方向参照が得られます。

![Img](./media/bottom1.png)

#### 5.2.1.2 コンポーネント知識

![Img](./media/2top.png)

**Micro:bit ドットマトリックス:**

![Img](./media/1001.png)

micro:bitボードのLEDドットマトリックスは、合計25個の発光ダイオードで構成されており、5個のグループがX軸とY軸に対応し、5×5のマトリックスを形成しています。それぞれが行（X）と列（Y）の交点に配置されています。座標点を設定することで、1つまたは複数のLEDを制御できます。

**ジョイスティック:**

| ![Img](./media/1002.png)| ![Img](./media/1003.png)  |
| :--: | :--: |
| 実物 | 回路図 |

このジョイスティックの内部コア構造は、それぞれ10KΩの抵抗値を持つ2つの調整可能な抵抗器（ポテンショメータ）で構成されています。

マイクロコントローラーのADCアナログピンを介してプッシュの方向（および振幅）を検出し、対応する次元のアナログ電気信号を出力します。実際の信号読み取り中、ジョイスティックのX軸とY軸のアナログ値が450〜600の範囲内で検出された場合、ジョイスティックがアクティブな操作なしにニュートラル（静止）状態にあると判断できます。

![Img](./media/2bottom.png)

#### 5.2.1.3 必要な部品

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png)  |![Img](./media/dianchi.png)|
| :--: | :--: | :--: |
| **micro:bit V2 ボード** (自己調達) ×1 | **micro:bit スマートゲームパッド** (組み立て済み) ×1 |**単4電池** (自己調達) ×4 |


#### 5.2.1.4 コードフロー

![Img](./media/1008.png)

#### 5.2.1.5 テストコード

⚠️ **以下のコードにはゲームパッドのMicroPythonライブラリが含まれています。ジョイスティックの感度は必要に応じて調整できます。**

**完全なコード:**

```python
from microbit import *
import utime

# Define the threshold for joystick movement
JOYSTICK_THRESHOLD = 200

# Initialize display
display.show(Image.HOUSE)

while True:
    # Read analog values from joystick X and Y axes
    x_value = pin1.read_analog()
    y_value = pin2.read_analog()

    # Determine direction based on joystick values
    if x_value < 512 - JOYSTICK_THRESHOLD:  # Left
        display.show(Image.ARROW_WEST)
    elif x_value > 512 + JOYSTICK_THRESHOLD:  # Right
        display.show(Image.ARROW_EAST)
    elif y_value < 512 - JOYSTICK_THRESHOLD:  # Up
        display.show(Image.ARROW_NORTH)
    elif y_value > 512 + JOYSTICK_THRESHOLD:  # Down
        display.show(Image.ARROW_SOUTH)
    else:  # Neutral
        display.show(Image.HOUSE)

    utime.sleep_ms(100)
```

![Img](./media/line1.png)

**簡単な説明:**

① micro:bit LEDマトリックスを初期化して ![Img](./media/1006.png) を表示させます。

```python
from microbit import *
import utime

# Define the threshold for joystick movement
JOYSTICK_THRESHOLD = 200

# Initialize display
display.show(Image.HOUSE)
```

② X軸とY軸の値を読み取り、操作方向を決定します。検出された場合、マトリックスは対応する矢印を表示します。そうでない場合、![Img](./media/1006.png) を表示します。

```python
while True:
    # Read analog values from joystick X and Y axes
    x_value = pin1.read_analog()
    y_value = pin2.read_analog()

    # Determine direction based on joystick values
    if x_value < 512 - JOYSTICK_THRESHOLD:  # Left
        display.show(Image.ARROW_WEST)
    elif x_value > 512 + JOYSTICK_THRESHOLD:  # Right
        display.show(Image.ARROW_EAST)
    elif y_value < 512 - JOYSTICK_THRESHOLD:  # Up
        display.show(Image.ARROW_NORTH)
    elif y_value > 512 + JOYSTICK_THRESHOLD:  # Down
        display.show(Image.ARROW_SOUTH)
    else:  # Neutral
        display.show(Image.HOUSE)

    utime.sleep_ms(100)
```


#### 5.2.1.6 テスト結果

![Img](./media/4top.png)

コードを書き込んだ後、micro:bitボードをゲームパッドのスロットに挿入し（**電池が取り付けられていることを確認**）、「ON」に切り替えます。

ゲームパッドのジョイスティックを操作すると、マトリックスに対応する矢印が表示されます。指を離して中央に戻すと、マトリックスに家のアイコンが表示されます。

![Img](./media/1009.gif)

<span style="color: rgb(0, 209, 0);">**ヒント:** ボードが応答しない場合は、micro:bitボードの背面にあるリセットボタンを押してください。</span>

![Img](./media/4bottom.png)
