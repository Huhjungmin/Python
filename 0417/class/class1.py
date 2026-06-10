n = int(input("입력할 값의 개수: "))
result = [ ]

for i in range(n):
    value = int(input(""))
    result.append(value)

s = sum(result)
print("값의 합계=", s)
