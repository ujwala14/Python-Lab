import math

def circle(r):
    return 3.14*r*r

def rect(l,b):
    return l*b

def stri(a,b,c):
    s=(a+b+c)/2
    ar=s*(s-a)*(s-b)*(s-c)
    ar=math.sqrt(ar)
    return ar
