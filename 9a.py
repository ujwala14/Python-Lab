'''time'''

class time:
    def __init__(self):
        self.hr=int(input("Enter hr: "))
        self.min=int(input("Enter min: "))
        self.sec=int(input("Enter sec: "))
    def calc_sec(self):
        tsec=self.hr*3600 + self.min*60 + self.sec
        print('Total sec: ',tsec,' s')

t=time()
t.calc_sec()
