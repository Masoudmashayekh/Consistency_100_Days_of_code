# Day 26 : List and Dictionary Comprehensions
# Key word: new_list = [new_item for item in list] 


# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1  = n + 1
#     new_list.append(add_1)

# print(new_list)

# numbers = [1, 2, 3]
# new_list  = [ n+1 for n in numbers] # List Comprehension
# print(new_list)

# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)

# new_list = [num for num in range(2,9,2)]
# print(new_list)

# new_list = [num * 2 for num in range(1, 5)]
# print(new_list)


# Conditional List Comprehension
# Key word: new_list = [new_item for item in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)