import area_module

ch=int(input('1:circle\n2:rectangle\n3:scalene triangle'
             '\nEnter choice for area: '))
if ch==1:
    r=int(input("Enter radius: "))
    print('Area: ',area_module.circle(r))
elif ch==2:
    l=int(input("Enter length: "))
    b=int(input("Enter breadth: "))
    print('Area: ',area_module.rect(l,b))
elif ch==3:
    a=int(input("Enter side1: "))
    b=int(input("Enter side2: "))
    c=int(input("Enter side3: "))
    print('Area: ',area_module.stri(a,b,c))
else:
    print('invalid choice: ')
