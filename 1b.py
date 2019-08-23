from tkinter import *

def onClickUp():
    print('up!!')
    val.set(val.get()+1)

def onClickDown():
    print('Down!!')
    val.set(val.get()-1)

root=Tk()
root.title('up down')
root.geometry('300x300')
val=IntVar()
val.set(0)

up=Button(root,text='Up',command=onClickUp)
up.pack()

down=Button(root,text='Down',command=onClickDown)
down.pack()

vlabel=Label(root,textvariable=val)
vlabel.pack()

root.mainloop()
