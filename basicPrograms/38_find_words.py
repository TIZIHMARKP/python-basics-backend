# Write a Python program to find words which are greater than given length k.

def find_words(words, k):
    #
    result = []

    for i in words:
        #
        if len(i) > k:
            #
            result.append(i)

    return result

word_list = ["apple", 'banana', "cherry", "date", "Cangaro", "through", 'Cameroon', "Womens", "Africa"]
k = int(input("Enter lenght of K: "))

long_words = find_words(word_list, k)

print(f"Words longer than {k} characters:  {long_words}")

    

