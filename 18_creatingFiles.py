
# ==================== Creating Files =====================
#  

# countryFile = open('countries1.txt', 'w')   # When writing a file, we make use of "w"
# countryFile = open('countries1.txt', 'a')   # When writing a file, we make use of "w"
newFile = open('newFile.py', 'w')   # When writing a file, we make use of "w"

# print(countryFile.write('\nThis is the new line'))
# print(countryFile.write('This is a new line'))
newFile.write('print(\'This is a new file\')')   # Creating a new file newFile.py

