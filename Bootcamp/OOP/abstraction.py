# this is an example of ABSTRACTON
# we create a class ANIMAL that is only to be used as a based for other classes
# AND cannot be instanciated

class Animal():
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("subclass must implement this abstract method")

class Dog(Animal):

    def speak(self):
        return self.name + " says Woof"

class Cat(Animal):

    def speak(self):
        return self.name + " says Meow"

jhon = Dog("Jhon")
Poly = Cat("Poly")

print(jhon.speak())
print(Poly.speak())