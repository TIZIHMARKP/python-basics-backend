def find_n_largest_elements(lst, n):
    #
    sorted_lst = sorted(lst, reverse=True)

    # 
    largest_elements = sorted_lst[:n]

    return largest_elements


numbers = [30, 10, 45, 5, 20, 15, 3, 345, 67, 83, 100, 173, 84, 95]

