word = input("Please enter a word: ")
vowel = 0
for j in word:
    if j in "aAeEiIoOuU":
        vowel = vowel + 1
print (word + " has " + str(vowel) + " vowels. ")

#TESTING RANGE

#for x in range(10):
    #print (x**2)
#for x in range (-10,11):
    #print (x**2)
