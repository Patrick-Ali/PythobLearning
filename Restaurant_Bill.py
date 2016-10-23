# Version 1 Restaurant Bill Patrick Ali 06/10/15

# Get the cost of the user
Cost = int(input("How much did it cost? £"))

# Find out if the customer is a student 
Student = input("Is the customer a student? Enter Yes or No: ")

# If the customer is a student then this will activate 
if Student == "Yes" or Student == "yes":
    
# Remove student discount from cost
    Discount_Student = Cost*20/100
    Cost = Cost - Discount_Student 

# Find out if the customer is involved in 121 com
    comp_121 = input("Is the student involved in 121 com? Enter Yes or No: ")

# If they are part of 121 comp then this activates
    if comp_121 == "Yes" or comp_121 == "yes":

# Remove 121 comp discount from cost 
        Discount_121 = Cost*5/100
        Cost = Cost - Discount_121
        print ("Your total bill is £" + str(Cost))

# If they are not part of 121 comp then print the bill with student discount 
    else:
        print ("Your total bill is £" + str(Cost))

# If they are not a student this activates 
elif Student == "No" or Student == "no":

# Find out if the customer is a member of staff
    Staff = input("Is the customer a member of staff? Enter Yes or No: ")

# If they are a member of staff then this part activates 
    if Staff == "Yes" or Staff == "yes":

# Remove staff discount from cost
        Discount_Staff = Cost*10/100
        Cost = Cost - Discount_Staff
        
# Find out if the customer is involved in 121 com
        comp_121 = input("Is the staff member involved in 121 com? Enter Yes or No: ")

# If they are part of 121 comp then this activates
        if comp_121 == "Yes" or comp_121 == "yes":

# Remove 121 comp discount from cost 
            Discount_121 = Cost*5/100
            Cost = Cost - Discount_121
            print ("Your total bill is £" + str(Cost))
            
# If they are not part of 121 comp then print the bill with staff discount 
        else:
            print ("Your total bill is £" + str(Cost))

# If they are not a member of staff this activates 
    elif Staff == "No" or Staff == "no":

# Find out if the customer is involved in 121 com
        comp_121 = input("Is the customer involved in 121 com? Enter Yes or No: ")

# If they are part of 121 comp then this activates
        if comp_121 == "Yes" or comp_121 == "yes":
            
# Remove 121 comp discount from cost     
            Discount_121 = Cost*5/100
            Cost = Cost - Discount_121
            print ("Your total bill is £" + str(Cost))
    
# If the customer is not involved in 121 com then this activates 
        else:
            print ("Your total bill is £" + str(Cost))
            
# For anyother answer this happens
    else:
        print ("Your total bill is £" + str(Cost))

# For anyother answer this happens
else:
    print ("Your total bill is £" + str(Cost))    
    
