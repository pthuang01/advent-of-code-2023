# 定義一個函數來解析遊戲的記錄
def parse_games(games):
    game_dict = {}
    for game in games:
        # 分割遊戲ID和回合
        game_id, rounds = game.split(': ')
        # 從遊戲ID中取出數字
        game_id = int(game_id.split(' ')[1])
        # 分割每一個回合
        rounds = rounds.split('; ')
        round_list = []
        for round in rounds:
            color_dict = {}
            # 分割每一種顏色的方塊
            colors = round.split(', ')
            for color in colors:
                # 分割數量和顏色
                num, color = color.split(' ')
                # 將數量轉換為整數並存儲到字典中
                color_dict[color] = int(num)
            # 將每一回合的結果存儲到列表中
            round_list.append(color_dict)
        # 將每一個遊戲的結果存儲到字典中
        game_dict[game_id] = round_list
    return game_dict

# 定義一個函數來檢查每一個遊戲是否可能只有12個紅色方塊，13個綠色方塊，和14個藍色方塊
def check_games(game_dict, red, green, blue):
    possible_games = []
    for game_id, rounds in game_dict.items():
        possible = True
        for round in rounds:
            # 如果任何一回合中的任何一種顏色的方塊數量超過了限制，則該遊戲不可能完成
            if round.get('red', 0) > red or round.get('green', 0) > green or round.get('blue', 0) > blue:
                possible = False
                break
        # 如果遊戲可能，則將其遊戲ID加入到可能的遊戲列表中
        if possible:
            possible_games.append(game_id)
    return possible_games

# 測試數據
games = [
    'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
]

# 解析遊戲的記錄
game_dict = parse_games(games)
# 檢查每一個遊戲是否可能只有12個紅色方塊，13個綠色方塊，和14個藍色方塊
possible_games = check_games(game_dict, 12, 13, 14)
# 輸出可能的遊戲ID的總和
print(sum(possible_games))
