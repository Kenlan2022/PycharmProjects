import random
def 產生42個號碼():
    x = list()
    for n in range(1, 43): #43不含, 1~42
        x.append(n) #將n加入list x
    return x

def 隨機抽出1個號碼(x):
    最前項 = 0
    最後項 = len(x) - 1
    i = random.randint(最前項, 最後項)# 亂數瘸定 抽第幾項
    v = x.pop(i)
    return v

# 自我挑戰
def 隨機抽出6個號碼(x):
    最前項 = 0             #X清單中第一個數編號
    最後項 = len(x)-1      #X清單中最後一個數的編號
    ll = list()           #樂透存放清單
    v = list()
    b = int()
    for i in range(6):      #執行6次
        b = random.randint(最前項, 最後項) #從最前項編號到最後項編號隨機取一個數
        v = x.pop(b) #從X中取物件放到V變數
        ll.append(v)
    return ll

def swap(data, x, y):
    temp = data[x]
    data[x] = data[y]
    data[y] = temp

def one_bubble(data, end_index):
    for j in range(end_index):
        if data[j] > data[j+1]:
            swap(data,j ,j+1)


#主流程
a = 產生42個號碼()
print(a)
print('----------------------')
#測試抽號碼
n = 隨機抽出1個號碼(a)
print(n)
print(a)

n = 隨機抽出1個號碼(a)
print(n)
print(a)
print('----------------------')
#自我挑戰
n = 隨機抽出6個號碼(a)
print(n)


print('----------------------')
#利用for循環6次, 其中i沒用到
for i in range(6):
    n = 隨機抽出1個號碼(a)
print(n)

a = 產生42個號碼()
print(a)
n = 隨機抽出6個號碼(a)
print(n)

data_count = len(n)
print(len(n))
for i in range(data_count-1-i):
    one_bubble(n,data_count-1-i)
    print('第',i,'回合結果:',n)
print('排序結束')