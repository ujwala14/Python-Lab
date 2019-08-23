def add(s,e):
    s.append(e)
def delete(s):
    if len(s)==0:
        return -1
    return s.pop(0)
def disp(s):
    print("The queue: ")
    for i in range(0,len(s)):
        print(s[i],end=' ')
    print()
