# Day 25: Working with CSV Files and Analysing Data with Pandas 


with open("./Day_25_CSV_Files_Pandas/weather_data.csv", mode= "r") as file:
    contents = file.readline()
    print(contents)