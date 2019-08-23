'''phone no. validation'''

import re
#phno="(800) 555.1212 #1234"
name=input("Enter name: ")
phno=input("Enter phno: ")

r1=re.match("\(\d{3}\)\s\d{3}\.\d{4}\s\#\d{4}$",phno)
while r1==None:
    print("Invalid phone no!")
    phno=input("Enter phno again: ")
    r1=re.match("\(\d{3}\)\s\d{3}\.\d{4}\s\#\d{4}$",phno)

print(r1)
print(r1.group())
print("validation successful!")
