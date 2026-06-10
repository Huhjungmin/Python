a = int(input("첫 번째 정수를 입력하시오: "))
b = int(input("두 번째 정수를 입력하시오: "))

gcd = 1  

limit = min(a, b)

for i in range(1, limit + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print(f"{a}와 {b}의 최대 공약수는 {gcd}입니다.")
