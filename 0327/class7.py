number = int(input("정수를 입력하시오: "))

for i in range(1, number + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()