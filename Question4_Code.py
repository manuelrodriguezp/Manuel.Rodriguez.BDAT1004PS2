# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 20:14:27 2020

@author: guill
"""


from tkinter import Tk, Label, Entry, RAISED

root = Tk()

#Mortgage
label = Label(root, text='Loan Amount:')
label.grid(row=1, column=0)

Ent = Entry(root)
Ent.grid(row=1, column=1)

label = Label(root, text='Interest rate:')
label.grid(row=2, column=0)

Ent = Entry(root)
Ent.grid(row=2, column=1)

label = Label(root, text='Loan terms:')
label.grid(row=3, column=0)

Ent = Entry(root)
Ent.grid(row=3, column=1)

label = Label(root, relief=RAISED, text='Compute mortgage:')
label.grid(row=4, column=0)

Ent = Entry(root)
Ent.grid(row=4, column=1)


#Calculator
Ent = Entry(root,
            width=25)
Ent.grid(row=0, column=2,columnspan=4)

labels = [[],
          ['','','MC', 'M+', 'M-', 'MR'],
          ['','','C ', '√ ', 'χ²', '+ '],
          ['','','7 ', '8 ', '9 ', '- '],     
          ['','','4 ', '5 ', '6 ', '* '],     
          ['','','1 ', '2 ', '3 ', '/ '],
          ['','','0 ', '. ', '+-', '= ']]

for r in range(1,7):
    for c in range(2, 6):
        # create label for row r and column c
        label = Label(root,
                      width=1,
                      height=1,
                      relief=RAISED,      
                      padx=10,            
                      text=labels[r][c])
        # place label in row r and column c
        label.grid(row=r, column=c)

root.mainloop()
