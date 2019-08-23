'''Write a python class called Mylist that shadows a python list:
it should overload + operator to append the data to the list.
Also provide constructor for your class that takes an existing list'''

class MyList:
    def __init__(self,list):
        self.listt=list
    def __add__(self, other):
        self.listt.append(other)
    def __str__(self):
        return str(self.listt)

a=[1,2,3]
ml=MyList(a)
print(ml)
ml+4
ml+5
print(ml)
