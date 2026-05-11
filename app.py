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

print(book1 == book3)  # False
print(book1 < book2)   # False
print(book2 < book1)   # True
print(book2 == book4)  # True

    
