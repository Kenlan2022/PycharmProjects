import random
def 隨機抽(x): #接受傳入一個list
    i = random.randint(0,len(x)-1)
    print("i = ",i)
    v = x.pop(i)
    return  v

#主流程
for y in range(3):
    x = [10,5,3]
    v = 隨機抽(x)
    print("結果",v)
    print()