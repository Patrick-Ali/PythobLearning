# Get the first number of the user
a = float(input ("Please enter a value for 'a' "))
# Get the second number of the user 
b = float(input("Please enter a value for 'b': "))
#Get the third number of the user 
c = float(input ("Please enter a value for 'c': "))

# Calculate the root 
d = float((b**2)-(4*a*c))

# Tell the user how many roots there are from the numbers they gave
if d < 0:
    print ("There are no roots. ")
elif d == 0:
    print ("There is one root. ")
elif d > 0:
    print ("There are two roots. ")


