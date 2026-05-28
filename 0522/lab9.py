penButton = Button(window, text='펜', command=use_pen)
penButton.grid(row=0, column=0, sticky=W+E)
brushButton = Button(window, text='브러쉬', command=use_brush)
brushButton.grid(row=0, column=1, sticky=W+E)
colorButton = Button(window, text='색상선택', command=choose_color)
colorButton.grid(row=0, column=2, sticky=W+E)
eraseButton = Button(window, text='지우개', command=use_eraser)
eraseButton.grid(row=0, column=3, sticky=W+E)
clearButton = Button(window, text='모두삭제', command=clear_all)
clearButton.grid(row=0, column=4, sticky=W+E)

var = DoubleVar()
...
scale = Scale(window, variable=var, orient=VERTICAL)
scale.grid(row=1, column=5, sticky=N+S)

canvas.bind('<B1-Motion>', paint)
canvas.bind('<ButtonRelease-1>', reset)


def paint(event):
    global var, erase_on, mode, old_x, old_y
    fill_color = "white"if mode == "erase"else mycolor
    if old_x and old_y:
        canvas.create_line(old_x, old_y, event.x, event.y,
            capstyle=ROUND, width=var.get(), fill=fill_color)
    old_x = event.x
    old_y = event.y
def reset(event):
    global old_x, old_y
    old_x, old_y = None, None

def use_pen(): # 펜버튼이선택되면모드를”pen"으로바꾼다. 
    global mode
    mode = "pen"
def use_brush():
    global mode
    mode = "brush"
def choose_color():
    global mycolor
    mycolor = askcolor(color=mycolor)[1]
def use_erase():
    global mode
    mode = "erase"
