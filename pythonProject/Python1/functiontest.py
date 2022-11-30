def leapyear(y):
    y = int(y)
    if y % 400 == 0:
        if y % 100 != 0:
            if y % 4 == 0:
                print("閏年")
            else:
                print("平年")
        else:
            print("閏年")
    else:
        print("平年")
y = input("請輸入年份:")

leapyear(y)