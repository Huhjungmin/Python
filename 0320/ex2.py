price = int(input("가격을입력하시오: "))
card = (input("카드종류를입력하시오: "))

if price > 20000 and card == "python":
    print("배송료가없습니다.")

else:
    print("배송료는3000원입니다.")