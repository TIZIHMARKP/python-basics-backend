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


    

