meterInches = 0.3/12
meterFoot = 0.3

footString = input("enter feet: ")
footInt = int(footString)

inchString = input("enter inches: ")
inchInt = int(inchString)

footHeightMeters = meterFoot*footInt
inchHeightMeters = meterInches*inchInt

heightMeters = round(footHeightMeters + inchHeightMeters, 2)

print("You are about: " + str(heightMeters) + " meters tall.")
