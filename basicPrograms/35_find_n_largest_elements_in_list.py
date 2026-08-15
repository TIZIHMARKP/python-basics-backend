def find_n_largest_elements(lst, n):
    #
    sorted_lst = sorted(lst, reverse=True)

    # 
    largest_elements = sorted_lst[:n]

    return largest_elements


numbers = [30, 10, 45, 5, 20, 15, 3, 345, 67, 83, 100, 173, 84, 95]

N = int(input("Input length N = "))

#
result = find_n_largest_elements(numbers, N)

# 
print(f"The {N} largest elements in the list are: ", result)

