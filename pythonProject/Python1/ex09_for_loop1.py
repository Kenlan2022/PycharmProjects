for i in range (1,3):
    print("我很強", i)
a = ["A", "B", "C" ,"D"]

print(a[1]) #B
print(a[2]) #C

for i in range(1,3):
    print(a[i])

a = ["apple", "banana", "cherry"]
for x in a:
    print(x)

print(range(3))
print(range(1,3))

print("長度",len(a))
for i in range(len(a)):
    print(f"第{i}項")
    print(a[i])
for n in range(1,4):
    print(n)
b = list()
for n in range(1,4): #4不含, 1~3
    b.append(n)#將n加入b
print("b", b)