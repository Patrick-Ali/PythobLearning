# Speend100.py - Version 1 - Patrick Ali - 11/10/15

# Amount the person has available to spend
spend = 100

# Beginning of loop that will only end when you run out of money  
while spend > 0:

    # How much the person has spent
    spent = int(input("How much have you spent £" ))

    # Calculate how much they have left
    spend = spend - spent

    # Tell them how much they have left to spend
    print ("Your budget is now £" + str(spend))

    # Once their budget has reached this point this will activate 
    if spend <= 0:

        # This is if the person has spent exactly their budget  
        if spend == 0:
            # This tells them they are out of money
           print ("You are out of money")
        else:
            # This tells them they are out of money and how much they are in debt due to over spending 
            print ("You are out of money and are in debt by £" + str((spend - spend) - spend))

        # This ends the loop 
        break
        
