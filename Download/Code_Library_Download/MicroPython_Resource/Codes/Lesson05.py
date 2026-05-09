import utime
import random
from microbit import *

# ===================== 全局配置与变量 =====================
# 玩家初始配置（micro:bit 像素坐标：col=列(0-4,左右), row=行(0-4,上下)）
player_fixed_row = 4    # 玩家固定行（最下方）
player_init_col = 4     # 玩家初始列（中间）
brick_move_speed = 300  # 砖块下落间隔(ms)

# 游戏状态：0=未开始 1=运行中 2=结束
game_state = 0
brick_x = 0             # 砖块当前列（左右）
brick_y = 0             # 砖块当前行（上下）
score = 0               # 得分
a_pressed_flag = False  # 左移键防抖标志
b_pressed_flag = False  # 右移键防抖标志
collision_x = False     # 碰撞检测-同列
collision_y = False     # 碰撞检测-同行
flash_count = 0         # 结束画面闪烁计数
time_passed = 0         # 时间差（砖块下落用）
current_time = 0        # 当前时间戳
last_brick_time = 0     # 砖块上次下落时间戳
start_flag = 0          # 开始按钮防抖标志
can_start = False       # 可开始游戏标志
ab_pressed = False      # A+B同时按下标志
player_col = player_init_col  # 玩家当前列

# 初始化引脚上拉（PULL_UP：按下=低电平0，松开=高电平1）
pin13.set_pull(pin13.PULL_UP)  # 右移键
pin15.set_pull(pin15.PULL_UP)  # 左移键

# ===================== 核心函数 =====================
def on_start():
    """开机初始化：随机生成砖块初始列"""
    global brick_x
    brick_x = random.randint(0, 4)

def draw_game():
    """绘制游戏画面：玩家（高亮）+ 砖块（低亮）"""
    global game_state, player_col, brick_x, brick_y
    display.clear()
    # 绘制玩家（固定在最下方行，亮度9=最亮）
    display.set_pixel(player_col, player_fixed_row, 9)
    # 游戏运行中绘制砖块（亮度3=低亮）
    if game_state == 1:
        display.set_pixel(brick_x, brick_y, 7)

def reset_game():
    """重置游戏所有状态"""
    global game_state, player_col, brick_x, brick_y, score
    global a_pressed_flag, b_pressed_flag
    game_state = 1
    player_col = player_init_col
    brick_x = random.randint(0, 4)
    brick_y = 0
    score = 0
    a_pressed_flag = False
    b_pressed_flag = False
    display.clear()

def check_collision():
    """碰撞检测：砖块与玩家同列同行则游戏结束"""
    global collision_x, collision_y, game_state, flash_count
    collision_x = (brick_x == player_col)
    collision_y = (brick_y == player_fixed_row)
    if collision_x and collision_y:
        game_state = 2
        display.clear()
        flash_count = 0

# ===================== 主循环 =====================
def on_forever():
    """游戏主逻辑循环"""
    global ab_pressed, can_start, start_flag, last_brick_time
    global flash_count, player_col, a_pressed_flag, b_pressed_flag
    global current_time, time_passed, brick_x, brick_y, score

    # 1. A+B 同时按：开始/重置游戏（防抖）
    ab_pressed = button_a.is_pressed() and button_b.is_pressed()
    can_start = ab_pressed and (game_state != 1)
    if can_start:
        if start_flag == 0:
            start_flag = 1
            utime.sleep_ms(20)
            if button_a.is_pressed() and button_b.is_pressed():
                reset_game()
                last_brick_time = running_time()
    else:
        start_flag = 0

    # 2. 游戏未开始状态
    if game_state == 0:
        display.show(Image.DIAMOND_SMALL)
        utime.sleep_ms(500)
        display.show(Image.DIAMOND)
        utime.sleep_ms(500)

    # 3. 游戏结束状态
    if game_state == 2:
        if flash_count < 3:
            display.scroll(score)
            utime.sleep_ms(300)
            display.clear()
            utime.sleep_ms(200)
            flash_count += 1
        else:
            display.scroll(score)
            utime.sleep_ms(500)

    # 4. 游戏运行中逻辑
    if game_state == 1:
        # 左移键（pin15）：修正电平判断 + 仅移动成功时设置flag
        if not pin15.read_digital():  # 按下=低电平0，触发左移
            if not a_pressed_flag:
                if player_col > 0:
                    player_col -= 1
                    a_pressed_flag = True  # 仅移动成功时设为True
                    utime.sleep_ms(50)
        else:
            a_pressed_flag = False  # 松开按键立即重置flag

        # 右移键（pin13）：修正电平判断 + 仅移动成功时设置flag
        if not pin13.read_digital():  # 按下=低电平0，触发右移
            if not b_pressed_flag:
                if player_col < 4:
                    player_col += 1
                    b_pressed_flag = True  # 仅移动成功时设为True
                    utime.sleep_ms(50)
        else:
            b_pressed_flag = False  # 松开按键立即重置flag

        # 砖块下落逻辑
        current_time = running_time()
        time_passed = current_time - last_brick_time
        if time_passed > brick_move_speed:
            last_brick_time = current_time
            brick_y += 1
            if brick_y > 4:
                brick_x = random.randint(0, 4)
                brick_y = 0
                score += 1

        # 碰撞检测 + 画面刷新
        check_collision()
        draw_game()

# ===================== 程序入口 =====================
if __name__ == "__main__":
    on_start()
    while True:
        on_forever()
        utime.sleep_ms(10)
