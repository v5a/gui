#创建一个下拉式菜单
from tkinter import *
import tkinter .messagebox
#创建主窗口
win = Tk()
win.config(bg='#87CEEB')
win.title("标题")
win.geometry('450x350+300+200')
 

#执行菜单命令，显示一个对话框
def doSomething() :
    tkinter.messagebox .askokcancel ("菜单","你正在选择快捷式菜单命令")
 
#创建-个快捷 式菜单(pop-up)
popupmenu = Menu (win, tearoff=0)
#新增快捷式菜单的项目
popupmenu.add_command (label="复制",command=doSomething)
popupmenu.add_command (label="粘贴",command=doSomething)
popupmenu.add_command (label="剪切",command=doSomething)
popupmenu.add_command (label="删除",command=doSomething)
#在单击鼠标右键的窗口(x,y)坐标处，显示此快捷式菜单
def showPopUpMenu(event) :
    popupmenu .post (event.x_root, event.y_root)
#设置单击鼠标右键后，显示此快捷式菜单
win.bind("<Button-3>", showPopUpMenu)










#创建一个执行函数，点击下拉菜单中命令时执行，其中event=0（可改用*event）让菜单快捷键生效
def menuCommand(event=0):
    tkinter .messagebox .showinfo("提示", "您正在使用下拉菜单功能")
 
#创建主目录菜单（顶级菜单）
mainmenu = Menu (win)
#在顶级菜单上新增"文件"菜单的子菜单，同时不添加分割线
filemenu = Menu (mainmenu, tearoff=False)
#新增"文件"菜单的菜单项，并使用 accelerator 设置菜单项的快捷键
filemenu.add_command (label="新建",command=menuCommand,accelerator="Ctrl+N")
filemenu.add_command (label="打开",command=menuCommand, accelerator="Ctrl+O")
filemenu.add_command (label="保存",command=menuCommand, accelerator="Ctrl+S")
# 添加一条分割线
filemenu.add_separator()
filemenu.add_command (label="退出",command=win. quit)
#在主目录菜单上新增"文件"选项，并通过menu参数与下拉菜单绑定
mainmenu.add_cascade (label="文件",menu=filemenu)
# 将主菜单设置在窗口上
win.config (menu=mainmenu)
# 绑定键盘事件，按下键盘上的相应的键时都会触发执行函数
win.bind ("<Control-n>",menuCommand)
win.bind ("<Control-N>", menuCommand)
win.bind ("<Control-o>",menuCommand)
win.bind ("<Control-O>", menuCommand)
win.bind ("<Control-s>", menuCommand)
win.bind ("<Control-S>",menuCommand)



# 创建另一个下拉菜单“编辑”
editmenu = Menu(mainmenu, tearoff=False)
mainmenu.add_cascade(label="编辑", menu=editmenu)
editmenu.add_command(label="剪切", command=menuCommand)
editmenu.add_command(label="拷贝", command=menuCommand)
editmenu.add_command(label="粘贴", command=menuCommand)






# 显示主窗口
win.mainloop()