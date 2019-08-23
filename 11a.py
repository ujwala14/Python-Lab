'''Write a python function names() that takes no input and
repeatedly asks the user to enter the
first name of a student in a class. When the user enters the empty string,
the function should
print for every name the number of students with that name.'''

def names():
    namelist=[]
    while 1:
        n=input("Enter next name: ")
        if n=='':
            break
        namelist.append(n)
    uniq_names=set(namelist)
    for n in uniq_names:
        print("there is/are {0} student/s named {1}".format(namelist.count(n),n))

names()
