import random
print("동전던지기게임을시작합니다.")
coin = random.randrange(2)
if coin == 0:
    print("앞면입니다.")
else:
    print("뒷면입니다.")
print("게임이종료되었습니다.")
