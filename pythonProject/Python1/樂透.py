import random
def 產生42號碼():
    x = list()
    for n in range(1,43):
        x.append(n)
    return x

def 隨機抽出1個號碼(x):
    最前項 = 0
    最後項 = len(x) - 1
    i = random.randint(最前項,最後項)
    v = x.pop(i)
    return v
