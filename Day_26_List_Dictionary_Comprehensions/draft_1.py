# Day 26 : List and Dictionary Comprehensions

# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1  = n + 1
#     new_list.append(add_1)

# print(new_list)

numbers = [1, 2, 3]
new_list  = [ n+1 for n in numbers] # List Comprehension
print(new_list)
