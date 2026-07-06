### 5.2.7 数字当てゲーム

#### 5.2.7.1 概要

![Img](./media/top1.png)

このプロジェクトでは、micro:bitボード、ゲームパッド、OLEDディスプレイを使用して、数字当てゲームを構築します。ゲームは1から100までのランダムな数字を生成し、プレイヤーはジョイスティックとボタンを使用して数字を推測します。OLEDディスプレイは、プレイヤーの推測と、それが高すぎるか低すぎるかを示します。プレイヤーが正しい数字を推測すると、OLEDディスプレイに「Great!!!」と表示されます。

![Img](./media/bottom1.png)

#### 5.2.7.2 必要な部品

| ![Img](./media/microbitV2.png)|  ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **micro:bit V2 ボード** (自己調達) ×1 | **micro:bit スマートゲームパッド** (組み立て済み) ×1 |**単4電池** (自己調達) ×4 |
|![Img](./media/OLED.png)|![Img](./media/7008.png)|
|**OLED ディスプレイ** (自己調達) ×1 |**F-F デュポンワイヤー**(自己調達) x4|

#### 5.2.7.3 配線図

![Img](./media/jiexian8.png)

**上記のように配線した後、micro:bitをゲームパッドコントロールボードのスロットに挿入します。**

| OLED ディスプレイ | micro:bit ゲームパッドコントロールボード |micro:bit ボードピン |
| :--: | :--: | :--: |
| GND |  GND | GND |
| VCC |  3V | 3V |
| SDA |  SDA | P20 |
| SCL |  SCL | P19 |

#### 5.2.7.4 コードフロー

![Img](./media/8001.png)

#### 5.2.7.5 テストコード

⚠️ **ここではOLEDライブラリが含まれているため、`https://github.com/keyestudio/pxt-environment-kit-master`をインポートする必要があります。**

**完全なコード:**

```python
from microbit import *
import utime
import random
from oled import OLED

# Initialize OLED display
# OLED(width, height, i2c_address)
# Default I2C address for SSD1306 is 0x3C or 0x3D
# micro:bit I2C pins are P19 (SCL) and P20 (SDA)
# The OLED library handles the I2C setup internally
oled = OLED()

# Game variables
secret_number = 0
guess = 0
min_val = 1
max_val = 100

# Joystick and button pins
joystick_x_pin = pin1
joystick_y_pin = pin2
button_c_pin = pin13
button_d_pin = pin14
button_e_pin = pin15
button_f_pin = pin16

# Set pull-ups for buttons
button_c_pin.set_pull(button_c_pin.PULL_UP)
button_d_pin.set_pull(button_d_pin.PULL_UP)
button_e_pin.set_pull(button_e_pin.PULL_UP)
button_f_pin.set_pull(button_f_pin.PULL_UP)

# Function to initialize or reset the game
def reset_game():
    global secret_number, guess, min_val, max_val
    secret_number = random.randint(1, 100)
    guess = 50 # Start with a middle guess
    min_val = 1
    max_val = 100
    oled.clear()
    oled.text("Guess the number", 0, 0)
    oled.text("1-100", 0, 10)
    oled.text("num: " + str(guess), 0, 20)
    oled.show()
    display.show(Image.HAPPY)

# Call reset_game to start the first game
reset_game()

while True:
    # Read joystick values
    x_value = joystick_x_pin.read_analog()
    y_value = joystick_y_pin.read_analog()

    # Read button states
    button_c_pressed = (button_c_pin.read_digital() == 0)
    button_d_pressed = (button_d_pin.read_digital() == 0)
    button_e_pressed = (button_e_pin.read_digital() == 0)
    button_f_pressed = (button_f_pin.read_digital() == 0)

    # Adjust guess based on joystick/button input
    if x_value > 700: # Joystick Right
        guess = min(max_val, guess + 1)
        utime.sleep_ms(100)
    elif x_value < 300: # Joystick Left
        guess = max(min_val, guess - 1)
        utime.sleep_ms(100)
    elif y_value < 300: # Joystick Up (increase by 10)
        guess = min(max_val, guess + 10)
        utime.sleep_ms(100)
    elif y_value > 700: # Joystick Down (decrease by 10)
        guess = max(min_val, guess - 10)
        utime.sleep_ms(100)
    elif button_c_pressed: # Button C (check guess)
        if guess == secret_number:
            oled.clear()
            oled.text("Great!!!", 0, 0)
            oled.show()
            display.show(Image.YES)
            utime.sleep(3) # Display for 3 seconds
            reset_game() # Start a new game
        elif guess < secret_number:
            oled.text("TO Low", 0, 30)
            oled.show()
            display.show(Image.ARROW_NORTH)
            min_val = guess + 1
        else: # guess > secret_number
            oled.text("TO High", 0, 30)
            oled.show()
            display.show(Image.ARROW_SOUTH)
            max_val = guess - 1
        utime.sleep_ms(200) # Debounce

    # Update OLED display with current guess
    oled.text("num: " + str(guess), 0, 20)
    oled.show()

    utime.sleep_ms(50) # Small delay for main loop
```

![Img](./media/line1.png)

**簡単な説明:**

① OLEDディスプレイを初期化し、ゲーム変数を設定し、ジョイスティックとボタンのピンを定義します。`reset_game()`関数を呼び出してゲームを開始します。

```python
from microbit import *
import utime
import random
from oled import OLED

# Initialize OLED display
# OLED(width, height, i2c_address)
# Default I2C address for SSD1306 is 0x3C or 0x3D
# micro:bit I2C pins are P19 (SCL) and P20 (SDA)
# The OLED library handles the I2C setup internally
oled = OLED()

# Game variables
secret_number = 0
guess = 0
min_val = 1
max_val = 100

# Joystick and button pins
joystick_x_pin = pin1
joystick_y_pin = pin2
button_c_pin = pin13
button_d_pin = pin14
button_e_pin = pin15
button_f_pin = pin16

# Set pull-ups for buttons
button_c_pin.set_pull(button_c_pin.PULL_UP)
button_d_pin.set_pull(button_d_pin.PULL_UP)
button_e_pin.set_pull(button_e_pin.PULL_UP)
button_f_pin.set_pull(button_f_pin.PULL_UP)

# Function to initialize or reset the game
def reset_game():
    global secret_number, guess, min_val, max_val
    secret_number = random.randint(1, 100)
    guess = 50 # Start with a middle guess
    min_val = 1
    max_val = 100
    oled.clear()
    oled.text("Guess the number", 0, 0)
    oled.text("1-100", 0, 10)
    oled.text("num: " + str(guess), 0, 20)
    oled.show()
    display.show(Image.HAPPY)

# Call reset_game to start the first game
reset_game()
```

② ジョイスティックとボタンの入力を読み取り、推測を調整します。ジョイスティックを右に倒すと推測が1増加し、左に倒すと1減少します。上に倒すと10増加し、下に倒すと10減少します。

```python
while True:
    # Read joystick values
    x_value = joystick_x_pin.read_analog()
    y_value = joystick_y_pin.read_analog()

    # Read button states
    button_c_pressed = (button_c_pin.read_digital() == 0)
    button_d_pressed = (button_d_pin.read_digital() == 0)
    button_e_pressed = (button_e_pin.read_digital() == 0)
    button_f_pressed = (button_f_pin.read_digital() == 0)

    # Adjust guess based on joystick/button input
    if x_value > 700: # Joystick Right
        guess = min(max_val, guess + 1)
        utime.sleep_ms(100)
    elif x_value < 300: # Joystick Left
        guess = max(min_val, guess - 1)
        utime.sleep_ms(100)
    elif y_value < 300: # Joystick Up (increase by 10)
        guess = min(max_val, guess + 10)
        utime.sleep_ms(100)
    elif y_value > 700: # Joystick Down (decrease by 10)
        guess = max(min_val, guess - 10)
        utime.sleep_ms(100)
```

③ ボタンCが押された場合、推測が秘密の数字と一致するかどうかを確認します。一致する場合は「Great!!!」と表示し、新しいゲームを開始します。推測が低すぎる場合は「TO Low」と表示し、高すぎる場合は「TO High」と表示します。

```python
    elif button_c_pressed: # Button C (check guess)
        if guess == secret_number:
            oled.clear()
            oled.text("Great!!!", 0, 0)
            oled.show()
            display.show(Image.YES)
            utime.sleep(3) # Display for 3 seconds
            reset_game() # Start a new game
        elif guess < secret_number:
            oled.text("TO Low", 0, 30)
            oled.show()
            display.show(Image.ARROW_NORTH)
            min_val = guess + 1
        else: # guess > secret_number
            oled.text("TO High", 0, 30)
            oled.show()
            display.show(Image.ARROW_SOUTH)
            max_val = guess - 1
        utime.sleep_ms(200) # Debounce
```

④ OLEDディスプレイを現在の推測で更新し、メインループに短い遅延を設けます。

```python
    # Update OLED display with current guess
    oled.text("num: " + str(guess), 0, 20)
    oled.show()

    utime.sleep_ms(50) # Small delay for main loop
```

#### 5.2.7.6 テスト結果

![Img](./media/4top.png)

コードを書き込んだ後、micro:bitボードをゲームパッドのスロットに挿入し（**電池が取り付けられていることを確認**）、「ON」に切り替えます。

OLEDディスプレイに「Guess the number」、「1-100」、「num: 50」と表示され、micro:bit LEDマトリックスに「HAPPY」アイコンが表示されます。

ジョイスティックを左右に動かして数字を調整し、Cを押して推測を確認します。推測が低すぎる場合は「TO Low」、高すぎる場合は「TO High」と表示されます。正しい数字を推測すると「Great!!!」と表示され、新しいゲームが開始されます。

![Img](./media/t7000.gif)

<span style="color: rgb(0, 209, 0);">**ヒント:** ボードが応答しない場合は、micro:bitボードの背面にあるリセットボタンを押してください。</span>

![Img](./media/4bottom.png)
