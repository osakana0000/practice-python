import random
from art import ascii_art, cpu_art
import os
import time


def get_number():
    flag = True
    while (True):
        try:
            player = random.randint(1, 3)
            if 1 <= player <= 3:
                return player
            else:
                print("１～３の数値を入力してください：", end="")
        except ValueError:
            print("文字が入力されました。数値を入力してください。：", end="")


def match_pattern(player, cpu):
    pattern = [
        [1, 2],
        [2, 3],
        [3, 1]
    ]
    if player == cpu:
        return 1

    for i in range(3):
        if player == pattern[i][0] and cpu == pattern[i][1]:
            return 2

    return 0


def main(total, win_count):
    # 勝ち2, あいこ1, 負け0
    hand_fig = {1: "グー", 2: "チョキ", 3: "パー"}

    if total > 0:
        print(f'{total}戦目')
        print(f'{win_count}勝', end="　")
        print("*" * int((win_count / total) * 100))
        print(f'{total - win_count}敗', end="　")
        print("*" * int((total - win_count) / total * 100))

    print("じゃん．．．けん．．．")
    while (True):
        print("グー：１　チョキ：２　パー：３　→　", end="")

        player = get_number()
        cpu = random.randint(1, 3)
        judge = match_pattern(player, cpu)

        print(f'あなた：{hand_fig[player]}　CPU：{hand_fig[cpu]}')
        print(ascii_art(judge))

        if judge == 2:
            return total + 1, win_count + 1
        elif judge == 0:
            return total + 1, win_count


if __name__ == "__main__":
    total = 0
    win_count = 0
    count = 1
    while (True):
        os.system("clear")
        print(cpu_art(count))

        total, win_count = main(total, win_count)

        if count == 10:
            count = 1
        else:
            count += 1

        time.sleep(0.05)
