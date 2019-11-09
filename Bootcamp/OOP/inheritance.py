# EXAMPLES OF INHERITANCE
# THIS would be the parent class or base class 
class Animal():
    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

#  this is the child class that inherate all attributes from the parent class

class Dog(Animal):
    def __init__(self):
        # here we are passing all attributes and methods from Animal to the Dog
        Animal.__init__(self)
        print("DOG CREATED")
    
    # you can Override methods by declaring them again in the child class
    # e.g.
    def eat(self):
        print("I am eating Dog's food")

# testing
mydog = Dog() 
mydog.who_am_i()
mydog.eat()