# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# Read: "r"
with open("./Day_24_Files_Directories_Paths/data/my_file.txt", mode="r") as file:
    contents = file.read()
    print(contents)
    
    
# Write: "w"
# with open("./Day_24_Files_Directories_Paths/data/my_file.txt", mode="w") as file:
#     file.write("New text.")
    
    
# Append: "a"
# with open("./Day_24_Files_Directories_Paths/data/new_file.txt", mode="a") as file:
#     file.write("\nNew Text 2")   