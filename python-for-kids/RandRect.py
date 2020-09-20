from tkinter import *
from tkinter import colorchooser
from random import randrange
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

maxh = input('Enter max height: ')
maxw = input('Enter max width: ')
lp01 = input('How many rectangles? ')
col1 = colorchooser.askcolor()
def rand_rect(width, height, color, loop):
    for i in range(0,loop): 
        x1 = randrange(width)
        y1 = randrange(height)
        x2 = x1 + randrange(width)
        y2 = y1 + randrange(height)
        canvas.create_rectangle(x1, y1, x2, y2, fill=color)

rand_rect(int(maxw),int(maxh), col1[1], int(lp01))
