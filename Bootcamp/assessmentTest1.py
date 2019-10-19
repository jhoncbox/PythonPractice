# Write a brief description of all the following Object Types and Data Structures we've learned about:

# Numbers: number types in python are int, float and complex.

# Strings: are conjuction of characters.

# Lists: list is a data structure in Python that is a MUTABLE or changable order of elements!!
#        Each element or value that is inside of a list is called an item. lists use squeare brakets

# Tuples: Tuples are likes Lists, with the difference that these are IMMUTABLE. once a tuple is create
#            it cannot change. Tuples uses parentheses.

# Dictionaries: is an unordered collection of items. While other compound data types have only value as an element,
#               a dictionary has a key: value pair. Dictionaries are optimized to retrieve values when the key is known.

# -----------------------------------------------------------------------------------------

##Write an equation that uses multiplication, 
##division, an exponent, addition, and subtraction that is equal to 100.25.

print(10e2*10/5-1950+50.25)

# Answer these 3 questions without typing code. Then type code to check your answer.

# What is the value of the expression 4 * (6 + 5)
# R = 44
# What is the value of the expression 4 * 6 + 5 
# R = 29
# What is the value of the expression 4 + 6 * 5
# R = 34

print(4 * (6 + 5))
print(4 * 6 + 5)
print(4 + 6 * 5)

# What is the type of the result of the expression 3 + 1.5 + 4?

print(type(3 + 1.5 + 4))

# What would you use to find a number’s square root, as well as its square?
# num = int(input("insert a number to calculate the squeare "))
# result = num * num
# print("the squeare of " , num , " is :" , result)

# SQUEARE ROOT
print(100 ** 0.5)

# STRINGS
# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
s = "hello"
print(s[1])

# Reverse the string 'hello' using slicing:
print(s[::-1])

# Given the string hello, give two methods of producing the letter 'o' using indexing.
print(s[4])
print(s[-1])

# LISTS
# Build this list [0,0,0] two separate ways.

# method 1
print([0]*3)
# method 2 (preferred)
list = [0,0,0]
print(list)

# Reassign 'hello' in this nested list to say 'goodbye' instead:
# PAY GOOD ATTENTION TO THE WAY TO ACCESS THE INNER LIST
list3 = [1,2,[3,4,'hello']]
list3[2][2] = "goodbay"
print(list3)

# Sort the list below:
list4 = [5,3,4,6,1]
# sorted(list4)
list4.sort()
print(list4)

# DICTIONARIES
# Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'}
# Grab 'hello'
print(d['simple_key'])
#----------------------------
d = {'k1':{'k2':'hello'}}
# Grab 'hello'
print(d['k1']['k2'])
## This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])
# Can you sort a dictionary? Why or why not?
# R = NO!, 'cause normal dictionaries are MAPPINGS not sequence 
#------------------------------------------------------------

# TUPLES
# What is the major difference between tuples and lists?
# R = 
# How do you create a tuple?
# R = using parenthesis

# Sets
# What is unique about a set?
#R = THEY DON'T ALLOW DUPLICATE ITEMS

# Use a set to find the unique values of the list below: 
list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))

# BOOLEANS
# What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)
# Answer before running cell
2 > 3
#R = FALSE
# Answer before running cell
3 <= 2
#R = FALSE
# Answer before running cell
3 == 2.0
#R = FALSE
# Answer before running cell
3.0 == 3
#R = TRUE
# Answer before running cell
4**0.5 != 2
#R = FALSE

