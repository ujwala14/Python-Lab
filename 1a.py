'''Write a python program to create a file and write contents into the file.
 Open the file created and count the number of words in the file.'''

f=open('file1.txt','w')
data=input("enter data to write to file: ")
f.write(data)
f.close()

f=open('file1.txt','r')
words=f.read().split(' ')
print(words)
print('No. of words: ',len(words))
