from tkinter import *
from tkinter import messagebox
import numpy as np
import pandas as pd


# read in csv file
def load_file():
    try:
        dataset = pd.read_csv(textfield.get())
        messagebox.showinfo("Message", "File has been loaded successfully")
    except:
        messagebox.showinfo("Warning", "please enter a valid path")


# option1 (Radiobutton1)
def Rem_row_na():
    dataset = pd.read_csv(textfield.get())
    NaFreeDataset = dataset.dropna()
    try:
        NaFreeDataset.to_csv(textfield_new_file.get(), index=False)
    except:
        messagebox.showinfo("Warning", "please enter a csv file name inside the textfield \n => e.g: example.csv")


# option2 (Radiobutton2)
def Replace_Na_with_0():
    dataset = pd.read_csv(textfield.get())
    ReplacedDataset = dataset.fillna(0)
    try:
        ReplacedDataset.to_csv(textfield_new_file.get(), index=False)
    except:
        messagebox.showinfo("Warning", "please enter a csv file name inside the textfield \n => e.g: example.csv")


# execute radiobuttons when button pressed
def button_action():
    value = var.get()
    if value == 'option 1':
        Rem_row_na()

    elif value == 'option 2':
        Replace_Na_with_0()


# create window
window = Tk()
# window name
window.title("Data Science Tool")
# window size
window.geometry("800x200")
# window color
window.configure(bg='dodger blue')

# define RadioButtons
var = StringVar()

selected_option = Label(window, bg="deep sky blue", width=50, text='You didn´t select an option')
selected_option.grid(row=0, column=1)


# print selected option
def print_selected():
    selected_option.config(text='You selected ' + var.get())


R1 = Radiobutton(window, text="Remove Rows with NA", variable=var, value="option 1", tristatevalue=0,
                 command=print_selected)
R1.grid(row=1, column=1)

R2 = Radiobutton(window, text="Replace NAs with 0", variable=var, value="option 2", tristatevalue=0,
                 command=print_selected)
R2.grid(row=2, column=1)

# create Textfield
textfield = Entry(window, bd=5, width=40)

# Label=Text for buttons
# create Labels

exit_label = Label(window, text="Close Window")
textfield_label = Label(window, text="Enter Path of File")
file_name = Label(window, text="Enter Name of new file")

# create Textfield
textfield = Entry(window, bd=5, width=40)
textfield_new_file = Entry(window, bd=5, width=40)

# create Buttons
RemoveNA_button = Button(window, text="Execute", command=button_action, bg="gray60")
exit_button = Button(window, text="Exit", command=window.quit,bg="gray60")
Load_in_file = Button(window, text="Load File", command=load_file, bg="gray60")

# positioning of the items
RemoveNA_button.grid(row=1, column=10)
exit_label.grid(row=5, column=1)
exit_button.grid(row=5, column=10)
textfield_label.grid(row=9, column=1)
textfield.grid(row=9, column=10)
Load_in_file.grid(row=9, column=15)
file_name.grid(row=10, column=1)
textfield_new_file.grid(row=10, column=10)

# color dodger blue
exit_label.configure(bg='dodger blue')
textfield_label.configure(bg='dodger blue')
file_name.configure(bg="dodger blue")
R1.configure(bg='dodger blue')
R2.configure(bg='dodger blue')

# call window and wait for user to enter
window.mainloop()
