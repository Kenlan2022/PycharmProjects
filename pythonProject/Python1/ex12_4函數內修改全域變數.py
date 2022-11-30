def myfunc():
    x = 200
    print('myunc local x', x)

def myfunc2():
    global x, y
    x = 1
    y = 2
    print('myfun2 修改 global x', x)
    print('myfunc 修改 global y', y)
    print('-------------------------------')
    myfunc()
    print('-------------------------------')
    print('主流程 global x', x)
    print('主流程 global y', y)
    print('-------------------------------')
    myfunc2()
    print('-------------------------------')
    print('主流程 global x', x)
    print('主程式 global y', y)

#設計函數，解決重複程式碼
def CreateList():
    i = []
    for n in range(1,43):
        i.append(n)
    return i

a = CreateList()
print(a)

#自我挑戰:設計函數，產生能指定數量號碼

def CreateCertainList(y):
    i = []
    for n in range(1,y+1):
        i.append(n)
    return i

b = CreateCertainList(3)
print(b)