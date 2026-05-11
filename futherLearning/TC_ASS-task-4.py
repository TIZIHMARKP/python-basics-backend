# ===========  Assingment Task 4 ===========

"""
1. What is Object-Oriented Programming (OOP) and why is it useful?

2. Define a class and an object in Python.

3. What is the difference between instance variables and class variables?

4. What is the `self` keyword and why is it necessary?

5. Explain how to create and use an object of a class.

6. How do you access attributes and methods from outside the class?

7. What are dunder (double underscore) methods and give examples.

8. Define a Person class with an attribute name and a method introduce. Create a Worker class with an attribute job. Create a Manager class that inherits from both Person and Worker, combining their attributes and methods. Test with a Manager object.

9. Create a Book class with attributes title and pages. Implement __eq__ to compare two books based on pages and __lt__ to compare based on page count. Test by comparing two Book objects.

"""




"""
# ========= TASk 1 ========
OOP is a programming style that groups related data and functions into reusable units called objects which are created from chasses, which act as blueprints or templates. In other words OOP is a programming paradigm that organizes code into classes (blueprints) and objects (instances of those blueprints). It is useful because: 
- Organization. OOP helps to organize objects or models real world entities naturally
- Reusability. It helps in code reusability. A class can be written once and many objects created from it via inheritance
- Maintainability. It is easier to debug and update isolated pieces of code with OOP
- Allows modular and scalable code design


# ========= TASk 2 ========
A class is a blueprint or template for creating objects. It defines the properties(attributes) and behaviors(methods) that objects created from it will have.
An object is an instance of a class. It is the actual thing created from the blueprint, with its own unique data.

# ========= TASk 3 ========
- Class variables are shared by all objects of a class while an instance variable is unique to a particular object
- Changing a class variable via call affects all objects whereas changing instance variable only affects that object. For example
class Student:
class Student:
    school_name = "Techieversity"  # Our class variable

    def __init__(self, name):
        self.name = name            # Our instance variable

student1 = Student("Tizih")
student2 = Student("John")

print(student1.school_name)  # Techieversity
print(student2.school_name)  # Techieversity

print(student1.name)   # Tizih
print(student2.name)   # John

Student.school_name = "TechCrush"
print(student1.school_name)  # TechCrush (Changed from Techieversity)
print(student2.school_name)  # TechCrush (Changed from Techieversity)

student1.name = "Mark"
print(student1.name)    # Mark (It only changed for Student1)
print(student2.name)    # John (Did not change)

# ========= TASk 4 ========
It refers to the instance calling the method. It is necessary because it is used to access attributes and methods of the object.

# ========= TASk 5 ========
To create and use an object of a class, we first create a class and call the class like a function, using its name followed by parentheses
- To use an object, we access its attributes and methods using dot notation(.). Example below
class Dog:
    def bark(self):
        print("Woof! woof!")
    # creating an object
my_dog = Dog()
my_dog.bark()  

# ========= TASk 6 ========
To access attributes and methods from outside the class, we use dot notation(.) on the object

# ========= TASk 7 ========
Dunder methods are special methods in Python that start and end with two underscores, such as __init__, __str__, __repr__, __len__, __add__, __eq__. They are also known as magic methods because python calls them automatically behind the scenes when certain actions happen

"""



# ========= TASk 8 ========

class Person:               # Parent class 1
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}")

class Worker:               # Parent class 2
    def __init__(self, job):
        self.job = job

class Manager(Person, Worker):    # Child class
    def __init__(self, name, job):  # combining and initialising the attribute of Person and Worker class
        Person.__init__(self, name)
        Worker.__init__(self, job)

    def outPut(self):
        print(f"{self.name} works as a {self.job}")

managerObj1 = Manager("Paul", "Plumber")
managerObj1.introduce()
print(f"Job: {managerObj1.job}")
managerObj1.outPut()


# ========= TASk 9 ========

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    # For ==
    def __eq__(self, other):
        # comparing base on pages
        return self.pages == other.pages
    
    # For <
    def __lt__(self, other):
        # comparing base on page counts
        return self.pages < other.pages

book1 = Book("Bible", 1000)   
book2 = Book('Romeo and Julieth', 200)
book3 = Book("Advance Python", 350)
book4 = Book("Python Basics", 200)

# Testing comparisons of objects
print(book1 == book3)  # False
print(book1 < book2)   # False
print(book2 > book1)   # False
print(book2 == book4)  # True

# With detailed messages
print(f"`{book1.title}` and `{book3.title}` same pages? {book1 == book3}")  # False
print(f"`{book1.title}` fewer pages than `{book2.title}`? {book1 < book3}")  # False
print(f"`{book2.title}` more pages than `{book1.title}`? {book1 > book1}")  # False
print(f"`{book2.title}` and `{book4.title}` same pages? {book2 == book4}")  # True

    