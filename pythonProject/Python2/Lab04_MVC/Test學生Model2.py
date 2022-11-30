#準備零件
from Python2.Lab03.日期 import Date

d = Date()
d.set(2000,1,1) #組裝3零件 2000 1 1

#準備零件

st1 = Student()
st1.set(1,"Tom",d) #組裝3零件
print(st1) #如果類別有__str__會自動呼叫

st2 = Student()
st2.set(2,"Amy", d) #組裝3零件
print(st2) #如果類別有__str__會自動呼叫

print("---修改日期---")

st1.birthdate.year = 1999
print(st1)
print(st2)


