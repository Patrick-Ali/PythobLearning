# Tea_Heat.py - Version 1 - Patrick Ali - 11/10/15

# This is how hot the tea is at the beginning 
heat = 100

# This ocunts the number of blows it takes for the tea to cool down
count = 0

# This begins the loop that will determine how many blows it takes for the tea to cool
while heat >= 70:

    # This performs the calculation on each blow
    heat = heat - (heat*10/100)
    # This tells the user how hot the tea is now
    print ("The current heat of the tea is %" + str(heat))
    # This adds one to count for every blow taken so as to get the final count
    # on the number of blows it takes 
    count = count + 1
    print ("This is blow number: " + str(count))
    if heat == 70:
        break
    
