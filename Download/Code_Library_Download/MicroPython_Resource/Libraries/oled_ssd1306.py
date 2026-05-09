# I2C LCD library for the micro:bit
# Thanks to adafruit_Python_SSD1306 library by Dmitrii (dmitryelj@gmail.com)
# Thanks to lopyi2c.py
# Thanks to ssd1306.py
# Author: 
# v1.1 - Fixed display issues
# Only supports display type I2C128x64

from microbit import Image, i2c
from ustruct import pack_into

# LCD Control constants
ADDR = 0x3C
screen = bytearray(1025)  # 1024 pixels + 1 control byte
screen[0] = 0x40  # Data mode
zoom = 0

def command(c):
    i2c.write(ADDR, b'\x00' + bytearray(c))

def initialize():
    cmd = [
        [0xAE],                     # SSD1306_DISPLAYOFF
        [0xA4],                     # SSD1306_DISPLAYALLON_RESUME
        [0xD5, 0xF0],               # SSD1306_SETDISPLAYCLOCKDIV
        [0xA8, 0x3F],               # SSD1306_SETMULTIPLEX
        [0xD3, 0x00],               # SSD1306_SETDISPLAYOFFSET
        [0x00 | 0x0],               # SSD1306_SETSTARTLINE
        [0x8D, 0x14],               # SSD1306_CHARGEPUMP
        [0x20, 0x00],               # SSD1306_MEMORYMODE (horizontal addressing)
        [0x21, 0, 127],             # SSD1306_COLUMNADDR
        [0x22, 0, 7],               # SSD1306_PAGEADDR (8 pages for 64px height)
        [0xA0 | 0x1],               # SSD1306_SEGREMAP (remap columns)
        [0xC8],                     # SSD1306_COMSCANDEC (reverse scan direction)
        [0xDA, 0x12],               # SSD1306_SETCOMPINS
        [0x81, 0xCF],               # SSD1306_SETCONTRAST
        [0xD9, 0xF1],               # SSD1306_SETPRECHARGE
        [0xDB, 0x40],               # SSD1306_SETVCOMDETECT
        [0xA6],                     # SSD1306_NORMALDISPLAY
        [0xD6, 0x00],               # zoom off (normal size)
        [0xAF]                      # SSD1306_DISPLAYON
    ]
    for c in cmd:
        command(c)
    clear_oled()

def set_pos(col=0, page=0):
    command([0xB0 | page])  # Set page address
    command([0x00 | (col & 0x0F)])  # Set lower column address
    command([0x10 | (col >> 4)])  # Set upper column address

def clear_oled(c=0):
    global screen
    for i in range(1, 1025):
        screen[i] = 0
    draw_screen()

def set_zoom(v):
    global zoom
    if zoom != v:
        command([0xD6, v])
        zoom = v

def draw_screen():
    set_zoom(0)  # Normal size (no zoom)
    # Update entire screen
    for page in range(0, 8):
        set_pos(0, page)
        start_idx = 1 + page * 128
        end_idx = start_idx + 128
        i2c.write(ADDR, b'\x40' + screen[start_idx:end_idx])

def add_text(x, y, text, draw=1):
    """
    Add text at position (x, y)
    x: column (0-20 characters)
    y: row (0-7 lines)
    """
    for i, char in enumerate(text):
        if x + i >= 21:  # Max 21 characters per line
            break
            
        # Get character image (5x5 pixels)
        char_img = Image(char)
        
        # Draw each column of the character
        for col in range(5):
            px_data = 0
            # Convert 5 rows to 8-bit vertical data (top 5 bits used)
            for row in range(5):
                if char_img.get_pixel(col, row) > 0:
                    px_data |= (1 << row)
            
            # Calculate screen position
            screen_x = (x + i) * 6 + col  # 6 pixels per character (5+1 spacing)
            screen_y = y * 8  # 8 pixels per row
            
            if screen_x < 128 and screen_y < 64:
                # Write to screen buffer
                page = screen_y // 8
                page_offset = screen_y % 8
                idx = 1 + page * 128 + screen_x
                
                if idx < len(screen):
                    # Clear existing bits for this column
                    screen[idx] &= ~(0x1F << page_offset)
                    # Set new bits
                    screen[idx] |= (px_data << page_offset)
    
    if draw:
        # Update only the affected rows
        for page in range(y, y + 1):  # Only update the row we wrote to
            set_pos(0, page)
            start_idx = 1 + page * 128
            end_idx = start_idx + 128
            i2c.write(ADDR, b'\x40' + screen[start_idx:end_idx])

def set_px(x, y, color, draw=1):
    """Set pixel at (x,y) to color (0 or 1)"""
    if x < 0 or x >= 128 or y < 0 or y >= 64:
        return
        
    page = y // 8
    shift = y % 8
    idx = 1 + page * 128 + x
    
    if color:
        screen[idx] |= (1 << shift)
    else:
        screen[idx] &= ~(1 << shift)
        
    if draw:
        set_pos(x, page)
        i2c.write(ADDR, bytearray([0x40, screen[idx]]))

def get_px(x, y):
    """Get pixel value at (x,y)"""
    if x < 0 or x >= 128 or y < 0 or y >= 64:
        return 0
        
    page = y // 8
    shift = y % 8
    idx = 1 + page * 128 + x
    return (screen[idx] >> shift) & 1

def draw_square(x1, y1, x2, y2, color, draw=1):
    """Draw a square outline"""
    # Top and bottom lines
    for x in range(x1, x2 + 1):
        set_px(x, y1, color, 0)
        set_px(x, y2, color, 0)
    # Left and right lines
    for y in range(y1, y2 + 1):
        set_px(x1, y, color, 0)
        set_px(x2, y, color, 0)
    if draw:
        draw_screen()

def fill_rect(x1, y1, x2, y2, color, draw=1):
    """Draw a filled rectangle"""
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            set_px(x, y, color, 0)
    if draw:
        draw_screen()

def reverse():
    """Reverse display (invert colors)"""
    for i in range(1, 1025):
        screen[i] = 0xFF - screen[i]
    draw_screen()
