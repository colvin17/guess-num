# 產生1~100隨機整數 (不印出)
# 讓使用者重複輸入數字去猜
# 猜對了，印出"答對了!"
# 猜錯了，印出"比答案大或小"

import random

r = random.randint(1, 100)
while True:
    num = input('請猜數字:')
    num = int(num)
    if num == r:
        print ('答對了!')
        break
    elif num > r:
        print('答錯了，比答案大')
    elif num < r:
        print('答錯了，比答案小')