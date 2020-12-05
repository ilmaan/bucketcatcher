from itertools import cycle
from random import randrange
from tkinter import Tk , Canvas , messagebox , font
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import tkinter as tk
import random

canvasw = 1200
canvash = 800



root = tk.Tk()
root.geometry('{}x{}'.format(canvasw, canvash))
root.title("GTA V")

canvas = tk.Canvas(root, width=canvasw , height=canvash)
canvas.pack()

img = ImageTk.PhotoImage(Image.open("back.png").resize((canvasw, canvash), Image.ANTIALIAS))
canvas.background = img  # Keep a reference in case this code is put in a function.
bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)



eg = PhotoImage(file = "eg.png")
ep = PhotoImage(file = "ep.png")
er = PhotoImage(file = "er.png")
ey = PhotoImage(file = "ey.png")

el = [eg,ep,er,ey]


ew = 45
eh = 55
es = 10

ev = 500
ei = 4000
dfcl = 0.95

catchcol = 'black'
catw = 100
cath = 100
catsx1 = canvasw / 2 - catw /2
catsy1 = canvash - cath -20
catsx2 = catsx1 + catw 
catsy2 = catsy1 + cath

cat = canvas.create_arc(catsx1,catsy1,catsx2,catsy2, start= 200 ,extent = 140, style='arc', outline=catchcol, width=3) 

catcher = PhotoImage(file="catcher1.png")    

canvas.create_image(canvasw-650,canvash-120, anchor=NW, image=catcher)

score = 0
scoret = canvas.create_text(10,10,anchor='nw' , font =('Arial',12,'bold'),fill='darkblue',text='Score :' + str(score)) 

liver = 3
livet = canvas.create_text(canvasw-100,10,anchor='nw' , font =('Arial',12,'bold'),fill='darkblue',text='Lives :' + str(liver)) 


egs = []

def crteg():
    x = randrange(10,740)
    y = 40
    newg = canvas.create_image(canvasw-650,canvash-800, anchor=NW, image=random.choice(el))
    egs.append(newg)
    root.after(ei,crteg)

def moveg():
    for e in egs:
        (ex1,ey1,ex2,ey2) = canvas.coords(eg)
        canvas.move(e,0,10)
        if ey2 > canvash:
            egdrp(e)

    root.after(ev,moveg)

def egdrp(e):
    egs.remove(e)
    lost()
    if liver == 0:
        messagebox.showinfo('GAME OVER LOSER','YOUR SCORE:' + str(score))
        root.destroy()

def lost():
    global liver
    liver -= 1
    canvas.itemconfigure(livet, text = 'Lives :' + str(liver))  

def catch():
    (catcx1,catcy1,catcx2,catcy2) = canvas.coords(catcher)
    for e in egs:
        (ex1,ey1,ex2,ey2) = canvas.coords(e)
        if catcx1 < ex1 and ex2 < catcx2 and catcy2 - ey2 < 40:
            egs.remove(e)
            canvas.delete(e)
            


root.mainloop()