#通常字串中的\是跳脫字元，用來搭配另一個字元，\n
#r字串(字串裡的字，寫什麼就是甚麼，不用多錯解釋，例如\)

print("Tomy\nAmy")
#Tom
#Amy

print("Tom\\nAmy")
#Tom\nAmy

print(r"Tom\nAmy")
#Tom \n Amy
#去掉\n的意義