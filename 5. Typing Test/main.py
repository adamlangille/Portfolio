from tkinter import *
import time

FONT_NAME = "Helvetica"
CREAM = "#F0EAD2"
LIGHT_GREEN = "#DDE5B6"
GREEN = "#ADC178"
LIGHT_BROWN = "#A98467"
BROWN = "#6C584C"

timer = None
seconds = 0

def start_timer():
    print("pog")
    global seconds
    seconds = 60
    count_down()


def count_down():
    global seconds
    print(seconds)
    if seconds == 0:
        timer_text.config(text=f"Times up!")
        return
    timer_text.config(text=f"Timer: {seconds}")
    seconds -= 1  
    window.after(1000, count_down)


def submit_word(event=None):
    user_text.delete(0, 'end')


window = Tk()
window.title("Typing Speed Test")
window.config(padx=100, pady=50, bg=BROWN)

title = Label(text="Typing Speed Test", fg=CREAM, bg=BROWN, font=(FONT_NAME, 30))
title.grid(column=2, row=0, columnspan=2, pady=20)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=2, row=1, sticky=(N, S, E, W))

timer_text = Label(text=f"Timer: {seconds}", fg="GREEN", bg=CREAM, font=(FONT_NAME, 20))
timer_text.grid(column=3, row=1)

text = StringVar()
user_text = Entry(window, textvariable=text, font=(FONT_NAME, 16), justify=CENTER)
user_text.grid(column=2, row=2, columnspan=2)

window.bind('<space>', submit_word)

window.mainloop()
