## Question 3

hourlyRate = input("insert the hourly rate of the employee: ") 
overTimePay = hourlyRate * 1.5
WeekHoursWorked = input("Insert the amount of normal hours worked: ")
WeekOverTimeHoursWorked = input("Insert the amount of Overtime hours worked: ")

TotalPaymentForTheWeek = hourlyRate*WeekHoursWorked + overTimePay*WeekOverTimeHoursWorked
print("Total amount to be paid to the employee: $"+str(TotalPaymentForTheWeek))