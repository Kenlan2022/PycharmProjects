lotto =[33,10,15,21,28,30]
name = "Tom"
字串 = ""#空字串,沒有字
字串 += name
字串 += "\n"
#"a" 自動建立檔案,若檔案存在,附加資料不覆蓋
with open("f.txt", "a") as f:
    for 號碼 in lotto:
        字串 += str(號碼) #str()數字轉字串
        字串 += "\n" #字串寫入檔案最後包含 Enter(換行)
    f.write(字串)