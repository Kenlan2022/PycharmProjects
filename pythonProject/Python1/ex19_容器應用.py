import random
print("--- 產生樂透 ---")
lotto = set() #set 建立空set
while True:
    n = random.randint(1,42)
    lotto.add(n) # add() set新增資料
    if len(lotto) == 6:
        break
print(lotto)

print("--- 輸入客戶名稱 ---")
name = input("name: ")

print("--- 打包到字典 ---")
data = dict() #dict() 建立空字典
data[name] = lotto #name當key, lotto當value
print(data)

print("--- 查詢樂透資料 ---")
key = input("請輸入key(name): ")
if key in data:
    print(data[key])
else:
    print("查無此key")


#:字典 增查修刪

a = dict()
print(a)

print("--- 新增(若key 不存在)---")
key = 100
value = "中正區"
a[key] = value
print(a)

print("--- 查詢 ---")
key = 100
print(a[key])

print("--- 修改(若key存在) ---")
key = 100
value = "中正"
a[key] = value
print(a)

a[key] = value
print("--- del 刪除 (若key 不存在會引起錯誤) ---")
key = 100
#key = 200
if key in a:
    del a[key]
    print(key, "刪除成功")
else:
    print(key, "刪除失敗 key 不存在")
print(a)

a = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print("--- 讀取所有 key ---")
for key in a:
#for key in a.keys():
    print(key)

print("--- 讀取所有 Value ---")
for value in a.values():
    print(value)

print("--- 讀取所有 item ---")
#每個item是tuple, 自動從tuple 讀取 key 與value
for key,value in a.items():
    print(key, value)