n = int(input("몇 번째 항까지 구할까요? "))

a = 0  
b = 1  

print(a, end=", ")

if n > 1:
    print(b, end=", ")

for i in range(2, n + 1):
    c = a + b
    print(c, end=", ")
    a = b
    b = c
