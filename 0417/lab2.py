list1 = [1, 2, 3, 4, 15, 99] 

list1.sort() 

print("두번째로큰수=", list1[-2]) 


list1 = [1, 2, 3, 4, 15, 99] 

list1.remove(max(list1)) 

print("두번째로큰수=", max(list1))