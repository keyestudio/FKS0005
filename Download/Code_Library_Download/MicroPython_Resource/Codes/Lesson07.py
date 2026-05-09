from microbit import *
from oled_ssd1306 import *
from random import *

# 初始化OLED和引脚
initialize()
clear_oled()

# 游戏核心变量（放在循环外，避免每次重置）
mode = 0          # 0:游戏初始化，1:游戏运行中
min_num = 1       # 猜数最小值
max_num = 100     # 猜数最大值
current_guess = 50# 当前猜测值
target_num = 0    # 随机目标数
state = 0         # 0:初始,1:猜大了,2:猜小了,3:猜对了
update_display = True  # 显示更新标记

# 设置引脚上拉（按键接地触发）
pin13.set_pull(pin13.PULL_UP)
pin15.set_pull(pin15.PULL_UP)
pin16.set_pull(pin16.PULL_UP)

while True:
    # 1. 游戏初始化：生成随机数，重置状态
    if mode == 0:
        min_num = 1
        max_num = 100
        current_guess = 50
        target_num = randint(min_num, max_num)  # 生成目标数
        state = 0
        mode = 1  # 切换到运行模式
        update_display = True

    # 2. 游戏运行逻辑
    if mode == 1:
        # 检测按键（独立检测，避免被显示逻辑阻塞）
        if pin15.read_digital() == 0:  # 引脚15按下：数字+1
            current_guess += 1
            if current_guess > max_num:
                current_guess = max_num
            update_display = True
            sleep(50)  # 消抖

        elif pin13.read_digital() == 0:  # 引脚13按下：数字-1
            current_guess -= 1
            if current_guess < min_num:
                current_guess = min_num
            update_display = True
            sleep(50)  # 消抖

        elif pin16.read_digital() == 0:  # 引脚16按下：确认猜测
            if current_guess > target_num:
                state = 1
                max_num = current_guess  # 缩小范围：最大值=当前值
            elif current_guess < target_num:
                state = 2
                min_num = current_guess  # 缩小范围：最小值=当前值
            else:
                state = 3  # 猜对了
                mode = 0   # 重置游戏
            update_display = True
            sleep(50)  # 消抖

        # 3. 更新OLED显示（仅当需要更新时执行）
        if update_display:
            clear_oled()  # 清屏
            # 显示猜数范围
            add_text(0, 0, "num:" + str(min_num) + "~" + str(max_num))
            # 显示当前猜测值
            add_text(8, 2, str(current_guess))
            # 显示提示状态
            if state == 1:
                add_text(0, 4, "TO High")
            elif state == 2:
                add_text(0, 4, "TO Low")
            elif state == 3:
                add_text(5, 4, "Bingo!")

            # 重置更新标记
            update_display = False

    # 4. 猜对后延时，让用户看到提示
    if state == 3:
        sleep(1000)
        state = 0
