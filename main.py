from tkinter import *
from tkinter import ttk, BooleanVar


#functions & variables

selected_software = []
def software_selected(software):
    selected_software.append(software)




#tkinter        -init
root = Tk()
root.title("New PC Setup Automater")
root.geometry("1100x900")

#tkinter        -variables
discord_var = BooleanVar(value=False)
osrs_var = BooleanVar(value=False)



#tkinter        -toplabels
Label(root, text="Select the software you wish to install from the list below")

#tkinter        -software checklist
ttk.Checkbutton(root, text="Discord", command=lambda: software_selected("disc"), variable=discord_var).grid(row=0, column=4, padx=10, pady=4)















root.mainloop()