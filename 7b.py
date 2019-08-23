'''Subset sum'''

def subsetSum(l,t):
    for i in range(0,len(l)):
        for j in range(i+1,len(l)):
            for k in range(j+1,len(l)):
                if l[i]+l[j]+l[k] == t:
                    print(l[i],l[j],l[k])
                    return True
    return False

# l=[5, 4, 10, 20, 15, 19]
# print(subsetSum(l,38))
# print(subsetSum(l,10))

l=[int(x) for x in input('Enter list of nos: ').split()]
t=int(input('Enter target: '))
print(subsetSum(l,t))
