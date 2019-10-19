# this are usefull operator that are builded in on Python.

# range()

# this range gives all numbers from 0 to 10
for num in range(10):
    print(num)

# this range gives the numbers between the parameters
for num2 in range(3,10):
    print(num2)

# this range gives the numbers between the 1st and 2nd parameter, with a lap step of the 3rd parameter
for num in range(0,10,2):
    print(num)

#ENUMERATE FUNCTION
# it gives the index count automatically in the form of tuples
band = "caramelos de cianuro"
for letter in enumerate(band):
    print(letter)
#------------------------------------
# ZIP
# zips together two or more lists
list1 = [1,2,3,4]
list2 = ['a','b','c','d']
list3 = [100,200,300,400]
# NOTE:it will always zip untill the list index of the shortest list 
for item in zip(list1,list2,list3):
    print(item)

# IN operator
#  it says wether a item is inside a list or not
print('x' in list2)
print('b' in list2)

# MIN , MAX and RAMDOM
list4 = [20,40,4,32,2,76,12]
print(max(list4))
print(min(list4))

from random import randint
print(randint(0,100))

#INPUT FUNCTION
input("enter a number ")
