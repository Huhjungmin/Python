import random

x = random.randint(1, 10)
y = random.randint(1, 10)
op = random.randint(0, 4)

if op == 0 :
    answer = int(input(str(x) + " + "
        + str(y) + "의 값은?"))
    if x+y == answer:
        print("맞았습니다.")
    else:
        print("틀렸습니다.")
elif op == 1 :
    answer = int(input(str(x) + " - "
        + str(y) + "의 값은?"))
    if x-y == answer:
        print("맞았습니다.")
    else:
        print("틀렸습니다.")
elif op == 2 :
    answer = int(input(str(x) + " * "
        + str(y) + "의 값은?"))
    if x*y == answer:
        print("맞았습니다.")
    else:
        print("틀렸습니다.")
else :
    answer = float(input(str(x) + " / "
        + str(y) + "의 값은?"))
    if x/y == answer:
        print("맞았습니다.")
    else:
        print("틀렸습니다.")