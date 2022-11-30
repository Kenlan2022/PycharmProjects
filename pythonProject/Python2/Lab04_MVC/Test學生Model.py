from Python2.Lab02物件導向後.models import Date, Student

#準備零件
d = Date()
d.set(2000,1,1) #組裝3零件 2000 1 1

#準備零件
st = Student()
st.set(1,"Tom", d) #組裝3零件
print(st) #如果類別有__str__會自動呼叫



