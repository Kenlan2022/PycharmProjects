print("hello, world")
A = 123.4556
B = 1233.4444
print("輸出數字到小數點第一位:%.1f" %A)
print("輸出數字到小數點第一位:%.2f" %B)

#dic01 = {math_class:1, 2, 3, 4}
#print(dic01)
#SyntaxError: ':' expected after dictionary key
print("----------------------------------------------")
#dic01 = {math_class:1, english_class:2, chinese_class:3}
#print(dic01)
#NameError: name 'math_class' is not defined
dic01 = {"math_class":1, "english_class":2, "chinese_class":3}
print(dic01["math_class"])
