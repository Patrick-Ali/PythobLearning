def Centigrade(x):
    Temperature = (x - 32) / 1.8
    return Temperature
def Fahrenheit(z):
    Temperature = 1.8 * z + 32
    return Temperature

Conversion = input("Do you want to convert from Centigrade or Fahrenheit, enter C for Centigrade or F for Fahrenheit: " )

if Conversion == "C" or Conversion == "c":
     print (str(Centigrade((int(input("Please entre temperature in Fahrenheit: "))))))
elif Conversion == "F" or Conversion == "f":
     print (str(Fahrenheit((int(input("Please entre temperature in Centigrade: "))))))

