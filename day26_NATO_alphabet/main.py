import pandas as pd

nato_df = pd.read_csv("nato_phonetic_alphabet.csv")
# Create a dict in this format:
# {"A": "Alpha", "B": "Bravo", etc}
# Without dict comprehension syntax.
# nato_dict = {}
# for (index, row) in nato_df.iterrows():
#     nato_dict[row.letter] = row.code

# print(nato_dict)
# And now with dict comprehension syntax.
nato_dict = {row.letter:row.code for (index, row) in nato_df.iterrows()}

not_a_word = True
# Let's use catching errors for the sake of the exercise, even though an if statement would have been fine.
while not_a_word:
    try:
        word = input("Type a word to translate into the NATO alphabet.\n").upper()
        nato_list = [nato_dict[letter] for letter in word] 
        # nato_list = [nato_dict[letter] for letter in word if letter in nato_dict]
    except:
        print("Please only use letters.")
    else:
        not_a_word = False

# This is the old way. 
# nato_list = []
# for letter in word:
#     if letter in nato_dict:
#        nato_list.append(nato_dict[letter]) 
# And now with list comprehension syntax.

print(nato_list)