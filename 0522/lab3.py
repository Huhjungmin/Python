from tkinter import*

window = Tk()

counter = 0

def clicked():
    global counter
    counter += 1
    label['text'] = '버튼클릭횟수: '+ str(counter)

label = Label(window, text="아직눌려지지않음")
label.pack()
button = Button(window, text="증가", command=clicked).pack()

window.mainloop()
