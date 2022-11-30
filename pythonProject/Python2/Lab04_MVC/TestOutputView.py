#準備零件
from Python2.Lab03.日期 import Date

d = Date()
d.set(2000,1,1) #組裝3零件 2000 1 1

#準備零件
st1 = Student()
st1.set(1,"Tom",d) #組裝3零件

#準備零件
ov = OutputView()
ov.set(st1)
ov.output()
