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
