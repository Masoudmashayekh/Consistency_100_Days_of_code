import pandas

#TODO 1. Create a dictionary in this format:{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("./Day_26_List_Dictionary_Comprehensions/nato_phonetic_alphabet.csv")
df = pandas.DataFrame(data)
dic_df = {row.letter: row.code for (index, row) in df.iterrows()}
print(dic_df)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = "pardis"
split_name = list(name.upper())

final = [{value for (key,value) in dic_df.items() if key == word} for word in split_name]
print(final)