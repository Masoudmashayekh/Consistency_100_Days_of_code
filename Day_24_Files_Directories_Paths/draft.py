# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()
with open("/Users/masoudmashayekh/Documents/Python/Consistency_100_Days_of_code/Day_24_Files_Directories_Paths/my_file.txt") as file:
    contents = file.read()
    print(contents)