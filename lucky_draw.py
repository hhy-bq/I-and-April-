import random

# ---------- 奖池 ----------
gold   = ["无敌金币", "至高金币", "完美金币"]
silver = ["无敌银币", "至高银币", "完美银币"]

players = ["小明", "小红", "小黑"]
ROUNDS = 10


for player in players:
    print(f"\n===== 当前玩家: {player} =====")

    # 这一局里每个人的战绩
    stats = {"金": 0, "银": 0, "空": 0}

    for i in range(1, ROUNDS + 1):
        roll = random.randint(1, 100)

        if roll <= 5:                       # 5%
            prize = random.choice(gold)
            print(f"第 {i:2d} 次  You are lucky! 你抽到了: {prize}")
            stats["金"] += 1

        elif roll <= 20:                    # 20% - 5% = 15%
            prize = random.choice(silver)
            print(f"第 {i:2d} 次  你抽到了: {prize}")
            stats["银"] += 1

        else:                               # 剩下 80%
            print(f"第 {i:2d} 次  believe in yourself, 下次一定！")
            stats["空"] += 1

    print(f"—— {player}：金 {stats['金']}，银 {stats['银']}，空 {stats['空']}")
