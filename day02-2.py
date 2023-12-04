# 定義遊戲數據
game_data = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]

# 轉換遊戲數據
games = []
for data in game_data:
    # 創建一個新的遊戲字典
    game = {}
    # 分割每個遊戲的回合
    rounds = data.split(":")[1].split(";")
    for round in rounds:
        # 分割每個回合的立方體
        cubes = round.split(",")
        for cube in cubes:
            # 分割立方體的數量和顏色
            parts = cube.strip().split(" ")
            count = int(parts[0])
            color = parts[1]
            # 如果顏色還沒有在遊戲字典中，則添加它
            if color not in game:
                game[color] = []
            # 將立方體的數量添加到遊戲字典中
            game[color].append(count)
    # 將遊戲字典添加到遊戲列表中
    games.append(game)

# 計算每個遊戲的最小立方體數量和能量
total_power = 0
for game in games:
    # 找到每種顏色的立方體的最大數量
    min_cubes = {color: max(game[color]) for color in game}
    # 計算乘積
    power = min_cubes["blue"] * min_cubes["red"] * min_cubes["green"]
    # 將能量添加到總能量中
    total_power += power

print(total_power)
