#控制
from Python2.Lab03.日期 import Date
from Python2.Lab04_MVC.models import Student
from Python2.Lab04_MVC.views import OutputView


class Controller:
    def __init__(self):
        pass
    def run(self):
        #準備零件
        d = Date()
        d.set(2000,1,1) #組裝3零件

        #準備零件
        st1 = Student() #組裝3零件
        st1.set(1,"Tom", d)

        #準備零件
        ov = OutputView()
        ov.set(st1)
        ov.output()

    

