'''Write a python class to represent city which contains a list of places to see.
Provide methods
to create the object with just the city name or with city name and places
(stored as list)
Provide methods to add a place of visit, to remove place of visit,
to display all places of visit.'''

class city:
    def __init__(self,cn,pl=[]):
        self.cname=cn
        self.places=pl
    def add_place(self,np):
        self.places.append(np)
    def del_place(self,p):
        if p in self.places:
            self.places.remove(p)
        else:
            print('not found!')
    def disp(self):
        print('city: ',self.cname)
        print('places to see: ',self.places)

# c1= city('bang',['p1','p2','p3'])
# c1.disp()
# c1.add_place('l9')
# c1.add_place('l7')
# c1.disp()
# c1.del_place('p2')
# c1.disp()

cn=input("Enter city name: ")
pl=input("Enter few places to see").split()
print(cn,pl)
c1=city(cn,pl)

while 1:
    ch=int(input("\n1:add\n2:del\n3:disp\nEnter choice: "))
    if ch==1:
        c1.add_place(input("Enter new place: "))
    elif ch==2:
        c1.del_place(input("Enter place to delete: "))
    elif ch==3:
        c1.disp()
    else:
        exit()
