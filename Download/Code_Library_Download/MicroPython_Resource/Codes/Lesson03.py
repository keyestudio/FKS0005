from microbit import *
import music  # micro:bit native music library


ROCKER_X_PIN = pin2    # X-axis of joystick (analog)
ROCKER_Y_PIN = pin1    # Y-axis of joystick (analog)

# JoyBit Buttons (Digital Inputs - Pull-Up)
C_KEY = pin15       # Up button
D_KEY = pin16     # Down button
E_KEY = pin13     # Left button
F_KEY = pin14    # Right button

# Beat Duration (matches BeatList.WHOLE_BEAT)
WHOLE_BEAT = 1000  # 1 second (ms)

# Joystick Thresholds (matches original 400/600 in MakeCode)
JOY_THRESH_LOW = 400
JOY_THRESH_HIGH = 600

# ==================== INITIALIZATION ====================
def init():
    # Enable micro:bit LED matrix (replace led.enable(True))
    display.on()

    # Set pull-up resistors for buttons (matches pins.set_pull)
    F_KEY.set_pull(F_KEY.PULL_UP)
    E_KEY.set_pull(E_KEY.PULL_UP)
    C_KEY.set_pull(C_KEY.PULL_UP)
    D_KEY.set_pull(D_KEY.PULL_UP)

    # Show eighth note icon (replace basic.show_icon)
    display.show(Image.MUSIC_CROTCHET)



def check_joystick():
    """Detect joystick position and play corresponding tone"""
    x_val = ROCKER_X_PIN.read_analog()  # 0-1023 (replace JoyBit.rocker_x())
    y_val = ROCKER_Y_PIN.read_analog()  # 0-1023 (replace JoyBit.rocker_y())

    # Right (X > 600, Y middle 400-600) → DO
    if x_val > JOY_THRESH_HIGH and (y_val > JOY_THRESH_LOW and y_val < JOY_THRESH_HIGH):
        music.play('c4:2')
        display.show(1)
    # Left (X < 400, Y middle) → RE
    elif x_val < JOY_THRESH_LOW and (y_val > JOY_THRESH_LOW and y_val < JOY_THRESH_HIGH):
        music.play('d4:2')
        display.show(2)
    # Up (Y > 600, X middle) → MI
    elif y_val > JOY_THRESH_HIGH and (x_val > JOY_THRESH_LOW and x_val < JOY_THRESH_HIGH):
        music.play('e4:2')
        display.show(3)
    # Down (Y < 400, X middle) → FA
    elif y_val < JOY_THRESH_LOW and (x_val > JOY_THRESH_LOW and x_val < JOY_THRESH_HIGH):
        music.play('f4:2')
        display.show(4)
def check_buttons():
    """Detect button presses (pull-up → low = pressed) and play tones"""
    # Debounce (20ms to avoid noise)
    debounce = 20

    # Up button (RUP) → SOL
    if C_KEY.read_digital() == 0:
        sleep(debounce)
        if C_KEY.read_digital() == 0:
            music.play('g4:2')
            display.show(5)
    # Down button (RDOWN) → LA
    elif D_KEY.read_digital() == 0:
        sleep(debounce)
        if D_KEY.read_digital() == 0:
            music.play('a4:2')
            display.show(6)
    # Left button (RLEFT) → SI
    elif E_KEY.read_digital() == 0:
        sleep(debounce)
        if E_KEY.read_digital() == 0:
            music.play('b4:2')
            display.show(7)
    # Right button (RRIGHT) → DO (high)
    elif F_KEY.read_digital() == 0:
        sleep(debounce)
        if F_KEY.read_digital() == 0:
            music.play('c5:2')
            display.show(1)
# ==================== MAIN LOOP ====================
if __name__ == "__main__":
    init()  # Run initialization

    while True:  # Replace basic.forever()
        check_joystick()   # Check joystick position
        check_buttons()    # Check button presses
        sleep(10)  # Reduce CPU load (negligible delay)
