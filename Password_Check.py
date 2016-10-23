#Password Check Version 1 Patrick Ali 29/09/15

# Allow the user to enter their password
Password_String = input ("Please enter your password.")

# Store the password they entered as a string 
Password = str(Password_String)

# Check the password they gave against the one 'stored' on the system

# If the password they entered matches the one on system
# then you allow them access
if Password == "Password":
    print ("Welcome")
# Otherwise you tell them it is incorrect and bar access 
else:
    print ("Incorect")
