import random

def longestrun(myList):
    size = 1
    max_size = 0
    for i in range(len(myList)-1):
        if myList[i+1] == myList[i]:
            size += 1
        else: 
            size = 1
        if max_size<size:
            max_size = size
    return max_size 

s = [ random.randint(0, 1) for _ in range(10) ]
print(s)
print("최대 연속 길이=", longestrun(s))
