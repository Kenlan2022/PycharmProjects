class Manager:
    def __init__(self): #串列當資料庫
        self.db = list()

    def save(self,obj): #新增資料
        self.db.append(obj)

    def all(self): #查詢所有資料
        return self.db

    def filter(self,id): #查詢單筆資料
        i = id-1
        return self.db[i]

class Product:
    #類別屬性 共享資料(全域變數)
    objects = Manager()
    def __init__(self,id,name,price):
        #物件屬性
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.id}{self.name}{self.price}"
