import time
from tkinter import * 

window = Tk() 

canvas = Canvas(window, bg = "white",  width = 300, height = 200)
canvas.pack()

id = canvas.create_text(10, 100, text = "파이썬 커피샵으로 오세요!")

while True:
   canvas.move(id, 2, 0)
   window.update()
   time.sleep(0.05)