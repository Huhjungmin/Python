stack = []

for i in range(3) :
    f = input("과일을입력하시오: ")
    stack.append(f)
for i in range(3) :
    print( stack.pop() )
