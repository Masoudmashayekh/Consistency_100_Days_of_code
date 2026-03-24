import pandas

data = pandas.read_csv("./Day_25_CSV_Files_Pandas/Central_Park_Squirrel_Census_Squirrel_Data.csv")
print(data.Primary_Fur_Color)
gray = 0
cinnamon = 0
black = 0

data_list = data.Primary_Fur_Color.to_list()
for i in data_list:
    if i == "Gray":
        gray += 1
    elif i == "Cinnamon":
        cinnamon += 1
    elif i == "Black":
        black += 1
       
print(f"{gray}, {cinnamon}, {black}")
        
data_dict ={
    "Fur Color":["Gray", ""]
}