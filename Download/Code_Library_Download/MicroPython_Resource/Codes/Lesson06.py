from microbit import *
import neopixel
import radio

# 全局变量
round2 = 1
check = 1
me = 0
you = 0
wins = 0
loses = 0
draws = 0
gameResults = []
strip = None

pin13.set_pull(pin13.PULL_UP)
pin15.set_pull(pin15.PULL_UP)
pin16.set_pull(pin16.PULL_UP)
# 初始化彩灯（4颗灯，连接到引脚P8）
strip = neopixel.NeoPixel(pin8, 4)

# 重置游戏状态
def resetGame():
    global me, you, round2, wins, loses, draws, gameResults, check
    me = 0
    you = 0
    round2 = 1
    wins = 0
    loses = 0
    draws = 0
    gameResults = []
    check = 1
    resetLights()
    display.show(Image.YES)

# 无线接收对手选择
def on_received_message(receivedMsg):
    global you
    if you == 0:
        # 如果是字符串类型的字符，转换为整数
        if isinstance(receivedMsg, str) and receivedMsg in ['1', '2', '3']:
            you = int(receivedMsg)
        # 如果是整数，直接使用
        elif isinstance(receivedMsg, int) and receivedMsg in [1, 2, 3]:
            you = receivedMsg

# 重置所有彩灯
def resetLights():
    for i in range(4):
        strip[i] = (0, 0, 0)  # 黑色
    strip.show()

# 判断是否需要第四局
def needFourthRound():
    # 情况1：三局都为平局 -> 需要第四局，返回2
    if wins == 0 and loses == 0 and draws == 3:
        return 2
    # 情况2：一胜一负一平 -> 需要第四局，返回1
    if wins == 1 and loses == 1 and draws == 1:
        return 1
    # 其他情况不需要第四局
    return 0

# 显示单局结果彩灯
def showRoundResult(roundNum, result):
    if roundNum <= 4:
        if result == 1:
            # 赢：绿色
            strip[roundNum - 1] = (0, 255, 0)
        elif result == 0:
            # 平：黄色
            strip[roundNum - 1] = (255, 255, 0)
        else:
            # 输：红色
            strip[roundNum - 1] = (255, 0, 0)
        strip.show()

# 初始化游戏
radio.on()
radio.config(group=1)
check = 1
me = 0
you = 0
strip.clear()
strip.show()
display.show(Image.YES)

# 主游戏循环
while True:

    # 双方都选择后处理结果
    if me != 0 and you != 0:
        # 当前局结果：1=赢, 0=平, -1=输
        resultSymbol = "="
        # 判断当前局胜负
        if me == you:
            resultSymbol = "="
            # 平局
            result2 = 0
            draws += 1
        elif me == 2 and you == 1 or (me == 3 and you == 2 or me == 1 and you == 3):
            resultSymbol = "W"
            # 赢
            result2 = 1
            wins += 1
        else:
            resultSymbol = "L"
            # 输
            result2 = -1
            loses += 1

        # 保存本局结果
        gameResults.append(result2)

        # 显示本局结果
        display.scroll(resultSymbol)

        # 显示对应彩灯
        showRoundResult(round2, result2)

        sleep(3000)  # 相当于 basic.pause(3000)

        # 判断游戏是否继续
        if round2 == 3:
            # 前三局结束，判断是否需要第四局
            fourth_round_needed = needFourthRound()
            if fourth_round_needed:
                # 需要第四局
                round2 = 4
                if fourth_round_needed == 2:
                    display.scroll("FINAL")
                sleep(1000)
                display.show(Image.YES)
                check = 1
                me = 0
                you = 0
            else:
                # 不需要第四局，游戏结束
                # 判断最终胜负
                if wins > loses:
                    display.scroll("WINNER")
                elif loses > wins:
                    display.scroll("LOSER")
                else:
                    display.scroll("TIE")
                sleep(3000)
                resetGame()
        elif round2 == 4:
            # 第四局结束，游戏结束
            display.scroll("GAME OVER")
            sleep(3000)
            resetGame()
        else:
            # 继续下一局（第1或2局后）
            round2 += 1
            display.show(Image.YES)
            check = 1
            me = 0
            you = 0

    # 检查按钮输入（原 on_forever2 函数）
    if check == 1:
        # 注意：micro:bit 只有两个按钮，这里使用组合键来模拟三个按钮
        # 假设使用以下映射：
        # RUP -> 按钮A
        # RLEFT -> 按钮B
        # RDOWN -> 同时按A+B

        if  pin13.read_digital()==0:
            # RDOWN（布）-> 发送字符 '3'，显示正方形
            radio.send('3')
            display.show(Image.SQUARE)
            me = 3
            check = 0
            sleep(200)
        elif pin15.read_digital()==0:
            # RUP（剪刀）-> 发送字符 '1'，显示剪刀
            radio.send('1')
            display.show(Image('99009:'
                                '99090:'
                                '00900:'
                                '99090:'
                                '99009'))
            me = 1
            check = 0
            sleep(200)
        elif pin16.read_digital()==0:
            # RLEFT（石头）-> 发送字符 '2'，显示小正方形
            radio.send('2')
            display.show(Image.SQUARE_SMALL)
            me = 2
            check = 0
            sleep(200)

    # 接收无线电数据
    try:
        received = radio.receive()
        if received is not None:
            on_received_message(received)
    except:
        pass

    sleep(100)  # 短暂延迟，防止CPU过载
