import random
tries = 0 
guess = 0 
answer = random.randint(1, 100) 

print("1부터100 사이의숫자를맞추시오")
while guess != answer:
    guess = int(input("숫자를입력하시오: "))
    tries = tries + 1
    if guess < answer:
        print("너무낮음!")
    elif guess > answer:
        print("너무높음!")
if guess == answer:
    print("축하합니다. 시도횟수=", tries)
else:
    print("정답은", answer)
