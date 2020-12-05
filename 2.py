from PIL import Image, ImageTk
import tkinter as tk

IMAGE_PATH = 'back.png'
WIDTH, HEIGTH = 1200, 800

root = tk.Tk()
root.geometry('{}x{}'.format(WIDTH, HEIGTH))

canvas = tk.Canvas(root, width=WIDTH, height=HEIGTH)
canvas.pack()

img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGTH), Image.ANTIALIAS))
canvas.background = img  # Keep a reference in case this code is put in a function.
bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)

# Put a tkinter widget on the canvas.
button = tk.Button(root, text="Start")
button_window = canvas.create_window(10, 10, anchor=tk.NW, window=button)

canvasw = 1200
canvash = 800

catchcol = 'black'
catw = 100
cath = 100
catsx1 = canvasw / 2 - catw /2
catsy1 = canvash - cath -20
catsx2 = catsx1 + catw 
catsy2 = catsy1 + cath

cat = canvas.create_arc(catsx1,catsy1,catsx2,catsy2, start= 200 ,extent = 140, style='arc', outline=catchcol, width=3) 

root.mainloop()