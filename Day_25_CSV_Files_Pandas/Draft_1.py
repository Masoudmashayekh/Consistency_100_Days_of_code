# Day 25: Working with CSV Files and Analysing Data with Pandas 


# with open("./Day_25_CSV_Files_Pandas/weather_data.csv", mode= "r") as data_file:
#     data = data_file.readlines()
#     print(data)

import csv

with open("./Day_25_CSV_Files_Pandas/weather_data.csv", mode= "r") as data_file:
    data = csv.reader(data_file)
    data = list(data)
    temperatures = []
    for row in data[1:]:
        temp = row[1]
        temperatures.append(int(temp))

    print(temperatures)