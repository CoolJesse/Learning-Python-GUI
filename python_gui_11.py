
#https://www.youtube.com/watch?v=FqIKEW-S8W0
from tkinter import *

def BigfootSays():
    print("ROAR!!!")

root = Tk()
root.geometry("500x300") #change default size of root

#******************************************************Main Menu****************************************************#

Bigfoot_menu = Menu(root)
root.config(menu=Bigfoot_menu)

fileMenu = Menu(Bigfoot_menu)
Bigfoot_menu.add_cascade(label="File", menu=fileMenu)

fileMenu.add_command(label="Look for Bigfoot", command=BigfootSays)
fileMenu.add_separator()

fileMenu.add_command(label="Try to catch Bigfoot", command=BigfootSays)
fileMenu.add_separator()

fileMenu.add_command(label="Chase Bigfoot", command=BigfootSays)
fileMenu.add_separator()

fileMenu.add_command(label="Run away from Bigfoot!", command=BigfootSays)


editMenu = Menu(Bigfoot_menu)
Bigfoot_menu.add_cascade(label="Edit", menu=editMenu)

editMenu.add_command(label="Rethink tactics", command=BigfootSays)
editMenu.add_separator()

editMenu.add_command(label="Set traps", command=BigfootSays)
editMenu.add_separator()

editMenu.add_command(label="Get a big gun", command= BigfootSays)

#*******************************************************Toolbar*****************************************************#

toolbar = Frame(root, bg="pink")

insertHere = Button(toolbar, text="Tell your Bigfoot story", command = BigfootSays)
insertHere.pack(side= LEFT, padx=2, pady=2)#pad gives extra space

printHere = Button(toolbar, text="Contact a Bigfoot expert", command=BigfootSays)
printHere.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

#**************************************************Status Bar********************************************************#

#bd stand for border, SUNKEN sinks label into window
status= Label(root, text="Prepairing to find Bigfoot...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
