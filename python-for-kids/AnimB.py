import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_polygon(10,10,10,60,50,35)

for i in range(0,60):
        canvas.move(1,5,5)
        tk.update()
        time.sleep(0.05)

for j in range(0,60):
        canvas.move(1,-5,-5)
        tk.update()
        time.sleep(0.05)
