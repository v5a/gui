import ctypes
import tkinter as tk
u32=ctypes.windll.user32


def go():
    b_back=u32.GetParent(b.winfo_id())
    a_back=u32.GetParent(a.winfo_id())
    u32.SetParent(b_back,a.winfo_id())

a=tk.Tk()
a.geometry('500x500')
a.title('嵌套子窗口测试')

b=tk.Toplevel()
b.title('子窗口')

a.after(100,go)
a.mainloop()

