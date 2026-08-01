# Defining punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# taking input
my_str = input("Enter a string: ")

# removing punctuation from the string
no_punct = ""
for char in my_str:
    if char not in punctuations:
        no_punct = no_punct + char

# displaying the unpunctuated string
print(no_punct)


