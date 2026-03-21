# Day 25: Working with CSV Files and Analysing Data with Pandas 


with open("./Day_25_CSV_Files_Pandas/weather_data.csv", mode= "r") as data_file:
    data = data_file.readlines()
    print(data)