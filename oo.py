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

# Create your Road class here

class Road:
# Instantiate Road objects here
    num_lanes = 2
    speed_limit = 25
    def __init__(self, name):
        self.name = name


# 3. Update Password
# #############################################################################
class User(object):
    """A user object."""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    # write the update_password method here


# 4. Build a Library
# #############################################################################
class Book(object):
    """A Book object."""

    def __init__(self, title, author):
        self.title = title
        self.author = author

# Create your Library class here

