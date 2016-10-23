#Prints a given numbers timestable along with the 12 times table

number = -1

while number < 0 or number > 12:
    number = int(input("Please enter a number between 0 adn 12: "))

for x in range (1):
    for y in range (13):
         print (str(y*number)+ " " + str(y*12))
