# Send a letter to everyone in team Avatar for your birthday.
import os
print(os.getcwd())
# Read the names into a list
name_list = []
with open(file="Input/Names/invited_names.txt") as name_file:
    # Read line by line since each line is a name.
    for line in name_file:
        name_list.append(line.strip())
# Get the original as data.
with open(file="Input/Letters/starting_letter.txt", mode="r") as original_file:
    original_letter = original_file.read()
    
#Replace the [name] placeholder with the actual name.
letters_dict = {}
for name in name_list:
    new_letter = original_letter.replace("[name]", name)
    new_letter = new_letter.replace("Angela", "Patrick")
    letters_dict[name] = new_letter
    

#Save the letters in the folder "ReadyToSend".
for name in letters_dict:
    with open(file=f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as write_file:
        write_file.write(letters_dict[name])
