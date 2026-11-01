import random

CHOICES = ["剪刀", "石头", "布"]

BEATS = {"剪刀": "布", "石头": "剪刀", "布": "石头"}

WIN_ROUNDS = 5

player_win = 0
npc_win = 0

while True:
    raw = input("请输入(1剪刀, 2石头, 3布): ")

    if raw not in ["1", "2", "3"]:
        print("输入错误，请输入 1、2 或 3")
        continue

    player = CHOICES[int(raw) - 1]
    npc = random.choice(CHOICES)

    print(f"你出了: {player}，电脑出了: {npc}")

    if player == npc:
        print("平局！")
    elif BEATS[player] == npc:
        print("你赢了！")
        player_win += 1
    else:
        print("人机赢了！")
        npc_win += 1

    print(f"当前比分 - 你: {player_win} , 人机: {npc_win}\n")

    if player_win >= WIN_ROUNDS or npc_win >= WIN_ROUNDS:
        break


if player_win > npc_win:
    print("恭喜！你的总分数赢了！")
else:
    print("很遗憾，人机赢了你。")
