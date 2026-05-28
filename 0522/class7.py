def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"


def decrease():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"

window = tk.Tk()
#window.geometry('300x40')

btn_decrease = tk.Button(master=window, width=10, text="감소", command=decrease)
btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window, width=10, text="0")
lbl_value.grid(row=0, column=1)

btn_increase = tk.Button(master=window, width=10, text="증가", command=increase)
btn_increase.grid(row=0, column=2, sticky="nsew")

window.mainloop()