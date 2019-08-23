'''graffit.txt-uppercase'''

f=open("graffit.txt",'w')
f.write("Avengerss..Assemble!")
f.write("\nI am Iron Man")
f.write("\nLove you 3000")
f.write("\nIts been a long long time...")
f.close()

f=open("graffit.txt",'r')
content=f.read()
f.close()

f=open("graffit.txt",'w')
content=content.upper()
f.write(content)
f.close()

