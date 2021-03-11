from tkinter import *
from tkinter import messagebox
import numpy as np
import pandas as pd


# read in csv file
def load_file():
    try:
        dataset = pd.read_csv(textfield.get())
        messagebox.showinfo("Message", "File has been loaded successfully in")
    except:
        messagebox.showinfo("Message", "please enter a valid path")


def Rem_row_na():
    dataset = pd.read_csv(textfield.get())
    dataset.dropna()


# execute when button pressed
def button_action():
    messagebox.showinfo("Message", "value: " + textfield.get())


# create window
window = Tk()
# window name
window.title("Data Science Tool")
# window size
window.geometry("500x500")

# define RadioButtons
var = IntVar()
R1 = Radiobutton(window, text="Remove Rows with NA", variable=var, value=1,
                 command=Rem_row_na)
R1.grid(row=1, column=1)

# create Textfield
textfield = Entry(window, bd=5, width=40)

# Label=Text for buttons
# create Labels
RemoveNa_label = Label(window, text="Replace all NA with 0")
exit_label = Label(window, text="Close Window")
textfield_label = Label(window, text="Enter Path of File")

# create Textfield
textfield = Entry(window, bd=5, width=40)

# create Buttons
RemoveNA_button = Button(window, text="Remove", command=button_action)
exit_button = Button(window, text="Exit", command=window.quit)
Load_in_file = Button(window, text="Load File", command=load_file)

# positioning of the items
RemoveNa_label.grid(row=4, column=1, columnspan=4)
RemoveNA_button.grid(row=4, column=10)
exit_label.grid(row=5, column=1)
exit_button.grid(row=5, column=10)
textfield_label.grid(row=9, column=1)
textfield.grid(row=9, column=10)
Load_in_file.grid(row=9, column=15)

# call window and wait for user to enter
window.mainloop()
