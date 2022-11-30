from Python2.Lab05.models import Product
from Python2.PyWeb作業01.views import Outputview


class Controller:
    def __init__(self):
        pass

    def run(self):
        product = Product()
        product.set(1,"Apple",100)
        ov = Outputview()
        ov.set(product)
        ov.output()