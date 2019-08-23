'''Define a python function generate_n_chars()
that takes an integer n and a character c and returns a string,
 n characters long. For example, generate_n_chars(5,"x") should
  return the string "xxxxx“ using keyword only parameters.'''

def generate_n_chars(n,c):
    return c*n

c=input('Enter char: ')
n=int(input('Enter no: '))
print(generate_n_chars(c=c,n=n))
