# ===========  Assingment Task 3 ===========

"""

1. What is a function and why is it important in programming?

2. Explain the concept of default parameters with an example.

3. What is logging and how is it different from print statements?

4. Why is it important to close a file after operations?

5. How are modules different from packages? Give examples of built-in modules.

6. Why is version control important in software development?

7. What is Git and how does it work? Mention five commands and their uses.

8. What is the difference between Git and GitHub?

9. Write a program that reads a CSV file scores.csv containing student names and scores (e.g., "Alice,85"). Define a function average_score() that calculates the average score, handling missing or invalid scores with try-except. Log each processed record and errors to a file. Save the program in a Git repository structure (e.g., with a README.md).

10. Write a program that uses the logging module to log a message "Program started" at the INFO level to a file named app.log


"""

'''
# ========= TASk 1 ========
What is a function and why is it important in programming?
*
A function is a reusable block of code which performs a specific or particular task. You define or give it a name and then call that name whenever you need to run that code. Functions are important in programming because of the following reasons:
- Reusability (Write once, use many times). Instead of copying and pasting the same line of code many times,  with a function we write once and call it many times thereby making it easy to read and write the code.
- Breaks complex problems into smaller pieces. A 500 or 1000 lines of code is hard to understand. Breaking it into small functions with each doing one thing, is much easier to read
- It facilitates testing and debugging. Small functions are easy to test and debug. Each function can be tested individually before putting them together
- Furthermore it facilitates code sharing. A function can be saved in modules and shared across different programs. For example python print() and input() are all built in functions that we use without thinking of their internal code.


# ========= TASk 2 ========
Explain the concept of default parameters with an example.
*
Default parameters allow a function or a block of code to have predefined values or variables for its parameters. If the user/programmer provides a value for that parameter, it overrides the default value, else if the user/programmer does not provide a value, the function automatically uses the default. For example

def cook(dish, spicies="salt"):
      print(f"Cooking {dish}, with {spicies}")
# using the default spicies
cook("eggs")       # Output: Cooking eggs with salt
# Overriding the default spicies
cook("eggs", "pepper")     # Output: Cooking eggs with pepper


# ========= TASk 3 ========
What is logging and how is it different from print statements?
*
Logging is a flexible method for recording events, errors and information that happens when a program runs during execution by. The logs are usually saved inside a file and can be reviewed by the programmer. Logging differs form print() in the following ways
- Logging supports several levels (DEBUG, INFO, WARNING, ERROR, CRITICAL) while print() has no levels
- Logging can write to files permanently while print() only shows in the terminal



# ========= TASk 4 ========
Why is it important to close a file after operations?
*
Closing a file after operations is important for the following reasons:
- It frees system resources. Each open file consumes CPU space and several CPU space have limits on how many files can be open simultaneously
- It allows other processes to be able to read or modify a file. When a file is kept open for long, some processes may be unable to read or modify the file
- Furthermore it prevents "too many open files" errors. A long running program that never close files may eventually crash


# ========= TASk 5 ========
How are modules different from packages? Give examples of built-in modules.
*
A module is a single file(.py) which contains functions, classes and variables that can be imported and reused, while a package is a collection of related modules organized in a directory that contains a special __init__.py file. The main differences include:
- Module = single file. Package = directory with multiple files
- Package always has __init__.py while a module does not need it
- A package may contain sub-packages and modules but a module cannot contain other modules
Examples of built-in modules include
- math module for maths operations
- datetime module for handling dates and times
- os module for operating system interface 


# ========= TASk 6 ========
Why is version control important in software development?
*
Version control is a system that tracks changes to files over time and let's you save your projects, go back to previous versions of your project and see who changed what and when. It's important in software development because of the following reasons
- It tracks history. It gives the records of who changed what, when and why
- It supports collaboration. Multiple developers can work simultaneously without conflicts
- Provides backup. Code is stored remotely (GitHub for example), protecting against data loss
- It further allows experimentation. Branches allow developers to try risky changes without affecting stable code



# ========= TASk 7 ========
What is Git and how does it work? Mention five commands and their uses.
*
Git is a distributed version control system that tracks changes in files and helps multiple people collaborate on projects. 
Git works by taking snapshots(commit) of a project overtime. The project files move through 3 areas: The working directory (Where work is done), the staging area (where all changes are made) and the repository ( where all commits are saved permanently) 
Five Git commands and their uses include
- git init. It creates a new Git repository in the current directory
- git add. It adds changes from the working directory to the staging area.
- git commit -m "message". It saves a permanent snapshot of staged changes with a descriptive message
- git status. Shows the current state of the repository (changed, stages, or untracked files)
- git log. Displays the commit history, including authors, dates, and messages


# ========= TASk 8 ========
What is the difference between Git and GitHub?
*
- Git is a version control system that runs locally on your computer, tracking changes, managing branches and saving commits of your code while gitHub is a cloud based hosting platform that stores Git repositories online and adding collaboration features like pull requests
- Git works offline while GitHub requires internet for syncing 
- Git is free and open source while GitHub is free for public repos but paid for private team features


# ========= TASk 9 ========
Write a program that reads a CSV file scores.csv containing student names and scores (e.g., "Alice,85"). Define a function average_score() that calculates the average score, handling missing or invalid scores with try-except. Log each processed record and errors to a file. Save the program in a Git repository structure (e.g., with a README.md).


https://github.com/TIZIHMARKP/python-score-average-calculator.git


'''


# ========= TASk 10 ========

import logging

logging.basicConfig(
    filename = "app.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Program started.")