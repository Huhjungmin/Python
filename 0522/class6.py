import tkinter as tk

window = tk.Tk()

for i in range(3):
    for j in range(10):
        button = tk.Button(window, text=f"{i}행,{j}열")
        button.grid(row=i, column=j)

window.mainloop()