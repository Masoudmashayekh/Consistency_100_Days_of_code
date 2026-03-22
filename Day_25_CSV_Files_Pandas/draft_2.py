import pandas

data = pandas.read_csv("./Day_25_CSV_Files_Pandas/weather_data.csv")
# print(data)
# print(data["temp"])
# print(type(data))
# print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)