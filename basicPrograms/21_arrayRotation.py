# Python Program for array rotation.

def rotate_array(arr, d):
    n = len(arr)

    if d < 0 or d >= n:
        return "Invalid rotation value"
    
    rotated_arr = [0] * n

    for i in range(n):
        rotated_arr[i] = arr[(i + d) % n]

    return rotated_arr

arr = [1, 2, 3, 4, 5, 6]

d = int(input(f"Enter number of positions to rotate less than {len(arr)}: "))

result = rotate_array(arr, d)

print("Original Array: ", arr)
print("Rotated Array: ", result)

