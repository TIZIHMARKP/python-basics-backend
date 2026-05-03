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


# ========= TASk 10 ========

import logging

logging.basicConfig(
    filename = "app.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Program started.")