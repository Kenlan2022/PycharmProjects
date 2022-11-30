v1 = {"name" : "Email", "year" : 2004 }
v2 = {"name" : "Tobias", "year" : 2007}
v3 = {"name" : "Linus", "year": 2011}
k1 = 1
k2 = 2
k3 = 3
#dict 巢狀資料結構
d = {
    k1 : v1,
    k2 : v2,
    k3 : v3,
}

for v in d.values():
    print(v)
print("查詢 v1", d[k1])
print("----------------------")
# list 巢狀資料結構
l = [v1, v2, v3]
for v in l :
    print(v)
print("查詢 v1", l[0])