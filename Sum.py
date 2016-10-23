#Showing Try except works

def add(a,b):
    try:
        c = a + b
        c = int(c)
        return c
    except TypeError:
        return None

a = input('Enter a number: ')
b = input('Enter a number: ')

a = float(a)

print(add(a,b))
