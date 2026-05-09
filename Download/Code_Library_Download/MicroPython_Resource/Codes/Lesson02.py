from microbit import *
import neopixel
import random
import utime

# ==================== Global Variable Initialization ====================
calor = 0                  # HSL hue value (0-359)
Mode = 0                   # Current operating mode (0-4; 0 = off)
np_pin = pin8              # Neopixel data pin (P8)
np_num = 4                 # Number of LED pixels in the strip
strip = neopixel.NeoPixel(np_pin, np_num)

# Global brightness factor (adjustable; 0.3 = 30% brightness)
BRIGHTNESS = 0.3

# Button pin definitions (JoyBit expansion board)
C_KEY = pin15   # Left button → Mode 1
D_KEY = pin16  # Right button → Mode 2
E_KEY = pin13     # Up button → Mode 3
F_KEY = pin14   # Down button → Mode 4

# Non-blocking mode state variables
mode1_index = 0      # Current color index for Mode 1
mode4_index = 0      # Current lit pixel index for Mode 4
last_btn_time = 0    # Button debounce timestamp (prevents sleep blocking)
btn_debounce_ms = 20 # Button debounce duration (ms)

# Non-blocking delay timestamps (independent for each mode to avoid interference)
mode1_last_time = 0  # Color switch timestamp for Mode 1
mode2_last_time = 0  # Hue gradient timestamp for Mode 2
mode3_last_time = 0  # Pixel shift timestamp for Mode 3
mode4_last_time = 0  # Pixel toggle timestamp for Mode 4

# Mode delay configuration (adjustable as needed)
MODE1_DELAY = 500    # Mode 1 color switch interval (ms)
MODE2_DELAY = 5      # Mode 2 hue gradient interval (ms)
MODE3_DELAY = 200    # Mode 3 pixel shift interval (ms)
MODE4_DELAY = 200    # Mode 4 pixel toggle interval (ms)

# ==================== Utility Functions ====================
# HSL to RGB conversion + brightness scaling
def hsl_to_rgb(h, s, l):
    h = h % 360
    s /= 100.0
    l /= 100.0

    c = (1 - abs(2 * l - 1)) * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = l - c / 2

    if 0 <= h < 60:
        r, g, b = c, x, 0
    elif 60 <= h < 120:
        r, g, b = x, c, 0
    elif 120 <= h < 180:
        r, g, b = 0, c, x
    elif 180 <= h < 240:
        r, g, b = 0, x, c
    elif 240 <= h < 300:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x

    r = int((r + m) * 255 * BRIGHTNESS)
    g = int((g + m) * 255 * BRIGHTNESS)
    b = int((b + m) * 255 * BRIGHTNESS)
    return (r, g, b)

# Non-blocking button detection (timestamp-based debounce)
def check_btn(pin):
    global last_btn_time
    current_time = utime.ticks_ms()
    # 1. Detect button press (pull-up → low level) 2. Debounce time elapsed
    if pin.read_digital() == 0 and utime.ticks_diff(current_time, last_btn_time) > btn_debounce_ms:
        last_btn_time = current_time  # Update debounce timestamp
        return True
    return False

# Manual neopixel right shift (non-blocking)
def neopixel_shift(strip):
    last_pixel = strip[np_num - 1]
    for i in range(np_num - 1, 0, -1):
        strip[i] = strip[i - 1]
    strip[0] = strip[0]

# ==================== Full Non-Blocking Mode Execution Functions ====================
def run_mode1():
    global mode1_index, mode1_last_time
    current_time = utime.ticks_ms()
    # Only switch color when delay interval is reached (non-blocking)
    if utime.ticks_diff(current_time, mode1_last_time) > MODE1_DELAY:
        mode1_last_time = current_time  # Update timestamp
        # Mode 1 color list (brightness-scaled)
        colors = [
            (int(255 * BRIGHTNESS), 0, 0),    # Red
            (0, int(255 * BRIGHTNESS), 0),    # Green
            (0, 0, int(255 * BRIGHTNESS)),    # Blue
            (int(255 * BRIGHTNESS), int(255 * BRIGHTNESS), 0),  # Yellow
            (int(128 * BRIGHTNESS), 0, int(128 * BRIGHTNESS))   # Purple
        ]
        strip.fill(colors[mode1_index])
        strip.show()
        mode1_index = (mode1_index + 1) % len(colors)

def run_mode2():
    global calor, mode2_last_time
    current_time = utime.ticks_ms()
    if utime.ticks_diff(current_time, mode2_last_time) > MODE2_DELAY:
        mode2_last_time = current_time
        calor = (calor + 1) % 360
        rgb = hsl_to_rgb(calor, 99, 15)
        strip.fill(rgb)
        strip.show()

def run_mode3():
    global mode3_last_time
    current_time = utime.ticks_ms()
    if utime.ticks_diff(current_time, mode3_last_time) > MODE3_DELAY:
        mode3_last_time = current_time
        neopixel_shift(strip)
        rand_h = random.randint(0, 360)
        rgb = hsl_to_rgb(rand_h, 99, 15)
        strip[0] = rgb
        strip.show()

def run_mode4():
    global mode4_index, mode4_last_time
    current_time = utime.ticks_ms()
    if utime.ticks_diff(current_time, mode4_last_time) > MODE4_DELAY:
        mode4_last_time = current_time
        strip.fill((0, 0, 0))  # Clear all pixels
        rand_h = random.randint(0, 360)
        rgb = hsl_to_rgb(rand_h, 99, 18)
        strip[mode4_index] = rgb
        strip.show()
        # Cycle index (0-3)
        mode4_index = (mode4_index + 1) % np_num

# ==================== Initialization ====================
def init():
    # Initialize button pull-up resistors
    C_KEY.set_pull(C_KEY.PULL_UP)
    D_KEY.set_pull(D_KEY.PULL_UP)
    E_KEY.set_pull(E_KEY.PULL_UP)
    F_KEY.set_pull(F_KEY.PULL_UP)
    # Initialize neopixel strip to off state
    strip.fill((0, 0, 0))
    strip.show()
    # Initialize mode timestamps (prevent immediate trigger on startup)
    global mode1_last_time, mode2_last_time, mode3_last_time, mode4_last_time
    current_time = utime.ticks_ms()
    mode1_last_time = current_time
    mode2_last_time = current_time
    mode3_last_time = current_time
    mode4_last_time = current_time

# ==================== Main Loop (Fully Non-Blocking) ====================
if __name__ == "__main__":
    init()
    while True:
        # ========== Step 1: Highest Priority - Button Detection (No Blocking) ==========
        if check_btn(C_KEY):
            Mode = 1
            mode1_index = 0
            mode1_last_time = utime.ticks_ms()  # Reset Mode 1 timestamp
            strip.fill((0, 0, 0))
            strip.show()
        elif check_btn(D_KEY):
            Mode = 2
            mode2_last_time = utime.ticks_ms()  # Reset Mode 2 timestamp
            strip.fill((0, 0, 0))
            strip.show()
        elif check_btn(E_KEY):
            Mode = 3
            mode3_last_time = utime.ticks_ms()  # Reset Mode 3 timestamp
            strip.fill((0, 0, 0))
            strip.show()
        elif check_btn(F_KEY):
            Mode = 4
            mode4_index = 0
            mode4_last_time = utime.ticks_ms()  # Reset Mode 4 timestamp
            strip.fill((0, 0, 0))
            strip.show()

        # ========== Step 2: Execute Current Mode (Fully Non-Blocking) ==========
        if Mode == 1:
            run_mode1()
        elif Mode == 2:
            run_mode2()
        elif Mode == 3:
            run_mode3()
        elif Mode == 4:
            run_mode4()
        else:
            # Mode 0: Turn off neopixel strip (short delay to reduce CPU usage)
            strip.fill((0, 0, 0))
            strip.show()
            utime.sleep_ms(10)  # 10ms delay doesn't affect button response (negligible)
