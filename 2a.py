'''Write a python program to create a class called Point ,
which represents a point. Overload the + operator to add two points.
Write functions to read and display the points.'''

class Point:
    '''rep a point'''
    def __init__(self):
        self.x=0
        self.y=0
    def read(self):
        self.x=int(input("Enter x coordinate: "))
        self.y=int(input("Enter y coordinate: "))
    def disp(self):
        print("({0},{1})".format(self.x,self.y))
    def __add__(self, other):
        a=Point()
        a.x=self.x + other.x
        a.y=self.y + other.y
        return a

p1=Point()
p2=Point()

print('For point 1')
p1.read()
print('For point 2')
p2.read()

print('point 1: ',end='\t')
p1.disp()
print('point 2: ',end='\t')
p2.disp()

p3=p1+p2
print('Addition of 2 points: ',end='\t')
p3.disp()
