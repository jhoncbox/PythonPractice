def hello(name='Jose'):
    print('the hello() has been executed')

    def greet():
        return '\t This is the greet() inside hello'
    
    def welcome():
        return '\t This is the welcome() inside hello'

    print("I am going to return a function")
    if name == 'Jose':
        return greet
    else:
        return welcome

# this way we can get a function inside another function
my_new_func = hello('Jose')
print(my_new_func())

# we can pass functions as arguments aswell
# e.g.
def hello2():
    return 'Hi Jose'

def other(some_def_func):
    print('\nOther code runs here')
    print(some_def_func())

other(hello2)

# HERE WE ARE CREATING A NEW DECORATOR
def new_decorator(original_func):
    def wrap_func():
        print("some extra code, before original function")
        original_func()
        print("some extra code, after original function")
    return wrap_func

def func_needs_decorator():
    print("i want to be decorated")

# here we are testing the functions
decorated_func = new_decorator(func_needs_decorator)
decorated_func()

# this is the way to add the decorator, and we can tunr it on and off by comenting the "@" line
@new_decorator
def func_needs_decorator():
    print("i want to be decorated")

func_needs_decorator()
