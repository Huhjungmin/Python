sum = 0
start = 1
end = 101

for i in range(start, end):
    sum += 1
    if i < 4:
        print(i, end="+")
    elif i == end-1:
        print("...+", i, end="=")

print(sum)
