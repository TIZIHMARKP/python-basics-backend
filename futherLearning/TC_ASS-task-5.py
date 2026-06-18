#      =========== QUESTION ==============

# 1. What are advanced data types in Python and why are they useful?

# 1. Describe the difference between list vs tuple and set vs dictionary.

# 3. Write a program that creates two sets of numbers, finds their intersection and union, and prints the results.

# 4. Write a program that defines a nested dictionary representing a classroom (e.g., { "class1": {"Alice": 85, "Bob": 90}, "class2": {"Charlie": 78}}). Create a function to calculate the average score for each class and return a dictionary with class names and their averages.

# 5. What is Flask and why is it used in web development?

# 6. Describe the request-response cycle in a Flask application.

# 7. How does Flask handle incoming HTTP requests?

# 8. What is the `flask run` command used for?


#      =========== ANSWERS ==============


# 3. Write a python program that creates two sets of numbers, finds their intersection and union, and prints the results.

# =================== SOLUTION =========================
# set_World = {1, 2, 3, 4, 5, 6, 7, 8, 9, }
# set_Africa = {3, 4, 5, 10}

# print("Union: ", set_World.union(set_Africa))          # Output: {1, 2, 3, 4, 5}
# print("Intersection: ", set_World.intersection(set_Africa))   # Output: {3}


# 4. Write a program that defines a nested dictionary representing a classroom (e.g., { "class1": {"Alice": 85, "Bob": 90}, "class2": {"Charlie": 78}}). Create a function to calculate the average score for each class and return a dictionary with class names and their averages.

# classRoom = {
#     "Form1": {"Alice": 85, "Bob": 90, "Mary": 88, "John": 70},
#     "Form2": {"David": 80, "Adam": 92, "Rice": 50},
#     "Form3": {"Burinyu": 70, "Tata": 75},
#     "Form4": {"Randy": 80}
# }

# def calcuAvg(classes):
#     avgs = {}

#     for className, studs in classes.items():
#         scores = studs.values()
#         avg = sum(scores) / len(scores)
#         avgs[className] = round(avg, 2)

#     return avgs

# AvgResult = calcuAvg(classRoom)
# print("Final Average Result: ", AvgResult)


