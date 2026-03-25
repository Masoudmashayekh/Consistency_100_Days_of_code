import pandas

data = pandas.read_csv("./Day_25_CSV_Files_Pandas/draft/Central_Park_Squirrel_Census_Squirrel_Data.csv")

gray = len(data[data["Primary_Fur_Color"] == "Gray"])
cinnamon = len(data[data["Primary_Fur_Color"] == "Cinnamon"])
black = len(data[data["Primary_Fur_Color"] == "Black"])
        
data_dict ={
    "Fur Color":["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("./Day_25_CSV_Files_Pandas/draft/Squirrel_Data.csv")
print(data_frame)