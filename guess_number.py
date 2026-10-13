"""
猜数字小游戏
-----------
规则：
  1. 电脑随机生成一个 1-100 之间的整数
  2. 用户输入自己猜的数字
  3. 程序提示"大了"或"小了"，直到猜中
  4. 猜中后显示总猜测次数

单文件运行：python guess_number.py
"""

import random  # 导入随机数模块

LOW = 1     # 数字范围下限
HIGH = 100  # 数字范围上限


def play_once():
    """进行一局游戏，返回本局猜测次数"""
    answer = random.randint(LOW, HIGH)  # 随机生成答案（含两端）
    count = 0                           # 记录猜测次数

    print(f"我已经想好了一个 {LOW} 到 {HIGH} 之间的整数，来猜猜看吧！")

    while True:
        raw = input("请输入你猜的数字：").strip()

        # 输入校验：必须是整数且在合法范围内
        if not raw.lstrip("-").isdigit():
            print("⚠️  输入无效，请输入一个整数。")
            continue
        guess = int(raw)
        if guess < LOW or guess > HIGH:
            print(f"⚠️  请输入 {LOW} 到 {HIGH} 之间的数字。")
            continue

        count += 1  # 有效猜测才计数

        if guess > answer:
            print("大了")
        elif guess < answer:
            print("小了")
        else:
            print(f"🎉 恭喜猜中！答案就是 {answer}。")
            print(f"你一共猜了 {count} 次。")
            break


def main():
    """主流程：可反复开局"""
    while True:
        play_once()
        again = input("再来一局？(y/n)：").strip().lower()
        if again != "y":
            print("游戏结束，下次见！")
            break


if __name__ == "__main__":
    main()
