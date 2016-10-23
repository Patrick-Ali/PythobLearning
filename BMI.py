# Get the users weight from the user 
WeightString = input ("What is your weight in kilograms?")
# Store the users weight as a decimal
WeightFloat = float(WeightString)

# Get the users height from the user 
HeightString = input ("What is your height in meters?")

# Store the users height as a decimal
HeightFloat = float(HeightString)

# Calculate the users height squared and store it as a deciaml
HeightSquared = float (HeightFloat * HeightFloat)

# Calculate the users Body Mass Index (BMI)
BMI = WeightFloat/HeightSquared

# Tell the user their current BMI based on the calculations performed above 
print ("Your current BMI is " + str(BMI))
