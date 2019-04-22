"""
1. Discussion
-------------

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   Classes have a few design advantages such as data storage, flexible,
   structured, and "has it's own smarts".

2. What is a class?

    Classes are a core part of object-oriented programming which has properties
    and methods. A Class is like an object constructor, or a "blueprint" for
    creating objects.

3. What is a method?
    
    A method is a function that takes a class instance as its first parameter.
    Methods are memebers of classes.

4. What is an instance in object orientation?

    An instance in object orientation is an individual object of a certain
    class. Instantiation is the creation of an instance of a class.

5. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is a python variable that belongs to a class rather than 
   a particular object. A instance attribute is a python variable that belongs 
   to a particular object.

"""

# 2. Road Class
# #############################################################################
'''
    ******************************************************
    * Pseudocode:                                        *
    * 1. Creat a Road Class with hard coded attributes   *
    ******************************************************
    '''

# Create your Road class here

class Road(object):
# Instantiate Road objects here
    num_lanes = 2
    speed_limit = 25
    def __init__(self, name):
        self.name = name


# 3. Update Password
# #############################################################################

    '''
    ********************************************************************
    * Pseudocode:                                                      *
    * 1. Create update_password method                                 *
    * 2. Checks if password is the User's password from our User class *
    * 3. If password matches, let user update password                 *
    * 4. If password doesn't match, print("Invalid login")             *
    ********************************************************************
    '''

class User(object):
    """A user object."""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    # write the update_password method here
    def update_password(self, current_password):
       
        if current_password == self.password:
             self.password = str(input("Please enter your new password: "))
        else:
            print("Invalid login")


# 4. Build a Library
# #############################################################################
    '''
    ************************************************************
    * Pseudocode:                                              *
    * 1. Create Library Class                                  *
    * 2. Add empty book list                                   *
    * 3. Add add_book method which calls the Book(object)      *
    * 3. Append user info of title and author into book list   *
    * 4. Create find books by author method which allows user  *
    *     to search the book titles by passing the author name *
    *     and prints the book titles written by that author    *
    ************************************************************
    '''

class Book(object):
    """A Book object."""

    def __init__(self, title, author):
        self.title = title
        self.author = author

# Create your Library class here
# Example to call Lib Class: Lib = Library()
# Then use the methods such as Lib.add_book("Game of Thrones", "Martin")
# Lib.find_books_by_author("Martin")
# >>> "Game of Thrones"

class Library(object):
    # Book List
    books = []

    # Add_book method which creates an instance of a Book() and stores it in list.
    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
    # Allows user to search through our book and using the authors name
    # and returning a print statement that book title by the author.
    def find_books_by_author(self, author):

        for book in self.books:
            if book.author == author:
                print(book.title)

