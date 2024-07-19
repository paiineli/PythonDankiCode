print(30 * '-')

list1 = ["chicago", "queens", "salvador", "pernambuco"]
print(list1)

list2 = [2, 3, 7, 8, 10]
print(list2)

list3 = [2.0, 3.5, 6.3]
print(list3)

list4 = [True, False]
print(list4)

# index    0       1      2      3     4
list5 = [True, "chicago", 2.5, False, 4]
print(list5)

print(type(list5))

print(list5[1])

# Slicing

print(list5[-1])  # returns the last element of the list

print(list5[::])  # returns the whole list

print(list5[1:])  # returns the list from index 1 to the end

print(list5[:3])  # returns the list from the beginning to index 2

print(list5[1:4]) # returns the list from index 1 to index 3

print(list5[1:5:2])

name = "earth"
print(name[2:4])

print(30 * '-')
