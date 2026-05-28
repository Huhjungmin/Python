from tkinter import *
window = Tk()
window.title("Welcome to tkinter")
window.geometry('200x40')
lbl = Label(window, text="Hi!")
lbl.grid(column=0, row=0)
def clicked():
    lbl.configure(text="clicked")
btn = Button(window, text="click me", command=clicked)
btn.grid(column=1, row=0)
window.mainloop()