miles = float(input("How many miles have you driven this week? "))

if miles > 10 and miles <= 100:
    #miles = miles - 10
    print ("You have traveled " + str(miles) + " miles, meaning you can get " + "£" + str((10*50+(miles-10)*37)/100)+ " back on expense. ")
elif miles > 100:
    print ("You have traveled " + str(miles) + " miles, meaning you can get £38.30 back on expense. ")
    print ( "As we only pay you up to £100,as a maximum return on travel expense")
elif miles <= 10:
    print ("You have traveled " + str(miles) + " miles, meaning you can get " + "£" + str(miles*50/100) + " back on expense. ")
