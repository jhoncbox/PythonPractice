"""
Program: Question2.py

Computes the sum and average of a series of input numbers.
"""

sum = 0
count = 0
while True:
    number = input("Enter a number or press Enter to quit: ")
    if number == "":
        break
    sum += float(number)
    count += 1

print("The sum is", sum)
if count > 0:
    print("The average is", sum / count)
