import tkinter
import time
import pyautogui
import tkinter.ttk

def btn_click():
    judgeunit()
    radio = var.get()
    inter = int(txt_2.get())
    if radio == 1:
        while True:
            pyautogui.moveRel(110,100, duration=1)
            for i in range(0, inter, 1):
                time.sleep(1)
    elif radio == 2:
        start = time.time()
        while True:
            time.sleep(1)
            pyautogui.click()
            if time.time() - start > judgeunit():
                print('!!BREAK!!')
                break


def judgeunit():
    num = int(txt_1.get())
    unit = combo.get()
    if unit == "秒":
        num = num * 1
        return num
    elif unit == "分":
        num = num*3
        return num
    elif unit == "時間":
        num = num * 3600
        return num
    elif unit == "無限":
        print("無限")
    else:
        print("エラー")


# 画面作成
tki = tkinter.Tk()
tki.geometry("400x300")
tki.title('SavageOperation')

# コンボボックス作成(winに配置, リストの値を読み取り専用に設定)
combo = tkinter.ttk.Combobox(tki, state="readonly", width=5)
# プルダウン
combo["values"] = ("秒", "分","時間","無限")
combo.pack()
combo.place(x=290, y=100)

combo2 = tkinter.ttk.Combobox(tki, state="readonly", width=5)
combo2["values"] = ("秒", "分","時間","無限")
combo2.pack()
combo2.place(x=290, y=150)

#ラジオボタン
var = tkinter.IntVar()

rdo1 = tkinter.Radiobutton(tki,  value=1,variable=var,text='マウス操作')
rdo1.place(x=70, y=40)

rdo2 = tkinter.Radiobutton(tki,  value=2,variable=var,text='クリック操作' )
rdo2.place(x=70, y=70)



# テキストボックス
txt_1 = tkinter.Entry(width=20)
txt_1.place(x=80, y=100)

txt_2 = tkinter.Entry(width=20)
txt_2.place(x=80, y=150)
# ボタン
btn = tkinter.Button(tki, text='実行', command=btn_click)
btn.place(x=140, y=190)

# 画面をそのまま表示
tki.mainloop()