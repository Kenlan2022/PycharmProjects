fruits = ["apple", "banna", "cherry"]
if "banna" in fruits:
    print("yes")
#S 不在fruits 當中才加入，避免資料重複加入
s = "aaa"
if s not in fruits:
    fruits.append(s)
