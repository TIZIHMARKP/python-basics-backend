# ==== PYTHON PROGRAM TO SPLIT ARRAY AND ADD THE FIRST PART TO THE END OF THE ARRAY ====

def split_and_add(arr, k):
    if k <= 0 or k >= len(arr):
        return arr
    
    # Spliting the array into two parts
    first_part = arr[:k]
    second_part = arr[k:]

    result = second_part + first_part

    return result

arr = [1, 2, 3, 4, 5]
# k = 2
size = int(input("Enter lenght limit to split array: "))
result = split_and_add(arr, size)
print("Original Array: ", arr)
print("Array after splitting and adding: ", result)

