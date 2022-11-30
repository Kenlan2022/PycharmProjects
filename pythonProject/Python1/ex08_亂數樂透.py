import random #載入程式模組

n = random.randint(1, 100) #產生隨機範圍內的數字
print(n)

#a = [1, 2, 3, 4, 5]
a = list((1 ,2 , 3, 4, 5))
print(a)
print("長度", len(a))

i = random.randint(1,3)
print("抽出i項", i)
v = a.pop(i)
print("值", v)

print(a)
print("長度", len(a))


