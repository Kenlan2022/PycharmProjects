class Serializer:
    def __init__(self):
        pass
    #所有產品資料

    def serializer(self,all):
        data = list() #list 相當於JSON arry
        for p in all:
            #將字典dict相當於JSON object
        d = {"id":p.id,"name":p.name,"price":p.price}
        data.append(d) #將 產品字典放到串列
        import json
        s = json.dumps(data) #data 轉換成Json 字串
        return s