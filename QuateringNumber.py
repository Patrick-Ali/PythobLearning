def Calculator_Quarter(z):
    """ This will half the half giving us a quarter of our original number """
    print(str(z/2))

    
def Calculator_Half(y):
    """ This will half our original number """
    Calculator_Quarter(y/2)


def Calculator(x):
    """ This will check to se if the number is divisable by 2, i.e. not zero, and if it is divisible it will
     activate the division function """
    if x == 0:
        print ("None")
    else:
        Calculator_Half(x)

# This will allow the user to enter the number they want quartering
Calculator(float(input("Enter a number: ")))


