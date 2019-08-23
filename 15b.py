'''sublist'''

def sublist(list1,list2):
    i=0
    for j in list2:
        if list1[i]==j:
            i+=1
        if i==len(list1):
            return True
    return False

print(sublist([15, 1, 100], [20, 15, 30, 50, 1, 100]))
print(sublist([15, 50, 20], [20, 15, 30, 50, 1, 100]))

l1=[int(x) for x in input("Enter list1: ").split()]
l2=[int(x) for x in input("Enter list2: ").split()]
print("l1 sublist of l2? ",sublist(l1,l2))
