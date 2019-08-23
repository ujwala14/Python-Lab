'''Write a program that creates a Canvas and a Button.
When the user presses the Button, it should draw a circle on the canvas.'''

from tkinter import *

def onclick():
    print('drawing...')
    cv.create_oval(50,50,200,200,fill='purple')

def clearall():
    cv.delete('all')

root=Tk()
root.geometry('500x500')
root.title('circle')

b=Button(root,text='draw a circle',command=onclick)
b.pack()

b2=Button(root,text='clear',command=clearall)
b2.pack()

cv=Canvas(root,bg='pink')
cv.pack()

root.mainloop()
