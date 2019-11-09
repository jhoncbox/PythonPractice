## this is an example of an object
class Dog():

    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS
    species = 'mammal'
    
    def __init__(self,breed,name):
        # Attributes we take in the argument
        # it is assigned using self.attribute_name
        self.breed = breed
        self.name = name
    # OPERATIONS/ACTIONES -----> attributes
    def bark(self,number):
        print('WOOF ! my name is {} and I am {} years old'.format(self.name,number))
        # print("WOOF ! my name is " + self.name +" and I'm "+number+ " old")

my_dog = Dog('husky','jhon')
print(my_dog.species)
my_dog.bark(10)

# --------------------------------------------------------------------
class Circle():
    # CLASS OBJECT ATTRIBUTE
    pi = 3.14
    # setting a default value
    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius*radius*self.pi

    # METHOD
    def get_circumference(self):
        print(self.radius * self.pi * 2)

my_circle = Circle()
my_circle.get_circumference()
my_circle.radius = 20
print(my_circle.area)