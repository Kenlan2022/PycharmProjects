from Python2.Lab06Manager.models import Product
p1 = Product(1, "Apple",100)
p2 = Product(2, "Banana",200)
all = [p1,p2]
data = list() #list 相當於 JSON array
for p in all:
    #將產品放到字典dict 相當JSON object
    d = {"id":p.id,"name":p.name,"price":p.price}
    data.append(d) #將 產品字典 放到 串列

import json
s = json.dumps(data) #data 轉換json 字串
print(s)
