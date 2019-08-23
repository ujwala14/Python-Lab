'''rotate list k rotations'''

def rotatelist(ls,k):
    if k<=0:
        return ls
    slice=-1*(k % len(ls))
    rl=ls[slice:]+ls[:slice]
    return rl

print(rotatelist([1,2,3,4,5],1)) #output is [5, 1, 2, 3, 4])
print(rotatelist([1,2,3,4,5],3)) #output is [3, 4, 5, 1, 2]
print(rotatelist([1,2,3,4,5],12)) #output is [4, 5, 1, 2, 3]

lst=[int(x) for x in input("Enter list").split()]
k=int(input("Enter no. of rotations: "))
rlst=rotatelist(lst,k)

print("before: ",lst)
print("after: ",rlst)
