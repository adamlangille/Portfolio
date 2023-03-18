from tkinter import *

FONT_NAME = "Helvetica"
CREAM = "#F0EAD2"
LIGHT_GREEN = "#DDE5B6"
GREEN = "#ADC178"
LIGHT_BROWN = "#A98467"
BROWN = "#6C584C"

def submit_word(event=None):
    if user_text.get:
        user_text.delete(0, 'end')


window = Tk()
window.title("Typing Test")
window.config(padx=100, pady=50, bg=BROWN)

title = Label(text="Typing Speed Test", fg=CREAM, bg=BROWN, font=(FONT_NAME, 30))
title.grid(column=1, row=0, pady=20)

user_text = Entry(font=(FONT_NAME, 16), justify=CENTER).grid(column=1, row=2)


window.bind('<space>', submit_word)

window.mainloop()
