# Time.py - Version 4 - Patrick Ali - 12/10/15

# Records the hour the user imputs 
Hour = int(input("What is the hour? (Goes up to 23): "))

#Check that the hour they entered is acceptable
if Hour <0 or Hour >=24:
    # If not then this line is printed
    print ("This is not right, as this hour is not recognised by this program, please try again")

# Otherwise if it is an acceptable number then this code executes
elif Hour >=0 or Hour <=23:

    # This records the minute the user imputs
    Minute = int(input("what is the minutes? (Goes up to 59): "))

    # This checks to see if the user imput is acceptable
    if Minute <0 or Minute >=60:
        # If the number they inputed is not acceptable then this line will be printed 
        print ("This is not right, as the minute is not recognised by this program, please try again")
        
    # Otherwise if the number inputed is acceptable then the below code is executed 
    else:
        
# As we are outputing a rounded version of the time to the nearest minute this block of code will check the
# number they inputed for the minute and check it against the below code to get the neareast 15 minutes.
# The code uses the idea of 7 minutes to the nearest 15 minutes, such as 1-7 will be just after the hour
# while 8-14 will be about quater past. The only time this does not happen is when the number hits one of the
# 15 minute mark exactly, like when it is quaterpast, instead of the code saying it is near it will say it is exactly

# This block of code checks whether the 'minute' number input is within the 1-7 range, if it is it will
# Out put the time as just after the hour 
        if Minute >=1 and Minute <=7:
            if Hour == 0:
                Hour = "Midnight"
                print (str("It's just after " + str(Hour)))
            elif Hour == 1:
                Hour = "One"
                Time = "Morning"
                print (str("It's just after " + str(Hour) + " in the "+ Time)) 
            elif Hour == 2:
                Hour = "Two"
                Time = "Morning"
                print (str("It's just after " + str(Hour) + " in the "+ Time)) 
            elif Hour == 3:
                Hour = "Three"
                Time = "Morning"
                print (str("It's just after " + str(Hour) + " in the "+ Time))
            elif Hour == 4:
                 Hour = "Four"
                 Time = "Morning"
                 print (str("It's just after " + str(Hour) + " in the "+ Time)) 
            elif Hour == 5:
                 Hour = "Five"
                 Time = "Morning"
                 print (str("It's just after " + str(Hour) + " in the "+ Time)) 
            elif Hour == 6:
                 Hour = "Six"
                 Time = "Morning"
                 print (str("It's just after " + str(Hour) + " in the "+ Time))
            elif Hour == 7:
                 Hour = "Seven"
                 Time = "Morning"
                 print (str("It's just after " + str(Hour) + " in the "+ Time)) 
            elif Hour == 8:
                 Hour = "Eight"
                 Time = "Morning"
                 print (str("It's just after " + str(Hour) + " in the "+ Time)) 
            elif Hour == 9:
                 Hour = "Nine"
                 Time = "Morning"
                 print (str("It's just after " + str(Hour) + " in the "+ Time))
            elif Hour == 10:
                 Hour = "Ten"
                 Time = "Morning"
                 print (str("It's just after " + str(Hour) + "in the "+ Time))
            elif Hour == 11:
                 Hour = "Eleven"
                 Time = "Morning"
                 print (str("It's just after " + str(Hour) + "in the "+ Time))
            elif Hour == 12:
                 Hour = "Mid-Day"
                 print (str("It's just after " + str(Hour)))
            elif Hour == 13:
                 Hour = "One"
                 Time = "Afternoon"
                 print (str("It's just after " + str(Hour) + " in the "+ Time)) 
            elif Hour == 14:
                 Hour = "Two"
                 Time = "Afternoon"
                 print (str("It's just after " + str(Hour) + " in the "+ Time)) 
            elif Hour == 15:
                 Hour = "Three"
                 Time = "Afternoon"
                 print (str("It's just after " + str(Hour) + " in the "+ Time)) 
            elif Hour == 16:
                 Hour = "Four"
                 Time = "Afternoon"
                 print (str("It's just after " + str(Hour) + " in the "+ Time)) 
            elif Hour == 17:
                 Hour = "Five"
                 Time = "Evening"
                 print (str("It's just after " + str(Hour) + " in the "+ Time)) 
            elif Hour == 18:
                 Hour = "Six"
                 Time = "Evening"
                 print (str("It's just after " + str(Hour) + " in the "+ Time)) 
            elif Hour == 19:
                 Hour = "Seven"
                 Time = "Evening"
                 print (str("It's just after " + str(Hour) + " in the "+ Time)) 
            elif Hour == 20:
                 Hour = "Eight"
                 Time = "Evening"
                 print (str("It's just after " + str(Hour) + " in the "+ Time)) 
            elif Hour == 21:
                 Hour = "Nine"
                 Time = "Night"
                 print (str("It's just after " + str(Hour) + " at "+ Time)) 
            elif Hour == 22:
                 Hour = "Ten"
                 Time = "Night"
                 print (str("It's just after " + str(Hour) + " at "+ Time)) 
            elif Hour == 23:
                 Hour = "Eleven"
                 Time = "Night"
                 print (str("It's just after " + str(Hour) + " at "+ Time))

# This block of code checks whether the 'minute' number input is exactly on the hour (i.e. '0'), if it is it will
# out put the time as exactly the hour        
        elif Minute == 0:
            if Hour == 0:
                Hour = "Midnight"
                print (str("The time is exactly " + str(Hour)))
            elif Hour == 1:
                Hour = "One"
                Time = "Morning"
                print (str("The time is exactly " + str(Hour) + " O'clock in the "+ Time)) 
            elif Hour == 2:
                Hour = "Two"
                Time = "Morning"
                print (str("The time is exactly half past " + str(Hour) + " O'clock in the "+ Time)) 
            elif Hour == 3:
                Hour = "Three"
                Time = "Morning"
                print (str("The time is exactly " + str(Hour) + " O'clock in the "+ Time))
            elif Hour == 4:
                 Hour = "Four"
                 Time = "Morning"
                 print (str("The time is exactly " + str(Hour) + " O'clock in the "+ Time)) 
            elif Hour == 5:
                 Hour = "Five"
                 Time = "Morning"
                 print (str("The time is exactly " + str(Hour) + " O'clock in the "+ Time)) 
            elif Hour == 6:
                 Hour = "Six"
                 Time = "Morning"
                 print (str("The time is exactly " + str(Hour) + " O'clock in the "+ Time))
            elif Hour == 7:
                 Hour = "Seven"
                 Time = "Morning"
                 print (str("The time is exactly " + str(Hour) + " O'clock in the "+ Time)) 
            elif Hour == 8:
                 Hour = "Eight"
                 Time = "Morning"
                 print (str("The time is exactly " + str(Hour) + " O'clock in the "+ Time)) 
            elif Hour == 9:
                 Hour = "Nine"
                 Time = "Morning"
                 print (str("The time is exactly " + str(Hour) + " O'clock in the "+ Time))
            elif Hour == 10:
                 Hour = "Ten"
                 Time = "Morning"
                 print (str("The time is exactly " + str(Hour) + " O'clock in the "+ Time))
            elif Hour == 11:
                 Hour = "Eleven"
                 Time = "Morning"
                 print (str("The time is exactly " + str(Hour) + " O'clock in the "+ Time))
            elif Hour == 12:
                 Hour = "Mid-Day"
                 print (str("The time is exactly " + str(Hour)))
            elif Hour == 13:
                 Hour = "One"
                 Time = "Afternoon"
                 print (str("The time is exactly " + str(Hour) + " O'clock in the "+ Time)) 
            elif Hour == 14:
                 Hour = "Two"
                 Time = "Afternoon"
                 print (str("The time is exactly " + str(Hour) + " O'clock in the "+ Time)) 
            elif Hour == 15:
                 Hour = "Three"
                 Time = "Afternoon"
                 print (str("The time is exactly " + str(Hour) + " O'clock in the "+ Time)) 
            elif Hour == 16:
                 Hour = "Four"
                 Time = "Afternoon"
                 print (str("The time is exactly " + str(Hour) + " O'clock in the "+ Time)) 
            elif Hour == 17:
                 Hour = "Five"
                 Time = "Evening"
                 print (str("The time is exactly  " + str(Hour) + " O'clock in the "+ Time)) 
            elif Hour == 18:
                 Hour = "Six"
                 Time = "Evening"
                 print (str("The time is exactly " + str(Hour) + " O'clock in the "+ Time)) 
            elif Hour == 19:
                 Hour = "Seven"
                 Time = "Evening"
                 print (str("The time is exactly " + str(Hour) + " O'clock in the "+ Time)) 
            elif Hour == 20:
                 Hour = "Eight"
                 Time = "Evening"
                 print (str("The time is exactly " + str(Hour) + " O'clock in the "+ Time)) 
            elif Hour == 21:
                 Hour = "Nine"
                 Time = "Night"
                 print (str("The time is exactly " + str(Hour) + " O'clock at "+ Time)) 
            elif Hour == 22:
                 Hour = "Ten"
                 Time = "Night"
                 print (str("The time is exactly " + str(Hour) + " O'clock at "+ Time)) 
            elif Hour == 23:
                 Hour = "Eleven"
                 Time = "Night"
                 print (str("The time is exactly " + str(Hour) + " O'clock at "+ Time))

# This block of code checks whether the 'minute' number input is exactly 45, if it is it will
# out put the time as exactly quarter to the hour         
        elif Minute == 45:
            if Hour == 0:
                Hour = "One"
                Time = "Morning"
                print (str("The time is exactly quarter to " + str(Hour)+ " in the "+ Time))
            elif Hour == 1:
                Hour = "Two"
                Time = "Morning"
                print (str("The time is exactly quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 2:
                Hour = "Three"
                Time = "Morning"
                print (str("The time is exactly quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 3:
                Hour = "Three"
                Time = "Morning"
                print (str("The time is exactly quarter to " + str(Hour) + " in the "+ Time))
            elif Hour == 4:
                 Hour = "Five"
                 Time = "Morning"
                 print (str("The time is exactly quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 5:
                 Hour = "Six"
                 Time = "Morning"
                 print (str("The time is exactly quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 6:
                 Hour = "Seven"
                 Time = "Morning"
                 print (str("The time is exactly quarter to " + str(Hour) + " in the "+ Time))
            elif Hour == 7:
                 Hour = "Seven"
                 Time = "Morning"
                 print (str("The time is exactly quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 8:
                 Hour = "Nine"
                 Time = "Morning"
                 print (str("The time is exactly quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 9:
                 Hour = "Ten"
                 Time = "Morning"
                 print (str("The time is exactly quarter to " + str(Hour) + " in the "+ Time))
            elif Hour == 10:
                 Hour = "Eleven"
                 Time = "Morning"
                 print (str("The time is exactly quarter to " + str(Hour) + "in the "+ Time))
            elif Hour == 11:
                 Hour = "Twelve"
                 Time = "Afternoon"
                 print (str("The time is exactly quarter to " + str(Hour) + "in the "+ Time))
            elif Hour == 12:
                 Hour = "One"
                 Time = "Afternoon"
                 print (str("The time is exactly quarter to " + str(Hour) + "in the "+ Time))
            elif Hour == 13:
                 Hour = "Two"
                 Time = "Afternoon"
                 print (str("The time is exactly quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 14:
                 Hour = "Three"
                 Time = "Afternoon"
                 print (str("The time is exactly quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 15:
                 Hour = "Four"
                 Time = "Afternoon"
                 print (str("The time is exactly quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 16:
                 Hour = "Five"
                 Time = "Afternoon"
                 print (str("The time is exactly quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 17:
                 Hour = "Six"
                 Time = "Evening"
                 print (str("The time is exactly quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 18:
                 Hour = "Seven"
                 Time = "Evening"
                 print (str("The time is exactly quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 19:
                 Hour = "Eight"
                 Time = "Evening"
                 print (str("The time is exactly quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 20:
                 Hour = "Nine"
                 Time = "Evening"
                 print (str("The time is exactly quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 21:
                 Hour = "Ten"
                 Time = "Night"
                 print (str("The time is exactly quarter to " + str(Hour) + " at "+ Time)) 
            elif Hour == 22:
                 Hour = "Eleven"
                 Time = "Night"
                 print (str("The time is exactly quarter to " + str(Hour) + " at "+ Time)) 
            elif Hour == 23:
                 Hour = "Twelve"
                 Time = "Morning"
                 print (str("The time is exactly quarter to " + str(Hour) + " in the "+ Time))

# This block of code checks whether the 'minute' number input is exactly 30, if it is it will
# out put the time as just exactly half past the hour      
        elif Minute == 30:
            if Hour == 0:
                Hour = "Midnight"
                print (str("The time is exactly half past " + str(Hour)))
            elif Hour == 1:
                Hour = "One"
                Time = "Morning"
                print (str("The time is exactly half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 2:
                Hour = "Two"
                Time = "Morning"
                print (str("The time is exactly half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 3:
                Hour = "Three"
                Time = "Morning"
                print (str("The time is exactly half past " + str(Hour) + " in the "+ Time))
            elif Hour == 4:
                 Hour = "Four"
                 Time = "Morning"
                 print (str("The time is exactly half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 5:
                 Hour = "Five"
                 Time = "Morning"
                 print (str("The time is exactly half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 6:
                 Hour = "Six"
                 Time = "Morning"
                 print (str("The time is exactly half past " + str(Hour) + " in the "+ Time))
            elif Hour == 7:
                 Hour = "Seven"
                 Time = "Morning"
                 print (str("The time is exactly half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 8:
                 Hour = "Eight"
                 Time = "Morning"
                 print (str("The time is exactly half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 9:
                 Hour = "Nine"
                 Time = "Morning"
                 print (str("The time is exactly half past " + str(Hour) + " in the "+ Time))
            elif Hour == 10:
                 Hour = "Ten"
                 Time = "Morning"
                 print (str("The time is exactly half past " + str(Hour) + "in the "+ Time))
            elif Hour == 11:
                 Hour = "Eleven"
                 Time = "Morning"
                 print (str("The time is exactly half past " + str(Hour) + "in the "+ Time))
            elif Hour == 12:
                 Hour = "Mid-Day"
                 print (str("The time is exactly half past " + str(Hour)))
            elif Hour == 13:
                 Hour = "One"
                 Time = "Afternoon"
                 print (str("The time is exactly half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 14:
                 Hour = "Two"
                 Time = "Afternoon"
                 print (str("The time is exactly half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 15:
                 Hour = "Three"
                 Time = "Afternoon"
                 print (str("The time is exactly half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 16:
                 Hour = "Four"
                 Time = "Afternoon"
                 print (str("The time is exactly half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 17:
                 Hour = "Five"
                 Time = "Evening"
                 print (str("The time is exactly half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 18:
                 Hour = "Six"
                 Time = "Evening"
                 print (str("The time is exactly half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 19:
                 Hour = "Seven"
                 Time = "Evening"
                 print (str("The time is exactly half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 20:
                 Hour = "Eight"
                 Time = "Evening"
                 print (str("The time is exactly half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 21:
                 Hour = "Nine"
                 Time = "Night"
                 print (str("The time is exactly half past " + str(Hour) + " at "+ Time)) 
            elif Hour == 22:
                 Hour = "Ten"
                 Time = "Night"
                 print (str("The time is exactly half past " + str(Hour) + " at "+ Time)) 
            elif Hour == 23:
                 Hour = "Eleven"
                 Time = "Night"
                 print (str("The time is exactly half past " + str(Hour) + " at "+ Time))

# This block of code checks whether the 'minute' number input is exactly 15, if it is it will
# out put the time as exactly quarter past              
        elif Minute == 15:
            if Hour == 0:
                Hour = "Midnight"
                print (str("The time is exactly quarter past " + str(Hour)))
            elif Hour == 1:
                Hour = "One"
                Time = "Morning"
                print (str("The time is exactly quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 2:
                Hour = "Two"
                Time = "Morning"
                print (str("The time is exactly quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 3:
                Hour = "Three"
                Time = "Morning"
                print (str("The time is exactly quarter past " + str(Hour) + " in the "+ Time))
            elif Hour == 4:
                 Hour = "Four"
                 Time = "Morning"
                 print (str("The time is exactly quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 5:
                 Hour = "Five"
                 Time = "Morning"
                 print (str("The time is exactly quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 6:
                 Hour = "Six"
                 Time = "Morning"
                 print (str("The time is exactly quarter past " + str(Hour) + " in the "+ Time))
            elif Hour == 7:
                 Hour = "Seven"
                 Time = "Morning"
                 print (str("The time is exactly quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 8:
                 Hour = "Eight"
                 Time = "Morning"
                 print (str("The time is exactly quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 9:
                 Hour = "Nine"
                 Time = "Morning"
                 print (str("The time is exactly quarter past " + str(Hour) + " in the "+ Time))
            elif Hour == 10:
                 Hour = "Ten"
                 Time = "Morning"
                 print (str("The time is exactly quarter past " + str(Hour) + "in the "+ Time))
            elif Hour == 11:
                 Hour = "Eleven"
                 Time = "Morning"
                 print (str("The time is exactly quarter past " + str(Hour) + "in the "+ Time))
            elif Hour == 12:
                 Hour = "Mid-Day"
                 print (str("The time is exactly quarter past " + str(Hour)))
            elif Hour == 13:
                 Hour = "One"
                 Time = "Afternoon"
                 print (str("The time is exactly quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 14:
                 Hour = "Two"
                 Time = "Afternoon"
                 print (str("The time is exactly quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 15:
                 Hour = "Three"
                 Time = "Afternoon"
                 print (str("The time is exactly quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 16:
                 Hour = "Four"
                 Time = "Afternoon"
                 print (str("The time is exactly quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 17:
                 Hour = "Five"
                 Time = "Evening"
                 print (str("The time is exactly quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 18:
                 Hour = "Six"
                 Time = "Evening"
                 print (str("The time is exactly quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 19:
                 Hour = "Seven"
                 Time = "Evening"
                 print (str("The time is exactly quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 20:
                 Hour = "Eight"
                 Time = "Evening"
                 print (str("The time is exactly quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 21:
                 Hour = "Nine"
                 Time = "Night"
                 print (str("The time is exactly quarter past " + str(Hour) + " at "+ Time)) 
            elif Hour == 22:
                 Hour = "Ten"
                 Time = "Night"
                 print (str("The time is exactly quarter past " + str(Hour) + " at "+ Time)) 
            elif Hour == 23:
                 Hour = "Eleven"
                 Time = "Night"
                 print (str("The time is exactly quarter past " + str(Hour) + " at "+ Time))
            

# This block of code checks whether the 'minute' number input is within the 8-14 range, if it is it will
# out put the time as about quarter past         
        elif Minute >=8 and Minute <=14:
            if Hour == 0:
                Hour = "Midnight"
                print (str("The time is about quarter past " + str(Hour)))
            elif Hour == 1:
                Hour = "One"
                Time = "Morning"
                print (str("The time is about quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 2:
                Hour = "Two"
                Time = "Morning"
                print (str("The time is about quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 3:
                Hour = "Three"
                Time = "Morning"
                print (str("The time is about quarter past " + str(Hour) + " in the "+ Time))
            elif Hour == 4:
                 Hour = "Four"
                 Time = "Morning"
                 print (str("The time is about quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 5:
                 Hour = "Five"
                 Time = "Morning"
                 print (str("The time is about quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 6:
                 Hour = "Six"
                 Time = "Morning"
                 print (str("The time is about quarter past " + str(Hour) + " in the "+ Time))
            elif Hour == 7:
                 Hour = "Seven"
                 Time = "Morning"
                 print (str("The time is about quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 8:
                 Hour = "Eight"
                 Time = "Morning"
                 print (str("The time is about quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 9:
                 Hour = "Nine"
                 Time = "Morning"
                 print (str("The time is about quarter past " + str(Hour) + " in the "+ Time))
            elif Hour == 10:
                 Hour = "Ten"
                 Time = "Morning"
                 print (str("The time is about quarter past " + str(Hour) + "in the "+ Time))
            elif Hour == 11:
                 Hour = "Eleven"
                 Time = "Morning"
                 print (str("The time is about quarter past " + str(Hour) + "in the "+ Time))
            elif Hour == 12:
                 Hour = "Mid-Day"
                 print (str("The time is about quarter past " + str(Hour)))
            elif Hour == 13:
                 Hour = "One"
                 Time = "Afternoon"
                 print (str("The time is about quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 14:
                 Hour = "Two"
                 Time = "Afternoon"
                 print (str("The time is about quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 15:
                 Hour = "Three"
                 Time = "Afternoon"
                 print (str("The time is about quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 16:
                 Hour = "Four"
                 Time = "Afternoon"
                 print (str("The time is about quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 17:
                 Hour = "Five"
                 Time = "Evening"
                 print (str("The time is about quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 18:
                 Hour = "Six"
                 Time = "Evening"
                 print (str("The time is about quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 19:
                 Hour = "Seven"
                 Time = "Evening"
                 print (str("The time is about quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 20:
                 Hour = "Eight"
                 Time = "Evening"
                 print (str("The time is about quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 21:
                 Hour = "Nine"
                 Time = "Night"
                 print (str("The time is about quarter past " + str(Hour) + " at "+ Time)) 
            elif Hour == 22:
                 Hour = "Ten"
                 Time = "Night"
                 print (str("The time is about quarter past " + str(Hour) + " at "+ Time)) 
            elif Hour == 23:
                 Hour = "Eleven"
                 Time = "Night"
                 print (str("The time is about quarter past " + str(Hour) + " at "+ Time))

# This block of code checks whether the 'minute' number input is within the 16-22 range, if it is it will
# out put the time as just after quarter past       
        elif Minute >=16 and Minute <=22:
            if Hour == 0:
                Hour = "Midnight"
                print (str("It's just after quarter past " + str(Hour)))
            elif Hour == 1:
                Hour = "One"
                Time = "Morning"
                print (str("It's just after quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 2:
                Hour = "Two"
                Time = "Morning"
                print (str("It's just after quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 3:
                Hour = "Three"
                Time = "Morning"
                print (str("It's just after quarter past " + str(Hour) + " in the "+ Time))
            elif Hour == 4:
                 Hour = "Four"
                 Time = "Morning"
                 print (str("It's just after quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 5:
                 Hour = "Five"
                 Time = "Morning"
                 print (str("It's just after quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 6:
                 Hour = "Six"
                 Time = "Morning"
                 print (str("It's just after quarter past " + str(Hour) + " in the "+ Time))
            elif Hour == 7:
                 Hour = "Seven"
                 Time = "Morning"
                 print (str("It's just after quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 8:
                 Hour = "Eight"
                 Time = "Morning"
                 print (str("It's just after quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 9:
                 Hour = "Nine"
                 Time = "Morning"
                 print (str("It's just after quarter past " + str(Hour) + " in the "+ Time))
            elif Hour == 10:
                 Hour = "Ten"
                 Time = "Morning"
                 print (str("It's just after quarter past " + str(Hour) + "in the "+ Time))
            elif Hour == 11:
                 Hour = "Eleven"
                 Time = "Morning"
                 print (str("It's just after quarter past " + str(Hour) + "in the "+ Time))
            elif Hour == 12:
                 Hour = "Mid-Day"
                 print (str("It's just after quarter past " + str(Hour)))
            elif Hour == 13:
                 Hour = "One"
                 Time = "Afternoon"
                 print (str("It's just after quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 14:
                 Hour = "Two"
                 Time = "Afternoon"
                 print (str("It's just after quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 15:
                 Hour = "Three"
                 Time = "Afternoon"
                 print (str("It's just after quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 16:
                 Hour = "Four"
                 Time = "Afternoon"
                 print (str("It's just after quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 17:
                 Hour = "Five"
                 Time = "Evening"
                 print (str("It's just after quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 18:
                 Hour = "Six"
                 Time = "Evening"
                 print (str("It's just after quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 19:
                 Hour = "Seven"
                 Time = "Evening"
                 print (str("It's just after quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 20:
                 Hour = "Eight"
                 Time = "Evening"
                 print (str("It's just after quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 21:
                 Hour = "Nine"
                 Time = "Night"
                 print (str("It's just after quarter past " + str(Hour) + " at "+ Time)) 
            elif Hour == 22:
                 Hour = "Ten"
                 Time = "Night"
                 print (str("It's just after quarter past " + str(Hour) + " at "+ Time)) 
            elif Hour == 23:
                 Hour = "Eleven"
                 Time = "Night"
                 print (str("It's just after quarter past " + str(Hour) + " at "+ Time))

# This block of code checks whether the 'minute' number input is within the 23-29 range, if it is it will
# out put the time as about half past       
        elif Minute >=23 and Minute <=29:
            if Hour == 0:
                Hour = "Midnight"
                print (str("The time is about half past " + str(Hour)))
            elif Hour == 1:
                Hour = "One"
                Time = "Morning"
                print (str("The time is about half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 2:
                Hour = "Two"
                Time = "Morning"
                print (str("The time is about half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 3:
                Hour = "Three"
                Time = "Morning"
                print (str("The time is about half past " + str(Hour) + " in the "+ Time))
            elif Hour == 4:
                 Hour = "Four"
                 Time = "Morning"
                 print (str("The time is about half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 5:
                 Hour = "Five"
                 Time = "Morning"
                 print (str("The time is about half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 6:
                 Hour = "Six"
                 Time = "Morning"
                 print (str("The time is about half past " + str(Hour) + " in the "+ Time))
            elif Hour == 7:
                 Hour = "Seven"
                 Time = "Morning"
                 print (str("The time is about half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 8:
                 Hour = "Eight"
                 Time = "Morning"
                 print (str("The time is about half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 9:
                 Hour = "Nine"
                 Time = "Morning"
                 print (str("The time is about half past " + str(Hour) + " in the "+ Time))
            elif Hour == 10:
                 Hour = "Ten"
                 Time = "Morning"
                 print (str("The time is about half past " + str(Hour) + "in the "+ Time))
            elif Hour == 11:
                 Hour = "Eleven"
                 Time = "Morning"
                 print (str("The time is about half past " + str(Hour) + "in the "+ Time))
            elif Hour == 12:
                 Hour = "Mid-Day"
                 print (str("The time is about half past " + str(Hour)))
            elif Hour == 13:
                 Hour = "One"
                 Time = "Afternoon"
                 print (str("The time is about half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 14:
                 Hour = "Two"
                 Time = "Afternoon"
                 print (str("The time is about half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 15:
                 Hour = "Three"
                 Time = "Afternoon"
                 print (str("The time is about half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 16:
                 Hour = "Four"
                 Time = "Afternoon"
                 print (str("The time is about half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 17:
                 Hour = "Five"
                 Time = "Evening"
                 print (str("The time is about half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 18:
                 Hour = "Six"
                 Time = "Evening"
                 print (str("The time is about half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 19:
                 Hour = "Seven"
                 Time = "Evening"
                 print (str("The time is about half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 20:
                 Hour = "Eight"
                 Time = "Evening"
                 print (str("The time is about half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 21:
                 Hour = "Nine"
                 Time = "Night"
                 print (str("The time is about half past " + str(Hour) + " at "+ Time)) 
            elif Hour == 22:
                 Hour = "Ten"
                 Time = "Night"
                 print (str("The time is about half past " + str(Hour) + " at "+ Time)) 
            elif Hour == 23:
                 Hour = "Eleven"
                 Time = "Night"
                 print (str("The time is about half past " + str(Hour) + " at "+ Time))

# This block of code checks whether the 'minute' number input is within the 31-37 range, if it is it will
# out put the time as just after half past       
        elif Minute >=31 and Minute <=37: 
            if Hour == 0:
                Hour = "Midnight"
                print (str("It's just after half past " + str(Hour)))
            elif Hour == 1:
                Hour = "One"
                Time = "Morning"
                print (str("It's just after half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 2:
                Hour = "Two"
                Time = "Morning"
                print (str("It's just after half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 3:
                Hour = "Three"
                Time = "Morning"
                print (str("It's just after half past " + str(Hour) + " in the "+ Time))
            elif Hour == 4:
                 Hour = "Four"
                 Time = "Morning"
                 print (str("It's just after half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 5:
                 Hour = "Five"
                 Time = "Morning"
                 print (str("It's just after half past  " + str(Hour) + " in the "+ Time)) 
            elif Hour == 6:
                 Hour = "Six"
                 Time = "Morning"
                 print (str("It's just after half past " + str(Hour) + " in the "+ Time))
            elif Hour == 7:
                 Hour = "Seven"
                 Time = "Morning"
                 print (str("It's just after half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 8:
                 Hour = "Eight"
                 Time = "Morning"
                 print (str("It's just after half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 9:
                 Hour = "Nine"
                 Time = "Morning"
                 print (str("It's just after half past " + str(Hour) + " in the "+ Time))
            elif Hour == 10:
                 Hour = "Ten"
                 Time = "Morning"
                 print (str("It's just after half past " + str(Hour) + "in the "+ Time))
            elif Hour == 11:
                 Hour = "Eleven"
                 Time = "Morning"
                 print (str("It's just after half past " + str(Hour) + "in the "+ Time))
            elif Hour == 12:
                 Hour = "Mid-Day"
                 print (str("It's just after half past " + str(Hour)))
            elif Hour == 13:
                 Hour = "One"
                 Time = "Afternoon"
                 print (str("It's just after half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 14:
                 Hour = "Two"
                 Time = "Afternoon"
                 print (str("It's just after half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 15:
                 Hour = "Three"
                 Time = "Afternoon"
                 print (str("It's just after half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 16:
                 Hour = "Four"
                 Time = "Afternoon"
                 print (str("It's just after half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 17:
                 Hour = "Five"
                 Time = "Evening"
                 print (str("It's just after half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 18:
                 Hour = "Six"
                 Time = "Evening"
                 print (str("It's just after half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 19:
                 Hour = "Seven"
                 Time = "Evening"
                 print (str("It's just after half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 20:
                 Hour = "Eight"
                 Time = "Evening"
                 print (str("It's just after half past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 21:
                 Hour = "Nine"
                 Time = "Night"
                 print (str("It's just after half past " + str(Hour) + " at "+ Time)) 
            elif Hour == 22:
                 Hour = "Ten"
                 Time = "Night"
                 print (str("It's just after half past " + str(Hour) + " at "+ Time)) 
            elif Hour == 23:
                 Hour = "Eleven"
                 Time = "Night"
                 print (str("It's just after half past " + str(Hour) + " at "+ Time))

# This block of code checks whether the 'minute' number input is within the 38-44 range, if it is it will
# out put the time as about quater to the next hour          
        elif Minute >=38 and Minute <=44:
            if Hour == 0:
                Hour = "One"
                Time = "Morning"
                print (str("The time is about quarter to " + str(Hour)+ " in the "+ Time))
            elif Hour == 1:
                Hour = "Two"
                Time = "Morning"
                print (str("The time is about quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 2:
                Hour = "Three"
                Time = "Morning"
                print (str("The time is about quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 3:
                Hour = "Three"
                Time = "Morning"
                print (str("The time is about quarter to " + str(Hour) + " in the "+ Time))
            elif Hour == 4:
                 Hour = "Five"
                 Time = "Morning"
                 print (str("The time is about quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 5:
                 Hour = "Six"
                 Time = "Morning"
                 print (str("The time is about quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 6:
                 Hour = "Seven"
                 Time = "Morning"
                 print (str("The time is about quarter to " + str(Hour) + " in the "+ Time))
            elif Hour == 7:
                 Hour = "Seven"
                 Time = "Morning"
                 print (str("The time is about quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 8:
                 Hour = "Nine"
                 Time = "Morning"
                 print (str("The time is about quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 9:
                 Hour = "Ten"
                 Time = "Morning"
                 print (str("The time is about quarter to " + str(Hour) + " in the "+ Time))
            elif Hour == 10:
                 Hour = "Eleven"
                 Time = "Morning"
                 print (str("The time is about quarter to " + str(Hour) + "in the "+ Time))
            elif Hour == 11:
                 Hour = "Twelve"
                 Time = "Afternoon"
                 print (str("The time is about quarter to " + str(Hour) + "in the "+ Time))
            elif Hour == 12:
                 Hour = "One"
                 Time = "Afternoon"
                 print (str("The time is about quarter to " + str(Hour) + "in the "+ Time))
            elif Hour == 13:
                 Hour = "Two"
                 Time = "Afternoon"
                 print (str("The time is about quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 14:
                 Hour = "Three"
                 Time = "Afternoon"
                 print (str("The time is about quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 15:
                 Hour = "Four"
                 Time = "Afternoon"
                 print (str("The time is about quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 16:
                 Hour = "Five"
                 Time = "Afternoon"
                 print (str("The time is about quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 17:
                 Hour = "Six"
                 Time = "Evening"
                 print (str("The time is about quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 18:
                 Hour = "Seven"
                 Time = "Evening"
                 print (str("The time is about quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 19:
                 Hour = "Eight"
                 Time = "Evening"
                 print (str("The time is about quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 20:
                 Hour = "Nine"
                 Time = "Evening"
                 print (str("The time is about quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 21:
                 Hour = "Ten"
                 Time = "Night"
                 print (str("The time is about quarter to " + str(Hour) + " at "+ Time)) 
            elif Hour == 22:
                 Hour = "Eleven"
                 Time = "Night"
                 print (str("The time is about quarter to " + str(Hour) + " at "+ Time)) 
            elif Hour == 23:
                 Hour = "Twelve"
                 Time = "Morning"
                 print (str("The time is about quarter to " + str(Hour) + " in the "+ Time))

# This block of code checks whether the 'minute' number input is within the 46-52 range, if it is it will
# out put the time as just after quater to the next hour         
        elif Minute >=46 and Minute <=52:
            if Hour == 0:
                Hour = "One"
                Time = "Night"
                print (str("It's just after quarter to " + str(Hour)+ " in the "+ Time))
            elif Hour == 1:
                Hour = "Two"
                Time = "Morning"
                print (str("It's just after quarter to" + str(Hour) + " in the "+ Time)) 
            elif Hour == 2:
                Hour = "Three"
                Time = "Morning"
                print (str("It's just after quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 3:
                Hour = "Four"
                Time = "Morning"
                print (str("It's just after quarter to " + str(Hour) + " in the "+ Time))
            elif Hour == 4:
                 Hour = "Five"
                 Time = "Morning"
                 print (str("It's just after quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 5:
                 Hour = "Six"
                 Time = "Morning"
                 print (str("It's just after quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 6:
                 Hour = "Seven"
                 Time = "Morning"
                 print (str("It's just after quarter to " + str(Hour) + " in the "+ Time))
            elif Hour == 7:
                 Hour = "Eight"
                 Time = "Morning"
                 print (str("It's just after quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 8:
                 Hour = "Nine"
                 Time = "Morning"
                 print (str("It's just after quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 9:
                 Hour = "Ten"
                 Time = "Morning"
                 print (str("It's just after quarter to " + str(Hour) + " in the "+ Time))
            elif Hour == 10:
                 Hour = "Eleven"
                 Time = "Morning"
                 print (str("It's just after quarter to " + str(Hour) + "in the "+ Time)) 
            elif Hour == 11:
                 Hour = "Eleven"
                 Time = "Morning"
                 print (str("It's just after quarter to " + str(Hour) + "in the "+ Time))
            elif Hour == 12:
                 Hour = "One"
                 Time = "Afternoon"
                 print (str("It's just after quarter to " + str(Hour)+ "in the "+ Time))
            elif Hour == 13:
                 Hour = "Two"
                 Time = "Afternoon"
                 print (str("It's just after quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 14:
                 Hour = "Three"
                 Time = "Afternoon"
                 print (str("It's just after quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 15:
                 Hour = "Four"
                 Time = "Afternoon"
                 print (str("It's just after quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 16:
                 Hour = "Five"
                 Time = "Afternoon"
                 print (str("It's just after quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 17:
                 Hour = "Six"
                 Time = "Evening"
                 print (str("It's just after quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 18:
                 Hour = "Seven"
                 Time = "Evening"
                 print (str("It's just after " + str(Hour) + " in the "+ Time)) 
            elif Hour == 19:
                 Hour = "Seven"
                 Time = "Evening"
                 print (str("It's just after quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 20:
                 Hour = "Nine"
                 Time = "Evening"
                 print (str("It's just after quarter to " + str(Hour) + " in the "+ Time)) 
            elif Hour == 21:
                 Hour = "Ten"
                 Time = "Night"
                 print (str("It's just after quarter to " + str(Hour) + " at "+ Time)) 
            elif Hour == 22:
                 Hour = "Eleven"
                 Time = "Night"
                 print (str("It's just after quarter to " + str(Hour) + " at "+ Time)) 
            elif Hour == 23:
                 Hour = "Twelve"
                 Time = "Morning"
                 print (str("It's just after quarter to " + str(Hour) + " in the "+ Time))

# This block of code checks whether the 'minute' number input is within the 53-59 range, if it is it will
# out put the time as just before the next hour         
        elif Minute >=53 and Minute <=59: 
            if Hour == 0:
               Hour = "One"
               Time = "Morning"
               print (str("It's nearly " + str(Hour)+ " in the "+ Time)) 
            elif Hour == 1:
                Hour = "Two"
                Time = "Morning"
                print (str("It's nearly " + str(Hour) + " in the "+ Time)) 
            elif Hour == 2:
                Hour = "Three"
                Time = "Morning"
                print (str("It's nearly " + str(Hour) + " in the "+ Time)) 
            elif Hour == 3:
                Hour = "Four"
                Time = "Morning"
                print (str("It's nearly " + str(Hour) + "in the "+ Time)) 
            elif Hour == 4:
                 Hour = "Five"
                 Time = "Morning"
                 print (str("It's nearly " + str(Hour) + " in the "+ Time)) 
            elif Hour == 5:
                 Hour = "Six"
                 Time = "Morning"
                 print (str("It's nearly " + str(Hour) + " in the "+ Time)) 
            elif Hour == 6:
                 Hour = "Seven"
                 Time = "Morning"
                 print (str("It's nearly " + str(Hour) + " in the "+ Time)) 
            elif Hour == 7:
                 Hour = "Eight"
                 Time = "Morning"
                 print (str("It's nearly " + str(Hour) + " in the "+ Time)) 
            elif Hour == 8:
                 Hour = "Nine"
                 Time = "Morning"
                 print (str("It's nearly " + str(Hour) + " in the "+ Time)) 
            elif Hour == 9:
                 Hour = "Ten"
                 Time = "Morning"
                 print (str("It's nearly  " + str(Hour) + " in the "+ Time)) 
            elif Hour == 10:
                 Hour = "Eleven"
                 Time = "Morning"
                 print (str("The time is about quarter past " + str(Hour) + " in the "+ Time)) 
            elif Hour == 11:
                 Hour = "Twelve"
                 Time = "Afternoon"
                 print (str("It's nearly " + str(Hour) + " in the "+ Time))
            elif Hour == 12:
                 Hour = "One"
                 Time = "Afternoon"
                 print (str("It's nearly " + str(Hour)+ " in the "+ Time)) 
            elif Hour == 13:
                 Hour = "Two"
                 Time = "Afternoon"
                 print (str("It's nearly " + str(Hour) + " in the "+ Time)) 
            elif Hour == 14:
                 Hour = "Three"
                 Time = "Afternoon"
                 print (str("It's nearly " + str(Hour) + " in the "+ Time)) 
            elif Hour == 15:
                 Hour = "Four"
                 Time = "Afternoon"
                 print (str("It's nearly " + str(Hour) + " in the "+ Time)) 
            elif Hour == 16:
                 Hour = "Five"
                 Time = "Afternoon"
                 print (str("It's nearly " + str(Hour) + " in the "+ Time)) 
            elif Hour == 17:
                 Hour = "Six"
                 Time = "Evening"
                 print (str("It's nearly " + str(Hour) + " in the "+ Time)) 
            elif Hour == 18:
                 Hour = "Seven"
                 Time = "Evening"
                 print (str("It's nearly " + str(Hour) + " in the "+ Time)) 
            elif Hour == 19:
                 Hour = "Eight"
                 Time = "Evening"
                 print (str("It's nearly " + str(Hour) + " in the "+ Time)) 
            elif Hour == 20:
                 Hour = "Nine"
                 Time = "Evening"
                 print (str("It's nearly " + str(Hour) + " in the "+ Time)) 
            elif Hour == 21:
                 Hour = "Ten"
                 Time = "Night"
                 print (str("It's nearly " + str(Hour) + " at "+ Time)) 
            elif Hour == 22:
                 Hour = "Eleven"
                 Time = "Night"
                 print (str("It's nearly " + str(Hour) + " at "+ Time)) 
            elif Hour == 23:
                 Hour = "Twelve"
                 Time = "Morning"
                 print (str("It's nearly " + str(Hour) + " in the "+ Time))

       
# This is incase something unexpected happens        
else:
    print ("Something has gone wrong please try again")

