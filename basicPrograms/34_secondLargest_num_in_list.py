# Sample list of numbers
numbers = [30, 10, 45, 5, 20, 31]

numbers.sort(reverse=True) # Sorting the list in descending order
 
if len(numbers) >= 2:     # checking if there are atleast 2 numbers in the list
    second_largest = numbers[1]
    print("The 2nd largest number in the list is: ", second_largest)

else:
    print("The list does not contain a second largest number")

