from tkinter import *
# 从 tkinter文件 导入所有
root = Tk() #TK()创建父容器(根容器)。
root.geometry('800x600')#x是字母不是乘号
# 创建容器frame,frame基本参数
# width  :  frame组件的宽度
# height :  frame组件的高度
# padx   :  frame的X方向的内边距
# pady   :  frame的Y方向的内边距
top_Frame = Frame(root
                  , width=750
                  , height=80
                  , highlightbackground="black"
                  , highlightthickness=1
                  , bd=3)
left_Frame = Frame(root
                   , width=200
                   , height=400
                   , highlightbackground="black"
                   , highlightthickness=1
                   , bd=3)
main_Frame = Frame(root
                   , width=335
                   , height=400
                   , highlightbackground="black"
                   , highlightthickness=1
                   , bd=3)
right_Frame = Frame(root
                    , width=200
                    , height=400
                    , highlightbackground="black"
                    , highlightthickness=1
                    , bd=3)
bottom_Frame = Frame(root
                     , width=750
                     , height=80
                     , highlightbackground="black"
                     , highlightthickness=1
                     , bd=3)
top_Frame.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
left_Frame.grid(row=1, column=0, padx=5, pady=5)
main_Frame.grid(row=1, column=1, padx=5, pady=5)
right_Frame.grid(row=1, column=2, padx=5, pady=5)
bottom_Frame.grid(row=2, column=0, columnspan=3, padx=5, pady=5)
root.mainloop()
