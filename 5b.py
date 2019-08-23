from mystack import stackf
from myqueue import queuef

ch=int(input("1:Stack\t2:queue\nEnter choice:"))
if ch==1:
    s=[]
    while 1:
        ch1=int(input("1:Push\t2:Pop\t3:Disp\t4:exit\nEnter choice: "))
        if ch1==1:
            e=int(input("\nEnter element : "))
            stackf.push(s,e)
        elif ch1==2:
            e=stackf.pop(s)
            if e==-1:
                print("Stack empty!")
            else:
                print("Element popped : ",e)
        elif ch1==3:
            stackf.disp(s)
        else:
            exit()
else:
    q=[]
    while 1:
        ch1=int(input("1:add\t2:del\t3:Disp\t4:exit\nEnter choice: "))
        if ch1==1:
            e=int(input("\nEnter element : "))
            queuef.add(q,e)
        elif ch1==2:
            e=queuef.delete(q)
            if e==-1:
                print("queue empty!")
            else:
                print("Element deleted: ",e)
        elif ch1==3:
            queuef.disp(q)
        else:
            exit()
