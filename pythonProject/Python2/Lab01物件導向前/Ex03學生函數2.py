def 初值(st): #區域變數 st
    name = None
    eng = None
    math = None

    st.append(name) #append 是list 函數
    st.apped(eng)
    st.append(math)

def 修改值(st, name=None, eng=None, math=None):
    st[0] = name
    st[1] = eng
    st[2] = math

def 總分(st):
    name = st[0]
    eng = st[1]
    math = st[2]
    #簡化寫法
    #name, eng, math =st
    tot = None
    if eng is not None and math is not None:
        tot = eng + math
    return tot

def 顯示(st):
    name = st[0]
    eng = st[1]
    math =st[2]
    tot = 總分(st)
    print(name, eng ,math, tot)

#主流程
st1 = list() #全域變數 st
初值(st1) #將全域變數st 傳送到變數st(複製)
顯示(st1)
修改值(st1, "Tom", 100, 99)
顯示(st1)
print("-------------")
st2 = list() #全域變數st
初值(st2)
顯示(st2)
修改值(st2, math=80, eng=85, name="Amy")
顯示(st2)
