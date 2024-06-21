from tkinter import *


def convert():
    miles = int(input_m.get())
    km = str(round(miles * 1.609344, 2))
    result.config(text=km)


# Create the window
window = Tk()

window.title("Convert Miles to Kilometers")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)
# 1 input text box.
input_m = Entry(width=10)
input_m.grid(row=0,column=1)
# 4 labels.
miles = Label(text="Miles")
miles.grid(row=0, column=2)

equal = Label(text="is equal to ")
equal.grid(row=1, column=0)

# This label gets updated with the converted number of km.
result = Label(text="0")
result.grid(row=1, column=1)

km = Label(text="km")
km.grid(row=1, column=2)

# 1 button to calculate.
button = Button(text="Calculate", command=convert)
button.grid(row=2, column=1)

window.mainloop()