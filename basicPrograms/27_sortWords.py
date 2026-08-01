# Program to sort alphabetically the words fro a string probided by the user
my_str = input("Enter a string: ")

# Breaking down the string into a list of words
words = [word.capitalize() for word in my_str.split()]

words.sort()

print("The sorted words are: ")
for word in words:
    print(word)


