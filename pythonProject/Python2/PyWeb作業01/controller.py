from Python2.PyWeb作業01.models import Product
from Python2.PyWeb作業01.views import Outputview


class Controller:
    def __init__(self):
        pass

    def run(self):
        pd1 = Product()
        pd1.set(1, "Apple", 100)

        pd2 = Product()
        pd2.set(2, "Banana", 200)

        ov1 = Outputview()
        ov1.set(pd=pd1)
        ov1.output()

        ov2 = Outputview()
        ov2.set(pd=pd2)
        ov2.output()