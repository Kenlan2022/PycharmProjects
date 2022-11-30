from Python2.Lab06Manager.models import Product
from Python2.Lab07_序列化.serializers import Serializer

p1 = Product(1,"Apple",100)
Product.objects.save(p1) #第0項

p2 = Product(2,"Banana",200) #第1項
Product.objects.save(p2)

#序列化JSON
ser = Serializer()
s = ser.serializer(Product.objects.all())
print(s)