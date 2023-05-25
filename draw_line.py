import tkinter as tk
def moveimg(event):
    # root.after(1)
    
    # b1=tk.Canvas(root,width=root.winfo_width(),height=root.winfo_height())
    b1.delete("all")
    x, y = event.x, event.y
    b1.create_line(x,0,x,root.winfo_height(),width=2)
    
    b1.create_line(0,y,root.winfo_width(),y,width=2)
    b1.pack()
    # b2.pack()
root=tk.Tk()
# root.geometry('320x240')
# root.geometry('640x480')
b1=tk.Canvas(root,width=640,height=480)
root.geometry('640x480')
root.resizable(width=False, height=False)

# b2=tk.Canvas(root)
root.bind("<Motion>", moveimg)
root.mainloop()