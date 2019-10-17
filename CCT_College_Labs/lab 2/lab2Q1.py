## getting the inputs

start_salary = float(input("Enter starting salary: "))
increase = int(input("Enter annual % increase: "))
Years = int(input("Enter the number of years: "))

##computing and displaying the results
print("year   Salary/n-----------------")
multiplier = 1 + increase/ 100
nextSal = start_salary

for year in range(1, Years + 1):
    print("%2d%12.2f" % (year, nextSal))
    nextSal *= multiplier