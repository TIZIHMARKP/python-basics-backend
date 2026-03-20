
# ====================  List Methods =====================
# continue at 01:03

list1 = [4, 2, 1, 5, 3]
list2 = ['banana', 'apples', 'mango', 'oranges', 'mango']
list2.append('cherry')
print(list2)
print(len(list2)) #5
list2.insert(1, 'Melon')
list2.remove('banana')
print(list2)
print(list2.index('mango'))  #2
print(list2.count('mango'))  #2

list2.reverse()
print(list2)

list3 = list2.copy()
list3.reverse()
print(list3)

del list2[0]
print(list2)

list2.pop()   # Removing the last value in the list
print(list2)
list2.pop(1)
print(list2) 

list2.clear()
print(list2)


list1.sort()
print(list1)   # Sorting a list