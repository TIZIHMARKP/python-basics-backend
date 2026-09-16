
def uncommon_words(str1, str2):

    words1 = set(str1.split())
    words2 = set(str2.split())

    uncommon_words_set = words1.symmetric_difference(words2)

    uncommon_words_list = list(uncommon_words_set)

    return uncommon_words_list

string1 = "Python is a programming language"
string2 = "Python is a computer language"

uncommon = uncommon_words(string1, string2)

print("Uncommon words: ", uncommon)
# uncommon words: ['computer', 'programming']
