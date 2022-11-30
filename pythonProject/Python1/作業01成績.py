import random
score = list()#全部成績
p = list()#及格成績
np =list()#不及格成績
for i in range (10):
    score.append(random.randint(1,100))
print(score)
#產生隨機數並加入成績List
for i in range(10):
    if score[i] >= 60:
        p.append(score[i])
    else:
        np.append(score[i])
print("及格:", p)
#列印及格成績
print("不及格:",np)
#列印部及格成績