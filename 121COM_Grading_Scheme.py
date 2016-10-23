# The 121COM grading scheme is as follows:
# Total grade is 30% from exam and 70% from coursework.
# Must have >40% overall and >35% in each component to pass

# The rough degree boundaries are:
# 3rd = 40-49%
# 2:1 = 50-59%
# 2:2 = 60-69%
# 1st = 70% and above

# The following script takes a users grades and lets them know what degree level that is equivalent to. 

# Runtime error '==' needed to be changed to '=' so as to do what they wanted
cwMark = int( input("What is the coursework mark? "))

# Runtime error '==' needed to be changed to '=' so as to do what they wanted
exMark = int( input("What is the exam mark? "))

if cwMark<35 or exMark<35:
    grade="FAIL"
    print("Component failed - no grade")
else:
    totMark = (30*exMark + 70*cwMark)/100
    if totMark<40:
        grade="FAIL"
        print("Very bad")    
    elif totMark<50:
        grade="3rd"
# Syntax error indent needed to be removed 
        print("Below Average")
    elif totMark<60:
        grade="2:2"
        print("Average")
    elif totMark<70:
        grade="2:2"
# Syntax error indent needed to be removed
        print("Good")
# Logic error need to change '>' to ">=" so that any one with a 70 mark will get a grade 
    elif totMark >= 70 and totMark != 100:
        grade="1st"
        print("Great!")
# Syntax error '=' needed to be changed to '==' so as represent what they wanted
    if totMark == 100:
        grade = "1st"
        print("In fact its perfect!")
        print("On track for a: " + str(grade))
