from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk, ImageDraw, ImageFont, ImageChops

LIGHT_PURPLE = "#E3BAC6"
MED_PURPLE = "#BC9EC1"
DARK_PURPLE = "#52414C"
CREAM = "#FDE8E9"
BLUE = "#6C91C2"
FONT_NAME = "Arial"
img = NONE
f_types = [('Jpg Files', '*.jpg')]


def upload_photo():
    global img
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = Image.open(filename)
    Label(text='Photo successfully uploaded.').grid(column=2, row=1)


def add_watermark_text():
    if img == NONE:
        upload_needed = Label(text='Upload photo first')
        upload_needed.grid(column=1, row=4)
    else:
        size = tuple((img.width, img.height))
        text = Image.new("RGBA", size, (255, 255, 255, 0))
        image = img.convert(mode="RGBA")
        w_font = ImageFont.truetype("arial.ttf", int(img.height/3))
        draw = ImageDraw.Draw(text)
        draw.text((10, 10), watermark_text.get(), font=w_font, fill=(255, 255, 255, 128))
        out = Image.alpha_composite(image, text)
        out.show()


def add_watermark_logo():
    if img == NONE:
        upload_needed = Label(text='Upload photo first')
        upload_needed.grid(column=1, row=4)
    else:
        size = (500, 300)
        filename = filedialog.askopenfilename(filetypes=f_types)
        logo = Image.open(filename)
        logo.putalpha(10)
        logo.thumbnail(size)
        out = img.copy()
        out.paste(logo)
        out.show()


window = Tk()
window.title("Watermarker")
window.config(padx=100, pady=50, bg=LIGHT_PURPLE)

title = Label(text="Watermark", fg=DARK_PURPLE, bg=LIGHT_PURPLE, font=(FONT_NAME, 50))
title.grid(column=1, row=0, pady=20)

upload_button = Button(text="Upload Image", highlightthickness=0, command=upload_photo)
upload_button.grid(column=1, row=1, pady=70)

watermark_text = StringVar()
Label(text='Watermark Text').grid(column=0, row=2)
Entry(textvariable=watermark_text).grid(column=0, row=3)
Button(text='Add to Picture', command=add_watermark_text).grid(column=0, row=4)

Button(text='Add Logo to Picture', command=add_watermark_logo).grid(column=2, row=3)


window.mainloop()
