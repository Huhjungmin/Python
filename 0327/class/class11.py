total = 0.0

for i in range(1, 100, 2):  # 1, 3, 5, ..., 99
    total += i / (i + 2)

print(total)
