import csv
import json


class Manager:
    def __init__(self): #建立list
        self.db = list()

    def save(self,obj): #添加資料
        self.db.append(obj)

    def all(self):
        return self.db

    def filter(self, id):
        i = id-1
        if self.db[i] is None:
            return("資料不存在")
        else:
            return(self.db[i])

    def delete(self,id):
        j = id -1
        if self.db[j] is not None:
            self.db[j] = None
            return("刪除成功")
        else:
            return("刪除失敗,資料不存在")

    def alter(self,id,name,price):
        i = id-1
        self.old_P = self.db[i]
        print(self.old_P)
        self.new_P = Product.set(i,name,price)
        print(self.new_P)
        print(self.new_P)

    def __str__(self):
        return f"{self.id}-{self.name}-{self.price}"


class Product:
    objects = Manager()

    def __init__(self):
        self.id = None
        self.name = None
        self.price = None

    def set(self,id,name,price):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.id}-{self.name}-{self.price}"


class Serializer:
    def __init__(self):
        pass

    def serialize(self,all):
        data = list()
        for p in all:
            d = {"id":p.id, "name":p.name, "price":p.price}
            data.append(d)
        s = json.dumps(data)
        return s

class CSV:
    def __init__(self):
        pass

    def saveCSV(self, data):
        with open("進階一.csv", "w", newline="") as self.csvfile:
            writer = csv.writer(self.csvfile)
            writer.writerow(data)

    def loadCSV(self):
        with open("進階一.csv", "r", newline="") as self.csvfile:
            self.reader = csv.reader(self.csvfile)
            for row in self.reader:
                return(row)

class Jason:
    def __init__(self):
        pass

    def saveJason(self,data):
        with open("進階二.jason", "w",newline="") as self.jsfile:
            self.jsfile.write(data)



