try:
    #可能發生的程式錯誤
    e = float(input('請輸入英文成績:'))
    print('輸入完成')
except ValueError:
    print('格式錯誤,請輸入0~100')
except: #壞寫法，不指名輸入錯誤類型
    print('不知名的錯誤')
finally:
    print('結束')

while True:
    try:
        m = float(input('請輸入數學成績:'))
        if m < 0 or m >100:
            print('請輸入0~100')
        else:
            break #結束迴圈
    except:
        print('格式錯誤，請輸入0~100')
print('輸入完成')

#自我挑戰:設計函數:輸入英文成績()、輸入數學成績()
def 輸入成績(科目名稱):
    #區域變數(變數在函數裡面)
    while True:
        try:
            #可能發生錯誤的程式
            s = f'請輸入{科目名稱}成績'
            x = float(input(s))
            if x < 0 or x > 100:
                print('請輸入0~100')
            else:
                break
        except ValueError: #好寫法，指名錯誤的處理類型
            print('格式錯誤，請輸入0~100')
    return x #返回結果
#主流程
#全域變數(變數在函式之外)
e = 輸入成績('英文')
print('結果', e)
m = 輸入成績('數學')
print('結果', m)