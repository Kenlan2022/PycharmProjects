from Python2.Lab02物件導向後.models import Date

d = Date()
print(d) #如果類別有__str__會自動呼叫

d.set(2022,1,2)
print(d) #如果有__str__會自動呼叫