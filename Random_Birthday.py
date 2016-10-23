# Get the random module
import random

# Create a list for the months
month = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Print out the results of a random selection from the list and a number between 0 and 32
print ("Your birthday is " + str(random.randint(0,32)) + " " + random.choice(month))

