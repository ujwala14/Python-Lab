'''wellbracketed(s)'''

def wellbracketed(s):
    stack=[]
    for i in s:
        if i=='(':
            stack.append(i)
        elif i==')' :
            if len(stack)!=0:
                stack.pop()
            else:
                return False
    if stack==[]:
        return True
    return False

print(wellbracketed("22)"))
print(wellbracketed("(a+b)(a-b)"))
print(wellbracketed("(a(b+c)-d)((e+f)"))

print(wellbracketed(input("Enter string: ")))


