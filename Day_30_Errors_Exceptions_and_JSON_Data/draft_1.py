# Errors and Exceptions
# try => except => else => finally

try:
    file = open("Day_30_Errors_Exceptions_and_JSON_Data/a_file.txt")
    a_dict = {"key": "value"}
    print(a_dict["Hi"])
except FileNotFoundError:
    file = open("Day_30_Errors_Exceptions_and_JSON_Data/a_file.txt", "w")
    file.write("Something")
except KeyError:
    print("That key does not exist.")