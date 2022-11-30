# 建立List 簡化寫法[]
a = ["apple", "banana", "apple", "cherry"]
print(a)
print(a[0])
print(a[1])
print('list 長度(數字項目)', len(a))
print("apple 長度(字數)", len(a[0]))
# 建立list可接受任意類型資料
b = [100, 3.14, "Hello"]
print(b)
print(b[0])
print(b[1])
print("b長度", len(b))
print("a", type(a))
print("b", type(b))
# 標準寫法 透過 list() 建立list
c = list(("a", "b", "c"))
print(c)
c.append("d")
print(c)
c.insert(1,"x")
print(c) #插入第1項之後，後方物件向後移一格
c.remove("a")
print(c)
c.pop(0)
print(c)