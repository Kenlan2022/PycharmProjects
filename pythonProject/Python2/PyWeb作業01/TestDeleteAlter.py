from Python2.PyWeb作業01.models import Product

p1 = Product()
p1.set(1, "Apple", 100)
Product.objects.save(p1)

p2 = Product()
p2.set(2, "Banana", 200)
Product.objects.save(p2)


print("---所有資料----")

print(Product.objects.all())
for p in Product.objects.all():
    print(p)


print("---查詢第1項----")
print(Product.objects.filter(id=1))

print("---刪除1----")
print(Product.objects.delete(id=1))

print("---查詢第1項----")
print(Product.objects.filter(id=1))

print("---查詢第2項----")
print(Product.objects.filter(id=2))