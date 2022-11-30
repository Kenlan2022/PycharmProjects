#串列當資料庫
db = list()

#新增
p1 = Product(1, "Apple", 100)
db.append(p1) #第0項

p2 = Product(2, "Banana", 200)
db.append(p2)

print("---所有資料---")
    for p in db:
        print(p)

print("---查詢 id=1---")
id = 1
i = id-1 #串列第i項
p = db[i]

print(p)

print("---修改 id=1---")
id = 1
i = id-1
old_p = db[i]
print("舊有資料, old_p")
new_p1 = Product(1, "New Apple", 1000)
db[i] = new_p1
print("修改成功", new_p1)

print("---所有資料---")
for p in db:
    print(p)

print("--- 刪除資料 id=1 ---")
id = 1
i = id-1
p = db[i]
if p is not None:
    print("刪除成功", p)
else:
    print("刪除資料,資料不存在")

print("--- 所有資料 ---")
for p in db:
    print(p)