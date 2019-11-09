import math
#Write a PYTHON code that allows the user to enter the age as an integer value. 
# The PYTHON code will verify if their age is above 17 or not. If their age is above 17,
#  the program should display "You may enter in the musical concert", if they are below 17, 
# the program should output "Sorry not tonight". [Note: You can use PYTHON compiler to check
#  the execution of the code].

age = int(input("please enter your age: "))

if age > 17:
    print("You may enter in the musical concert")
else:
    print("Sorry not tonight")

#-----------------------------------------

# Determines if a number is prime.
# # returns 1 if number is prime
# def isPrime(number):
#     for x in range(2,number):
#         if (number%x==0):
# 	        return 0
#     return 1
# # test numbers between 2 and 1,000
# for number in range(2,1001):
#     if isPrime( number):
#         print(number)

# print(math.sqrt(36))
