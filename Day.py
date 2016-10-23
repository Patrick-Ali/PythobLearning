# Testing Try Except statements and Error Riasing

def numToDay(n):
    Mtup = (" ", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
    try:
        if n > 7:
            raise ValueError("There are only 7 days!")
##        elif type(n) is not int():
##            raise TypeError("This is not a numerical value!")
        else:
            return (Mtup[n])
    except TypeError:
        raise TypeError("This is not a numerical value!")
        

print (numToDay(12))
