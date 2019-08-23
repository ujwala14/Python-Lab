'''geometric sequence'''

def geometric(l):
    r=l[1]/l[0]
    for i in range(2,len(l)):
        r1=l[i]/l[i-1]
        if r1!=r:
            return False
    return True

#print(geometric([2, 4, 8, 16, 32, 64, 128, 256]))
#print(geometric([2, 4, 6, 8]))

a=[int(x) for x in input("Enter list of nos: ").split()]
print('The list: ',a)
print('Geometric seq? ',geometric(a))
