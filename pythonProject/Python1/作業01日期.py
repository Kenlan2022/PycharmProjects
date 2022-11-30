import random
def leapyear(y): #判斷閏年函數
    f = y%4 == 0 #4的倍數
    h = y%100 == 0 #100的倍數
    fh = y%400 == 0 #400的倍數
    l1 = f and (not h) #條件1
    l2 = fh #條件2
    if l1 or l2:
        return True
    else:
        return False
y = random.randint(1,9999)
m = random.randint(1,12)
a = [y] #將年份加進list
a.append(m) #將月份加進List
if leapyear(y) == True and (m == 2):
    d = random.randint(1,29)
    a.append(d)
elif leapyear(y) == False and(m == 2):
    d = random.randint(1,28)
    a.append(d)
elif m == 1 or 3 or 5 or 7 or 8 or 10 :
    d = random.randint(1,31)
    a.append(d)
else:
    d = random.randint(1,30)
    a.append(d)
#判斷日期並加入
print(a)


