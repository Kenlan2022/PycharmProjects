

import random

def Client():
    while True:
        name = input("請輸入名字:")
        a = list(name)
        if name != "" and len(a) >= 2:
            return name
        else:
            print("格式不正確")
            continue
a = Client()
print(type(a))