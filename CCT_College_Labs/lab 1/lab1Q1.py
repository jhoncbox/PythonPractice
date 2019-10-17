## QUESTION 1

print("Hello!, please Insert number of VHS and/or DVDs to Rent")
new_num = float(input("number of VHS to RENT: "))
old_num = float(input("number of DVD to RENT: "))

NEW_rental = 3.00
OLD_rental = 2.00

totalCostPerNight = new_num*NEW_rental + old_num*OLD_rental

night = int(input("number of nights to be rented for: "))

totalRentalCost = totalCostPerNight * night

print("The total cost of the rental is: $" + str(totalRentalCost))




