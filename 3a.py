'''inheritance'''

class vehicle:
    def __init__(self):
        self.level=1
        print('\ni am a vehicle')
    def __str__(self):
        return "hierarchy level : "+str(self.level)

class bike(vehicle):
    def __init__(self):
        vehicle.__init__(self)
        self.level=2
        print('i am a bike')

class car(vehicle):
    def __init__(self):
        vehicle.__init__(self)
        self.level=2
        print('i am a car')

class pedal(bike):
    def __init__(self):
        bike.__init__(self)
        self.level=3
        print('i am a pedal bike')

class motor(bike):
    def __init__(self):
        bike.__init__(self)
        self.level=3
        print('i am a motor bike')

v=vehicle()
print(v)
b=bike()
print(b)
c=car()
print(c)
pb=pedal()
print(pb)
mb=motor()
print(mb)

