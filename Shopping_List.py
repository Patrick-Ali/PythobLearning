# Shopping_List.py - Version 1 - Patrick Ali - 11/10/15
Shopping_List = []

# Start Loop that will go until the user chooses to end
while True:

    # Allow the user to add items to their list
    Add_Shopping = input("what would you like to add to the list? " )
    

    # This makes sure that it is not already on the list
    # If it is already on the list then it is not added to the list
    if Add_Shopping in Shopping_List:
        continue

    # If it is not already on the list then this will execute 
    else:

        # This is adds the item to the shopping list, it also lowers
        # any capitals in an attempt to remove dupllicate items
        Shopping_List.append(Add_Shopping.lower())

        # This asks the user if they want to continue adding to the list
        User_Command = input("Continue adding to list? If you do then type Yes otherwise type No: ")

        # If the user is finished then this code will be executed 
        if User_Command == "No" or User_Command == "no":

            # Once the code has been executed then the list will be printed
            # So the user can review it
            print ("Your shopping list is " + str(Shopping_List))

            # This will end the loop 
            break
