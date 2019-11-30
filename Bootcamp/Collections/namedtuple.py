from collections import namedtuple
# this module works by adding name to the index of a tupple
# when tuples are too big, rembering the exact index of a value could be difficult
# is basically like creating a new object, you will se why
# e.g.
Dog = namedtuple("Dog", 'age breed name')
# then we create and object dog
bongo = Dog(age=2, breed ="streetMix", name="Bongo")
print(bongo)
print(bongo.age)
print(bongo.name)

