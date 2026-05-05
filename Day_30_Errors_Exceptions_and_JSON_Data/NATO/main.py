import pandas

data = pandas.read_csv("Day_30_Errors_Exceptions_and_JSON_Data/NATO/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


go_on = True
while go_on:
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        go_on = False
    

print(output_list)
