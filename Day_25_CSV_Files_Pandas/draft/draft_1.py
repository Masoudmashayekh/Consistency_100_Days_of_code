# Day 25: Working with CSV Files and Analysing Data with Pandas 


# with open("./Day_25_CSV_Files_Pandas/weather_data.csv", mode= "r") as data_file:
#     data = data_file.readlines()
#     print(data)

import csv

with open("./Day_25_CSV_Files_Pandas/draft/weather_data.csv", mode= "r") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

    print(temperatures)