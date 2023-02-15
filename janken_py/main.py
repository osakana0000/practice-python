import random
from art import ascii_art
import os


def get_number():
    flag = True
    while (True):
        try:
            player = int(input())
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


def main():
    os.system("clear")

    # 勝ち2, あいこ1, 負け0
    hand_fig = {1: "グー", 2: "チョキ", 3: "パー"}

    print("じゃん．．．けん．．．")
    while (True):
        print("グー：１　チョキ：２　パー：３　→　", end="")

        player = get_number()
        cpu = random.randint(1, 3)
        judge = match_pattern(player, cpu)

        print(f'あなた：{hand_fig[player]}　CPU：{hand_fig[cpu]}')
        print(ascii_art(judge))

        if judge == 2 or judge == 0:
            break


if __name__ == "__main__":
    main()
    # get_number()
