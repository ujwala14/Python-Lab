'''gui_buttons_nice_job'''

from tkinter import *

def onfirst():
    print('1st')
    b2=Button(root,text='Second',command=onsecond)
    b2.pack()
def onsecond():
    print("2nd")
    l=Label(root,text='Nice job!!')
    l.pack()

root=Tk()
root.title("nice job")
root.geometry("300x300")

b1=Button(root,text='First',command=onfirst)
b1.pack()

root.mainloop()
