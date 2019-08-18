import random
from tkinter import *
import tkinter.messagebox

window = Tk()
label1 = Label(window, text = "With this program, you will have the option to roll a 4, 6, 8, 10, 12 or 20 sided dice. The choice is yours...")
label1.grid(row = 0, column = 0)

label1 = Label(window, text = 'Which dice do you want to roll?  ')
label1.grid(row = 1, column = 0)

def roll(event):
	if entry.get()=='4' or entry.get()=='d4' or entry.get()=='D4' or entry.get()=='Dice 4' or entry.get()=='4 Side' or entry.get()=='4 side' or entry.get()=='4 Sided' or entry.get()=='4 sided':
		tkinter.messagebox.showinfo("Result", random.randint(1,4))

	if entry.get()=='6' or entry.get()=='d6' or entry.get()=='D6' or entry.get()=='Dice 6' or entry.get()=='6 Side' or entry.get()=='6 side' or entry.get()=='6 Sided' or entry.get()=='6 sided':
		tkinter.messagebox.showinfo("Result", random.randint(1,6))

	if entry.get()=='8' or entry.get()=='d8' or entry.get()=='D8' or entry.get()=='Dice 8' or entry.get()=='8 Side' or entry.get()=='8 side' or entry.get()=='8 Sided' or entry.get()=='8 sided':
		tkinter.messagebox.showinfo("Result", random.randint(1,8))

	if entry.get()=='10' or entry.get()=='d10' or entry.get()=='D10' or entry.get()=='Dice 10' or entry.get()=='10 Side' or entry.get()=='10 side' or entry.get()=='10 Sided' or entry.get()=='10 sided':
		tkinter.messagebox.showinfo("Result", random.randint(1,10))

	if entry.get()=='12' or entry.get()=='d12' or entry.get()=='D12' or entry.get()=='Dice 12' or entry.get()=='12 Side' or entry.get()=='12 side' or entry.get()=='12 Sided' or entry.get()=='12 sided':
		tkinter.messagebox.showinfo("Result", random.randint(1,12))

	if entry.get()=='20' or entry.get()=='d20' or entry.get()=='D20' or entry.get()=='Dice 20' or entry.get()=='20 Side' or entry.get()=='20 side' or entry.get()=='20 Sided' or entry.get()=='20 sided':
		tkinter.messagebox.showinfo("Result", random.randint(1,20))

entry = Entry(window)
entry.grid(row = 2, column = 0)
entry.bind("<Return>", roll)

start_button = Button(window, text = "Roll", fg = "green", command = entry)
start_button.bind("<Button-1>", roll)

start_button.grid(row = 3, column = 0)
window.mainloop()
