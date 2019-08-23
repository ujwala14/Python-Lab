'''Write a python program to demonstrate ‘Key Error’,
‘Value Error’, ‘Index Error’'''
import random

try:
    n=random.randint(1,5)
    if n==1:
        l=[1,2,3]
        print(l[10])
    elif n==2:
        d={1:'a',2:'b',4:'d'}
        print(d[3])
    elif n==3:
        print(int('abc'))
    else:
        print('avengers..assemble')

except ValueError:
    print('value error!')
except KeyError:
    print('key not found!')
except IndexError:
    print('index of list : out of bounds!')
else:
    print('great!No errors!!')
