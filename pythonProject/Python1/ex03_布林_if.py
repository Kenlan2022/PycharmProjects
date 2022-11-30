a = "Hello"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

eng = 100
print(eng == 100)# true
if eng == 100:
    print("棒棒棒")
if eng >= 80:
    print("棒棒")
if eng>= 60:
    print("棒")
print("---------------")
score = input("請輸入分數:")#由input函式輸入的變數值為STRING
print(score)
if int(score) == 100:
    print("棒棒棒")
elif int(score) >= 80:
    print("棒棒")
elif int(score) >= 60:
    print("棒")
elif int(score) <= 59:
    print("NEED MORE EFFORT")
print("-------------------")
score = input("請輸入分數:")#由input函式輸入的變數值為STRING
print(score)
score = int(score)
if score == 100:
    print("棒棒棒")
elif score >= 80:
    print("棒棒")
elif score >= 60:
    print("棒")
elif score <= 59:
    print("NEED MORE EFFORT")