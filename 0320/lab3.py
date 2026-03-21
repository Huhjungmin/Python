temp = float(input("온도를입력하시오: "))
if temp <= 0:
    print("물의상태는얼음입니다.")
elif temp > 0 and temp < 100: 
    print("물의상태는액체입니다.")
else:
    print("물의상태는기체입니다.")
