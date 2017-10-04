from tkinter import *

def leftClick(event):
    print("You messed up")

votes = {'President': 'Dracula', 'Vice President': 'The Wolfman', 'Secretary of State': 'Frankenstein\'s Monster',
         'Secretary of the Interior': 'Bigfoot', 'Head of the EPA': 'Swamp Thing', 'Secretary of Health and Human'
                                                                                      'Services': 'The Mummy'}
for key, value in votes.items():
    print(key, ': ', value)

print (len(votes))

root =Tk()
root.geometry("500x300")
root.wm_title("Final Confirmation")


'''
i = 0
j = 1
l = 2

while i <= len(votes):

    for key, value in votes.items():
        
        i = Label(root, text=key)
        i.pack()
        #i.grid(row=i, column=0, sticky=E)

        j = Label(root, text=value)
        j.pack()
        #j.grid(row=i, column=2)

        l = Button(root, text="Change Vote")
        l.bind("<Button-1>", leftClick)
        l.pack()
        #l.grid(row=i, column=3)

        i+=3
        j+=3
        l+=3

'''
counter = len(votes)

final_votes = [Label(root, text="President:" + ' ' + "Bigfoot")]
final_votes[0].grid(row=0, column=0, sticky=W)

final_button = [Button(root, text="Change Vote")]
final_button[0].bind("<Button-1>", leftClick)
final_button[0].grid(row=0, column=3)

counter

'''i = 0
while(<=i*2)
    final_votes[i] = Label(root, text="President:" + ' ' + "Bigfoot")
    final_votes[i].grid(row=counter, column=0, sticky=W)

    final_votes[i+1] = Button(root, text="Change Vote")
    final_votes[i+1].bind("<Button-1>", leftClick)
    final_votes[i+1].grid(row=0, column=3)

    counter+=2'''

'''
election_1 =Label(root, text="President:" + ' ' + "Bigfoot")
election_1.grid(row=0, column=0, sticky=W)

button_1 = Button(root, text="Change Vote")
button_1.bind("<Button-1>", leftClick)
button_1.grid(row=0, column=3)

election_2 =Label(root, text="Vice President:" + ' ' + "The Wolfman")
election_2.grid(row=1, column=0, sticky=W)


button_2 = Button(root, text="Change Vote")
button_2.bind("<Button-1>", leftClick)
button_2.grid(row=1, column=3)
'''

root.mainloop()
