import pandas

data = pandas.read_csv("./Day_25_CSV_Files_Pandas/Central_Park_Squirrel_Census_Squirrel_Data.csv")
print(data.Primary_Fur_Color)
x = 0
y = 0
z = 0

gray = data.Primary_Fur_Color == "Gray"
print(gray)