# Version 1 Patrick Ali 06/10/15

# Get the Language of the user 
Language = input("What language do you speak? ")

# Determine if it is English, with or without a capital 
if Language == "English" or Language == "english":
# Say hello and welcome them to Coventry
    print ("Hello")
    print ("Welcome to Coventry.")

# Determine if it is French, with or without a capital
elif Language == "French" or Language == "french":
# Say hello and welcome them to Coventry
    print ("Bonjour")
    print ("Bienvenue à Coventry")

# Determine if it is Mandarin, with or without a capital
elif Language == "Mandarin" or Language == "mandarin":
# Say hello and welcome them to Coventry
    print ("您好")
    print ("欢迎来到考文垂")

# If it is none of the above we apologise and tell them we don't know that
# Language 
else:
    print ("Sorry but I don't speak " + str(Language) + ".")
