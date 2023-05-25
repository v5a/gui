from tkinter import *

root = Tk()

def callback(event):#event形参来获取对应事件描述
    print(event.keysym)#keysym显示特殊按键
    


frame = Frame(root, width =200, height= 200)
frame.bind("<Key>",callback)
frame.focus_set()



frame.pack()
#<Button-1>Button：表示鼠标的点击事件 “—”左边是事件本身，右边是事件描述
#1：表示左键 2：中间键的滚轮点击 3：右键




mainloop()