# Python Program for array rotation.

def rotate_array(arr, d):
    n = len(arr)

    #  Checking if 'd' is valid, it should be within the range of array len
    if d < 0 or d >= n:
        return "Invalid rotation value"
    
    #  Creating a new array to store the rotated elements.
    rotated_arr = [0] * n

    # performing the rotation
    for i in range(n):
        rotated_arr[i] = arr[(i + d) % n]

    return rotated_arr

arr = [1, 2, 3, 4, 5, 6]

d = int(input(f"Enter number of positions to rotate less than {len(arr)}: "))

result = rotate_array(arr, d)

print("Original Array: ", arr)
print("Rotated Array: ", result)

