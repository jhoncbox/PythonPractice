## get any ampunt of numbers from the user and sum them up if the user
# just presses enter.

##starting variables
sum = 0
count = 0

## the while loop is used so if the user inserts a number and press enter
# it will sum up and add to the sum variable and add up 1 number to the count
# variable, if the user just presses enter the program finishes and shows the results
while True:
    number = input("Enter a number and press enter, or just press enter to quit: ")
    if number == "":
        break
    sum += float(number)
    count += 1

print("The sum is: ", sum)
if count > 0:
    print("The average is", sum/count)