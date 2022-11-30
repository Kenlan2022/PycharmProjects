a =[]
a.append(3.14)
a.append(100)
a.append("hello")
print(a)
print(a[0])
a[0] = "Tom"
print(a)

print("--- tuple不可修改的list---")
b = (3.14, 100, "hello")
print(b)
print(b[0])
#b[0] = "Tom" #禁止修改
#print(b)

#讀取 打包 packing 裝箱
fruits = ("apple", "banna", "cherry")
f1 = fruits[0]
f2 = fruits[1]
f3 = fruits[2]
print(f1, f2, f3)
#簡化一行 unpacking 拆箱(複製資料)
f1 , f2, f3 = fruits
print(f1, f2, f3)
print(fruits)

print("--- for 迴圈 批次處理 容器資料 ---")
for x in fruits:
    print(x)
print("--- for 迴圈 索引資料 批次處理 容器資料---")
print("len(fruits)",len(fruits)) #3
for i in range(len(fruits)): #range(3) -> range(0,3) 不含3 ,0~2
    print("i", i)
    print(f"第{i}項{fruits[i]}")
print("--- set 是無序的不可修改的，並且不允許重複值 ---")
fruits = {"apple", "banna", "cherry", "apple"} #自動過濾重複值
print(fruits)
print("len(fruits)", len(fruits)) #3

fruits.add("guava") #add() 新增資料
print(fruits)
print("len(fruits)", len(fruits)) #3

fruits.add("guava") #add()新增資料
print(fruits)
print("len(fruits)", len(fruits)) #3

print("刪除 芭樂")
#x = fruits.remove("guava") #沒有返回值 None
#print("x", x)# None
fruits.remove("guava") #刪除 guava
print(fruits)
fruits.discard("guava") #刪除不存在的 guava 不會引發錯誤
#fruits.remove("guava") #刪除不存在的 guava 引發錯誤

print("--- set 放樂透號碼 ---")
import random
lotto = set()
while True:
    n = random.randint(1,42)
    lotto.add(n) #自動過濾重複資料
    if len(lotto) == 6:
        break
print("樂透開獎", lotto)

print("--- 字典 dict ---")
# st = {3.14} # set
# st = {} # dict
st = dict()
print("type(st) =", type(st))

#dict{key: value, Key: value ...}
st = {
    "name" : "Tom",
    "eng" : 100,
    "math" : 99
}
print(st)

print("--- dict 透過 key 取值 ---")
key = "name"
print("key為name 取值", st[key])
st = {0: "Tom", 1: 100, 2: 99}
key = 0
print("key為0取值, st[key]")

print('--- dict 客戶樂透 資料查詢 ---')
#寫法一 是先建立資料
lotto = {
    "Tom" :{13 ,5 , 22, 30, 41, 10},
    "Amy" :{40, 15, 2 ,10 , 16, 18}
}
print(lotto)
key = input("請輸入名字查詢樂透資料:")
if key in lotto: #如果key存在dict
    print(lotto[key]) #透過key取值
else:
    print("查無此人")
print()
print("寫法2 事後 建立資料")
lotto = dict()
print("目前配對資料", lotto)
print()

print("新增 配對資料")
key = "Tom"
Value = {13, 5, 22 ,30, 41, 10}
print(key)
print(Value)
lotto[key] = Value #key 若不存在，代表新增配對資料
print("目前配對資料", lotto)
print()

print("修改 配對資料")
key = "Tom"
Value = {1,2,3,4,5,6}
print(key)
print(Value)
lotto[key] = Value #key 若存在，代表修改配對資料
print("目前配對資料", lotto)
print()