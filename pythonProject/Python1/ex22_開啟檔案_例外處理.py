try:
    with open("b.txt") as f: #with open 簡化寫法 最後自動 close()
        print("開檔成功")
    print("關檔成功")
except FileNotFoundError:
    print("b.txt找不到")

