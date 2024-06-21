# import tkinter

# window = tkinter.Tk()

# window.title("GUI me")
# window.minsize(width=500, height=300)

# # Label example.
# my_label = tkinter.Label(text="Label it", font=("Arial", 24, "bold"))
# # Place it into the screen. Otherwise you never see it.
# my_label.pack(side="right")



# window.mainloop()

def add(*args):
    # It's a tuple type.
    print(type(args))
    result = 0
    for n in args:
        result += n
    return n

# print(add(1))
# print(add(1, 2, 3))

def calculate(n, **kwargs):
    # It's a dict type.
    # print(type(kwargs))
    # Key is the parameter name. Value is the argument value.
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n
    
# print(calculate(n=4, multiply=5, add=3))

# This is how tkinter's Label() class looks.
class Car:
    
    def __init__(self, **kw) -> None:
        # This way it makes them a required argument.
        # self.make = kw["make"]
        # self.model = kw["model"]
        # This way makes them optional arguments.
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)
print(my_car.model)
my_other_car = Car(make="Honda")
# This will print none since there's no data initialized. Since we set it to optional it will not throw an error.
print(my_other_car.model)

# More tkinter. Doing it this way makes it so you don't need to type tkinter.<Class>
from tkinter import *

window = Tk()

window.title("GUI me")
window.minsize(width=500, height=300)

# Label example.
my_label = Label(text="Label it", font=("Arial", 24, "bold"))
# Place it into the screen. Otherwise you never see it.
my_label.pack()

# 2 ways
my_label["text"] = "New Text"
my_label.config(text="New Text")


def button_clicked():
    print("I got clicked.")
    # my_label["text"] = "Button clicked!"
    given_input = usr_input.get()
    # my_label["text"] = given_input
    my_label.config(text=given_input)
    
# Button. Make it so it gets whatever you put in the entry (text box).
button = Button(text="Click me", command=button_clicked)
button.pack()

# Entry
usr_input = Entry(width=10)
usr_input.pack()
# users_input = usr_input.get()


# Angela's tkinter example to display all the pieces.
#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()



window.mainloop()