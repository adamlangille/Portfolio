from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

LIGHT_PURPLE = "#E3BAC6"
MED_PURPLE = "#BC9EC1"
DARK_PURPLE = "#52414C"
CREAM = "#FDE8E9"
BLUE = "#6C91C2"
FONT_NAME = "Arial"
img = NONE

def upload_photo():
    global img
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = Image.open(filename)
    img.thumbnail((500, 500))
    img = ImageTk.PhotoImage(img)
    width = img.width()
    height = img.height()
    canvas = Canvas(width=width, height=height, bg=MED_PURPLE, highlightthickness=0)
    canvas.create_image(width/2, height/2, image=img)
    canvas.grid(column=1, row=1)
    


window = Tk()
window.title("Watermarker")
window.config(padx=100, pady=50, bg=LIGHT_PURPLE)

title = Label(text="Watermark", fg=DARK_PURPLE, bg=LIGHT_PURPLE, font=(FONT_NAME, 50))
title.grid(column=1, row=0)



upload_button = Button(text="Upload", highlightthickness=0, command=upload_photo)
upload_button.grid(column=1, row=1)

window.mainloop()
