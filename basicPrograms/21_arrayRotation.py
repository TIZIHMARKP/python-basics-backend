# Python Program for array rotation.

def rotate_array(arr, d):
    n = len(arr)

    if d < 0 or d >= n:
        return "Invalid rotation value"
    
    rotated_arr = [0] * n

    for i in range(n):
        rotated_arr[i] = arr[(i + d) % n]

    return rotated_arr

