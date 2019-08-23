'''re - correction'''
import re

def correct(string):
    string=re.sub("\s\s+"," ",string)
    string=re.sub("\.",". ",string)
    string=re.sub("\s\s+"," ",string)

    return string

print(correct("This is .very funny and  cool.  Indeed!"))

string=input("Enter string: ")
string=correct(string)
print("Corrected string: ")
print(string)
