# https://www.youtube.com/watch?v=IYHJRnVOFlw&t=1s

from tkinter import *


class MonstersButtons:
    def __init__(self, master): #second parameter for GUI, master means root or main window
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("ROAR, I AM BIGFOOT!!!")


root = Tk()
b = MonstersButtons(root) #calling MonstersButtons constructor
root.mainloop()
