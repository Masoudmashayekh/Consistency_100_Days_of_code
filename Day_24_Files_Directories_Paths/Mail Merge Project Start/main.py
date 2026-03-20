#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Day_24_Files_Directories_Paths/Mail Merge Project Start/Input/Names/invited_names.txt", mode="r") as file:
    contents = file.read()
    names_list = contents.split("\n")
    print(names_list)

for name in names_list:
    with open("./Day_24_Files_Directories_Paths/Mail Merge Project Start/Input/Letters/starting_letter.txt", mode="r") as letter_file:
        letter = letter_file.read()
        replaced_letter = letter.replace("[name]", f"{name}")
        with open(f"./Day_24_Files_Directories_Paths/Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}", mode="w") as ready_to_send:
            ready_to_send.write(replaced_letter)        
    
        