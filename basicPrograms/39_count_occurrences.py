
def count_occurrences(lis, element):
    count = lis.count(element)
    return count

# 
my_list = [1, 2, 3, 4, 2, 5, 2, 3, 4, 6, 5]
print("Elements in list; ", my_list)
element_to_count = int(input("Enter element to count: "))

occurrences = count_occurrences(my_list, element_to_count)
print(f"The element {element_to_count} appears {occurrences} times in the list")
