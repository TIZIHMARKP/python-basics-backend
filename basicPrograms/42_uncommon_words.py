
def uncommon_words(str1, str2):
    # Spliting the stings into words, then we convert them to sets
    words1 = set(str1.split())
    words2 = set(str2.split())

    # We find uncommon words by making us of the set difference
    uncommon_words_set = words1.symmetric_difference(words2)

    # We convert the list of uncommon words back to a list
    uncommon_words_list = list(uncommon_words_set)

    return uncommon_words_list

string1 = "Python is a programming language"
string2 = "Python is a computer language"

uncommon = uncommon_words(string1, string2)

print("Uncommon words: ", uncommon)
# Uncommon words: ['computer', 'programming']
