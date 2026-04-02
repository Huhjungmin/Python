number = int(input("Enter the number of rows: "))

for i in range(number):
    
    for j in range(number - i - 1):
        print(" ", end="")
    
    # 별 출력
    for j in range(2 * i + 1):
        print("*", end="")
    
    print("")
