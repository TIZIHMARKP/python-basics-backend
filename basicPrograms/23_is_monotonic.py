# A monotonic array is one that is entirely non-increasing or non-decreasing.

def isMonotonic(arr):
    increasing = decreasing = True

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        elif arr[i] < arr[i - 1]:
            increasing = False

    return increasing or decreasing
            

# Testing the Function
arr1 = [1, 2, 3, 4]   # Monotonic (non-decreasing)
arr2 = [3, 2, 1]      # Monotonic (non-decreasing)
arr3 = [1, 3, 2, 4]    # Not monotonic

print("Array 1 is monotonic: ", isMonotonic(arr1))
print("Array 2 is monotonic: ", isMonotonic(arr2))
print("Array 3 is monotonic: ", isMonotonic(arr3))