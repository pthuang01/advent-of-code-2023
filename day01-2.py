'''
你的計算似乎不太正確。看起來有些數字實際上是用字母拼出來的：one, two, three, four, five, six, seven, eight, 和 nine 也算作有效的「數字」。

帶著這個新的訊息，你現在需要找到每一行的真正的第一個和最後一個數字。例如：

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
在這個例子中，校準值分別是 29, 83, 13, 24, 42, 14, 和 76。把它們加起來得到 281。

所有校準值的總和是多少？
'''
# 定義一個函數 find_numbers，輸入是一個字串 s
def find_numbers(s):
    # 建立一個字典 num_dict，將英文數字對應到阿拉伯數字
    num_dict = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 
                'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    # 建立一個空的列表 num_list，用來儲存找到的數字
    num_list = []
    # 遍歷字串 s 的每個字符
    for i in range(len(s)):
        # 遍歷從當前字符開始的每個子字串
        for j in range(i+1, min(i+6, len(s)+1)):
            # 取出子字串
            sub = s[i:j]
            # 如果子字串在 num_dict 中，則將其對應的阿拉伯數字添加到 num_list
            if sub in num_dict:
                num_list.append(num_dict[sub])
            # 如果子字串是數字，則直接添加到 num_list
            elif sub.isdigit():
                num_list.append(sub)
    # 如果 num_list 為空，則返回 None
    if len(num_list) == 0:
        return None
    # 如果 num_list 只有一個元素，則返回兩次該元素
    elif len(num_list) == 1:
        return num_list[0] + num_list[0]
    # 否則，返回 num_list 的第一個和最後一個元素的和
    else:
        return num_list[0] + num_list[-1]

# 建立一個字串列表 strings
strings = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen"]
# 初始化一個變數 total 為 0，用來儲存所有數字的總和
total = 0
# 遍歷 strings 中的每個字串
for s in strings:
    # 調用 find_numbers 函數找到字串中的數字，並加到 total
    total += int(find_numbers(s))

# 輸出 total
print(total)
