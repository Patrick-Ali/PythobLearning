# This allows the user to input their sentence 
sentence = input("input your sentence here: ")

# This breaks up the sentence into indavidual words
sentence2 = sentence.split(" ")

# This prints their sentence as broken into indavidual words
print (sentence2)

# Thia prints their sentence into serperate words and counts them
for x in sorted(sentence2):
    print (x + " " + str(sentence2.count(x)))
