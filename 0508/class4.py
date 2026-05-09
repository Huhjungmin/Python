mydict = {}

for i in range(2):
    date = input("날짜를 입력하시오: ")
    job = input("일정을 입력하시오: ")

    if date in mydict:
        mydict[date].append(job)
    else:
        mydict[date] = []
        mydict[date].append(job)

print(mydict)