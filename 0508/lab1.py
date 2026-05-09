s1=input("첫번째문자열:")
s2=input("두번째문자열:")

list1 = list( set(s1) & set(s2) ) 

print("\n공통적인글자:", end=" ")
for i in list1:
    print(i, end=" ")
