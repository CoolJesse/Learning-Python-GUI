# https://www.youtube.com/watch?v=IB6VkXJVf0Y

from tkinter import *
import tkinter.messagebox

root = Tk()
root.geometry("500x600")

tkinter.messagebox.showinfo("Window into the truth", "Bigfoot is real")

answer = tkinter.messagebox.askquestion("Question 1", "Do you believe in Bigfoot?")

if answer == 'yes':
    print("Me too!")

else:
    print("I'll show you, I'll show everyone!")

root.mainloop()
