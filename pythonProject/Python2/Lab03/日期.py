class Date:
    def __init__(self):
        self.year = None
        self.month = None
        self.day = None

    def 修改值(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    def 顯示(self):
        print(self.year,self.month,self.day)






#建立物件
d1 = Date()
d1.顯示()
d1.修改值(2022,2,10)
d1.顯示()