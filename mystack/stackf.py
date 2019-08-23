def push(s,e):
    s.append(e)
def pop(s):
    if len(s)==0:
        return -1
    return s.pop(len(s)-1)
def disp(s):
    print("The stack: ")
    for i in range(len(s)-1,-1,-1):
        print(s[i])
