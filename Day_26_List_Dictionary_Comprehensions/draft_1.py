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

# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

# short_names = [name for name in names if len(name) < 5]
# print(short_names)

# long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)



# Dictionary Comprehension
# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key: new_value for (key,value) in dict.items()}
# new_dict = {new_key: new_value for (key,value) in dict.items() if test}

#-------------------------------------------

# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# students_scores = {student: random.randint(0, 100) for student in names}
# print(students_scores)
# passed_students = {student: score for (student,score) in students_scores.items() if score > 75}
# print(passed_students)




#-------------------------------------------

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word:len(word) for word in sentence.split()}
# print(result)


#-------------------------------------------

# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

# weather_f = { key: (value*9/5)+32 for (key,value) in weather_c.items()}

# print(weather_f)

#------------------------------------------- How to Iterate over a Pandas DataFrame

student_dic={
    "students": ["Angela", "Alex", "Jon"],
    "scores": [44, 65, 99]
}

# Looping through dictionaries:
for (key: value) in studedents.items():