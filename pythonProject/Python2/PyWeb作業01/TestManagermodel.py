from Python2.PyWeb作業01.models import Product

p1 = Product()
p1.set(1,"mango", 100)
Product.objects.save(p1)

p2 = Product()
p2.set(2,"Apple", 200)
Product.objects.save(p2)

print("---查詢 all---")
for p in Product.objects.all():
    print(p)


print("---查詢 id = 1---")
print(Product.objects.filter(id=1))