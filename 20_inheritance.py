
# ==================== Inheritance In Python =====================
#  Inheritance means taking from an existing class and then taking out the method and everything in it and putting it in a new class

from new import Student

class Person(Student):
    pass

p1 = Person
print(p1.name)

