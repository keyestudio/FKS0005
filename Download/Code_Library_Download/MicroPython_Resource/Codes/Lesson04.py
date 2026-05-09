from microbit import *
import music
import neopixel
import random

# 全局变量初始化
volume = 50
music_mode = 0  # 0=手动模式, 1=随机模式
music2 = 0  # 当前音乐索引
last_music2 = -1  # 上一次播放的音乐索引
hue = 0  # 灯光色相值

# 初始化NeoPixel
strip = neopixel.NeoPixel(pin8, 4)

# 预定义旋律列表 - MicroPython内置旋律
melodies = [
    "DADADADUM",
    "ENTERTAINER",
    "PRELUDE",
    "ODE",
    "NYAN",
    "RINGTONE",
    "FUNK",
    "BLUES",
    "BIRTHDAY",
    "WEDDING",
    "FUNERAL",
    "PUNCHLINE",
    "BADDY",
    "CHASE",
    "BA_DING",
    "WAWAWAWAA",
    "JUMP_UP",
    "JUMP_DOWN",
    "POWER_UP",
    "POWER_DOWN"
]

# 设置引脚上拉电阻
pin13.set_pull(pin13.PULL_UP)
pin14.set_pull(pin14.PULL_UP)
pin15.set_pull(pin15.PULL_UP)
pin16.set_pull(pin16.PULL_UP)

# 初始化音量
set_volume(volume)

# 按钮A回调函数 - 音量增加
def on_button_a():
    global volume
    volume += 10
    if volume > 250:
        volume = 250
    set_volume(volume)


# 按钮B回调函数 - 音量减少
def on_button_b():
    global volume
    volume -= 10
    if volume < 20:
        volume = 20
    set_volume(volume)


# 更新灯光效果
def update_lights():
    global hue

    # 将HSL转换为RGB（简化版）
    h = hue / 360.0

    # 计算RGB值
    if hue < 60:
        r = 255
        g = int(hue / 60.0 * 255)
        b = 0
    elif hue < 120:
        r = int((120 - hue) / 60.0 * 255)
        g = 255
        b = 0
    elif hue < 180:
        r = 0
        g = 255
        b = int((hue - 120) / 60.0 * 255)
    elif hue < 240:
        r = 0
        g = int((240 - hue) / 60.0 * 255)
        b = 255
    elif hue < 300:
        r = int((hue - 240) / 60.0 * 255)
        g = 0
        b = 255
    else:
        r = 255
        g = 0
        b = int((360 - hue) / 60.0 * 255)

    # 设置亮度（30%）
    r = int(r * 0.3)
    g = int(g * 0.3)
    b = int(b * 0.3)

    # 设置所有LED颜色
    for i in range(4):
        strip[i] = (r, g, b)
    strip.show()

    # 更新色相
    hue += 1
    if hue >= 360:
        hue = 0

# 防抖动和引脚状态管理类
class PinState:
    def __init__(self, pin):
        self.pin = pin
        self.last_state = pin.read_digital()
        self.last_time = running_time()

    def check(self):
        current_state = self.pin.read_digital()
        current_time = running_time()

        # 检测下降沿（按下）
        if current_state == 0 and self.last_state == 1:
            # 防抖动检查
            if current_time - self.last_time > 50:  # 50ms防抖动
                self.last_state = current_state
                self.last_time = current_time
                return True

        self.last_state = current_state
        return False

# 主程序
def main():
    global music_mode, music2, last_music2, hue

    # 初始化引脚状态管理器
    pin13_state = PinState(pin13)
    pin14_state = PinState(pin14)
    pin15_state = PinState(pin15)
    pin16_state = PinState(pin16)

    # 灯光更新时间记录
    last_light_update = running_time()
    light_update_interval = 10  # ms




    # 主循环
    while True:
        current_time = running_time()

        # 1. 检查按钮A和B
        if button_a.was_pressed():
            on_button_a()

        if button_b.was_pressed():
            on_button_b()

        # 2. 检查引脚状态
        if pin16_state.check():  # P13按下 - 手动模式
            music_mode = 0
            sleep(500)
            display.clear()

        if pin14_state.check():  # P14按下 - 随机模式
            music_mode = 1
            sleep(500)
            display.clear()

        # 3. 根据模式处理导航按钮
        if music_mode == 0:  # 手动模式
            if pin15_state.check():  # P15按下 - 下一首
                music2 += 1
                if music2 > 19:
                    music2 = 0


            if pin13_state.check():  # P16按下 - 上一首
                music2 -= 1
                if music2 < 0:
                    music2 = 19


        else:  # 随机模式
            if pin15_state.check():  # P15按下 - 随机选择
                music2 = random.randint(0, 19)


            if pin13_state.check():  # P16按下 - 随机选择
                music2 = random.randint(0, 19)


        # 4. 播放音乐（如果音乐索引变化）
        if music2 != last_music2:
            try:
                music.stop()  # 停止当前播放
                # 播放选中的旋律
                melody_name = melodies[music2]
                melody_func = getattr(music, melody_name)
                music.play(melody_func, wait=False)
                last_music2 = music2

            except Exception as e:
                display.scroll("ERR", delay=150)

        # 5. 更新灯光效果
        if current_time - last_light_update >= light_update_interval:
            update_lights()
            last_light_update = current_time
        if music_mode:
            display.show(Image('00000:'
                               '99099:'
                               '00900:'
                               '99099:'
                               '00000'))
        else:
            display.show(Image('00900:'
                               '00090:'
                               '99999:'
                               '00090:'
                               '00900'))

        # 7. 短暂延时，防止过于频繁的循环
        sleep(10)

# 启动程序
if __name__ == "__main__":
    main()
