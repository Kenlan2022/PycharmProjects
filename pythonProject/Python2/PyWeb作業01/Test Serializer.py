from Python2.PyWeb作業01.models import Product, Serializer

p1 = Product()
p1.set(1, "Apple", 100)
Product.objects.save(p1)


p2 = Product()
p2.set(2, "Banana", 200)
Product.objects.save(p2)

print("----儲存成jason格式----")
ser = Serializer()
s = ser.serialize(Product.objects.all())
print(s)
