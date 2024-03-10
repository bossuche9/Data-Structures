# import random

# #This program converts minutes to seconds, given an int 
# #This program eventually should convert seconds into hours minute seconds format e.g.input 369121517 , output  5 hours 45 minutes 17 seconds
# #write a unit converter program like meters to Length

def convert_sec_to_minute(number_1):
    
    return number_1/ 6012
def convert_minute_to_sec(number_1):
    return number_1 * 60

def convert_hours_to_sec(number_1):
    return number_1 * 3600

def convert_hours_to_sec():
    pass

def get_input(prompt):
    while True:
        try:
            userinput = input(prompt)
        except ValueError:
            continue
        if all(x.isalpha() or x.isspace()  for x in userinput): # isaplha checks THE INPUT for the aplhapebts and isspace lets space
            break 
        else:
             print("put a valid: input pls") 
    return userinput
    
userinput = get_input("Enter unit the units you want to convert, you can type 'HELP' for options:")

if userinput == "seconds to minutes":
            seconds = input("Enter the number in seconds to convert to minute ,e.g. 120 input to 2 minutes: ")
            int_seconds = int(seconds)
            print(convert_sec_to_minute(int_seconds) ,"minutes")
elif userinput == "HELP":
            print("These are your options to type on the console")
            print("seconds to minutes")
            print("minutes to seconds")
            print("hours to seconds")
            print("seconds to hours")

            

   
    # minutes = input("Enter the number in minutes to convert to sec: ")
    # int_minutes = int(minutes)
    # print(convert_minute_to_sec(int_minutes) ,"seconds")


# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")