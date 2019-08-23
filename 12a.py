'''Write a python function partition() that splits a list of soccer
players into two groups. More
precisely, it takes a list of first names (strings) as input and
prints the names of those soccer
players whose first name starts with a letter between and including A and M.'''

def partition(strings):
    for s in strings:
        if s[0].upper() in "ABCDEFGHIJKLM":
            print(s)

# partition(['Eleanor', 'Evelyn', 'Sammy', 'Owen', 'Gavin'])
# partition(['Xena', 'Sammy', 'Owen'])

names=input("Enter player names: ").split()
partition(names)
