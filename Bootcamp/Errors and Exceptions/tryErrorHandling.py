# here is a simple sample on how to to handle or detect an error in a function
def ask_for_int():
    while True:
        try:
            # ask the user for a number
            result = int(input("please provide a number: "))
        except:
            print("whoops! that's not a number")
            continue
        else:
            print("Yes, thank you")
            break
        finally:
            print("End of try/except/finally")
            print("finally running")
       
# ask_for_int()

# -----------------------------------------------------
# Errors and Exceptions Homework
# Problem 1
# Handle the exception thrown by the code below by using try and except blocks.
try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("nope, you can't get squeare values from strings")


# Problem 2
# Handle the exception thrown by the code below by using try and except blocks.
#  Then use a finally block to print 'All Done.'
try:
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    print("A number divided by Zero is infinite")
finally:
    print("all done")

# Problem 3
# Write a function that asks for an integer and prints the square of it.
#  Use a while loop with a try, except, else block to account for incorrect inputs.
def ask():
    while True:
        try:
            # ask the user for a number
            result = int(input("input a number: "))
        except:
            print("An Error ocurred, please try again")
            continue
        else:
            print("Here is the result")
            print(result**2)
            break

ask()
        
