import random

print("행운의매직볼로오늘의운세를출력합니다. ")
answers = random.randint(1, 8)
if answers == 1:
    print("확실히이루어집니다.")
elif answers == 2:
    print("좋아보이네요")
elif answers == 3:
    print("믿으셔도됩니다.")
elif answers == 4:
    print("저의생각에는no입니다.")
else: 
    print("다시질문해주세요.")
