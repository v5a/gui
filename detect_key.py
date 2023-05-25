from tkinter import *

app = Tk()
#event形参来获取对应事件描述
def callback(event):
    print(event.char)

frame = Frame(app, width = 200, height = 200)
#调用键盘Key第一个字母大写
frame.bind("<Key>",callback)
frame.focus_set()

frame.pack()

mainloop()