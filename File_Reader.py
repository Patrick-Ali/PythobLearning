def Backwards():
    f = open("Boring.txt", "r")

    f = list(f)

    print (f[::-1])

    f.close()

def FiveLines():
    f = open("Boring.txt", "r")
    
    f = list(f)

    C = "C"

    B = 0

    E = 4

    while C == "C":
       C =input("Do you want to continue? ")
       if C == "C":
           print(f[B:E])
           B = B + 5
           E = E + 5
           if B > 33:
               break
       else:
           break


print(FiveLines())
