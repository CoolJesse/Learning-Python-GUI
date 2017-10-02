#https://www.youtube.com/watch?v=D24Vx3_IM8U
from tkinter import *

def BigfootSays():
    print("ROAR!!!")

root = Tk()
root.geometry("500x300") #change default size of root

#******************************************************Main Menu****************************************************#

Bigfoot_menu = Menu(root)
root.config(menu=Bigfoot_menu)

subMenu = Menu(Bigfoot_menu)
Bigfoot_menu.add_cascade(label="File", menu=subMenu)

subMenu.add_command(label="Do you hear that?", command=BigfootSays)
subMenu.add_separator()

subMenu.add_command(label="Is that a Bigfoot I see?", command=BigfootSays)
subMenu.add_separator()

subMenu.add_command(label="Let's get out of here!", command=BigfootSays)

editMenu = Menu(Bigfoot_menu)
Bigfoot_menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=BigfootSays)

#*******************************************************Toolbar*****************************************************#

toolbar = Frame(root, bg="pink")

insertHere = Button(toolbar, text="Insert Image", command = BigfootSays)
insertHere.pack(side= LEFT, padx=2, pady=2)#pad gives extra space

printHere = Button(toolbar, text="Print", command=BigfootSays)
printHere.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

root.mainloop()
