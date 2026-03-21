print("========================")
print("메뉴1번: 치즈버거")
print("메뉴2번: 치킨버거")
print("메뉴3번: 불고기버거")
print("========================")

selection = int(input("메뉴를선택하세요:"))
if selection >= 1and selection <= 3:
    print("메뉴", selection)
else:
    print("잘못입력하셨습니다.")
