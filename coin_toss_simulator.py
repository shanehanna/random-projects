from tkinter import *
import tkinter.messagebox

window = Tk()
label = Label(window, text = "How many flips do you want to simulate? ")
label.grid(row = 0, column = 0)

def flip(event):
    import random

    heads = 0
    tails = 0
    last_flip = 0
    current_streak = 0
    top_streak = 0
    streak_drought = 0
    top_drought = 0
    i = 0

# tracks number of heads/tails

    runs = (int)(number_flips.get())

    while (i < runs):
        run = random.randint(1,2)

        if run == 1:
            heads += 1
            i+=1

        elif run == 2:
            tails += 1
            i+=1

# tracks the current streak

        if(last_flip == run):
            current_streak += 1
            if(current_streak > top_streak):
                top_streak = current_streak
        else:
            current_streak = 0

 #tracks streak drought

        if(last_flip != run):
            streak_drought += 1
            if(streak_drought > top_drought):
                top_drought = streak_drought
        else:
            streak_drought = 0

# store last run

        last_flip = run

    tkinter.messagebox.showinfo("Results", "Heads: " + str(heads) + "\n" + "Tails: " + str(tails) + "\n" + "Longest Streak: " + str(top_streak) + "\n" + "Most flips without a repeat: " + str(top_drought))
# end flip()

number_flips = Entry(window)
number_flips.grid(row = 1, column = 0)

start_button = Button(window, text = "Start", fg = "green", command = number_flips)
start_button.bind("<Button-1>", flip)
start_button.grid(row = 2, column = 0)

window.mainloop()
