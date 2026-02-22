from tkinter import *
from tkinter import ttk, BooleanVar
import subprocess


#functions & variables

def submit():
	selected = []
#software
	if discord_var.get():
		if "disc" not in selected:
			selected.append("disc")
	if chrome_var.get():
		if "chrome" not in selected:
			selected.append("chrome")
			subprocess.run(['ms-settings:defaultapps'], check=True, shell=True)

	if firefox_var.get():
		if "firefox" not in selected:
			selected.append("firefox")
			subprocess.run(['ms-settings:defaultapps'], check=True, shell=True)

#launchers		
	if steam_var.get():
		if "steam" not in selected:
			selected.append("steam")
	if epic_var.get():
		if "epic" not in selected:
			selected.append("epic")
	if ea_var.get():
		if "ea" not in selected:
			selected.append("ea")
#osrs		
	if osrs_var.get():
		if "osrs" not in selected:
			selected.append("osrs")
	if alora_var.get():
		if "alora" not in selected:
			selected.append("alora")
#dev			
	if python_var.get():
		if "python" not in selected:
			selected.append("python")
	if pycharm_var.get():
		if "pycharm" not in selected:
			selected.append("pycharm")

	print("Selected software:", selected)


#tkinter        -init
root = Tk()
root.title("New PC Setup Automater")

#tkinter        -variables
discord_var = BooleanVar(value=False)
chrome_var = BooleanVar(value=False)
firefox_var = BooleanVar(value=False)


osrs_var = BooleanVar(value=False)
alora_var = BooleanVar(value=False)

steam_var = BooleanVar(value=False)
epic_var = BooleanVar(value=False)
ea_var = BooleanVar(value=False)

python_var=BooleanVar(value=False)
pycharm_var=BooleanVar(value=False)


#tkinter        -toplabels
Label(root, text="Software").grid(row=1, column=1, padx=10, pady=4)
Label(root, text="Game Launchers").grid(row=1, column=5, padx=10, pady=4)
Label(root, text="OSRS Shit").grid(row=1, column=9, padx=10, pady=4)
Label(root, text="Developer Shit").grid(row=1, column=13, padx=10, pady=4)


#tkinter        -software checklist
ttk.Checkbutton(root, text="Discord", variable=discord_var).grid(row=2, column=1, padx=10, pady=4)
ttk.Checkbutton(root, text="Chrome", variable=chrome_var).grid(row=3, column=1, padx=10, pady=4)
ttk.Checkbutton(root, text="Firefox", variable=firefox_var).grid(row=4, column=1, padx=10, pady=4)

#tkinter 		-game launchers
ttk.Checkbutton(root, text="Steam", variable=steam_var).grid(row=2, column=5, padx=10, pady=4)
ttk.Checkbutton(root, text="Epic", variable=epic_var).grid(row=3, column=5, padx=10, pady=4)
ttk.Checkbutton(root, text="EA", variable=ea_var).grid(row=4, column=5, padx=10, pady=4)


#tkinter		-osrs list
ttk.Checkbutton(root, text="OSRS", variable=osrs_var).grid(row=2, column=9, padx=10, pady=4)
ttk.Checkbutton(root, text="Alora", variable=alora_var).grid(row=3, column=9, padx=10, pady=4)

#tkinter		-dev list
ttk.Checkbutton(root, text="Python", variable=python_var).grid(row=2, column=13, padx=10, pady=4)
ttk.Checkbutton(root, text="PyCharm", variable=pycharm_var).grid(row=3, column=13, padx=10, pady=4)

#tkinter 		-buttons
Button(root, text="Install Selected Software", command=submit).grid(row=6, column=9, pady=20)







root.mainloop()
