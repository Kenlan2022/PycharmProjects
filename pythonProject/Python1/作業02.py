#使用input() 輸入 客戶名稱 與 6個樂透號碼
    #客戶名稱客戶名稱長度至少2個字
    #樂透號碼不能重複
print("------使用input()輸入客戶名稱與6個樂透號碼------")
import random
import os

def Client():
    while True:
        name = input("請輸入名字:")
        a = list(name)
        if name != "" and len(a) >= 2:
            # print('--')
            return name
        else:
            print("格式不正確")
            continue

def Lottery():
    lotto = set() #set 建立空set
    while len(lotto)<6:
        n = random.randint(1,42)
        lotto.add(n) # add() set新增資料
    return lotto


def main1():
    name = Client()
    NameList = set()
    NameList.add(name)
    LotteryList = {name:Lottery()}
    print (LotteryList)
    return LotteryList
main1()

#儲存文字檔
    #客戶名稱
    #6個樂透號碼
print("------儲存文字檔------")
def main2():
    with open("儲存文字檔.txt", "w") as f:
        a = str(main1())
        f.write(a)

main2()
#進階挑戰1
    #連續輸入3筆資料(客戶名稱、樂透號碼)
    #客戶名稱不能重複
    #採用 附加模式 寫入3筆資料，文字檔最終會有4筆資料(包含前一次寫入資料)
print("------進階挑戰1------")

def main3():
    TempList = list()
    while len(TempList) < 3: #如果暫存清單比3小
        Lotto1 = Lottery()
        Lotto2 = Lottery()
        Lotto3 = Lottery()
        LottoDic = {frozenset(Lotto1), frozenset(Lotto2), frozenset(Lotto3)}


        Temp = Client()
        if Temp not in TempList:
            TempList.append(Temp)
            continue
        else:
            print("名稱重複")
            TempList.remove(Temp)
            continue

    ClientLottery = {
        TempList[0] : Lotto1,
        TempList[1] : Lotto2,
        TempList[2] : Lotto3,
    }
    print(ClientLottery)

    with open("儲存文字檔.txt", "a") as f:
        a = str(ClientLottery)
        f.write(a)

    print("------進階挑戰2------")

#進階挑戰2
    #修改客戶資料
        #選項1:修改名字
        #選項2:修改樂透號碼(重新產生一組號碼)
    #修改資料後，儲存文字檔



    while True:
        Value1 = input("選項1: 修改名字" "\n" "選項2: 修改樂透號碼""\n")
        if Value1 == "1":
            print("請輸入舊名字")
            name = Client()
            print("請輸入新名字")
            newname = Client()
            a = list()
            with open("儲存文字檔.txt", "r+") as f:
                for row in f:
                    row = row.replace(str(name),str(newname))
                    a.append(row)
                    f.write(str(a))
                # print("------------------------")
                # print(a)

        elif Value1 == "2":
            name = Client()
            # print('++++++++++++')
            if name in ClientLottery:
                # print('2222')
                newLottery = Lottery()
                ClientLottery[name] = newLottery
                with open("儲存文字檔.txt", "w") as f:
                    a = str(ClientLottery)
                    f.write(a)
            else:
                # print('-----------------')
                continue

        else:
            print("格式不正確")
            continue

main3()