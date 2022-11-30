from Python2.PyWeb作業01.models import Product, Serializer, Jason

p1 = Product()
p1.set(1, "Apple", 100)
p1.objects.save(p1)

p2 = Product()
p2.set(1, "Banana", 200)
p2.objects.save(p2)

ser = Serializer()
a = ser.serialize(Product.objects.all()) #將檔案改成jason格式
b = Jason()                              #存成Jason檔
b.saveJason(a)

