# Leap year calculator version 1 02/10/15 - Patrick Ali

# Get the year that the user wants to check
year = int(input("Please enter a year to find out if it is a leap year: "))

# Divide by four and store the remainder
# This is so we can chek the remainder, as if it is zero then it is a leap year
# if it isn't zero then it is not a leap year
Four = year%4

# Divide by four hundered and strore the remainder
# This is so we can chek the remainder, as if it is zero then it is a leap year
# if it isn't zero then it is not a leap year
Four_Hundred = year%400  

# Start answering the question
print ("Is " + str(year) + " a leap year? ")

# If dividing it by four gives a remainder of zero then it is a laep year
if Four == 0:
    print ("Answer: Yes " )
# If dividing it by four hundred gives a remainder of zero then it is a laep year
elif Four_Hundred == 0:
    print ("Answer: Yes " )
# If dividing it by four hundreed doesn't give you a remainder of zero
# Then it isn't a laep year
elif Four_Hundred != 0:
    print ("Answer: No " )
# If dividing it by four doesn't give you a remainder of zero then it isn't a laep year
elif Four != 0:
    print ("Answer: No " )
    
