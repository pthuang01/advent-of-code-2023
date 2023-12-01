'''
題目：
在每行上，透過將第一位數字和最後一位數字（按順序）組合形成一個兩位數來找到校準值。

例如：

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
在本例中，這四行的校準值為12、38、15、 和77。將這些加在一起產生142.

考慮您的整個校準文件。所有校準值的總和是多少？
'''
import re  # 引入正規表達式模組

def find_calibration_values(lines):
    total = 0  # 初始化總和為0
    for line in lines:  # 遍歷每一行
        digits = re.findall(r'\d', line)  # 使用正規表達式找出所有的數字
        if digits:  # 如果該行有數字
            calibration_value = int(digits[0] + digits[-1])  # 將第一個數字和最後一個數字組合成一個兩位數的數字
            total += calibration_value  # 將該行的校準值加到總和上
    return total  # 返回總和

lines = [  # 校準文件
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet"
]

print(find_calibration_values(lines))  # 印出總和
