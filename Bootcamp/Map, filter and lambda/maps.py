#  ON THIS SECTION WE ARE LEARNING ABOUT FUNCTION MAP
# map is a function that maps a function with a *iterable objects
# "Make an iterator that computes the function using arguments from each of the iterables.
# Stops when the shortest iterable is exhausted."

def square(num):
    return num**2

my_nums = [1,2,3,4,5,6]
#  this will print all items in the "my_nums" list after they passed through the function "square"
for item in map(square,my_nums):
    print(item)

# you can brign back the result using the build in function "List"
list(map(square,my_nums))

# FILTER FUNCTION
# Return an iterator yielding those items of iterable for which function(item) is true.
# If function is None, return the items that are true.
def check_even(num):
    return num%2==0

for n in filter(check_even,my_nums):
    print(n)

# LAMBDA EXPRESSIONS: step by step of how to write a lambda expression
# 1. we are going to transform this function into lambda
def square(num):
    result = num**2
    return result
# 2. by elimination "result" and placing the action after after the return word, we get the same output
def square(num):
    return num**2
# 3. although python takes in count the spaces when when writing a loop or function or if statement 
#  placing everythingon this function on the same line will do the work aswell
def square(num): return num**2
# 4. Lambda expressions is also known as a anonimous expression, is some functionallity that you intent
# # to use one time, be cause of this we dont use a name or the "def" key word nor the return keyword.
lambda num: num**2 

# LAMBDA IS USED IN CONJUCTION WITH THE MAP AND FILTER FUNCTION

list(map(lambda num: num**2,my_nums))
#OR
filter(lambda num:num%2 == 0,my_nums)
