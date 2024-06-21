# Study aid - Notes card program
# Patrick Harrold
# June 6, 2024

from tkinter import *
import random
import pandas as pd
import time
BACKGROUND_COLOR = "#B1DDC6"
WAIT_TIME = 5

# Get the note card data and put it into a dict.
french_df = pd.read_csv("data/french_words.csv")
raw_french_dict = french_df.to_dict()
# Cleanup the dict so the front is the key and the back is the value.
# french_dict = {}
# for i in range(100):
#     front = raw_french_dict["French"][i]
#     back = raw_french_dict["English"][i]
#     french_dict[front] = back
    
# This way is cleaner than the one above so we can randomly choose an item from the list of dicts.
french_list = french_df.to_dict(orient='records')

dict_word = {}

# Get a new word and wait then display the English word.
def new_word():
    # It's a list of dicts, and each dict contains the word in French and English.
    global dict_word
    global flip_time
    # If we're getting a new card we might need to cancel the previous card timer.
    window.after_cancel(flip_time)
    dict_word = random.choice(french_list)
    # Get the french word.
    french_word = dict_word["French"]
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(word, text=french_word) 
    flip_time = window.after(3000, func=backside)

# Show the backside of the card    
def backside():
    translation = dict_word["English"]
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(word, text=translation) 
    canvas.itemconfig(backside, image=back_img)
    

def known_word():
    # Add the current word to the known_words csv. 
    global dict_word
    global french_df
    global french_list
    # Try just in case the file doesn't exist.
    try:
        with open(file="data/known_french_words.csv", mode="a") as known_file:
            known_file.write(f"{dict_word["French"]}, {dict_word['English']}\n")
    except FileNotFoundError:
        with open(file="data/known_french_words.csv", mode="w") as known_file:
            known_file.write(f"{dict_word["French"]}, {dict_word['English']}\n")
    # Remove the current word from the source csv.
    french_df = french_df[(french_df.French != dict_word["French"])]
    french_df.to_csv("data/french_words.csv")
    # Remove the current word from the current french_list.
    # location = french_list.index(dict_word)
    # french_list.pop(location)
    french_list.remove(dict_word)
    new_word()

    
    


# Start with all note cards as incorrect.
# Randomize which note card you're getting.

# If a note card is correct, delete it from the dict.
# If a note card is incorrect, leave it in.

# Place the images on the GUI.
window = Tk()
window.title("Study Aid")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_time = window.after(3000, func=backside)

canvas = Canvas(width=800, height=526)
# Gather all the images.
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
background = canvas.create_image(400, 263, image=front_img)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
# Build the buttons.

right_button = Button(image=right_img, highlightthickness=0, command=known_word)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=new_word)
right_button.grid(row=1, column=0)
wrong_button.grid(row=1, column=1)
# Get the first word.
new_word()
window.mainloop()