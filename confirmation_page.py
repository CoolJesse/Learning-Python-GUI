from tkinter import *

def leftClick(event):
    print("You messed up")

root =Tk()
root.geometry("500x300")

election_1 =Label(root, text="President:")
election_1.grid(row=0, column=0, sticky=E)
election_1_choice =Label(root, text="Bigfoot")
election_1_choice.grid(row=0, column=2)

button_1 = Button(root, text="Change Vote")
button_1.bind("<Button-1>", leftClick)
button_1.grid(row=0, column=3)

election_2 =Label(root, text="Vice President:")
election_2.grid(row=1, column=0, sticky=E)
election_2_choice = Label(root, text="The Wolfman")
election_2_choice.grid(row=1, column=2)

button_2 = Button(root, text="Change Vote")
button_2.bind("<Button-1>", leftClick)
button_2.grid(row=1, column=3)


root.mainloop()
