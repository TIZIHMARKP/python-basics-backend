
# ==================== 2D Lists and Nested Loops In Python =====================
# 2D list means multiple list inside a list variable
# 

my_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(my_list)
print(my_list[0][0])      # 1
print(my_list[1][1])      # 5

# ================  Nested Loop ==============
# Nested loop is a loop in a loop

for lists in my_list:
    print(my_list)

for lists in my_list:
    for row in lists:
        print(row)

        