def find_n_largest_elements(lst, n):
    #
    sorted_lst = sorted(lst, reverse=True)

    # 
    largest_elements = sorted_lst[:n]

    return largest_elements


