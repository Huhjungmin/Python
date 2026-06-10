n = int(input("정수="))
s = 0
s += n % 10
n //= 10
s += n % 10
n //= 10
s += n % 10
n //= 10
s += n % 10
n //= 10
print(s)
