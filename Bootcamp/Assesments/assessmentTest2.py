# STATEMENTS ASSESSMENTS TEST
# Let's test your knowledge!

#Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'

for x in st.split():
    if x.startswith("s"):
        print(x)

#----------------------------------------------------------------------------------------
#Use range() to print all the even numbers from 0 to 10.
nums = range(0,10,2)
for x in nums:
    print(x)

#----------------------------------------------------------------------------------------
#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
list1 = [x for x in range(1,50) if x%3==0]
print(list1)

#----------------------------------------------------------------------------------------
#Go through the string below and if the length of a word is even print "even!"
st2 = 'Print every word in this sentence that has an even number of letters'
for x in st2.split():
    if len(x)%2==0:    
        print(x)

#----------------------------------------------------------------------------------------
# Write a program that prints the integers from 1 to 100. 
# But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
for x in range(1,101):
    if x%3==0 and x%5==0:
        print("FizzBuzz")
    elif x%5==0:
        print("Buzz")
    elif x%3==0:
        print("Fizz")
    else:
        print(x)
#----------------------------------------------------------------------------------------
# Use List Comprehension to create a list of the first letters of every word in the string below:
st3 = 'Create a list of the first letters of every word in this string'
list2 = [x[0] for x in st3.split(" ")]
print(list2)
#----------------------------------------------------------------------------------------
# 
