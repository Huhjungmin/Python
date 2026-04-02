n = int(input("숫자를 입력하세요: "))

i = n
result = 1

while i > 0:
    print(i, end="")
    result = result * i  
    
    if i > 1:
        print("x", end="")
    
    i = i - 1

print(" =", result)