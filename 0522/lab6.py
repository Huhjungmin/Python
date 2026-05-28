from tkinter import *

# i번째 버튼을 눌렀을 때 실행
def checked(i):
    global player

    button = buttons[i]

    # 이미 눌린 버튼이면 종료
    if button["text"] != " ":
        return

    # 현재 플레이어 표시
    button["text"] = player

    # 플레이어에 따라 색 변경
    if player == "X":
        button["bg"] = "yellow"
        player = "O"
    else:
        button["bg"] = "lightgreen"
        player = "X"


# 윈도우 생성
window = Tk()
window.title("틱택토")

# 시작 플레이어
player = "X"

# 버튼 저장 리스트
buttons = []

# 3x3 버튼 생성
for i in range(9):
    b = Button(
        window,
        text=" ",
        width=10,
        height=5,
        command=lambda k=i: checked(k)
    )

    b.grid(row=i // 3, column=i % 3)

    buttons.append(b)

window.mainloop()