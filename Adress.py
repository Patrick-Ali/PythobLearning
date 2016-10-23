def Address (Street, City, County, PostCode):
    """
    This function will take the address form the user then return it in a more correct format
    """
    Return_Adress = str(str(Street+ ",").center(150) + "\n" + str(City + ",").center(150) + "\n" + str(County + ",").center(150) + "\n" + str(PostCode).center(150))
    return Return_Adress

 
print (Address(input("Enter House/Flat number and street: "), input("Enter City: "), input("Enter County: "), input("Enter Post Code: ")))
