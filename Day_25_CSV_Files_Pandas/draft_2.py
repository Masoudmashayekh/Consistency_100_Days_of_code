import pandas

data = pandas.read_csv("./Day_25_CSV_Files_Pandas/weather_data.csv")
# print(data)
# print(data["temp"])
# print(type(data))
# print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
print(len(temp_list))
temp_average = (sum(temp_list)/len(temp_list))
print(temp_average)
print(data["temp"].mean())
print(data["temp"].max())

# Get data in columns
print(data["condition"])
print(data.day)