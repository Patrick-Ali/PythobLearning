# Ask user their name
Grettings = input ("Whats your name? ")
# Store the users name for later use 
Name = str(Grettings)
# Greet the user by using their name stored earlier 
print ("Hello " + str(Grettings) + " it's nice to meet you.")
AgeString = input ("How old are you?")
AgeInt = int(AgeString)
DogYears = 7
AgeInDogYrs = AgeInt * DogYears
print ("Did you know you are " + str(AgeInDogYrs)+ " in dog years.")

