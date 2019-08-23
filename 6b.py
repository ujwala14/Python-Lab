'''Write a python function exclamation() that takes input as a
string and returns it with this modification: Every vowel is replaced
by four consecutive copies of itself and an exclamation mark (!) is
added at the end.'''

def exclamation(s):
    ns=''
    for i in range(0,len(s)):
        if s[i] in 'aeiouAEIOU':
            ns+=s[i]*4
        else:
            ns+=s[i]
    ns+='!'
    return ns

print(exclamation('argh'))
print(exclamation('hello'))
str=input("Enter string: ")
print(exclamation(str))
