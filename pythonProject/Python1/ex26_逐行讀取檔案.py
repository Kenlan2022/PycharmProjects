with open("f.txt") as f:
    for 行 in f :
        #\n行是換行符號
        #行 是從檔案讀到的一行字串 字串有replace() 取代功能
        #https://w3schools.com/python/ref_string_replace.asp
        行 = 行.replace("\n","") #尋找Enter 取代成沒有字(刪除)
        print(行)