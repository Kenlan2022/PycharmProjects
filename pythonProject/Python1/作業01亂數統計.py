import random

def GenerateTenInt():
    l = list()
    for i in range(1,11):
        for j in range(5):
            a = random.randint(1,5)
        l.append(a)
    return (l)

#用亂數產生10個整數，值範圍1~5
c = GenerateTenInt()
print("隨機10個5以內整數: ",GenerateTenInt())
print("---------")
# 統計奇數偶數
def Distinguish (numbers):
    OddNumber = list()
    EvenNumber = list()
    for i in range(len(numbers)):
        if numbers[i]%2 == 0:
            EvenNumber.append(numbers[i])
        else:
            OddNumber.append(numbers[i])
    print("有{0}個奇數, 數列:".format(len(OddNumber)), sorted(OddNumber))
    print("有{0}個偶數, 數列:".format(len(EvenNumber)), sorted(EvenNumber))

a= Distinguish(c)
print("---------")
# 最大值
d = max(c)
print("最大值: ",d)
print("---------")
# 最小值
e = min(c)
print("最小值: ",e)
print("---------")
# 加總
f = sum(c)
print("加總: ",f)
print("---------")
# 平均
def Average(numbers):
    while True:
        try:
            x = sum(numbers)
            y = x/len(numbers)
            return y
        except ValueError:
            return str("格式錯誤")


print("平均: ",Average(c))
print("---------")
# 1~5個出現幾次
def CountNumbers(numbers):
    for i in range(1,6):
        for j in range(len(numbers)):
            a = numbers.count(i)
        print("數字{0}有{1}個".format(i,a))

C = CountNumbers(c)