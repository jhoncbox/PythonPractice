# this special methods are create to help with the functionality of the class
# e.g.

class Book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    # this method helps to create a strign representation of the class
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    # this method tells the number of pages for each book by using the len keyword
    def __len__(self):
        return self.pages

    # this method gives a message when a book is delete
    def __del__(self):
        print("book {} object has been deleted".format(self.title))

b = Book("cosas de la vida", "jhon", 300)
c = Book("jamon cerrano", "mariana", 400)

print(b)
print(c)
print(len(b))